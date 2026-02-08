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
SERVICES_DIR = os.path.join(CORE_DIR, 'services')

# Add all needed directories to path
for path in [BACKEND_DIR, CORE_DIR, SERVICES_DIR]:
    if path not in sys.path:
        sys.path.insert(0, path)

# Import create_app from backend/core package
from core import create_app

# Create app instance for gunicorn (app:app)
app = create_app(os.environ.get('FLASK_ENV', 'production'))
