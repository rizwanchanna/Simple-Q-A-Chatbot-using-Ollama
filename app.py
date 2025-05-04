import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv



load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With Ollama"

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful massistant . Please  repsonse to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,llm,temperature,max_tokens):
    llm=Ollama(model=llm)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

# Load a fun icon 
st.set_page_config(page_title="Q&A Chatbot", page_icon="🤖", layout="centered")

# App title and description
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 Enhanced Q&A Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask anything and get instant answers powered by Ollama</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar controls
st.sidebar.header("⚙️ Configuration")
llm = st.sidebar.selectbox("Select Open Source Model", ["llama3"])
temperature = st.sidebar.slider("Creativity (Temperature)", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Response Length (Tokens)", min_value=50, max_value=300, value=150)

# Input field
st.markdown("### 💬 Talk to the Chatbot")
user_input = st.text_input("Type your question below:")

# Response area
if user_input:
    with st.spinner("Thinking... 🤔"):
        response = generate_response(user_input, llm, temperature, max_tokens)
        st.markdown("#### 🤖 Response:")
        st.success(response)
else:
    st.info("👆 Enter a question above to start chatting!")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: small;'>Made with ❤️ using Streamlit and Ollama</div>",
    unsafe_allow_html=True
)