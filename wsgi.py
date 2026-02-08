"""
WSGI Entry Point for Render Deployment
"""
import os
import sys

# Get the directory containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Add backend directory to Python path
BACKEND_DIR = os.path.join(BASE_DIR, 'backend')
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

# Now import from app package inside backend
from app import create_app

# Create the application instance
app = create_app(os.environ.get('FLASK_ENV', 'production'))

if __name__ == "__main__":
    app.run()
