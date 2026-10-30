"""Portfolio content and site configuration for Kundan Singh Shekhawat.

Edit this single file to update site metadata, projects, skills, experience,
education, and certifications.
"""
from pathlib import Path

_PUBLIC_IMAGES = Path(__file__).resolve().parent.parent.parent / "public" / "images"
_PROFILE_IMAGE = (
    "/public/images/profile.jpg"
    if (_PUBLIC_IMAGES / "profile.jpg").exists()
    else "/public/images/profile-avatar.svg"
)

site = {
    "name": "Kundan Singh Shekhawat",
    "first_name": "KUNDAN SINGH",
    "last_name": "SHEKHAWAT",
    "short_name": "KS",
    "monogram_first": "K",
    "monogram_last": "S",
    "role": "Python Full-Stack Developer",
    "page_title": "Kundan Singh Shekhawat | Python Full-Stack Developer",
    "meta_description": (
        "Python full-stack developer and B.Tech (CSE, AI & ML) student building "
        "REST APIs, React frontends, and ML inference services with FastAPI, Docker and AWS."
    ),
    "header_tagline": "Python full-stack developer building APIs and ML services",
    "header_tagline_top": "PYTHON FULL-STACK DEVELOPER",
    "header_tagline_bottom": "BUILDING APIS & ML SERVICES",
    "portfolio_year": "2026",
    "email": "kbtjodh@gmail.com",
    "location": "Jaipur, India · Open to remote",
    "availability": "Open to internships and full-time roles, graduating 2027",
    "tagline": (
        "I build REST APIs, React frontends, and ML-powered services that ship to production."
    ),
    "about_teaser": (
        "A selection of work across APIs, full-stack apps and machine learning."
    ),
    "bio_paragraphs": [
        (
            "Python full-stack developer and third-year B.Tech student (Computer Science, AI & ML) "
            "who builds REST APIs, React frontends, and database-backed applications. Experienced in "
            "integrating trained machine learning models into production-style services with FastAPI, "
            "Docker, and AWS EC2. Focused on clean API design, modular code structure, automated "
            "testing, and shipping working software end to end."
        ),
    ],
    "profile_image": _PROFILE_IMAGE,
    "resume_url": "/public/resume.pdf",
    "stats": [
        {"number": "4", "suffix": "", "label": "Projects Built"},
        {"number": "93", "suffix": "%", "label": "Model Accuracy"},
        {"number": "2", "suffix": "", "label": "Internships & Trainings"},
    ],
    "quote": {
        "text": "Build it, test it, ship it.",
    },
    "social": {
        "github": "https://github.com/Kundan-Singh-Shekhawat",
        "github_display": "github.com/Kundan-Singh-Shekhawat",
        "linkedin": "https://www.linkedin.com/in/kundan-singh-shekhawat-ai/",
        "linkedin_display": "linkedin.com/in/kundan-singh-shekhawat-ai",
        "email": "mailto:kbtjodh@gmail.com",
    },
}

projects = [
    {
        "slug": "malicious-link-detector",
        "short_title": "MALICIOUS LINK DETECTOR",
        "title": "Malicious Link Detector",
        "category": "ML Inference API",
        "short_description": (
            "A FastAPI service that accepts a URL, extracts features, and returns a "
            "malicious-probability score and a benign/malicious decision."
        ),
        "short_summary": "A FastAPI service that scores URLs as benign or malicious with an ML model.",
        "problem": (
            "Static keyword rules struggle to catch obfuscated phishing and malicious URLs, "
            "while offline models need a consistent serving schema and configurable decision "
            "thresholds to run reliably in production."
        ),
        "solution": (
            "Built a containerized FastAPI inference service that loads the trained TF-IDF "
            "Logistic Regression model once at startup, persists feature names for schema "
            "consistency, and exposes a configurable probability threshold deployed on AWS EC2."
        ),
        "features": [
            "Loads the trained TF-IDF Logistic Regression model once at startup for efficient inference",
            "Persists feature names so training and serving schemas stay consistent",
            "Configurable decision threshold, separating model confidence from decision policy",
            "Trained offline to 93% accuracy, 91% precision and 92% recall on the test set, up from a 72% accuracy keyword-based baseline",
            "Containerized with Docker, deployed on AWS EC2, interactive API docs via Swagger UI",
        ],
        "tech_stack": ["Python", "FastAPI", "scikit-learn", "Pandas", "Docker", "AWS EC2"],
        "image": "/images/projects/malicious-link-detector.png",
        "live_url": None,
        "github_url": "https://github.com/Kundan-Singh-Shekhawat/malicious-link-detector",
        "featured": True,
        "is_compact": False,
    },
    {
        "slug": "meeting-room-booking",
        "short_title": "MEETING ROOM BOOKING",
        "title": "Meeting Room Booking System",
        "category": "Full-Stack Web App",
        "short_description": (
            "A full-stack application with a Flask/SQLAlchemy backend and React frontend to "
            "view and create meeting rooms and book time slots without double-bookings or overlaps."
        ),
        "short_summary": "A Flask and React app for booking meeting rooms without double-bookings.",
        "problem": (
            "Room scheduling requires strict overlap prevention and a predictable API response "
            "contract so the frontend can reliably display rooms, bookings, and conflict errors."
        ),
        "solution": (
            "Engineered a Flask and SQLAlchemy backend with time-slot conflict rules isolated "
            "in a dedicated service layer, modular room and booking blueprints, a unified "
            "{data, error} JSON envelope for the React frontend, and automated pytest coverage."
        ),
        "features": [
            "REST endpoints with a unified {data, error} response envelope, giving the frontend one predictable place to parse results and errors",
            "Time-slot conflict logic isolated in a service layer, separate from Flask routing",
            "Routes split into room and booking modules for testability and easy extension",
            "Automated pytest tests covering the booking and conflict rules",
        ],
        "tech_stack": ["Python", "Flask", "SQLAlchemy", "SQLite", "React", "pytest", "REST APIs"],
        "image": "/images/projects/meeting-room-booking.png",
        "live_url": None,
        "github_url": "https://github.com/Kundan-Singh-Shekhawat/meeting-room-booking",
        "featured": True,
        "is_compact": False,
    },
    {
        "slug": "web-interaction-bot-detector",
        "short_title": "WEB INTERACTION BOT DETECTOR",
        "title": "Web Interaction Bot Detector",
        "category": "Machine Learning",
        "short_description": (
            "A behavior-based detector that classifies web sessions as human or bot from "
            "interaction patterns such as event timing, session duration, pages visited, and "
            "mouse/scroll activity."
        ),
        "short_summary": "A behavior-based detector that tells humans from bots using session patterns.",
        "problem": (
            "Automated bots can spoof standard HTTP headers, requiring behavioral session "
            "analysis with adjustable risk tolerance to balance false positives and false negatives."
        ),
        "solution": (
            "Developed a machine learning classifier driven by behavioral interaction features "
            "and probability thresholding, evaluated against synthetic sessions including fast "
            "humans and stealthy bots."
        ),
        "features": [
            "Built around probability scores with an adjustable threshold, so the action taken (block, CAPTCHA, log) can follow risk tolerance",
            "Synthetic sessions, including hard cases like fast humans and stealthy bots, used to test the trade-off between false positives and false negatives",
        ],
        "tech_stack": ["Python", "scikit-learn", "Pandas", "NumPy"],
        "image": "/images/projects/web-interaction-bot-detector.png",
        "live_url": None,
        "github_url": "https://github.com/Kundan-Singh-Shekhawat/web-interaction-bot-detector",
        "featured": True,
        "is_compact": False,
    },
    {
        "slug": "taskr",
        "short_title": "TASKR",
        "title": "taskr",
        "category": "Command-Line Tool",
        "short_description": (
            "A terminal task manager to add, list, complete, and delete tasks, stored in a "
            "local JSON file."
        ),
        "short_summary": "A terminal task manager to add, list, complete, and delete tasks, stored in a local JSON file.",
        "problem": (
            "Developers working in the terminal need a lightweight way to manage daily tasks "
            "locally without external services."
        ),
        "solution": (
            "Built a Python CLI tool supporting add, list, complete, and delete commands backed "
            "by a local JSON file."
        ),
        "features": [
            "Add, list, complete, and delete tasks directly from the terminal",
            "Persistent local task storage in a structured JSON file",
        ],
        "tech_stack": ["Python", "JSON"],
        "image": "/images/projects/taskr.png",
        "live_url": None,
        "github_url": "https://github.com/Kundan-Singh-Shekhawat/taskr",
        "featured": False,
        "is_compact": True,
    },
]

# Skills with levels shown as progress bars on the Home page
toolkit_bars = [
    {"name": "Python", "percent": 85},
    {"name": "FastAPI", "percent": 80},
    {"name": "Flask", "percent": 80},
    {"name": "SQL / SQLAlchemy", "percent": 75},
    {"name": "scikit-learn", "percent": 70},
    {"name": "React", "percent": 65},
    {"name": "Docker", "percent": 65},
]

# Grouped skills for the About page (no progress bars)
skills = {
    "Languages": [
        "Python",
        "JavaScript (React/JSX)",
        "C",
        "C++",
    ],
    "Backend & APIs": [
        "Flask",
        "FastAPI",
        "RESTful API Design",
        "Uvicorn",
        "Swagger/OpenAPI Docs",
        "Service Layer Architecture",
    ],
    "Frontend": [
        "React",
        "JSX Components",
        "REST API Consumption",
    ],
    "Databases & ORM": [
        "SQLite",
        "SQLAlchemy",
    ],
    "AI Integration": [
        "Serving ML Models as Inference APIs",
        "Probability Thresholding",
        "scikit-learn",
        "TF-IDF",
        "Logistic Regression",
        "Text Classification",
        "Generative AI Fundamentals",
    ],
    "Data & Libraries": [
        "Pandas",
        "NumPy",
        "Matplotlib",
    ],
    "Testing": [
        "pytest",
        "Unit Testing of Business Logic",
    ],
    "DevOps & Tools": [
        "Docker",
        "AWS EC2",
        "Git",
        "Linux",
    ],
}

experience = [
    {
        "role": "Data Science and Machine Learning with Gen AI, Intern",
        "company": "GRRAS Solutions Pvt. Ltd., Jaipur",
        "period": "May 2026 – Aug 2026",
        "highlights": [
            "Completed a four-month internship in Data Science and Machine Learning with Generative AI, awarded a Certificate of Internship with distinction.",
            "Completed the assigned project on time, with performance noted by the company as exceeding expectations.",
        ],
    },
    {
        "role": "Ethical Hacking Training",
        "company": "Internshala",
        "period": "Training",
        "highlights": [
            "Completed the training program and was recognized as a Top Performer.",
        ],
    },
]

education = [
    {
        "degree": "Bachelor of Technology (B.Tech), Computer Science Engineering (AI & ML)",
        "institution": "Jodhpur Institute of Engineering and Technology, Jodhpur, Rajasthan",
        "period": "Expected 2027",
    },
]

certifications = [
    "Certificate of Internship, Data Science and Machine Learning with Gen AI, GRRAS Solutions Pvt. Ltd. (Sep 2026)",
    "Soft Skill Development, NPTEL (IIT Kharagpur), Jan–Mar 2025",
    "C Programming Certification, Infosys",
    "Hack-ito 2.0 Participation, GDSC JIET (Sep 2023)",
]


def get_project_by_slug(slug: str):
    """Return a single project dict matching the given slug, or None."""
    for project in projects:
        if project["slug"] == slug:
            return project
    return None


def has_project_image(project: dict) -> bool:
    """Return True only when the project's image field is non-empty and the file exists on disk."""
    image_url = (project or {}).get("image") or ""
    if not image_url or not isinstance(image_url, str):
        return False
    public_root = _PUBLIC_IMAGES.parent
    rel = image_url.lstrip("/")
    if rel.startswith("public/"):
        rel = rel[len("public/"):]
    return (public_root / rel).is_file()

