#!/usr/bin/env python3
"""
Simple script to test the FastAPI endpoints
"""
import requests
import json
from typing import Dict, Any

BASE_URL = "http://127.0.0.1:8000"

def test_endpoint(method: str, endpoint: str, data: Dict[Any, Any] = None, params: Dict[str, Any] = None):
    """Test an API endpoint and print the results"""
    url = f"{BASE_URL}{endpoint}"
    
    print(f"\n{'='*50}")
    print(f"Testing: {method.upper()} {endpoint}")
    print(f"URL: {url}")
    
    if params:
        print(f"Query params: {params}")
    if data:
        print(f"Request body: {json.dumps(data, indent=2)}")
    
    try:
        if method.lower() == "get":
            response = requests.get(url, params=params)
        elif method.lower() == "post":
            response = requests.post(url, json=data, params=params)
        elif method.lower() == "put":
            response = requests.put(url, json=data, params=params)
        elif method.lower() == "delete":
            response = requests.delete(url, params=params)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2, default=str)}")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the API. Make sure the server is running!")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Run API tests"""
    print("🚀 Testing FastAPI Learning API")
    print("Make sure your FastAPI server is running on http://127.0.0.1:8000")
    
    # Test basic endpoints
    test_endpoint("GET", "/")
    test_endpoint("GET", "/health")
    
    # Test user endpoints
    test_endpoint("GET", "/users/", params={"skip": 0, "limit": 5})
    test_endpoint("GET", "/users/1")
    test_endpoint("GET", "/users/1/profile", params={"include_stats": True})
    
    # Test creating a new user
    new_user = {
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "age": 28
    }
    test_endpoint("POST", "/users/", data=new_user)
    
    # Test updating a user
    update_data = {
        "name": "Alice Johnson (Updated)",
        "age": 29
    }
    test_endpoint("PUT", "/users/3", data=update_data)
    
    # Test filtering active users
    test_endpoint("GET", "/users/", params={"active_only": True})
    
    print(f"\n{'='*50}")
    print("✅ API testing complete!")
    print("Visit http://127.0.0.1:8000/docs to see the interactive API documentation")

if __name__ == "__main__":
    main()
