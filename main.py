from fastapi import FastAPI, HTTPException, Query, Path, Body
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import uvicorn

# Create FastAPI instance
app = FastAPI(
    title="FastAPI Learning API",
    description="A comprehensive example API for learning FastAPI",
    version="1.0.0"
)

# Pydantic models for request/response validation
class User(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=100, description="User's full name")
    email: str = Field(..., description="User's email address")
    age: int = Field(..., gt=0, le=120, description="User's age")
    is_active: bool = Field(default=True, description="Whether the user is active")
    created_at: Optional[datetime] = None

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: str
    age: int = Field(..., gt=0, le=120)

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[str] = None
    age: Optional[int] = Field(None, gt=0, le=120)
    is_active: Optional[bool] = None

# In-memory database (for demo purposes)
fake_users_db: List[User] = [
    User(id=1, name="John Doe", email="john@example.com", age=30, created_at=datetime.now()),
    User(id=2, name="Jane Smith", email="jane@example.com", age=25, created_at=datetime.now()),
]

# 1. Basic GET endpoint
@app.get("/")
async def root():
    """
    Root endpoint - returns a welcome message
    """
    return {"message": "Welcome to FastAPI Learning API!"}

# 2. GET endpoint with path parameters
@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(..., gt=0, description="The ID of the user to retrieve")):
    """
    Get a specific user by ID
    """
    user = next((user for user in fake_users_db if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 3. GET endpoint with query parameters
@app.get("/users/", response_model=List[User])
async def get_users(
    skip: int = Query(0, ge=0, description="Number of users to skip"),
    limit: int = Query(10, gt=0, le=100, description="Number of users to return"),
    active_only: bool = Query(False, description="Filter only active users")
):
    """
    Get a list of users with pagination and filtering
    """
    users = fake_users_db
    
    if active_only:
        users = [user for user in users if user.is_active]
    
    return users[skip: skip + limit]

# 4. POST endpoint - Create new user
@app.post("/users/", response_model=User, status_code=201)
async def create_user(user: UserCreate):
    """
    Create a new user
    """
    # Check if email already exists
    if any(existing_user.email == user.email for existing_user in fake_users_db):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    new_id = max([user.id for user in fake_users_db], default=0) + 1
    new_user = User(
        id=new_id,
        name=user.name,
        email=user.email,
        age=user.age,
        created_at=datetime.now()
    )
    
    fake_users_db.append(new_user)
    return new_user

# 5. PUT endpoint - Update user
@app.put("/users/{user_id}", response_model=User)
async def update_user(
    user_id: int = Path(..., gt=0),
    user_update: UserUpdate = Body(...)
):
    """
    Update an existing user
    """
    user = next((user for user in fake_users_db if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update only provided fields
    update_data = user_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(user, field, value)
    
    return user

# 6. DELETE endpoint
@app.delete("/users/{user_id}")
async def delete_user(user_id: int = Path(..., gt=0)):
    """
    Delete a user
    """
    user_index = next((i for i, user in enumerate(fake_users_db) if user.id == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    deleted_user = fake_users_db.pop(user_index)
    return {"message": f"User {deleted_user.name} deleted successfully"}

# 7. Advanced endpoint with multiple parameters
@app.get("/users/{user_id}/profile")
async def get_user_profile(
    user_id: int = Path(..., gt=0),
    include_stats: bool = Query(False, description="Include user statistics")
):
    """
    Get user profile with optional statistics
    """
    user = next((user for user in fake_users_db if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    profile = {
        "user": user,
        "profile_url": f"/users/{user_id}/profile"
    }
    
    if include_stats:
        profile["stats"] = {
            "days_since_created": (datetime.now() - user.created_at).days if user.created_at else 0,
            "account_age_category": "New" if user.created_at and (datetime.now() - user.created_at).days < 30 else "Established"
        }
    
    return profile

# 8. Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now(),
        "total_users": len(fake_users_db)
    }

# Run the server
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

