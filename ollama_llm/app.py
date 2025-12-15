import os 
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import  streamlit as st 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


os.environ["OPENAI_API_KEY"]= os.getenv("OPEN_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
## langsmith Tracking 
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]= "true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["OPENAI_MODEL_NAME"]="openai/gpt-oss-20b:free"
 
## prompt Template 

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant . please response to the question asked"),
        ("user","Question:{question}")
    ]
)

## streamlit framework 

st.title("Langchain Demo with Google Gemma model")
input_text = st.text_input("what question you have in mind?")


## Ollama Llama2 model 
llm = Ollama(model = 'gemma3:1b')

output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))