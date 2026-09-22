from flask import Flask, render_template, request
import db

db.initialize()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        assert data.
        db.add_entry()
    return render_template("index.html")

app.run(debug=True)