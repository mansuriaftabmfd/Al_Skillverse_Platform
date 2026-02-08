"""
Application Entry Point for Render Deployment
Supports: gunicorn "app:create_app()"
"""
import os
import sys

# Add directories to Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, 'backend')
CORE_DIR = os.path.join(BACKEND_DIR, 'core')

# Add both backend and backend/core to path
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)
if CORE_DIR not in sys.path:
    sys.path.insert(0, CORE_DIR)

# Import create_app from backend/core package
from core import create_app

# Create app instance for gunicorn (app:app)
app = create_app(os.environ.get('FLASK_ENV', 'production'))
