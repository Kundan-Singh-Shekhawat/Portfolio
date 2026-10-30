"""JSON API routes for projects and contact submissions."""
from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.data.projects import projects
from app.database import get_db
from app.models import ContactMessage
from app.schemas import ContactFormSchema

router = APIRouter(prefix="/api", tags=["api"])


@router.get("/projects")
async def api_list_projects():
    """Return the full list of portfolio projects as JSON."""
    return {
        "count": len(projects),
        "projects": projects,
    }


@router.post("/contact", status_code=status.HTTP_201_CREATED)
async def api_submit_contact(
    request: Request,
    db: Session = Depends(get_db),
):
    """Accept JSON or Form data for contact submissions, validate, and persist to DB."""
    content_type = request.headers.get("content-type", "")
    if "application/json" in content_type:
        try:
            payload = await request.json()
        except Exception as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid JSON payload.",
            ) from exc
    else:
        form = await request.form()
        payload = dict(form)

    try:
        validated = ContactFormSchema(**payload)
    except ValidationError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=exc.errors(),
        ) from exc

    # Honeypot spam check: return fake success without saving to DB
    if validated.website and validated.website.strip():
        return {
            "status": "ok",
            "message": "Thank you! Your message has been received.",
        }

    try:
        record = ContactMessage(
            name=validated.name,
            email=str(validated.email),
            message=validated.message,
        )
        db.add(record)
        db.commit()
        db.refresh(record)
    except Exception as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to save contact message.",
        ) from exc

    return {
        "status": "ok",
        "message": "Thank you! Your message has been saved.",
        "data": {
            "id": record.id,
            "name": record.name,
            "email": record.email,
            "created_at": record.created_at.isoformat() if record.created_at else None,
        },
    }
