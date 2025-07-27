# import requests
# url = "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true"
# resp = requests.get(url, timeout=10)
# resp.raise_for_status()
# weather = resp.json()
# print(weather)
import openai
from dotenv import load_dotenv
import os

load_dotenv() 

# Now you can use them
api_key = os.getenv("OPENAI_API_KEY")

# 🔑 TODO: Replace with your own key or set OPENAI_API_KEY in the environment
openai.api_key = api_key

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello! I'm Wania"}]
)
print(response.choices[0].message.content)