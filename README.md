# Task Management API

A RESTful API for task management built with FastAPI and SQLModel, using PostgreSQL as the database backend. This API allows users to sign up, manage their profiles, and handle tasks with various operations.

## Features

- User creation (signup)
- User management (view, update, delete)
- Task management (create, read, update, delete)
- Asynchronous database operations
- PostgreSQL integration

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Oyshik-ICT/task-tracker.git

   cd task-tracker
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root with your PostgreSQL database URL:
   ```
   DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/database_name
   ```

## Database Migrations

This project uses Alembic for database migrations:

1. Initialize the database:
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```

2. Apply migrations:
   ```bash
   alembic upgrade head
   ```

## Running the Application

Start the FastAPI server:
```bash
uvicorn src:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### User Endpoints

#### Create a User
- **URL:** `/users/signup`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```
- **Success Response:** `201 Created`
- **Error Response:** `409 Conflict` if the user already exists

#### Get All Users
- **URL:** `/users/`
- **Method:** `GET`
- **Success Response:** `200 OK`
  ```json
  [
    {
      "uid": "uuid-string",
      "email": "user@example.com",
      "created_at": "2023-01-01T00:00:00"
    }
  ]
  ```

#### Get User by ID
- **URL:** `/users/{user_uid}`
- **Method:** `GET`
- **Success Response:** `200 OK`
- **Error Response:** `404 Not Found` if the user doesn't exist

#### Update User
- **URL:** `/users/{user_uid}`
- **Method:** `PATCH`
- **Request Body:**
  ```json
  {
    "email": "newemail@example.com",
    "password": "newpassword123"
  }
  ```
- **Success Response:** `200 OK`
- **Error Response:** `404 Not Found` if the user doesn't exist

#### Delete User
- **URL:** `/users/{user_uid}`
- **Method:** `DELETE`
- **Success Response:** `204 No Content`
- **Error Response:** `404 Not Found` if the user doesn't exist

### Task Endpoints

#### Create a Task
- **URL:** `/tasks/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "name": "Task Name",
    "description": "Task Description",
    "user_id": "user-uuid-string"
  }
  ```
- **Success Response:** `201 Created`

#### Get All Tasks
- **URL:** `/tasks/`
- **Method:** `GET`
- **Success Response:** `200 OK`
  ```json
  [
    {
      "uid": "task-uuid-string",
      "name": "Task Name",
      "description": "Task Description",
      "status": "pending",
      "user_id": "user-uuid-string",
      "created_at": "2023-01-01T00:00:00"
    }
  ]
  ```

#### Get Task by ID
- **URL:** `/tasks/{task_uid}`
- **Method:** `GET`
- **Success Response:** `200 OK`
- **Error Response:** `404 Not Found` if the task doesn't exist

#### Update Task
- **URL:** `/tasks/{task_uid}`
- **Method:** `PATCH`
- **Request Body:**
  ```json
  {
    "name": "Updated Task Name",
    "description": "Updated Task Description",
    "status": "in_progress"
  }
  ```
- **Success Response:** `200 OK`
- **Error Response:** `404 Not Found` if the task doesn't exist

#### Delete Task
- **URL:** `/tasks/{task_uid}`
- **Method:** `DELETE`
- **Success Response:** `204 No Content`
- **Error Response:** `404 Not Found` if the task doesn't exist


## Common Issues and Troubleshooting

- **Database Connection Issues**: Make sure PostgreSQL is running and your DATABASE_URL is correct in the .env file.
- **Migration Errors**: If you encounter migration errors, try deleting the migration versions and recreating them.
- **Dependency Errors**: Ensure all required packages are installed via `pip install -r requirements.txt`.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [PostgreSQL](https://www.postgresql.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)