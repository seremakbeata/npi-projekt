import pytest
from flask import Flask
from app.models import db

# Proste testy bez łączenia z bazą
def test_math():
    assert 1 + 1 == 2

def test_string():
    assert "hello".upper() == "HELLO"

def test_app_creation():
    # Test tworzenia aplikacji z konfiguracją testową
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    # Prosty endpoint testowy
    @app.route('/test')
    def test_route():
        return 'OK', 200
    
    with app.app_context():
        db.create_all()
    
    # Test klienta
    with app.test_client() as client:
        response = client.get('/test')
        assert response.status_code == 200
        assert response.data == b'OK'