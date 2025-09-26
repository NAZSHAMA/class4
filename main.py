from agents import Agent, Runner, function_tool
from connection import config
from datetime import datetime
config.GEMINI_API_KEY = "AIzaSyAUJNGvZRJvuHFN1qPndfNh2aWWf2R37Qs"

@function_tool
def get_date():
    _now = datetime.now()
    return_now.strftime(" the date is%Y-%m-%d ")

agent=Agent(
    name="assestant",
    instructions="You are a helpful assistant.",
    tools=[get_date]
)
result=Runner.run_sync(agent, "tell me the current date and time",)
print(result.final_output)
