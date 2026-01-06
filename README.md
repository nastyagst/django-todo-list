# Django Todo List

A simple and functional Todo List application built with Django. It allows users to create, update, delete, and complete tasks, as well as manage tags.

## Features

* **Task Management:** Create, read, update, and delete tasks.
* **Status Toggling:** Easily mark tasks as "Done" or "Undo" them with a single click.
* **Smart Ordering:** Unfinished tasks are always displayed at the top.
* **Tag System:** Organize tasks by assigning multiple tags.
* **Deadlines:** Visual indicators for task deadlines (highlighted in red).
* **Responsive UI:** Clean and user-friendly interface using Bootstrap 5.

## Technologies

* Python
* Django
* SQLite
* Bootstrap 5

## Installation & Setup

Follow these steps to run the project locally:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nastyagst/django-todo-list.git
    cd django-todo-list
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # For Windows:
    venv\Scripts\activate
    # For Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6.  **Open the application:**
    Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)