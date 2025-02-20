# To-Do List Application

This is a simple to-do list application built with Flask, SQLAlchemy, and WTForms.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/todo-list-app.git
    cd todo-list-app
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Run the application:
    ```sh
    python manage.py
    ```

6. Open a web browser and go to `http://127.0.0.1:5000/` to view the application.

## Features

- Add tasks
- Edit tasks
- Delete tasks

## License

This project is licensed under the MIT License.
