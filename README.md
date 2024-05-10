# To-Do Manager Server

This is a simple API server to track your To Do tasks.
It is built as a backend service for [this React application](https://github.com/nilaster/todo_website).

## Installation

Clone the repository

```Bash
git clone https://github.com/nilaster/todo-server.git
```

## Create a virtual environment

It's recommended to use a virtual environment to isolate project dependencies. You can use tools like venv or virtualenv.

```Bash
python -m venv .venv
source .venv/bin/activate # For Linux/macOS
.venv\Scripts\activate.bat # For Windows
```

## Install dependencies

Install the required Python packages listed in requirements.txt.

```Bash
pip install -r requirements.txt
```

## Running Tests

Run the test suite with Django's built-in test runner:

```Bash
python manage.py test
```

## Running Locally

Apply database migrations

```Bash
python manage.py makemigrations
python manage.py migrate
```

## Start the development server

```Bash
python manage.py runserver
```

This will start the Django development server, usually accessible at http://127.0.0.1:8000/.

## Deployment

This server leverages GitHub Actions for a streamlined deployment process to AWS Elastic Beanstalk. Any push to the master branch will automatically trigger a build and deployment workflow.
