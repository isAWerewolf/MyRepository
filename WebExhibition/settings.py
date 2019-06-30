import os
from WebExhibition import app

dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'DrivingConditions.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
