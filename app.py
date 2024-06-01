from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/gray", methods=["GET", "POST"])
def gray():
    return render_template("gray.html")

@app.route("/gray_resultado")
def gray_resultado():
    bits = request.args.get("bits")
    if not bits:
        bits = 0
    tabela = criar_tabela_gray(int(bits))
    if tabela[0] == "erro":
        print("erro")
    else:
        return render_template("gray_resultado.html", resultado=tabela)

@app.route("/conversao", methods=["GET", "POST"])
def conversao():
    resultado = ''
    if request.method == 'POST':
        base_origem = request.form["base_origem"]
        base_destino = request.form["base_destino"]
        valor = request.form["valor"]
        
        if base_origem == 'bin':
            if not validar_binario(valor):
                resultado="erro"
            elif base_destino == 'dec':
                resultado = binario_para_decimal(valor)
            elif base_origem == 'bin' and base_destino == 'hex':
                resultado = binario_para_hexadecimal(valor)
            else:
                resultado = valor
        elif base_origem == 'dec':
            if not validar_decimal(valor):
                resultado="erro"
            elif base_destino == 'bin':
                resultado = decimal_para_binario(float(valor))
            elif base_destino == 'hex':
                resultado = decimal_para_hexadecimal(float(valor))
            else:
                resultado = valor
        elif base_origem == 'hex':
            if not validar_hexadecimal(valor):
                resultado="erro"
            elif base_destino == 'bin':
                resultado = hexadecimal_para_binario(valor)
            elif base_destino == 'dec':
                resultado = hexadecimal_para_decimal(valor)
            else:
                resultado = valor
        else:
            return render_template("conversao.html", resultado="erro")

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
            if not validar_binario(valor1) or not validar_binario(valor2):
                resultado="erro"
            elif operacao == '+':
                resultado = binario_para_decimal(valor1) + binario_para_decimal(valor2)
                resultado = decimal_para_binario(resultado)
            elif operacao == '-':
                resultado = binario_para_decimal(valor1) - binario_para_decimal(valor2)
                resultado = decimal_para_binario(resultado)
        elif base == 'dec':
            if not validar_decimal(valor1) or not validar_decimal(valor2):
                resultado="erro"
            elif operacao == '+':
                resultado = float(valor1) + float(valor2)
            elif operacao == '-':
                resultado = float(valor1) - float(valor2)
        elif base == 'hex':
            if not validar_hexadecimal(valor1) or not validar_hexadecimal(valor2):
                resultado="erro"
            elif operacao == '+':
                resultado = hexadecimal_para_decimal(valor1) + hexadecimal_para_decimal(valor2)
                resultado = decimal_para_hexadecimal(resultado)
            elif operacao == '-':
                resultado = hexadecimal_para_decimal(valor1) - hexadecimal_para_decimal(valor2)
                resultado = decimal_para_hexadecimal(resultado)

    return render_template("operacoes.html", resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
