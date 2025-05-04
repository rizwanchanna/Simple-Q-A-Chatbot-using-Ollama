# 🤖 Enhanced Q&A Chatbot with Ollama

This project is a **Streamlit-based Q&A chatbot** powered by **open-source LLMs from Ollama**, designed to deliver quick and relevant answers to user queries. The application leverages LangChain to manage prompts and responses, and provides a clean, interactive interface for chatting.

---

## 🚀 Features

- ✅ Powered by Ollama (local LLMs like LLaMA 3)
- ✅ Uses LangChain for prompt management and output parsing
- ✅ Dynamic model configuration via sidebar
- ✅ Customizable creativity and response length
- ✅ Easy-to-use Streamlit UI

---

## 📦 Tech Stack

- [Streamlit](https://streamlit.io/) – Frontend interface  
- [Ollama](https://ollama.com/) – LLM runtime (e.g., LLaMA 3)  
- [LangChain](https://www.langchain.com/) – LLM orchestration  
- [Python](https://www.python.org/) – Backend logic  
- [dotenv](https://pypi.org/project/python-dotenv/) – Environment variable management

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/yourusername/qa-chatbot-ollama.git
cd qa-chatbot-ollama

### 2. Install Dependencies
Ensure you have Python 3.9+ and install required packages:
pip install -r requirements.txt

### 3. Setup Environment Variables
Create a .env file in the root directory:
LANGCHAIN_API_KEY=your_langchain_api_key

### 4. Run Ollama
Make sure you have Ollama installed and running, and download the desired model (e.g., LLaMA 3):
ollama run llama3

### 5. Launch the App
streamlit run app.py

## 🧠 How It Works
1. User types a question in the chat interface.

2. The question is passed through a prompt template.

3. LangChain constructs and executes a chain using the selected Ollama model.

4. Response is returned and rendered on the frontend.

## 📌 Notes
- This app currently supports llama3 by default. You can expand support to other Ollama models.

- LangChain tracing is enabled for debugging and insights.
