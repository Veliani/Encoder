import os
from flask import Flask, render_template, request
import urllib.parse

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        repeat = int(request.form["repeat"])
        encoded = urllib.parse.quote(text)
        result = (encoded + "\n") * repeat
    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # <-- Ini wajib
    app.run(host="0.0.0.0", port=port)        # <-- Biar Render bisa akses
