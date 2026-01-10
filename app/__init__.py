from flask import Flask
from app.config import Config
from app.models import db
from app.routes import init_routes
import os

def create_app(test_config=None):
    app = Flask(__name__)
    
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.update(test_config)
    
    db.init_app(app)
    init_routes(app)
    
    # TYLKO tworzenie tabel - bez łączenia z bazą
    with app.app_context():
        try:
            db.create_all()
        except:
            # Ignoruj błędy w testach
            pass
    
    return app