# Smart Task Manager

A full-stack task management web application built using Flask, PostgreSQL, Pandas, NumPy, and WebSockets.

## Features

- User Registration & Login
- Task CRUD Operations
- Real-Time Notifications using SocketIO
- Analytics Dashboard
- PostgreSQL Database Integration
- Responsive Frontend UI

## Tech Stack

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Pandas
- NumPy
- SocketIO
- HTML/CSS/JavaScript

## Setup Instructions

### Clone Repository

```bash
git clone <your-github-link>
cd smart-task-manager
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create `.env`

```env
DATABASE_URL=postgresql://username@localhost/task_manager
SECRET_KEY=supersecretkey
JWT_SECRET_KEY=jwtsecretkey
```

### Run Application

```bash
python3 run.py
```

Application runs at:

```txt
http://127.0.0.1:5000
```

## Author

Khushi Kailasam