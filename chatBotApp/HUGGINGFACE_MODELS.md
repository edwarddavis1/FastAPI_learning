# Using Hugging Face Models in the ChatBot App

This document provides guidance on how to use different Hugging Face models with this application.

## Getting a Hugging Face API Token

1. Create a Hugging Face account at [huggingface.co](https://huggingface.co)
2. Go to your profile settings: [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
3. Create a new token with read access
4. Copy the token and paste it in the `.env` file

## Available Models

Here are some recommended models you can use:

### Conversation Models

-   `google/gemma-7b-it` - Google's Gemma model with instruction tuning
-   `meta-llama/llama-2-7b-chat` - Meta's LLaMA 2 chat model
-   `mistralai/mistral-7b-instruct` - Mistral AI's instruction model
-   `tiiuae/falcon-7b-instruct` - Falcon instruction model

### Considerations for Model Selection

1. **API Access**: Some models require special access permissions. Make sure your Hugging Face account has access to the model you want to use.

2. **Model Size**: Larger models generally provide better responses but may have longer response times.

3. **Usage Quotas**: Be aware of Hugging Face's usage quotas for the Inference API.

## Changing the Model

To use a different model:

1. Open the `.env` file
2. Change the `MODEL_ID` value to your preferred model
3. Restart the application

Example:

```
MODEL_ID=mistralai/mistral-7b-instruct
```

## Adjusting Model Parameters

You can adjust model parameters in the `main.py` file. Look for the `payload` dictionary in the `websocket_endpoint` function.

Parameters to consider:

-   `max_new_tokens`: Controls the maximum length of the response
-   `temperature`: Controls randomness (higher = more random)
-   `top_p`: Controls diversity of responses
-   `do_sample`: Set to true for more creative responses

Example adjustment:

```python
payload = {
    "inputs": formatted_prompt,
    "parameters": {
        "max_new_tokens": 500,  # Increased from 250
        "temperature": 0.9,     # Increased from 0.7
        "top_p": 0.95,          # Increased from 0.9
        "do_sample": True
    },
    "options": {
        "wait_for_model": True
    }
}
```

## Local Models

For advanced users, it's possible to use this application with locally hosted models using projects like [text-generation-webui](https://github.com/oobabooga/text-generation-webui) or [llama.cpp server](https://github.com/ggerganov/llama.cpp/blob/master/examples/server/README.md).

To do this, you would need to:

1. Host your model locally with an API compatible with our implementation
2. Modify the API_URL in main.py to point to your local server
3. Adjust the payload format if necessary

## Troubleshooting

Common issues:

1. **"Error: Authorization header is required"** - Your Hugging Face API token is missing or incorrect

2. **"Error: Model [model_id] is currently loading"** - The model is being loaded on Hugging Face's servers. Wait a moment and try again.

3. **"Error: Rate limit reached"** - You've exceeded your usage quota. Wait or upgrade your Hugging Face account.

4. **Slow responses** - Larger models take longer to generate responses. Consider using a smaller model or adjusting `max_new_tokens`.
