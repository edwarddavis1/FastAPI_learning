# %%
from huggingface_hub import InferenceClient
import os
import base64

# %%
# Hugging Face Inference Providers configuration
HF_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

# Initialize the InferenceClient for the new Inference Providers system
client = InferenceClient(api_key=HF_API_TOKEN) if HF_API_TOKEN else None
# %%
image_path = "imgs/panda.JPG"
with open(image_path, "rb") as f:
    base64_image = base64.b64encode(f.read()).decode("utf-8")
image_url = f"data:image/JPG;base64,{base64_image}"
# %%

client = InferenceClient("meta-llama/Llama-3.2-11B-Vision-Instruct")
completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": image_url},
                },
                {
                    "type": "text",
                    "text": "Describe this image in one sentence.",
                },
            ],
        },
    ],
)
bot_response = completion.choices[0].message.content
print(bot_response)
# %%
