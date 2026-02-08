# SkillVerse - Professional Service Marketplace

SkillVerse is a comprehensive platform connecting skill providers with clients. Built with Flask, it features a modern, responsive UI, real-time chat, wallet system, and admin administration.

## 🚀 Features

*   **User Roles**: Admin, Service Provider, Client (Client converts to Provider automatically upon creating a service).
*   **Service Marketplace**: Browse, search, filter, and purchase services.
*   **Real-time Chat**: Socket.IO powered messaging system for orders.
*   **Wallet System**: Integrated wallet for managing earnings and payments.
*   **Admin Dashboard**: Manage users, services, requests, and platform analytics.
*   **AskVera AI**: AI-powered assistant for user help (Configurable).
*   **Responsive Design**: Mobile-first architecture with Dark/Light mode support.

## 📂 Project Structure

This project follows an industry-standard **split frontend/backend** architecture:

```
SkillVerse/
├── backend/                        # Server-side Logic (Flask)
│   ├── app/                        # Application Core
│   │   ├── __init__.py             # App Factory
│   │   ├── models.py               # Database Models (ORM)
│   │   ├── extensions.py           # Flask Extensions Init
│   │   ├── socket_events.py        # Socket.IO Event Handlers
│   │   ├── routes/                 # API & Page Controllers
│   │   │   ├── __init__.py
│   │   │   ├── web_routes.py       # Main Web Routes
│   │   │   └── chat_routes.py      # Chat API Routes
│   │   └── services/               # Business Logic Layer
│   │       ├── __init__.py
│   │       ├── business_service.py # Core Business Logic
│   │       ├── payment_service.py  # Payment & Wallet
│   │       ├── chat_service.py     # Chat Management
│   │       └── email_service.py    # Email Notifications
│   ├── scripts/                    # Utility Scripts
│   │   └── seed_database.py        # DB Initialization & Seeding
│   ├── config.py                   # Configuration Settings
│   ├── run.py                      # Application Entry Point
│   ├── Procfile                    # Render/Heroku Deployment
│   ├── .env.example                # Environment Template
│   └── requirements.txt            # Python Dependencies
│
├── frontend/                       # Client-side Assets
│   ├── templates/                  # HTML Templates (Jinja2)
│   │   ├── admin/                  # Admin Dashboard Views
│   │   ├── auth/                   # Authentication Views
│   │   ├── user/                   # User Dashboard Views
│   │   ├── emails/                 # Email Templates
│   │   ├── errors/                 # Error Pages (404, 500)
│   │   ├── legal/                  # Terms & Privacy Pages
│   │   ├── components/             # Reusable UI Components
│   │   ├── base.html               # Base Layout Template
│   │   ├── index.html              # Homepage
│   │   └── services.html           # Service Listing Page
│   ├── static/                     # Static Assets
│   │   ├── css/                    # Stylesheets
│   │   ├── js/                     # JavaScript Files
│   │   ├── images/                 # Static Images
│   │   ├── avatars/                # User Profile Pictures
│   │   ├── uploads/                # Service Images
│   │   └── portfolio/              # Portfolio Images
│   └── invoices/                   # Generated PDF Invoices
│
├── docs/                           # Project Documentation
├── .gitignore                      # Git Ignore Rules
├── README.md                       # Project Documentation
└── start.bat                       # Windows Quick Start Script
```

## 🛠️ Tech Stack

*   **Backend**: Python 3.8+, Flask, SQLAlchemy, Flask-SocketIO
*   **Frontend**: HTML5, CSS3, JavaScript (ES6+), Bootstrap 5
*   **Database**: PostgreSQL (Production) / SQLite (Development)
*   **Real-time**: WebSocket via Flask-SocketIO
*   **AI Integration**: Groq API (AskVera Chatbot)
*   **Email**: Flask-Mail with SMTP
*   **Deployment**: Gunicorn + Render

## 🏁 Quick Start

### Prerequisites
*   Python 3.8+
*   PostgreSQL (optional, defaults to SQLite)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd SkillVerse
    ```

2.  **Run the Quick Start Script** (Windows):
    ```bash
    .\start.bat
    ```
    This script will:
    *   Install dependencies from `backend/requirements.txt`
    *   Setup `backend/.env` file
    *   Initialize the database with seed data
    *   Start the development server

### Manual Setup

1.  Create virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate          # Windows
    source venv/bin/activate       # macOS/Linux
    ```

2.  Install dependencies:
    ```bash
    pip install -r backend/requirements.txt
    ```

3.  Configure Environment:
    ```bash
    cp backend/.env.example backend/.env
    ```
    Update `.env` with your credentials.

4.  Run Application:
    ```bash
    cd backend
    python run.py
    ```

### Default Admin Credentials
*   **Email**: `admin@skillverse.com`
*   **Password**: `admin123`

## 🌐 Deployment to Render

1.  Create a new **Web Service** on Render
2.  Connect your GitHub repository
3.  Configure:
    *   **Root Directory**: `backend`
    *   **Build Command**: `pip install -r requirements.txt`
    *   **Start Command**: `gunicorn "app:create_app()"`
4.  Add **Environment Variables**:
    | Variable | Description |
    |----------|-------------|
    | `DATABASE_URL` | PostgreSQL connection string |
    | `SECRET_KEY` | Random secret key |
    | `FLASK_ENV` | `production` |
    | `GROQ_API_KEY` | Groq API key (for AskVera) |

## 🤝 Contributing

1.  Fork the repository
2.  Create feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit changes (`git commit -m 'Add AmazingFeature'`)
4.  Push to branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

Proprietary Software. Internal Use Only.
