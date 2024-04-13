from decouple import config
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
SECRET_KEY = config('OPENAI_API_KEY')

#LLMs
llm = OpenAI(openai_api_key=SECRET_KEY)
#response1 = llm.invoke("who is the PM of India ?")
#print(response1)

#chat models
chat = ChatOpenAI(openai_api_key=SECRET_KEY,model="gpt-3.5-turbo-0125")
messages = [
    SystemMessage(content="You're an advanced assistant"),
    HumanMessage(content="What doese DallE model do ?"),
]
response2 = chat.invoke(messages)
print(response2)