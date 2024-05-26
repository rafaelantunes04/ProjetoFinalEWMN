from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calcular", methods=["POST"])
def calcular():
    valor1 = int(request.form["valor1"])
    valor2 = int(request.form["valor2"])

    resultado = valor1 + valor2

    return render_template("result.html", resultado=resultado)

@app.route("/")
def index():
    return render_template("index.html")