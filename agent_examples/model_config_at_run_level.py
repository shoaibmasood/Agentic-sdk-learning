import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv


load_dotenv()  

api_key = os.getenv("GEMINI_API_KEY")
GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")

# 1. Which LLM Service?
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=api_key,
    base_url=GEMINI_BASE_URL
)

# 2. Which LLM Model?
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

# gemini-2.5 as agent brain - chat completions
math_agent: Agent = Agent(name="MathAgent",instructions="You are a helpful math assistant.") 

def main():
    config = RunConfig(
        model=llm_model,
        model_provider = external_client,
        tracing_disabled=True
    )
    result: Runner = Runner.run_sync(math_agent, input="why learn math for AI Agents?", run_config=config)
    print("\nCALLING AGENT\n")
    print(result.final_output)

if __name__ == "__main__":
    main()