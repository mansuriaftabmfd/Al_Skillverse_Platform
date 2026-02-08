"""
Application Entry Point for Render Deployment
This file exists at root level to support: gunicorn "application:create_app()"
"""
import os
import sys

# Add backend directory to Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, 'backend')

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

# Now we can import from the app package inside backend
from app import create_app

# Create default app instance
app = create_app(os.environ.get('FLASK_ENV', 'production'))
