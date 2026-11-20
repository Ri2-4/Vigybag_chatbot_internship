from pydantic import BaseModel, Field, field_validator


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="User message"
    )

    session_id: str = Field(
        ...,
        min_length=1,
        description="Unique session id"
    )

    @field_validator("message")
    @classmethod
    def validate_message(cls, value):
        if not value.strip():
            raise ValueError("Message cannot be empty.")
        return value

    @field_validator("session_id")
    @classmethod
    def validate_session_id(cls, value):
        if not value.strip():
            raise ValueError("Session ID cannot be empty.")
        return value


class ChatData(BaseModel):
    answer: str


class ChatResponse(BaseModel):
    success: bool
    message: str
    data: ChatData