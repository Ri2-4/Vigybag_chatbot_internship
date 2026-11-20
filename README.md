# VigyBag Chatbot

An AI-powered customer support chatbot for **VigyBag**, built using Retrieval-Augmented Generation (RAG). The chatbot answers customer queries using the product's FAQ knowledge base and conversation history, providing contextual and relevant responses.

This project includes a modular AI pipeline and a REST API built with FastAPI.

## Features

- **Retrieval-Augmented Generation (RAG)** – Retrieves relevant FAQ information before generating responses.
- **Vector Search** – Uses ChromaDB for storing and retrieving FAQ embeddings.
- **Semantic Embeddings** – Uses Hugging Face sentence-transformer embeddings.
- **LLM Integration** – Supports multiple LLM providers with fallback handling.
- **Conversation Memory** – Maintains conversation history using session IDs.
- **FastAPI Backend** – Exposes chatbot functionality through REST API endpoints.
- **Input Validation** – Validates incoming requests using Pydantic.
- **Modular Architecture** – Separates loading, chunking, embeddings, retrieval, prompting, and response generation.
- **API Testing** – Includes tests for backend endpoints using pytest.

## Tech Stack

- Python
- FastAPI
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Google Gemini
- Groq
- Pydantic
- Pytest

## Project Structure

```text
ChatBot/
│
├── ai/
│   ├── chunking.py
│   ├── config.py
│   ├── embeddings.py
│   ├── ingest.py
│   ├── llm.py
│   ├── loader.py
│   ├── main.py
│   ├── memory.py
│   ├── prompt.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   └── schemas.py
│
├── providers/
│   ├── gemini.py
│   └── groq.py
│
├── data/
│   └── faq.json
│
├── tests/
│   └── test_api.py
│
├── app.py
├── requirements.txt
├── pytest.ini
└── .gitignore
```

## RAG Pipeline

The chatbot follows a Retrieval-Augmented Generation pipeline:

1. **User Query** – The user sends a question to the chatbot.
2. **Retrieval** – Relevant FAQ chunks are retrieved from ChromaDB.
3. **Context Formation** – Retrieved documents and conversation history are combined.
4. **Prompt Construction** – A contextual prompt is prepared for the language model.
5. **LLM Response Generation** – The configured LLM provider generates a response.
6. **Response** – The chatbot returns the answer to the user through the API.

```text
User Query
    ↓
Retriever (ChromaDB)
    ↓
Relevant FAQ Context
    ↓
Prompt + Conversation History
    ↓
LLM Provider
    ↓
Generated Answer
    ↓
API Response
```

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Ri2-4/Vigybag_chatbot_internship.git
cd Vigybag_chatbot_internship
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add the API keys required by the configured LLM providers.

```env
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file or expose API keys publicly.

### 5. Prepare the vector database

If the vector database has not been created yet, run:

```bash
python -m ai.ingest
```

This loads the FAQ data, processes and chunks the documents, generates embeddings, and stores them in ChromaDB.

> Embedding generation may take time and is subject to API/model limits.

## Running the API

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The API will run locally at:

```text
http://127.0.0.1:8000
```

### API Documentation

Interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative API documentation:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome endpoint |
| GET | `/api/v1/health` | Health check |
| POST | `/api/v1/chat` | Send a message to the chatbot |

### Chat API

**Endpoint**

```http
POST /api/v1/chat
```

**Request Body**

```json
{
  "message": "What is your return policy?",
  "session_id": "user_001"
}
```

**Example Response**

```json
{
  "success": true,
  "message": "Response generated successfully",
  "data": {
    "answer": "..."
  }
}
```

The `session_id` is used to associate messages with a conversation session.

## Testing

Run the API tests using:

```bash
pytest
```

## Environment & Security

- API keys should be stored in environment variables.
- `.env` files should never be committed.
- Chat histories are local and excluded from version control.
- Vector database files are stored locally and excluded from version control.

## Future Improvements

- Frontend integration
- Improved retrieval and reranking
- Enhanced conversation management
- Additional evaluation and monitoring
- Deployment to a cloud platform

---

## Author

Developed as part of the VigyBag chatbot internship project.
