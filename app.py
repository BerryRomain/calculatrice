from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    expression = ""
    if request.method == "POST":
        expression = request.form.get("expression", "")
        try:
            result = eval(expression)  # ⚠️ simplification, OK pour un petit projet
        except Exception:
            result = "Erreur"
    return render_template("index.html", result=result, expression=expression)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
