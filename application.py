from flask import Flask, render_template, request, session

app = Flask(__name__)
TEMPLATES_AUTO_RELOAD=True

@app.route("/")
def home():
    return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug=True)