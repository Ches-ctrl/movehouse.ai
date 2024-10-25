import os
import requests

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
    "url": "https://canadahvac.com/contact-hvac-canada/",
    "webhook_callback_url": None,
    "navigation_goal": "Fill out the contact us form and submit it. Your goal is complete when the page says your message has been sent.",
    "data_extraction_goal": None,
    "proxy_location": "RESIDENTIAL",
    "navigation_payload": {
        "name": "John Doe",
        "email": "john.doe@gmail.com",
        "phone": "123-456-7890",
        "message": "Hello, I have a question about your services."
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
