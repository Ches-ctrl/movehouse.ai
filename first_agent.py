import os
from getpass import getpass
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import ChatGPTConfig
from camel.agents import ChatAgent
from camel.toolkits import MathToolkit, SearchToolkit
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

sys_msg = 'You are an expert at coming up with hackathon ideas for multi-agent systems'

# Define the model, here in this case we use gpt-4o-mini
model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig().as_dict(), # [Optional] the config for model
)

agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    message_window_size=10, # [Optional] the length for chat memory
)

# Pre-defined user message
# usr_msg = 'I am entering the CAMEL-AI hackathon, what are some good ideas around multi-agent systems?'

# Define a user message
usr_msg = input('Please enter your message for the agent: ')

# Sending the message to the agent
response = agent.step(usr_msg)

# Check the response (just for illustrative purpose)
print(response.msgs[0].content)

print("===========================")
print("======= Tool Calls ========")
print("===========================")

# =================

# Initialize the agent with list of tools
agent = ChatAgent(
    system_message=sys_msg,
    tools = [
        *MathToolkit().get_tools(),
        *SearchToolkit().get_tools(),
    ]
)

# Let agent step the message
response = agent.step("What is CAMEL AI?")

# Check tool calling
print(response.info['tool_calls'])

# Get response content
print(response.msgs[0].content)
