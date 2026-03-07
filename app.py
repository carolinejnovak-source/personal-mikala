from flask import Flask, render_template, request, redirect, url_for, session, flash
from auth import login_required, check_credentials

app = Flask(__name__)
app.secret_key = "personal-mikala-secret-key-2026"

PROJECTS = [
    {
        "name": "Mom Radio 📻",
        "description": "Music discovery for millennial moms — 30 curated US & European songs, thumbs up/down reactions, and Spotify-style recommendations.",
        "url": "https://mom-radio.onrender.com",
        "status": "live",
    },
    {
        "name": "Personal Spending Dashboard",
        "description": "Monthly spending tracker with custom categories, drill-down charts, and Chase CSV import.",
        "url": "https://personal-spending.onrender.com",
        "status": "live",
    },
    {
        "name": "Stock Tracker 📈",
        "description": "Live stock prices, 1-year and 5-year averages, and interactive price history charts for 20 healthcare IT companies.",
        "url": "https://stock-tracker-d9xo.onrender.com",
        "status": "live",
    },
    {
        "name": "Mikala Spending 🌙",
        "description": "Monthly cost tracker for all Mikala-related subscriptions — Render, Hostinger, GitHub, SlyNumber, and Anthropic token spend.",
        "url": "https://mikala-spending.onrender.com",
        "status": "live",
    },
]

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        if check_credentials(username, password):
            session["logged_in"] = True
            session["username"] = username
            return redirect(request.args.get("next") or url_for("index"))
        flash("Invalid username or password.", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/")
@login_required
def index():
    return render_template("index.html", projects=PROJECTS)

if __name__ == "__main__":
    app.run(debug=True)        {
            "name": "Pasta Making Mastery",
            "url": "https://pasta-quiz.onrender.com",
            "description": "5 interactive quizzes to test your pasta making knowledge — from dough to sauce. Get a final score!",
            "status": "live",
        },
    ] flask import Flask, render_template, request, redirect, url_for, session, flash
from auth import login_required, check_credentials

app = Flask(__name__)
app.secret_key = "personal-mikala-secret-key-2026"

PROJECTS = [
    {
        "name": "Mom Radio 📻",
        "description": "Music discovery for millennial moms — 30 curated US & European songs, thumbs up/down reactions, and Spotify-style recommendations.",
        "url": "https://mom-radio.onrender.com",
        "status": "live",
    },
    {
        "name": "Personal Spending Dashboard",
        "description": "Monthly spending tracker with custom categories, drill-down charts, and Chase CSV import.",
        "url": "https://personal-spending.onrender.com",
        "status": "live",
    },
    {
        "name": "Stock Tracker 📈",
        "description": "Live stock prices, 1-year and 5-year averages, and interactive price history charts for 20 healthcare IT companies.",
        "url": "https://stock-tracker-d9xo.onrender.com",
        "status": "live",
    },
    {
        "name": "Mikala Spending 🌙",
        "description": "Monthly cost tracker for all Mikala-related subscriptions — Render, Hostinger, GitHub, SlyNumber, and Anthropic token spend.",
        "url": "https://mikala-spending.onrender.com",
        "status": "live",
    },
]

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        if check_credentials(username, password):
            session["logged_in"] = True
            session["username"] = username
            return redirect(request.args.get("next") or url_for("index"))
        flash("Invalid username or password.", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/")
@login_required
def index():
    return render_template("index.html", projects=PROJECTS)

if __name__ == "__main__":
    app.run(debug=True)
