"""
app.py — The heart of your Flask portfolio website.
This file starts the web server and tells Flask what page to show
when someone visits a specific URL (called a "route").
"""

from flask import Flask, render_template, request, flash, redirect, url_for

# Create the Flask app. __name__ tells Flask where to find your files.
app = Flask(__name__)
app.secret_key = "huma-portfolio-secret-key"  # Required for flash messages

# ── PROJECT DATA ──────────────────────────────────────────────────────────────
# This list holds your portfolio projects.
# Later you can move this to a database, but a list is perfect for a beginner.
PROJECTS = [
    {
        "id": 1,
        "title": "Weather CLI App",
        "description": "A command-line tool that fetches real-time weather data using the OpenWeatherMap API. Users can search any city and get temperature, humidity, and wind speed.",
        "tech": ["Python", "Requests", "API", "CLI"],
        "github": "https://github.com/yourusername/weather-cli",
        "demo": None,
        "emoji": "🌤️",
        "featured": True,
    },
    {
        "id": 2,
        "title": "Student Grade Tracker",
        "description": "A Python application that reads student grades from a CSV file, calculates averages, assigns letter grades, and generates a formatted summary report.",
        "tech": ["Python", "CSV", "File I/O", "OOP"],
        "github": "https://github.com/yourusername/grade-tracker",
        "demo": None,
        "emoji": "📊",
        "featured": True,
    },
    {
        "id": 3,
        "title": "Task Manager (To-Do App)",
        "description": "A Flask web app that lets users add, complete, and delete tasks. Data is stored in a local JSON file. Full CRUD operations with a clean UI.",
        "tech": ["Python", "Flask", "JSON", "HTML/CSS"],
        "github": "https://github.com/yourusername/task-manager",
        "demo": None,
        "emoji": "✅",
        "featured": True,
    },
    {
        "id": 4,
        "title": "Password Generator",
        "description": "A secure password generator with customizable length and character sets. Includes a strength checker and clipboard copy feature.",
        "tech": ["Python", "Secrets", "Tkinter"],
        "github": "https://github.com/yourusername/password-gen",
        "demo": None,
        "emoji": "🔐",
        "featured": False,
    },
    {
        "id": 5,
        "title": "Web Scraper — Job Listings",
        "description": "Scrapes job listings from a public board, filters by keyword, and exports results to a CSV file using BeautifulSoup and Requests.",
        "tech": ["Python", "BeautifulSoup", "Requests", "CSV"],
        "github": "https://github.com/yourusername/job-scraper",
        "demo": None,
        "emoji": "🕷️",
        "featured": False,
    },
    {
        "id": 6,
        "title": "Quiz Game — Python OOP",
        "description": "An interactive terminal quiz game built with Object-Oriented Programming concepts. Tracks scores, shuffles questions, and shows a final result summary.",
        "tech": ["Python", "OOP", "JSON", "CLI"],
        "github": "https://github.com/yourusername/quiz-game",
        "demo": None,
        "emoji": "🧠",
        "featured": False,
    },
]

SKILLS = {
    "Languages": ["Python", "HTML", "CSS", "JavaScript (basic)", "SQL (basic)"],
    "Frameworks & Tools": ["Flask", "Git", "GitHub", "VS Code", "Linux CLI"],
    "Concepts": ["OOP", "REST APIs", "Web Scraping", "File I/O", "Responsive Design"],
    "Currently Learning": ["Django", "PostgreSQL", "Docker", "React"],
}


# ── ROUTES (Pages) ────────────────────────────────────────────────────────────

@app.route("/")
def home():
    """Home page — first page visitors see."""
    featured = [p for p in PROJECTS if p["featured"]]
    return render_template("home.html", projects=featured)


@app.route("/about")
def about():
    """About Me page — education, skills, journey."""
    return render_template("about.html", skills=SKILLS)


@app.route("/projects")
def projects():
    """Projects page — all portfolio projects."""
    return render_template("projects.html", projects=PROJECTS)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Contact page — shows the form (GET) and processes it (POST).
    GET  = user is just visiting the page.
    POST = user submitted the form.
    """
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # Basic validation
        if not name or not email or not message:
            flash("Please fill in all fields.", "error")
        elif "@" not in email:
            flash("Please enter a valid email address.", "error")
        else:
            # In a real app you would send an email here using Flask-Mail.
            # For now we just show a success message.
            flash(f"Thanks {name}! Your message was received. I'll reply soon.", "success")
            return redirect(url_for("contact"))

    return render_template("contact.html")


# ── RUN THE APP ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # debug=True → auto-reloads when you save a file. Turn off in production!
    app.run(debug=True)
