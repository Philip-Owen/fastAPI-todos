# FastAPI Todos

A REST API built with FastAPI to manage todos.

## How to run

- Clone this repo & navigate to directory
- 2 Options:
  - With Docker:
    - `docker build -t <imageName> .`
    - `docker run -p <yourPort>:8000 <imageName>`
  - Locally with Python 3:
    - Install dependencies:
      - `pip install requirements.txt`
    - Start the server:
      - `uvicorn main:app`

## How to use

- API is available at `http://127.0.0.1:8000`

  - Endpoints:
    - GET
      - `/` View all todos
      - `/in-progress` View all todos in progress
      - `/completed` View all todos completed
      - `/:id` View todo by ID
    - POST
      - `/add-todo` Add todo
    - PUT
      - `/:id/completed` Mark todo as completed
      - `/:id/in-progress` Mark todo as in progress
    - DELETE
      - `/all/delete` Delete all todos
      - `/:id/delete` Delete todo by ID

- Full API documentation is available at `http://127.0.0.1:8000/docs` for SwaggerUI and `http://127.0.0.1:8000/redoc` for ReDoc.
