from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    full_name = db.Column(db.String(120))
    role = db.Column(db.String(20), default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    analyses = db.relationship('PersonalityResult', backref='user', lazy=True)
    chat_messages = db.relationship('ChatMessage', backref='user', lazy=True)

    def set_password(self, p): self.password_hash = generate_password_hash(p)
    def check_password(self, p): return check_password_hash(self.password_hash, p)


class PersonalityResult(db.Model):
    __tablename__ = 'personality_results'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    input_text = db.Column(db.Text, nullable=False)
    personality_type = db.Column(db.String(50))
    emotion = db.Column(db.String(50))
    tone = db.Column(db.String(50))
    confidence = db.Column(db.Float)
    friendly_score    = db.Column(db.Float, default=0)
    professional_score= db.Column(db.Float, default=0)
    aggressive_score  = db.Column(db.Float, default=0)
    emotional_score   = db.Column(db.Float, default=0)
    analytical_score  = db.Column(db.Float, default=0)
    assertive_score   = db.Column(db.Float, default=0)
    happy_score       = db.Column(db.Float, default=0)
    sad_score         = db.Column(db.Float, default=0)
    angry_score       = db.Column(db.Float, default=0)
    neutral_score     = db.Column(db.Float, default=0)
    excited_score     = db.Column(db.Float, default=0)
    recommendation = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class ChatMessage(db.Model):
    __tablename__ = 'chat_messages'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text)
    is_user = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
