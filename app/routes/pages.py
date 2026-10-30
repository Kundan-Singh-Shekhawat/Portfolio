"""HTML page routes for the portfolio website."""
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.config import TEMPLATES_DIR
from app.data.projects import (
    certifications,
    education,
    experience,
    get_project_by_slug,
    has_project_image,
    projects,
    site,
    skills,
    toolkit_bars,
)
from app.database import get_db
from app.models import ContactMessage
from app.schemas import ContactFormSchema

router = APIRouter()
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


def _base_context(request: Request, **kwargs) -> dict:
    """Build standard template context including global site metadata."""
    context = {
        "request": request,
        "site": site,
        "has_project_image": has_project_image,
    }
    context.update(kwargs)
    return context


@router.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    """Render the home page with hero, featured projects, skills, and impact stats."""
    main_projects = [p for p in projects if not p.get("is_compact")]
    compact_projects = [p for p in projects if p.get("is_compact")]
    return templates.TemplateResponse(
        request,
        "index.html",
        _base_context(
            request,
            page_title=site["page_title"],
            meta_description=site["meta_description"],
            active_page="home",
            featured_projects=main_projects,
            compact_projects=compact_projects,
            all_projects_count=len(projects),
            skills=skills,
            toolkit_bars=toolkit_bars,
        ),
    )


@router.get("/projects", response_class=HTMLResponse)
async def projects_page(request: Request):
    """Render the full projects page (main cards + compact row for smaller projects)."""
    main_projects = [p for p in projects if not p.get("is_compact")]
    compact_projects = [p for p in projects if p.get("is_compact")]
    return templates.TemplateResponse(
        request,
        "projects.html",
        _base_context(
            request,
            page_title=f"Projects | {site['name']}",
            meta_description=site["meta_description"],
            active_page="projects",
            projects=projects,
            main_projects=main_projects,
            compact_projects=compact_projects,
        ),
    )


@router.get("/projects/{slug}", response_class=HTMLResponse)
async def project_detail_page(request: Request, slug: str):
    """Render an individual project's case study / detail page."""
    project = get_project_by_slug(slug)
    if not project:
        return templates.TemplateResponse(
            request,
            "404.html",
            _base_context(
                request,
                page_title=f"Project Not Found | {site['name']}",
                meta_description=site["meta_description"],
                active_page="projects",
            ),
            status_code=404,
        )

    other_projects = [p for p in projects if p["slug"] != slug]
    return templates.TemplateResponse(
        request,
        "project_detail.html",
        _base_context(
            request,
            page_title=f"{project['title']} | {site['name']}",
            meta_description=project["short_description"],
            active_page="projects",
            project=project,
            other_projects=other_projects,
        ),
    )


@router.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    """Render the about page with bio, grouped skills (no bars), experience, education, and certifications."""
    return templates.TemplateResponse(
        request,
        "about.html",
        _base_context(
            request,
            page_title=f"About | {site['name']}",
            meta_description=site["meta_description"],
            active_page="about",
            skills=skills,
            toolkit_bars=toolkit_bars,
            experience=experience,
            education=education,
            certifications=certifications,
            projects_count=len(projects),
        ),
    )


@router.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    """Render the contact page and form."""
    return templates.TemplateResponse(
        request,
        "contact.html",
        _base_context(
            request,
            page_title=f"Contact | {site['name']}",
            meta_description=site["meta_description"],
            active_page="contact",
            success=False,
            errors=[],
            form_data={"name": "", "email": "", "message": ""},
        ),
    )


@router.post("/contact", response_class=HTMLResponse)
async def submit_contact_form(
    request: Request,
    name: str = Form(default=""),
    email: str = Form(default=""),
    message: str = Form(default=""),
    website: str = Form(default=""),
    db: Session = Depends(get_db),
):
    """Validate and store contact form submissions with honeypot spam protection."""
    form_data = {"name": name, "email": email, "message": message}

    # Honeypot check: if hidden 'website' field is filled by a bot, silently succeed
    if website and website.strip():
        return templates.TemplateResponse(
            request,
            "contact.html",
            _base_context(
                request,
                page_title=f"Contact | {site['name']}",
                meta_description=site["meta_description"],
                active_page="contact",
                success=True,
                errors=[],
                form_data={"name": "", "email": "", "message": ""},
            ),
        )

    try:
        validated = ContactFormSchema(
            name=name,
            email=email,
            message=message,
            website=website,
        )
    except ValidationError as exc:
        error_messages = []
        for err in exc.errors():
            field = err.get("loc", ["field"])[-1]
            msg = err.get("msg", "Invalid input.")
            error_messages.append(f"{str(field).capitalize()}: {msg}")
        return templates.TemplateResponse(
            request,
            "contact.html",
            _base_context(
                request,
                page_title=f"Contact | {site['name']}",
                meta_description=site["meta_description"],
                active_page="contact",
                success=False,
                errors=error_messages,
                form_data=form_data,
            ),
            status_code=422,
        )

    try:
        new_msg = ContactMessage(
            name=validated.name,
            email=str(validated.email),
            message=validated.message,
        )
        db.add(new_msg)
        db.commit()
        db.refresh(new_msg)
    except Exception:
        db.rollback()
        return templates.TemplateResponse(
            request,
            "contact.html",
            _base_context(
                request,
                page_title=f"Contact | {site['name']}",
                meta_description=site["meta_description"],
                active_page="contact",
                success=False,
                errors=["Could not save your message right now. Please try again or email directly."],
                form_data=form_data,
            ),
            status_code=500,
        )

    return templates.TemplateResponse(
        request,
        "contact.html",
        _base_context(
            request,
            page_title=f"Contact | {site['name']}",
            meta_description=site["meta_description"],
            active_page="contact",
            success=True,
            errors=[],
            form_data={"name": "", "email": "", "message": ""},
        ),
    )
