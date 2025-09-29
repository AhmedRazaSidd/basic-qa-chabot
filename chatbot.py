from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=GROQ_API_KEY,
    temperature=0
)

# Prompt Template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Answer in short and clear sentences."),
    ("user", "{question}")
])

# Function to ask a question
def ask_question(question: str) -> str:
    formatted_prompt = prompt_template.format_messages(question=question)
    response = llm.invoke(formatted_prompt)
    return response.content
