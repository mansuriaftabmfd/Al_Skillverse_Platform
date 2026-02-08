"""
Application Entry Point for Render Deployment
Supports: gunicorn "app:create_app()"
"""
import os
import sys
import importlib.util

# Add backend directory to Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, 'backend')

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

# Load the app module from backend/app/__init__.py directly to avoid circular import
spec = importlib.util.spec_from_file_location(
    "backend_app", 
    os.path.join(BACKEND_DIR, 'app', '__init__.py')
)
backend_app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(backend_app)

# Get create_app function
create_app = backend_app.create_app
