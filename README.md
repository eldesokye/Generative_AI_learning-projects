# Generative_AI_learning-projects

# Generative AI Learning Projects 🚀

This repository is a **hands-on learning collection of Generative AI, LLMs, and LangChain projects**, covering everything from basic chatbot implementations to **RAG (Retrieval-Augmented Generation)**, **Conversational Q&A**, and **LCEL-based applications**.

It is structured as a modular playground for experimenting with **OpenAI, Ollama, LangChain, vector retrieval, and document-based Q&A systems**.

---

## 📁 Repository Structure

```text
.
├── 4.RAG Document Q&A
│   ├── research_papers
│   │   ├── Attention.pdf
│   │   └── LLM.pdf
│   └── app.py
│
├── building_chatbot
│   ├── 1-chatbots.ipynb
│   └── vectorRetriever.ipynb
│
├── Conversational_Q&A_chatbot
│   ├── 1-Langchain
│   └── conversation_Q&A.ipynb
│
├── langchain Projects
│   └── 1-Q&A Chatbot
│       ├── venv
│       ├── .env
│       ├── app.py
│       └── requirements.txt
│
├── LCEL
│   ├── serve.py
│   └── simplellmLCEL.ipynb
│
├── myenv311
│
├── ollama_llm
│   └── app.py
│
├── openai
│   ├── GettingStarted.ipynb
│   └── simple app.ipynb
│
├── Q&A chatbot
│   └── venv
│
├── .gitignore
└── LICENSE
✨ Key Features

🔹 LLM Fundamentals

Basic chatbot implementations

OpenAI API usage

Ollama local LLM integration

🔹 LangChain Projects

Prompt chaining

Conversational memory

Vector-based retrieval

Q&A chatbots

🔹 RAG (Retrieval-Augmented Generation)

Document ingestion (PDFs)

Vector stores

Research paper-based Q&A

🔹 LCEL (LangChain Expression Language)

Lightweight, composable LLM pipelines

Server-based deployment example

🧠 Technologies Used

Python 3.10+

LangChain

OpenAI API

Ollama

FAISS / Vector Retrieval

Jupyter Notebooks

dotenv

FastAPI / CLI apps (where applicable)

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/Generative_AI_learning-projects.git
cd Generative_AI_learning-projects

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


(Some projects maintain their own requirements.txt inside subfolders.)

🔑 Environment Variables

Create a .env file in the relevant project folder:

OPENAI_API_KEY=your_openai_api_key


For Ollama-based projects, ensure Ollama is running locally.

▶️ Running Projects
Example: RAG Document Q&A
cd "4.RAG Document Q&A"
python app.py

Example: LangChain Q&A Chatbot
cd "langchain Projects/1-Q&A Chatbot"
python app.py

Jupyter Notebooks
jupyter notebook

📌 Learning Goals

This repository is designed to:

Understand LLM workflows

Build real-world AI chatbots

Learn retrieval and document grounding

Experiment with local vs cloud LLMs

Practice LangChain best practices

🛣️ Future Improvements

 Add Streamlit UI for chatbots

 Add evaluation metrics

 Dockerize applications

 Centralized requirements management

 Deployment examples (AWS / GCP)

🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.

📄 License

This project is licensed under the MIT License.
See the LICENSE file for details.

👤 Author
Hesham Yahya Eldesoky
AI / ML Enthusiast | Generative AI Developer