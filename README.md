# FastAPI Learning Project

This project demonstrates the fundamentals of FastAPI, a modern web framework for building APIs with Python.

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- uv (for dependency management)

### Installation
```bash
# Clone or navigate to the project directory
cd FastAPI_learning

# Install dependencies (already done if using uv)
uv sync
```

### Running the API
```bash
# Run the FastAPI server
python main.py

# Alternative using uvicorn directly
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at: http://127.0.0.1:8000

## 📚 FastAPI Concepts Explained

### 1. **FastAPI Instance**
```python
app = FastAPI(title="API Title", description="API Description")
```
- Creates the main application instance
- Can include metadata like title, description, version

### 2. **Pydantic Models**
```python
class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., gt=0, le=120)
```
- Used for request/response validation
- Automatic JSON serialization/deserialization
- Built-in validation with helpful error messages

### 3. **HTTP Methods & Decorators**
- `@app.get()` - Read data
- `@app.post()` - Create data
- `@app.put()` - Update data
- `@app.delete()` - Delete data

### 4. **Path Parameters**
```python
@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(..., gt=0)):
```
- Extract values from URL path
- Automatic validation and type conversion

### 5. **Query Parameters**
```python
@app.get("/users/")
async def get_users(skip: int = Query(0, ge=0), limit: int = Query(10, gt=0)):
```
- Optional parameters in URL query string
- Default values and validation

### 6. **Request Body**
```python
@app.post("/users/")
async def create_user(user: UserCreate):
```
- Automatically parsed from JSON
- Validated against Pydantic model

### 7. **Response Models**
```python
@app.get("/users/", response_model=List[User])
```
- Defines the structure of API responses
- Automatic serialization and documentation

## 🛠 API Endpoints

### Users API
- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /users/` - List users (with pagination)
- `GET /users/{user_id}` - Get specific user
- `GET /users/{user_id}/profile` - Get user profile
- `POST /users/` - Create new user
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user

## 🧪 Testing the API

### Interactive Documentation
Visit http://127.0.0.1:8000/docs for Swagger UI documentation where you can:
- See all endpoints
- Test API calls directly
- View request/response schemas

### Alternative Documentation
Visit http://127.0.0.1:8000/redoc for ReDoc documentation

### Programmatic Testing
```bash
# Run the test script
python test_api.py
```

### Manual Testing with curl
```bash
# Get all users
curl "http://127.0.0.1:8000/users/"

# Get specific user
curl "http://127.0.0.1:8000/users/1"

# Create new user
curl -X POST "http://127.0.0.1:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{"name": "New User", "email": "new@example.com", "age": 25}'

# Update user
curl -X PUT "http://127.0.0.1:8000/users/1" \
     -H "Content-Type: application/json" \
     -d '{"name": "Updated Name"}'
```

## 🔑 Key FastAPI Features Demonstrated

### 1. **Automatic Validation**
- Type hints automatically validate request data
- Helpful error messages for invalid input
- No need for manual validation code

### 2. **Automatic Documentation**
- Interactive API docs generated automatically
- Based on your code and type hints
- No separate documentation maintenance

### 3. **Editor Support**
- Full IDE support with autocompletion
- Type checking catches errors early
- Better development experience

### 4. **Performance**
- Built on Starlette and Pydantic
- Async/await support for high performance
- Comparable to Node.js and Go

### 5. **Standards-Based**
- OpenAPI (formerly Swagger) specification
- JSON Schema for data validation
- OAuth2, API keys, etc. for security

## 🎯 Next Steps

1. **Add Authentication**: Implement JWT tokens or API keys
2. **Database Integration**: Replace in-memory storage with SQLAlchemy
3. **Error Handling**: Add custom exception handlers
4. **Middleware**: Add logging, CORS, rate limiting
5. **Testing**: Write unit tests with pytest
6. **Deployment**: Deploy to cloud platforms

## 📖 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [OpenAPI Specification](https://swagger.io/specification/)

Happy coding! 🎉