import os
import requests
import json

from getpass import getpass
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field
from camel.agents import ChatAgent
from camel.loaders import Firecrawl

print("=======")
print("Loading")
print("=======")

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
firecrawl_api_key = os.getenv('FIRECRAWL_API_KEY')

firecrawl = Firecrawl()

firecrawl_response = firecrawl.crawl(url="https://www.rightmove.co.uk/property-for-sale/find.html?searchLocation=London&useLocationIdentifier=true&locationIdentifier=REGION%5E87490&radius=0.0&_includeSSTC=on&includeSSTC=false")

# firecrawl_response = firecrawl.crawl(url="https://www.camel-ai.org/about")

print(firecrawl_response["status"])

print(firecrawl_response["data"][0]["markdown"])

print("=======")
print("User input")
print("=======")

usr_msg = input('What criteria are important for you in a house? Price, square meters, description, number of bedrooms or number of bathrooms\n')

agent = ChatAgent(
    system_message="You're a helpful assistant",
    message_window_size=10,
    )

response = agent.step(f"based on {firecrawl_response}, choose the property that best fits your criteria: {usr_msg}")
print(response.msgs[0].content)

print("=======")
print("Task Submission")
print("=======")

url = agent.step(f"give me the url of the property that best fits your criteria: {usr_msg}").msgs[0].content

print(url)

usr_msg = input('What are your contact details? Name, email, phone number and message\n')

agent2 = ChatAgent(
    system_message="You're a helpful assistant",
    message_window_size=10,
    )

user_input = agent.step(f"Take the user input and structure it as an appropriate JSON with name, email, phone, message as the keys {usr_msg}. Only output JSON.")

print(user_input)

user_input_json = user_input.msgs[0].content

print(user_input_json)

# Define the API endpoint
url = "https://api.skyvern.com/api/v1/tasks"

# Set up the headers, including the API key for authentication
headers = {
    "Content-Type": "application/json",
    "x-api-key": os.getenv('SKYVERN_API_KEY')
}

# Define the payload data
data = {
    "title": None,
    "url": url,
    "webhook_callback_url": None,
    "navigation_goal": "Fill out the contact us form and submit it. Your goal is complete when the page says your message has been sent.",
    "data_extraction_goal": None,
    "proxy_location": "RESIDENTIAL",
    "navigation_payload": {
        "name": user_input_json["name"],
        "email": user_input_json["email"],
        "phone": user_input_json["phone"],
        "message": user_input_json["message"]
    },
    "extracted_information_schema": None,
    "totp_verification_url": None,
    "totp_identifier": None,
    "error_code_mapping": None
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Check the response
if response.status_code == 200:
    print("Request was successful.")
    print(response.json())  # Prints the response JSON if needed
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.json())  # Prints the error response JSON if needed
