# config.py

import os
from dotenv import load_dotenv

load_dotenv()


# Providers in priority order
LLM_PRIORITY = os.getenv(
    "LLM_PRIORITY",
    "gemini"
).split(",")


# Models
GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-120b"
)

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4o-mini"
)


# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

API_TITLE = "VigyBag Chatbot API"
API_VERSION = "1.0.0"
API_PREFIX = "/api/v1"

ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
]

VECTOR_DB_PATH = "vectorstore/chroma_db"

MAX_MESSAGE_LENGTH = 1000


if __name__ == "__main__":
    print("Priority :", LLM_PRIORITY)
    print("Gemini   :", GEMINI_MODEL)
    print("Groq     :", GROQ_MODEL)
    print("OpenAI   :", OPENAI_MODEL)