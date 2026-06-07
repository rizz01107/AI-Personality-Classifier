import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gcuf-ai-personality-fyp-2024-super-secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ai_classifier.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/images/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
