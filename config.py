import os
from dotenv import load_dotenv
load_dotenv()

def get_db_uri():
    db_uri = os.getenv('DATABASE_URI') or ""
    if "{DB_AUTH_TOKEN}" in db_uri and os.getenv('DB_AUTH_TOKEN'):
       return db_uri.replace('{DB_AUTH_TOKEN}', os.getenv('DB_AUTH_TOKEN') or "")
    return db_uri


class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = get_db_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv('FLASK_ENV') != 'production'
