import os
import asyncio
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(disabled=True)

api_key = os.getenv("GEMINI_API_KEY")
GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")
# 1. Which LLM Service?
#Construct a new async AsyncOpenAI client instance.
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=api_key,
    base_url=GEMINI_BASE_URL)
# 2. Which LLM Model?
#Construct a new OpenAIChatCompletionsModel instance.
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)
# gemini-2.5 as agent brain - chat completions 
async def  main():
  # Create the Recipe Agent
  agent = Agent(
      name="RecipeBot",
      instructions=(
          """You are a helpful recipe assistant. A user will give you a few ingredients
          they have at home, and you will suggest one simple and quick recipe using only those items.
          Keep it short, step-by-step, and easy for beginners to cook."""
      ),
      model=llm_model
  )

  print("\n🍳 What can I cook today?\n")
  ingredients = "eggs, tomatoes, onions, and bread"
  result:Runner = await Runner.run(agent, f"I have these at home: {ingredients}. What can I cook?")

  print(result)
  print(result.final_output)
if __name__ == "__main__":
    asyncio.run(main())