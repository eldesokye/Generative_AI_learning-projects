import streamlit as st 
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os 
from dotenv import load_dotenv
load_dotenv()
 

os.environ["OPENAI_API_KEY"]= os.getenv("OPEN_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
## langsmith Tracking 
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]= "true"
os.environ["LANGCHAIN_PROJECT"]="Q&A Chatbot with OPENAI"
os.environ["OPENAI_MODEL_NAME"]="openai/gpt-oss-20b:free"

## prompt template 

prompt =ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant . Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,api_key,llm,temperature,max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(model=llm)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer = chain.invoke({"question":question})
    return answer


#### Title of the app 
st.title("Enhance Q&A Chatbot With OpenAI")


### Sidebar for settings 

st.sidebar.title("Settings")
api_key=st.sidebar.text_input ("Enter Your Open AI API key: " ,type = "password")

### Dropdown to select various Open AI models 

llm = st.sidebar.selectbox("select an open AI models",["amazon/nova-2-lite-v1:free","arcee-ai/trinity-mini:free","openai/gpt-oss-20b:free"])


### Adjust response parameter 
temperature = st.sidebar.slider("Temperature",min_value=0.0 , max_value=1.0, value=0.7)
max_tokens= st.sidebar.slider("Max Tokens",min_value=50 , max_value=300, value=150)

## Main interface for user input 

st.write("Go A head and ask any question : ")

user_input= st.text_input("YOu : ")


if user_input and api_key:
    response = generate_response(user_input,api_key , llm ,temperature,max_tokens )

    st.write(response)
elif user_input:
    st.warning("please enter the OpenAI api key in the sider bar")

else: 
    st.write("please provide the user input ")



