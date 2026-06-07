from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, PersonalityResult, ChatMessage, User
from utils.ai_engine import analyze_text, get_chat_response
from datetime import datetime

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
@login_required
def index():
    analyses = PersonalityResult.query.filter_by(user_id=current_user.id)\
        .order_by(PersonalityResult.created_at.desc()).limit(6).all()
    total = PersonalityResult.query.filter_by(user_id=current_user.id).count()
    chats = ChatMessage.query.filter_by(user_id=current_user.id).count()
    return render_template('dashboard/index.html', analyses=analyses, total=total, chats=chats)

@dashboard_bp.route('/analyze', methods=['GET', 'POST'])
@login_required
def analyze():
    result = None
    input_text = ''
    if request.method == 'POST':
        text = request.form.get('text', '').strip()
        input_text = text
        if not text:
            flash('Please enter some text to analyze.', 'warning')
        else:
            a = analyze_text(text)
            rec = PersonalityResult(
                user_id=current_user.id,
                input_text=text,
                personality_type=a['personality_type'],
                emotion=a['emotion'],
                tone=a['tone'],
                confidence=a['confidence'],
                friendly_score=a['friendly_score'],
                professional_score=a['professional_score'],
                aggressive_score=a['aggressive_score'],
                emotional_score=a['emotional_score'],
                analytical_score=a['analytical_score'],
                assertive_score=a['assertive_score'],
                happy_score=a['happy_score'],
                sad_score=a['sad_score'],
                angry_score=a['angry_score'],
                neutral_score=a['neutral_score'],
                excited_score=a['excited_score'],
                recommendation=a['recommendation'],
            )
            db.session.add(rec)
            db.session.commit()
            result = a
    return render_template('dashboard/analyze.html', result=result, input_text=input_text)

@dashboard_bp.route('/history')
@login_required
def history():
    page = request.args.get('page', 1, type=int)
    analyses = PersonalityResult.query.filter_by(user_id=current_user.id)\
        .order_by(PersonalityResult.created_at.desc()).all()
    return render_template('dashboard/history.html', analyses=analyses)

@dashboard_bp.route('/chatbot')
@login_required
def chatbot():
    messages = ChatMessage.query.filter_by(user_id=current_user.id)\
        .order_by(ChatMessage.created_at.asc()).limit(60).all()
    return render_template('dashboard/chatbot.html', messages=messages)

@dashboard_bp.route('/chat/send', methods=['POST'])
@login_required
def chat_send():
    data = request.get_json() or {}
    message = data.get('message', '').strip()
    if not message:
        return jsonify({'error': 'Empty'}), 400
    response = get_chat_response(message)
    um = ChatMessage(user_id=current_user.id, message=message, is_user=True)
    am = ChatMessage(user_id=current_user.id, message=response, is_user=False, response=response)
    db.session.add_all([um, am])
    db.session.commit()
    return jsonify({'response': response})

@dashboard_bp.route('/analytics')
@login_required
def analytics():
    analyses = PersonalityResult.query.filter_by(user_id=current_user.id).all()
    pc, ec = {}, {}
    for a in analyses:
        pc[a.personality_type] = pc.get(a.personality_type, 0) + 1
        ec[a.emotion] = ec.get(a.emotion, 0) + 1
    return render_template('dashboard/analytics.html', personality_counts=pc,
                           emotion_counts=ec, total=len(analyses), analyses=analyses)

@dashboard_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        fn = request.form.get('full_name', '').strip()
        if fn:
            current_user.full_name = fn
            db.session.commit()
            flash('Profile updated successfully!', 'success')
    return render_template('dashboard/settings.html')

@dashboard_bp.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        flash('Access denied.', 'danger')
        return redirect(url_for('dashboard.index'))
    users    = User.query.order_by(User.created_at.desc()).all()
    analyses = PersonalityResult.query.order_by(PersonalityResult.created_at.desc()).limit(25).all()
    return render_template('dashboard/admin.html',
                           users=users, analyses=analyses,
                           total_users=User.query.count(),
                           total_analyses=PersonalityResult.query.count(),
                           total_chats=ChatMessage.query.count())
