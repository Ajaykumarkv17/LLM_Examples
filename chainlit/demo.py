from openai import AsyncOpenAI


import chainlit as cl

cl.instrument_openai()

client = AsyncOpenAI(api_key="YOUR_OPENAI_API_KEY")