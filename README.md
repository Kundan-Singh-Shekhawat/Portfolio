# Kundan Singh Shekhawat | Python Full-Stack Developer Portfolio

Personal developer portfolio for **Kundan Singh Shekhawat** — a Python full-stack developer and B.Tech (CSE, AI & ML) student building REST APIs, React frontends, and ML inference services with FastAPI, Flask, Docker, and AWS EC2.

## Tech Stack

- **Backend:** Python 3, FastAPI, Uvicorn
- **Templating & UI:** Jinja2, Tailwind CSS (via CDN), Custom CSS (`public/css/styles.css`), Vanilla JavaScript (`public/js/main.js`)
- **Database & ORM:** SQLAlchemy 2.0, PostgreSQL (`psycopg2-binary`) in production, SQLite fallback (`portfolio.db`) for local development
- **Validation:** Pydantic v2 (`pydantic[email]`), `python-multipart`
- **Deployment:** Vercel Serverless Functions (`api/index.py` + `vercel.json`)

## Folder Structure

```text
portfolio/
├── api/index.py              # Vercel entry point: `from app.main import app`
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI app, mounts static files, includes routers
│   ├── config.py             # loads env vars (DATABASE_URL)
│   ├── database.py           # SQLAlchemy engine/session; uses DATABASE_URL or local SQLite fallback
│   ├── models.py             # ContactMessage (id, name, email, message, created_at)
│   ├── schemas.py            # Pydantic validation for the contact form
│   ├── routes/
│   │   ├── pages.py          # HTML routes: /, /projects, /projects/{slug}, /about, /contact
│   │   └── api.py            # JSON routes: GET /api/projects, POST /api/contact
│   └── data/projects.py      # Centralized site config, projects, skills, experience, education
├── templates/                # base.html, index.html, projects.html, project_detail.html, about.html, contact.html, 404.html
├── public/                   # css/styles.css, js/main.js, images/, resume.pdf
├── .env.example              # DATABASE_URL=
├── requirements.txt
├── vercel.json
└── README.md
```

## Featured Projects

1. **Malicious Link Detector** (`malicious-link-detector`) — ML Inference API built with FastAPI, scikit-learn, Pandas, Docker, and AWS EC2.
2. **Meeting Room Booking System** (`meeting-room-booking`) — Full-Stack Web App built with Python, Flask, SQLAlchemy, SQLite, React, and pytest.
3. **Web Interaction Bot Detector** (`web-interaction-bot-detector`) — Machine Learning session classifier built with Python, scikit-learn, Pandas, and NumPy.
4. **taskr** (`taskr`) — Command-Line Tool built with Python and JSON.

## Local Setup

1. **Create and activate the virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies inside the virtual environment:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables (optional for local dev):**

   ```bash
   cp .env.example .env
   ```
   Leave `DATABASE_URL` empty in `.env` to automatically use a local SQLite database (`portfolio.db`) during development.

4. **Run the development server:**

   ```bash
   uvicorn app.main:app --reload
   ```

5. **Open in your browser:**
   - Website: `http://127.0.0.1:8000`
   - JSON Projects API: `http://127.0.0.1:8000/api/projects`
   - Interactive OpenAPI Docs: `http://127.0.0.1:8000/docs`

## Environment Variables

| Variable | Description | Default (Local) |
| :--- | :--- | :--- |
| `DATABASE_URL` | PostgreSQL connection URL (`postgresql://user:pass@host:5432/db`) | Falls back to local `sqlite:///./portfolio.db` |

## Deploying on Vercel

1. Push this repository to GitHub.
2. Import the repository into [Vercel](https://vercel.com/new).
3. In your Vercel project settings, add the `DATABASE_URL` environment variable pointing to a managed PostgreSQL database (such as Neon, Supabase, or Railway).
4. Click **Deploy**. Vercel automatically uses `vercel.json` to bundle `templates/**` and `public/**` into the `api/index.py` serverless function and route all requests through FastAPI.

## Updating Content, Screenshots & Assets

All portfolio copy and metadata live in **`app/data/projects.py`**:

- **Profile Photo:** Save your portrait photo as `public/images/profile.jpg` (it will automatically replace the default `public/images/profile-avatar.svg` placeholder on the hero green circle).
- **Project Screenshots:** Drop project screenshots into `public/images/` and update each project's `image` path in `app/data/projects.py`.
- **Resume:** Replace `public/resume.pdf` with your latest PDF resume.
