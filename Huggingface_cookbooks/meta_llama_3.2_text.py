from huggingface_hub import InferenceClient

from dotenv import load_dotenv
import os
load_dotenv()

api_key=os.getenv("HUGGINGFACE_API_TOKEN")
client = InferenceClient(api_key=api_key)

for message in client.chat_completion(
	model="meta-llama/Llama-3.2-3B-Instruct",
	messages=[{"role": "user", "content": "What is the capital of France?"}],
	max_tokens=500,
	stream=True,
):
    print(message.choices[0].delta.content, end="")