"""
SkillVerse Application Entry Point

Run this file to start the application.

Author: SkillVerse Team
Purpose: Entry point for running the Flask application
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app import create_app
from backend.app.extensions import socketio

if __name__ == '__main__':
    """
    Run the application
    
    This block only executes when running this file directly
    (not when importing as a module)
    """
    
    # Get configuration from environment variable or use default
    config_name = os.environ.get('FLASK_ENV', 'development')
    
    # Create application instance
    app = create_app(config_name)
    
    # Run development server with SocketIO
    # In production, use a WSGI server like Gunicorn or uWSGI
    socketio.run(
        app,
        host='0.0.0.0',  # Listen on all network interfaces
        port=5000,        # Port number
        debug=app.config.get('DEBUG', False),
        allow_unsafe_werkzeug=True
    )
