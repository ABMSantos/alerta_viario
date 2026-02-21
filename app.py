from flask import Flask, render_template, jsonify
from dados import pontos_criticos

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dados")
def dados():
    return jsonify(pontos_criticos)

if __name__ == "__main__":
    app.run(debug=True)