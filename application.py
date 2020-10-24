from flask import Flask, render_template, request, session

app = Flask(__name__)
TEMPLATES_AUTO_RELOAD=True

@app.route("/")
def home():
    return render_template("home.html", title="Find Events")

@app.route("/favorites.html")
def favorites():
    return render_template("favorites.html", title="Favorite Events")

@app.route("/my-events.html")
def my_events():
    return render_template("my-events.html", title="My Events") 


@app.route("/calendar.html")
def calendar():
    return render_template("calendar.html")
    
if __name__ == "__main__":
    app.run(debug=True)