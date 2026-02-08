"""
App Entry Point for Render Deployment
This file exists at root level to support: gunicorn "app:create_app()"
"""
import os
import sys

# Add backend directory to Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, 'backend')

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

# Import create_app from backend/app package
from app import create_app as _create_app

def create_app(config_name=None):
    """Wrapper for the actual create_app function"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'production')
    return _create_app(config_name)

# Also create an app instance for wsgi
app = create_app()
