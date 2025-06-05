import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware


class Fruit(BaseModel):
    name: str


class Fruits(BaseModel):
    fruits: List[Fruit]


app = FastAPI()

origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# initialise the in-memory database (won't persist across restarts)
# init_fruit = Fruit(name="apple", color="green", weight=64)

memory_db = {"fruits": []}


@app.get("/fruits", response_model=Fruits)
def get_fruits():
    return Fruits(fruits=memory_db["fruits"])


@app.post("/fruits", response_model=Fruits)
def post_fruits(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return Fruits(fruits=memory_db["fruits"])


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
