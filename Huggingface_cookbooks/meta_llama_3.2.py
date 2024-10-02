from huggingface_hub import InferenceClient

from dotenv import load_dotenv
import os
load_dotenv()

api_key=os.getenv("HUGGINGFACE_API_TOKEN")
client = InferenceClient(api_key=api_key)

image_url = "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"

for message in client.chat_completion(
	model="meta-llama/Llama-3.2-11B-Vision-Instruct",
	messages=[
		{
			"role": "user",
			"content": [
				{"type": "image_url", "image_url": {"url": image_url}},
				{"type": "text", "text": "Describe this image in one sentence."},
			],
		}
	],
	max_tokens=500,
	stream=True,
):
	print(message.choices[0].delta.content, end="")