#app.py
from ai.schemas import ChatRequest, ChatResponse, ChatData
from fastapi.middleware.cors import CORSMiddleware
from ai.config import API_TITLE, API_VERSION, ALLOWED_ORIGINS, API_PREFIX

from fastapi import FastAPI, HTTPException
import logging
from ai.rag_pipeline import generate_answer

logger = logging.getLogger(__name__)

app = FastAPI(title=API_TITLE,
    version=API_VERSION,)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home():
    return {"message": "Welcome to VigyBag Chatbot API"}

@app.get(f"{API_PREFIX}/health")
def health():
    return {
        "status": "healthy"
    }


@app.post(f"{API_PREFIX}/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:
        logger.info(f"Received request from session: {request.session_id}")
        answer = generate_answer(
            request.message,
            session_id=request.session_id,
        )

        return ChatResponse(
    success=True,
    message="Response generated successfully",
    data=ChatData(
        answer=answer
    )
    )

    except Exception as e:
        logger.exception(f"Failed to generate response: {e}")
        raise HTTPException(
        status_code=500,
        detail="Unable to process your request."
        )