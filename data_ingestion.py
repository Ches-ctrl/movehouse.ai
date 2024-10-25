import os
from getpass import getpass
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field
from camel.agents import ChatAgent
from camel.loaders import Firecrawl

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
firecrawl_api_key = os.getenv('FIRECRAWL_API_KEY')

firecrawl = Firecrawl()

firecrawl_response = firecrawl.crawl(url="https://www.camel-ai.org/about")

print(firecrawl_response["status"])

print(firecrawl_response["data"][0]["markdown"])

print("===========================")
print("========== Agent ==========")
print("===========================")

agent = ChatAgent(
    system_message="You're a helpful assistant",
    message_window_size=10, # [Optional] the length for chat memory
    )

response = agent.step(f"based on {firecrawl_response}, tell how what is CAMEL")
print(response.msgs[0].content)


print("===========================")
print("=== Structured Outputs ====")
print("===========================")

class ArticleSchema(BaseModel):
    title: str
    points: int
    by: str
    commentsURL: str


class TopArticlesSchema(BaseModel):
    top: List[ArticleSchema] = Field(
        ..., max_length=5, description="Top 5 stories"
    )


response = firecrawl.structured_scrape(
    url='https://news.ycombinator.com', response_format=TopArticlesSchema
)

print(response)
