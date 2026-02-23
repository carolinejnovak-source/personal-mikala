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
