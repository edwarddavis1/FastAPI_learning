from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # When someone visits this path, the "root" function is run
def root():
    return {"Hello": "World"}


