"""SQLAlchemy database models."""
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database import Base


class ContactMessage(Base):
    """Stores contact form submissions."""

    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, index=True)
    message = Column(Text, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
