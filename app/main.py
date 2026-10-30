"""FastAPI application entry point."""
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.config import PUBLIC_DIR, TEMPLATES_DIR
from app.data.projects import site
from app.database import Base, engine
from app.routes import api as api_router
from app.routes import pages as pages_router


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """Initialize database tables on startup."""
    try:
        Base.metadata.create_all(bind=engine)
    except Exception:
        # Ensure read-only environments never crash on startup if DB is unreachable
        pass
    yield


app = FastAPI(
    title=f"{site['name']} — {site['role']}",
    description=site["tagline"],
    version="1.0.0",
    lifespan=lifespan,
)

# Create tables eagerly as well for serverless environments where lifespan may be skipped
try:
    Base.metadata.create_all(bind=engine)
except Exception:
    pass

# Mount static assets from /public and /images
app.mount("/public", StaticFiles(directory=str(PUBLIC_DIR)), name="public")
app.mount("/images", StaticFiles(directory=str(PUBLIC_DIR / "images")), name="images")

# Include HTML and API routers
app.include_router(pages_router.router)
app.include_router(api_router.router)

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    """Render custom 404 HTML page for browser routes and JSON for /api/* routes."""
    if request.url.path.startswith("/api/"):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )
    if exc.status_code == 404:
        return templates.TemplateResponse(
            request,
            "404.html",
            {
                "request": request,
                "site": site,
                "page_title": f"404 Not Found — {site['name']}",
                "meta_description": "The page you are looking for does not exist.",
                "active_page": "",
            },
            status_code=404,
        )
    return HTMLResponse(content=str(exc.detail), status_code=exc.status_code)
