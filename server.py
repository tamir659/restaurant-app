import os

from flask import Flask
from db import db
from routes.site import site_bp
from routes.staff import staff_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///restaurant.db')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-only-change-me')

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(site_bp)
app.register_blueprint(staff_bp)

if __name__ == '__main__':
    app.run(debug=True)
