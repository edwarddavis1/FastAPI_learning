# ChatBot App with Hugging Face Inference Providers

A web application that allows users to chat with Large Language Models (LLMs) using Hugging Face's **new Inference Providers system**.

## ✨ Features

-   Real-time chat interface with WebSocket communication
-   Integration with Hugging Face's **modern Inference Providers API**
-   Uses DeepSeek-V3 model for high-quality responses
-   Responsive design for desktop and mobile devices
-   OpenAI-compatible chat completion format

## 🔄 Recent Migration

This app has been **successfully migrated** from the deprecated `api-inference.huggingface.co` to the new **Inference Providers system**, providing:

-   Better reliability and performance
-   Access to more models
-   Modern OpenAI-compatible API format
-   Improved error handling

## Prerequisites

-   Python 3.8 or higher
-   A Hugging Face API token (get it from [Hugging Face](https://huggingface.co/settings/tokens))
-   **Note**: For reliable usage, consider a [Hugging Face PRO subscription](https://huggingface.co/subscribe/pro) ($9/month with $2 inference credits)

## Installation

1. Clone the repository or navigate to the project folder

2. Install dependencies using uv (recommended):

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

3. Install additional dependencies for the new system:

```bash
uv add huggingface_hub
# or
pip install huggingface_hub
```

    .\venv\Scripts\activate
    ```

    - macOS/Linux:

    ```
    source venv/bin/activate
    ```

4. Install the required packages:

```
pip install -r requirements.txt
```

5. Set up your environment variables:
    - Open the `.env` file
    - Replace `your_huggingface_token_here` with your actual Hugging Face API token
        - You can get a token from [Hugging Face settings](https://huggingface.co/settings/tokens)
    - Optionally, change the `MODEL_ID` to use a different model

## Running the Application

Run the application with:

```
python run.py
```

Or alternatively:

```
uvicorn main:app --reload
```

The application will be available at http://localhost:8000

## Usage

1. Open your browser and navigate to http://localhost:8000
2. Type your message in the input field
3. Press the "Send" button or hit Enter to send the message
4. Wait for the AI to respond

## Customization

-   To change the model, update the `MODEL_ID` in the `.env` file
-   Modify the CSS in `app/static/css/styles.css` to change the appearance
-   Adjust model parameters in `main.py` to alter the AI's behavior

## License

This project is licensed under the MIT License.
