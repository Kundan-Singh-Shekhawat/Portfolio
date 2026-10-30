"""Pydantic schemas for request validation and response serialization."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class ContactFormSchema(BaseModel):
    """Validates incoming contact form payloads."""

    name: str = Field(..., min_length=2, max_length=100, description="Sender name")
    email: EmailStr = Field(..., description="Sender email address")
    message: str = Field(..., min_length=10, max_length=5000, description="Message body")
    website: Optional[str] = Field(default="", description="Honeypot field for spam bots")

    @field_validator("name", "message")
    @classmethod
    def strip_whitespace(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("Field cannot be empty or whitespace only.")
        return cleaned


class ContactMessageResponse(BaseModel):
    """Serializes saved contact messages."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    message: str
    created_at: datetime
