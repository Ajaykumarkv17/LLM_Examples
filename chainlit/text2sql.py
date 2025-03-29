from openai import AsyncOpenAI

import os 
from dotenv import load_dotenv

load_dotenv()

# Load environment variables from .env file
api_key = os.getenv("GITHUB_API_KEY")
base_url = os.getenv("BASE_URL")
import chainlit as cl

cl.instrument_openai()

client = AsyncOpenAI(api_key=api_key ,base_url=base_url)

template = """SQL tables (and columns):
* Customers(customer_id, signup_date)
* Streaming(customer_id, video_id, watch_date, watch_minutes)

A well-written SQL query that {input}:
```"""


settings = {
    "model": "gpt-4o-mini",
}

@cl.set_starters
async def starters():
    return [
       cl.Starter(
           label=">50 minutes watched",
           message="Compute the number of customers who watched more than 50 minutes of video this month."
       )
    ]

@cl.on_message
async def main(message: cl.Message):
    stream = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": template.format(input=message.content),
            }
        ], stream=True, **settings
    )

    msg = await cl.Message(content="", language="sql").send()

    async for part in stream:
        if token := part.choices[0].delta.content or "":
            await msg.stream_token(token)

    await msg.update()