from flask import Flask
from flask_login import LoginManager
from config import Config
from models import db, User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    lm = LoginManager(app)
    lm.login_view = 'auth.login'
    lm.login_message = 'Please login to access the dashboard.'
    lm.login_message_category = 'info'

    @lm.user_loader
    def load_user(uid):
        return User.query.get(int(uid))

    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.dashboard import dashboard_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    with app.app_context():
        db.create_all()
        _seed()

    return app

def _seed():
    if not User.query.filter_by(email='admin@aipersonality.com').first():
        a = User(username='admin', email='admin@aipersonality.com',
                 full_name='System Administrator', role='admin')
        a.set_password('Admin@1234')
        db.session.add(a)
        db.session.commit()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
