import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,set_default_openai_client,set_default_openai_api, set_tracing_disabled
from agents.run import RunConfig
from dotenv import load_dotenv
import asyncio

load_dotenv()  

api_key = os.getenv("GEMINI_API_KEY")
GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")

set_default_openai_api("chat_completions")
# 1. Which LLM Service?
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=api_key,
    base_url=GEMINI_BASE_URL
)

set_default_openai_client(external_client)

# gemini-2.5 as agent brain - chat completions
math_agent: Agent = Agent(name="MathAgent",model="gemini-2.0-flash",instructions="You are a helpful math assistant.") 

async def main():
    result: Runner = await Runner.run(starting_agent=math_agent, input="what is your name?")
    print("\nCALLING AGENT\n")
    print(result)
    
if __name__ == "__main__":
    asyncio.run(main())