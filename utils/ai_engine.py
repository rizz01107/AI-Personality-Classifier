import re, random, math

PERSONALITY_KW = {
    'Friendly':     ['hello','hi','thanks','please','help','kind','nice','love','great','wonderful','appreciate','happy','glad','smile','welcome','friend','warm','care','thank','grateful'],
    'Professional': ['meeting','project','deadline','report','business','strategy','objective','deliverable','stakeholder','roi','kpi','agenda','professional','proposal','client','contract','quarterly','schedule','productivity'],
    'Aggressive':   ['demand','now','immediately','unacceptable','ridiculous','worst','terrible','useless','incompetent','failure','stupid','hate','disgusting','furious','never','pathetic','awful'],
    'Emotional':    ['feel','feeling','heart','soul','cry','tears','hurt','pain','lonely','miss','emotional','sensitive','upset','worried','anxious','afraid','nervous','scared','overwhelmed'],
    'Analytical':   ['analyze','data','research','study','evidence','fact','statistics','logic','reason','therefore','conclude','hypothesis','theory','result','pattern','metric','because','since','thus'],
    'Assertive':    ['must','should','need','require','expect','insist','clear','direct','certain','confident','decision','action','commit','responsibility','accountable','ensure','will','definitely'],
}

EMOTION_KW = {
    'Happy':      ['happy','joy','excited','wonderful','great','amazing','love','fantastic','blessed','grateful','awesome','excellent','brilliant','thrilled','delighted','cheerful'],
    'Sad':        ['sad','unhappy','depressed','miserable','cry','tears','lonely','hopeless','broken','grief','sorrow','miss','lost','empty','hurt','gloomy','down'],
    'Angry':      ['angry','furious','rage','hate','mad','outraged','frustrated','irritated','annoyed','disgusted','infuriated','livid','enraged','bitter'],
    'Neutral':    ['okay','fine','alright','normal','usual','regular','standard','average','moderate','typical','basic','so','just'],
    'Excited':    ['excited','thrilled','pumped','ecstatic','enthusiastic','eager','wow','incredible','unbelievable','awesome','cant wait','looking forward'],
    'Frustrated': ['frustrated','stuck','difficult','problem','issue','cannot','unable','struggle','hard','complicated','messy','wrong','fail','broken','error'],
    'Confused':   ['confused','unclear','understand','dont know','what','why','unsure','uncertain','lost','vague','ambiguous','huh','mean'],
}

RECS = {
    'Friendly':     'Your warm communication style builds trust effortlessly. In professional settings, balance friendliness with clear objectives to maximise impact.',
    'Professional': 'Your structured communication signals credibility. Add occasional warmth and personal touches to strengthen relationships beyond business outcomes.',
    'Aggressive':   'Your direct style shows passion, but can create defensiveness. Try softening demands with collaborative language — "Let\'s solve this together" works better than ultimatums.',
    'Emotional':    'Your expressive communication conveys depth and authenticity. In formal contexts, pair emotional language with factual support for stronger persuasion.',
    'Analytical':   'Your evidence-based approach builds compelling arguments. Connect data to human impact to engage audiences who respond more to stories than statistics.',
    'Assertive':    'Your confident communication sets clear expectations. Ensure assertiveness stays two-way — invite others\' input so they feel ownership, not just instruction.',
}

def preprocess(text):
    return re.sub(r'[^a-z0-9\s]', ' ', text.lower()).split()

def _score(words, kmap):
    scores = {k: sum(1.0 for w in words if w in kws) + random.uniform(.1, .3) for k, kws in kmap.items()}
    total = sum(scores.values()) or 1.0
    return {k: round(v / total * 100, 1) for k, v in scores.items()}

def _confidence(scores):
    vals = list(scores.values())
    exps = [math.exp(v / 15) for v in vals]
    s = sum(exps)
    return round(max(exps) / s, 3)

def analyze_text(text):
    words = preprocess(text) or ['okay']
    ps = _score(words, PERSONALITY_KW)
    es = _score(words, EMOTION_KW)
    pt = max(ps, key=ps.get)
    em = max(es, key=es.get)
    conf = _confidence(ps)
    pos = sum(1 for w in words if w in {'good','great','excellent','wonderful','amazing','love','happy','best','brilliant','fantastic'})
    neg = sum(1 for w in words if w in {'bad','terrible','horrible','awful','hate','worst','poor','wrong','failed','broken','useless'})
    tone = 'Positive' if pos > neg else ('Negative' if neg > pos else 'Neutral')
    return {
        'personality_type':   pt,
        'emotion':            em,
        'tone':               tone,
        'confidence':         conf,
        'personality_scores': ps,
        'emotion_scores':     es,
        'recommendation':     RECS.get(pt, 'Focus on clear, empathetic communication for better interactions.'),
        'word_count':         len(words),
        'friendly_score':     ps.get('Friendly', 0) / 100,
        'professional_score': ps.get('Professional', 0) / 100,
        'aggressive_score':   ps.get('Aggressive', 0) / 100,
        'emotional_score':    ps.get('Emotional', 0) / 100,
        'analytical_score':   ps.get('Analytical', 0) / 100,
        'assertive_score':    ps.get('Assertive', 0) / 100,
        'happy_score':        es.get('Happy', 0) / 100,
        'sad_score':          es.get('Sad', 0) / 100,
        'angry_score':        es.get('Angry', 0) / 100,
        'neutral_score':      es.get('Neutral', 0) / 100,
        'excited_score':      es.get('Excited', 0) / 100,
    }

CHAT_KB = {
    'hello': "Hello! 👋 I'm your AI Communication Assistant. Ask me anything about personality types, emotions, or communication strategies!",
    'hi':    "Hi there! 😊 Ready to explore your personality and communication style?",
    'help':  "I can help you understand personality types, emotion detection, tone analysis, and give communication tips. What would you like to know?",
    'personality': "Personality types reveal how we communicate. Our AI detects: Friendly 😊, Professional 👔, Analytical 🧠, Assertive 💪, Emotional 💖, and more — each with unique strengths.",
    'emotion': "Emotions detected include: 😊 Happy, 😢 Sad, 😠 Angry, 😐 Neutral, 🤩 Excited, 😤 Frustrated, and 😕 Confused — each based on your word choices.",
    'analyze': "Go to the 'Analyze Text' section in your dashboard, paste any message or email, and hit Analyze. You'll get a full personality + emotion breakdown instantly!",
    'friendly': "Friendly communicators are warm, approachable, and build trust naturally. They use inclusive language, express gratitude, and make others feel valued. 😊",
    'professional': "Professional communicators are goal-driven, structured, and efficient. They excel in business contexts and focus on deliverables and strategy. 👔",
    'aggressive': "Aggressive communication can signal passion but may create conflict. Softening language and focusing on solutions helps transform this style positively. 💢",
    'analytical': "Analytical communicators back every point with facts and logic. They're great at problem-solving but benefit from adding emotional warmth to connect better. 🧠",
    'assertive': "Assertive communicators set clear expectations with confidence. The key is balancing assertiveness with empathy — be direct but always respectful. 💪",
    'tip': "Communication Tip 💡: Mirror the tone of your audience. If they're formal, be formal. If casual, relax your language. Adaptability is the #1 communication skill!",
    'improve': "To improve your communication: 1️⃣ Be clear and concise, 2️⃣ Listen actively, 3️⃣ Match your tone to the context, 4️⃣ Use empathetic language, 5️⃣ Give specific feedback.",
    'gcuf': "This project is developed by Hafsa Bibi (Roll: 610) and Muhammad Talha Rehman Khan (Roll: 598) under supervision of Miss Habiba Nadeem at GCUF Layyah Campus. 🎓",
}

def get_chat_response(message):
    ml = message.lower()
    for key, resp in CHAT_KB.items():
        if key in ml:
            return resp
    tips = [
        "Great question! Try using the Analyze Text feature to get a detailed personality breakdown of any message. 🧠",
        "Communication is a skill that improves with awareness. Our AI helps you see patterns you might not notice yourself! 📊",
        "Did you know? People with an Analytical personality style are 40% more likely to ask 'why' before 'how'. What's your style? 🔍",
        "Try pasting an email you wrote into the analyzer — the results might surprise you! ✉️",
        "Tip: The most effective communicators adapt their style based on their audience. Are you a natural adapter? 🎯",
    ]
    return random.choice(tips)
