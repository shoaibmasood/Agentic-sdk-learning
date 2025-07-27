import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()  

api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key= api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


response = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[{"role": "user", "content": "Say hello! I'm Shoaib"}]
)
print(response.choices[0].message.content)
