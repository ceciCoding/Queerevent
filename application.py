from flask import Flask, render_template, request, session, url_for
app = Flask(__name__)
TEMPLATES_AUTO_RELOAD=True

@app.route("/")
def home():
    return render_template("home.html", title="Find Events")

@app.route("/landing.html")
def landing():
    return render_template("landing.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/create-account.html")
def create():
    return render_template("create-account.html")

@app.route("/account.html")
def account():
    return render_template("account.html")

@app.route("/edit.html")
def edit():
    return render_template("edit.html")

@app.route("/favorites.html")
def favorites():
    return render_template("favorites.html", title="Favorite Events")

@app.route("/my-events.html")
def my_events():
    return render_template("my-events.html", title="My Events") 

@app.route("/calendar.html")
def calendar():
    return render_template("calendar.html")

@app.route("/new.html")
def new_event():
    return render_template("new.html")

@app.route("/event.html")
def event():
    return render_template("event.html")
    
if __name__ == "__main__":
    app.run(debug=True)