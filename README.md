# 🤖 AI Chat App

A full-stack AI-powered chat application built with **React** and **Flask**, designed to provide an interactive conversational experience with AI models.

## 🚀 Features

* 🔐 User authentication and login
* 💬 AI-powered conversational chat
* 🤖 Support for multiple AI model providers
* 📝 Chat history management
* 📁 File upload support
* 🎤 Voice interaction support
* ⚡ React-based responsive frontend
* 🔧 Flask REST API backend
* 🔒 Environment-based API key configuration
* 📱 Clean and responsive user interface

## 🛠️ Technologies Used

### Frontend

* React
* JavaScript
* Vite
* HTML5
* CSS3

### Backend

* Python
* Flask
* REST API
* JWT Authentication

### AI Integration

* Google Gemini
* OpenAI
* Groq

### Development Tools

* Git
* GitHub
* VS Code
* Python Virtual Environment

## 📁 Project Structure

```text
AI-Chat-App-Starter/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── ...
│
├── .gitignore
├── README.md
└── .env.example
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Chat-App.git
cd AI-Chat-App
```

### 2. Backend Setup

Create and activate a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required Python packages:

```powershell
pip install -r backend/requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file inside the backend directory or project location according to the application's configuration.

Example:

```env
SECRET_KEY=your_secret_key
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

**Never commit your `.env` file or API keys to GitHub.**

### 4. Start the Backend

```powershell
cd backend
python app.py
```

The backend runs locally on:

```text
http://127.0.0.1:5000
```

### 5. Start the Frontend

Open another PowerShell terminal:

```powershell
cd frontend
npm install
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

## 🔄 Application Flow

```text
User
  ↓
React Frontend
  ↓
Flask REST API
  ↓
Authentication / Request Processing
  ↓
AI Model Provider
  ↓
AI Response
  ↓
React Chat Interface
```

## 🔐 Security

* API keys are stored using environment variables.
* `.env` files are excluded from Git using `.gitignore`.
* JWT-based authentication is used for protected requests.
* User-uploaded files are excluded from version control.

## 🎯 Project Purpose

This project was developed to understand and implement a complete **full-stack AI application**, including frontend development, backend REST APIs, authentication, AI model integration, file handling, and application deployment concepts.

## 📚 Learning Outcomes

Through this project, I gained practical experience with:

* Full-stack web application development
* React frontend development
* Flask backend development
* REST API integration
* JWT authentication
* AI API integration
* Environment variable management
* Git and GitHub version control
* Debugging and API testing
* Frontend-backend communication

## 👨‍💻 Author

**Kiran Mali**

* GitHub: https://github.com/KIRANMALI2004
* LinkedIn: https://linkedin.com/in/kiran-mali-375a28308

---

⭐ If you find this project useful, feel free to explore the repository.
