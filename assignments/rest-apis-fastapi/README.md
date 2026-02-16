# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework that demonstrates Create, Read, Update, and Delete (CRUD) operations, request validation, and error handling.

## 📝 Tasks

### 🛠️ Set Up FastAPI Project and Basic Routes

#### Description
Initialize a FastAPI application with basic project structure, install required dependencies, and create foundational endpoints to understand FastAPI routing and Pydantic models.

#### Requirements
Completed program should:

- Create a FastAPI application instance.
- Define a Pydantic model for data validation (e.g., `Item` or `Book` model).
- Implement a GET endpoint to retrieve all items/records.
- Implement a GET endpoint with path parameter to retrieve a single item by ID.
- Use `uvicorn` to run the server and test with OpenAPI documentation.


### 🛠️ Implement CRUD Operations

#### Description
Extend the API with complete Create, Read, Update, and Delete operations using in-memory storage (e.g., a list or dictionary) and proper HTTP status codes.

#### Requirements
Completed program should:

- Implement POST endpoint to create new items with request body validation.
- Implement PUT endpoint to update existing items by ID.
- Implement DELETE endpoint to remove items by ID.
- Return appropriate HTTP status codes (201 for created, 200 for success, 404 for not found, etc.).
- Include error handling for missing resources and invalid input.


### 🛠️ Add Advanced Features (Optional)

#### Description
Enhance the API with query parameters, filtering, and documentation examples.

#### Requirements
Completed program should:

- Add query parameters to filter items (e.g., `/items?skip=0&limit=10`).
- Include request and response examples in the model definitions.
- Add proper docstrings and tags to organize endpoints.
- Implement pagination for list endpoints.

## 🧰 Starter Files

- `starter-code.py` — minimal scaffold with FastAPI setup and TODO comments.

## ▶️ How to run

1. Install dependencies:
```bash
pip install fastapi uvicorn pydantic
```

2. Run the starter script:
```bash
python3 starter-code.py
```

Or use uvicorn directly:
```bash
uvicorn starter-code:app --reload
```

3. Access the API documentation at `http://localhost:8000/docs`

## 💡 Hints

- Use Pydantic BaseModel for request/response validation.
- Use path parameters `{item_id}` for identifying specific resources.
- Use request body with `Body(...)` for POST/PUT operations.
- The `@app.get()`, `@app.post()`, `@app.put()`, `@app.delete()` decorators define HTTP methods.
- FastAPI automatically generates OpenAPI documentation from your code.

## 🚀 Stretch Goals

- Add a SQLite database with SQLAlchemy ORM instead of in-memory storage.
- Implement authentication with JWT tokens.
- Add logging for API requests.
- Create a simple frontend to consume the API.
- Deploy to a cloud platform (Heroku, Railway, or Azure).

## 🎓 Learning Outcomes

- Understand REST API principles and HTTP methods.
- Work with FastAPI framework for rapid API development.
- Validate data with Pydantic models.
- Handle errors and edge cases gracefully.
- Leverage automatic OpenAPI documentation generation.
