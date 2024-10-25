import os
from getpass import getpass
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import ChatGPTConfig
from camel.agents import ChatAgent
from dotenv import load_dotenv

# Prompt for the API key securely
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

# Define a user message
usr_msg = 'I am entering the CAMEL-AI hackathon, what are some good ideas around multi-agent systems?'

# Sending the message to the agent
response = agent.step(usr_msg)

# Check the response (just for illustrative purpose)
print(response.msgs[0].content)
