# Task Manager

A simple and modern **Task Management Web Application** built using **Python Flask, SQLAlchemy, MySQL, HTML, and CSS**.

The application allows users to create an account, log in, create and organize tasks using categories and tags, and view their tasks through a clean, responsive interface.

## Features

* 🔐 User Registration
* 🔑 User Login and Logout
* 📝 Create Tasks
* 📋 View Personal Tasks
* 🗂️ Create and View Categories
* 🏷️ Add Tags to Tasks
* 👤 User-specific task management
* 💾 MySQL database integration
* 🛡️ Password validation and authentication
* 📱 Responsive and modern UI
* 🎨 Custom CSS styling
* 🔗 Flask/Jinja2 dynamic routing

## Tech Stack

### Backend

* Python
* Flask
* SQLAlchemy

### Database

* MySQL
* PyMySQL

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Development Tools

* Git
* GitHub
* Visual Studio Code

## Project Structure

```text
Task_management/
│
├── task_manager.py
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── create_task.html
│   ├── view_task.html
│   └── view_categories.html
│
├── static/
│   └── css/
│       └── style.css
│
├── requirements.txt
│
└── README.md
```

> The exact project structure may vary depending on your local setup.

## Application Pages

### Home

The home page provides access to the main task management functionality.

Users can:

* Create a task
* View existing tasks
* View categories
* Log out

### Registration

New users can create an account by providing:

* Username
* Email
* Password

The password must contain at least 8 characters.

### Login

Registered users can log in using:

* Username
* Email
* Password

### Create Task

Users can create a task by entering:

* Task title
* Description
* Category
* Tag

### View Tasks

The application displays tasks belonging to the currently logged-in user.

Each task displays information such as:

* Task ID
* Task title
* Description

### View Categories

Users can view the categories associated with their tasks.

Each category displays:

* Category name
* Category ID

## Database

The application uses **MySQL** for persistent data storage and **SQLAlchemy ORM** for database operations.

The database can contain tables for entities such as:

```text
Users
Tasks
Categories
```

A typical relationship is:

```text
User
 │
 ├── Tasks
 │
 └── Categories
```

This allows each user to manage their own tasks and categories.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Task_management.git
```

Move into the project directory:

```bash
cd Task_management
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet, install the main packages:

```bash
pip install Flask SQLAlchemy PyMySQL
```

## MySQL Configuration

Make sure MySQL Server is installed and running.

Create the database:

```sql
CREATE DATABASE tasks;
```

Configure your SQLAlchemy connection in the Flask application.

Example:

```python
DATABASE_URL = "mysql+pymysql://username:password@localhost/tasks"
```

Replace:

```text
username
password
```

with your MySQL credentials.

## Running the Application

Activate your virtual environment and run:

```bash
python task_manager.py
```

You should see something similar to:

```text
 * Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Basic Workflow

```text
Register
   ↓
Login
   ↓
Home
   ↓
Create Task
   ↓
Add Category & Tag
   ↓
View Tasks
   ↓
View Categories
```

## Security

The application includes basic authentication functionality.

Recommended improvements for production include:

* Password hashing
* Environment variables for database credentials
* Flask secret key stored securely
* CSRF protection
* Input sanitization
* Proper error handling
* Secure session configuration

## Future Improvements

Possible features that can be added in the future:

* ✅ Mark tasks as completed
* ✏️ Edit tasks
* 🗑️ Delete tasks
* 🔍 Search tasks
* 🔽 Filter tasks by category
* 📅 Add task deadlines
* 🚦 Add task priority
* 📊 Task statistics dashboard
* 🔔 Task reminders
* 🏷️ Improved tag management
* 🌙 Dark mode
* 👥 Multiple-user collaboration
* 🔒 Improved authentication and authorization

## Screenshots

You can add screenshots of your application here:

```markdown
## Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Login Page
![Login Page](screenshots/login.png)

### Create Task
![Create Task](screenshots/create_task.png)

### View Tasks
![View Tasks](screenshots/view_tasks.png)
```

Create a `screenshots` folder and place your screenshots inside it.

## Learning Objectives

This project demonstrates practical use of:

* Flask routing
* HTTP GET and POST requests
* HTML forms
* Jinja2 templates
* Flask sessions
* SQLAlchemy ORM
* MySQL database connectivity
* One-to-many relationships
* CRUD-oriented application design
* User authentication
* Frontend styling with CSS
* Git and GitHub

## Author

**Arya Churi**

MCA Student
Maharashtra, India

## License

This project is created for **educational and learning purposes**.

You are free to modify and improve the project for your own learning.
