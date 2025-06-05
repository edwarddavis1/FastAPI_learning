# About this chatbot project

## Backend

In the backend I've used python and FastAPI.

**Python** was required to use the huggingface API, allowing for the catelogue of language models to be run on the hugging face cloud infrastructure. This is important because running these models locally is not feasible due to their size and resource requirements.

**FastAPI** was used to implement websockets which allows the backend and frontend to communicate in a two way, real-time system. This was preferred over a REST API, (one way, request-response), as websockets allows for instant delivery of messages (rather than checking every 2s for example) and is more efficient.

### Details

**Logging**

-   Logging was used as it is useful for aiding the debugging process - much better than just using a load of random print statements!
-   The logging for the app tracks _startup_, _HF API interactions_, _error handling_ and _response validation_.
-   E.g. whenever regular python code handles an exception, the error message is given to the logger via `logger.error(error_msg)`.

**`load_dotenv()`**

-   Handles secret variables - i.e. hugging face API key. This is stored in a `.env.` file, which is included in the `.gitignore`. This makes sure that the API key is never accidentally pushed to the public repo.

**WebSocket `ConnectionManager`**
