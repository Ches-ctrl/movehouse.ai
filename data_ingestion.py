import os
from getpass import getpass
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field
from camel.loaders import Firecrawl

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
firecrawl_api_key = os.getenv('FIRECRAWL_API_KEY')

firecrawl = Firecrawl()

firecrawl_response = firecrawl.crawl(url="https://www.camel-ai.org/about")

print(firecrawl_response["status"])

print(firecrawl_response["data"][0]["markdown"])
