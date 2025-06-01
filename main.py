from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Mount static files directory to serve HTML, CSS, JS files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_root():
    """Serve the main HTML page"""
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)


@app.get("/api/hello")
async def say_hello():
    """API endpoint that prints Hello and returns it"""
    message = "Hello"
    print(message)  # This prints to the console/terminal
    return {"message": message}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
