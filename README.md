
# Vedic Dorm: Django-Based Hostel Management System

## Project Overview
**Vedic Dorm** is a hostel management system developed using Django. The system streamlines hostel operations such as room allocations, visitor requests, and administrative tasks. With an intuitive interface, it ensures smooth communication between students, parents, and administrators, enhancing the student living experience.

---

## Features
- **Room Allocation:** Easy and efficient management of hostel room assignments.
- **Visitor Requests:** Manage visitor permissions and logs.
- **Administrative Tasks:** Tools for hostel staff to handle daily operations efficiently.
- **User Roles:** Separate portals for students, parents, and administrators.

---

## Tools & Technologies
- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML, CSS

---

## Prerequisites
Ensure the following are installed on your system before proceeding:
- Python (Version 3.8 or higher)
- pip (Python package manager)
- Django (Version 4.0 or higher)
- Virtualenv (optional but recommended)

---

## Setup and Installation

1. **Clone the Repository**  
   Open your terminal and clone the project repository:
   ```bash
   git clone https://github.com/username/vedic-dorm.git
   cd vedic-dorm
   ```

2. **Create a Virtual Environment** (Optional but recommended)  
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install Required Dependencies**  
   Install the necessary Python libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Migration**  
   Set up the database by applying Django migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**  
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**  
   Open a web browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

---

## Project Structure
```
vedic-dorm/
│
├── vedic_dorm/                # Main project folder
│   ├── settings.py            # Project settings
│   ├── urls.py                # URL configurations
│   ├── wsgi.py                # WSGI application
│
├── hostel/                    # App for managing hostel features
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates
│   ├── views.py               # Application views
│   ├── models.py              # Database models
│   ├── urls.py                # App URL patterns
│
├── static/                    # Static files (CSS, images)
├── templates/                 # General templates
├── manage.py                  # Django management script
├── requirements.txt           # Dependencies list
```

---

## Usage
1. Log in or register as a student, parent, or administrator.
2. Manage room allocations, visitor requests, and administrative tasks through an intuitive dashboard.
3. Customize settings and manage user permissions based on your role.

---

## Contribution
To contribute to this project, fork the repository, make your changes, and create a pull request.

---

