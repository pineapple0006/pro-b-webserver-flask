from flask import Flask, render_template, request
import db

db.initialize()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        assert data["user"]
        assert data["quote"]
        assert data["quote_by"]
        db.add_entry(user=data["user"], quote=data["quote"], quote_by=data["quote_by"])
    query = request.args.get("query", "")
    return render_template("index.html", entries=db.get_entries(query))

app.run(debug=True)