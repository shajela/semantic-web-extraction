import os

from dotenv import load_dotenv
from langchain.chains import create_extraction_chain
from langchain_openai import ChatOpenAI

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(temperature=0, 
                 model="gpt-3.5-turbo-0613",
                 openai_api_key=openai_api_key)


def extract(content, schema):
    return create_extraction_chain(schema=schema, llm=llm).invoke(content)['text']
