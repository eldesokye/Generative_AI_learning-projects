from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os 
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]= os.getenv("OPEN_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
## langsmith Tracking 
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]= "true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["OPENAI_MODEL_NAME"]="openai/gpt-oss-20b:free"
groq_api_key= os.getenv("GROQ_API_KEY")  

model = ChatGroq(model = "openai/gpt-oss-20b",groq_api_key = groq_api_key)


## 1-create prompt template 

system_template = "translate the following into {language}:"
prompt_template = ChatPromptTemplate(
    [('system',system_template),
    ("user",'{text}')]
)
parser = StrOutputParser()

### create the chain 

chain = prompt_template|model|parser


## App definition 
app = FastAPI(title = "langchain server ",
              version="1.0",
              description = "A simple Api server using Lnagchain runnable interfaces")

# adding chain route
add_routes(
    app,
    chain,
    path='/chain'
)

if __name__== "__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)