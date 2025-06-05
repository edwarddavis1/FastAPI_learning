import os
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import logging
from pathlib import Path
from huggingface_hub import InferenceClient

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = FastAPI(title="ChatBot App with Hugging Face LLM")

# Mount static files
app.mount("/static", StaticFiles(directory=Path("app/static")), name="static")

# Templates
templates = Jinja2Templates(directory=Path("app/templates"))

# Hugging Face Inference Providers configuration
HF_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
MODEL_ID = os.getenv(
    "MODEL_ID", "deepseek-ai/DeepSeek-V3-0324"
)  # Using the working model from our tests

# Initialize the InferenceClient for the new Inference Providers system
client = InferenceClient(api_key=HF_API_TOKEN) if HF_API_TOKEN else None

if not HF_API_TOKEN:
    logger.error("HUGGINGFACE_API_TOKEN not found in environment variables!")
else:
    logger.info(f"Initialized InferenceClient with model: {MODEL_ID}")


class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)


manager = ConnectionManager()


async def query_huggingface(user_message):
    """
    Query the NEW Hugging Face Inference Providers API with the given message
    Uses the modern InferenceClient with chat completion format
    """
    try:
        if not client:
            return {
                "error": "InferenceClient not initialized. Check your HUGGINGFACE_API_TOKEN."
            }

        logger.info(f"Sending request to Hugging Face Inference Providers")
        logger.info(f"Model: {MODEL_ID}")
        logger.info(f"User message: {user_message}")

        # Use the new chat completion format (OpenAI-compatible)
        completion = client.chat.completions.create(
            model=MODEL_ID,
            messages=[{"role": "user", "content": user_message}],
            max_tokens=200,
            temperature=0.7,
        )
        # Extract the response
        bot_response = completion.choices[0].message.content

        if bot_response:
            logger.info(f"Received successful response: {bot_response[:100]}...")
            return {"response": bot_response}
        else:
            error_msg = "Received empty response from the model"
            logger.warning(error_msg)
            return {"error": error_msg}

    except Exception as e:
        error_msg = f"Exception occurred: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return {"error": error_msg}


@app.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "app_name": "My ChatBot", "model_name": MODEL_ID},
    )


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        conversation_history = []

        while True:
            data = await websocket.receive_text()
            user_message = data.strip()

            # Add user message to conversation history
            conversation_history.append({"role": "user", "content": user_message})

            # Send a "thinking" message
            await manager.send_message("Bot is thinking...", websocket)

            # Get response from Hugging Face Inference Providers
            response = await query_huggingface(user_message)
            # Extract bot's reply from the new response format
            if "error" in response:
                bot_reply = f"Error: {response['error']}"
                logger.error(f"Error from Hugging Face: {response['error']}")
            elif "response" in response and response["response"]:
                bot_reply = response["response"].strip()
            else:
                bot_reply = "Sorry, I couldn't understand the model's response."

            # Add bot reply to conversation history
            conversation_history.append({"role": "assistant", "content": bot_reply})

            # Send bot's reply to the client
            await manager.send_message(bot_reply, websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        logger.error(f"WebSocket error: {str(e)}", exc_info=True)
        try:
            await manager.send_message(f"Connection error: {str(e)}", websocket)
        except:
            pass
        manager.disconnect(websocket)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
