from flask import Flask, render_template, request
from conversoes import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    valor1 = int(request.form["valor1"])
    valor2 = int(request.form["valor2"])
    resultado = valor1 + valor2
    return render_template("result.html", resultado=resultado)

@app.route("/gray", methods=["GET", "POST"])
def gray():
    resultado = ''
    if request.method == 'POST':
        bits = int(request.form["bits"])
        resultado = criar_tabela_gray(bits)
    return render_template("gray.html", resultado=resultado)

@app.route("/conversao", methods=["GET", "POST"])
def conversao():
    resultado = ''
    if request.method == 'POST':
        base_origem = request.form["base_origem"]
        base_destino = request.form["base_destino"]
        valor = request.form["valor"]

        if base_origem == 'bin' and base_destino == 'dec':
            resultado = binario_para_decimal(valor)
        elif base_origem == 'bin' and base_destino == 'hex':
            resultado = binario_para_hexadecimal(valor)
        elif base_origem == 'dec' and base_destino == 'bin':
            resultado = decimal_para_binario(float(valor))
        elif base_origem == 'dec' and base_destino == 'hex':
            resultado = decimal_para_hexadecimal(float(valor))
        elif base_origem == 'hex' and base_destino == 'bin':
            resultado = hexadecimal_para_binario(valor)
        elif base_origem == 'hex' and base_destino == 'dec':
            resultado = hexadecimal_para_decimal(valor)

    return render_template("conversao.html", resultado=resultado)

@app.route("/operacoes", methods=["GET", "POST"])
def operacoes():
    resultado = ''
    if request.method == 'POST':
        base = request.form["base"]
        operacao = request.form["operacao"]
        valor1 = request.form["valor1"]
        valor2 = request.form["valor2"]

        if base == 'bin':
            if operacao == '+':
                resultado = binario_para_decimal(valor1) + binario_para_decimal(valor2)
                resultado = decimal_para_binario(resultado)
            elif operacao == '-':
                resultado = binario_para_decimal(valor1) - binario_para_decimal(valor2)
                resultado = decimal_para_binario(resultado)
        elif base == 'dec':
            if operacao == '+':
                resultado = float(valor1) + float(valor2)
            elif operacao == '-':
                resultado = float(valor1) - float(valor2)
        elif base == 'hex':
            if operacao == '+':
                resultado = hexadecimal_para_decimal(valor1) + hexadecimal_para_decimal(valor2)
                resultado = decimal_para_hexadecimal(resultado)
            elif operacao == '-':
                resultado = hexadecimal_para_decimal(valor1) - hexadecimal_para_decimal(valor2)
                resultado = decimal_para_hexadecimal(resultado)

    return render_template("operacoes.html", resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
