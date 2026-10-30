"""SQLAlchemy database engine and session management."""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import BASE_DIR, DATABASE_URL, IS_VERCEL

if DATABASE_URL:
    SQLALCHEMY_DATABASE_URL = DATABASE_URL
    connect_args = {}
elif IS_VERCEL:
    # Avoid writing to read-only filesystem on Vercel if DATABASE_URL is not configured
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
    connect_args = {"check_same_thread": False}
else:
    sqlite_path = BASE_DIR / "portfolio.db"
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{sqlite_path}"
    connect_args = {"check_same_thread": False}

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """FastAPI dependency that yields a SQLAlchemy database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
