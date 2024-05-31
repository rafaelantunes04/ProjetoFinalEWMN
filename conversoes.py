def validar_binario(valor: str) -> bool:
    """
    Verifica se o valor fornecido é um número binário válido.
    """
    if not valor:
        return False  # Retorna False para entradas vazias

    ponto_decimal = valor.count(".")
    if ponto_decimal > 1:
        return False  # Retorna False se houver mais de um ponto decimal

    # Verifica se todos os dígitos são "0" ou "1", permitindo apenas um ponto decimal
    return all(digito in "01." for digito in valor)


def validar_decimal(valor: str) -> bool:
    """
    Verifica se o valor fornecido é um número decimal válido.
    """
    if not valor:
        return False  # Retorna False para entradas vazias

    try:
        float(valor)
        return True
    except ValueError:
        return False


def validar_hexadecimal(valor: str) -> bool:
    """
    Verifica se o valor fornecido é um número hexadecimal válido.
    """
    if not valor:
        return False  # Retorna False para entradas vazias

    ponto_decimal = valor.count(".")
    if ponto_decimal > 1:
        return False  # Retorna False se houver mais de um ponto decimal

    # Verifica se todos os dígitos são válidos para um número hexadecimal, permitindo apenas um ponto decimal
    return all(digito.upper() in "0123456789ABCDEF." for digito in valor)


def criar_tabela_gray(n):
    gray_table = ["0", "1"]
    for i in range(2, n + 1):
        gray_table = ["0" + code for code in gray_table] + ["1" + code for code in reversed(gray_table)]
    return gray_table


def binario_para_decimal(valor):
    """
    Converte um número binario para decimal
    """
    if not validar_binario(valor):
        return ("erro", "número introduzido não é binário")
    
    parte_inteira, parte_fracionaria = valor.split(".") if "." in valor else (valor, "0")
    decimal = 0
    for i, bit in enumerate(parte_inteira[::-1]):
        decimal += int(bit) * (2 ** i)
    for i, bit in enumerate(parte_fracionaria):
        decimal += int(bit) * (2 ** -(i + 1))
    return decimal


def binario_para_hexadecimal(valor):
    """
    Converte um número binario para hexadecimal
    """
    if not validar_binario(valor):
        return ("erro", "número introduzido não é binário")
    
    decimal = binario_para_decimal(valor)
    return decimal_para_hexadecimal(decimal)


def decimal_para_binario(valor):
    """
    Converte um número decimal para binario
    """
    if not validar_decimal(valor):
        return ("erro", "número introduzido não é decimal")

    parte_inteira = int(valor)
    parte_fracionaria = valor - parte_inteira
    parte_inteira_bin = ""
    while parte_inteira > 0:
        parte_inteira_bin = str(parte_inteira % 2) + parte_inteira_bin
        parte_inteira //= 2
    parte_fracionaria_bin = ""
    while parte_fracionaria > 0 and len(parte_fracionaria_bin) < 23:
        parte_fracionaria *= 2
        bit = int(parte_fracionaria)
        parte_fracionaria_bin += str(bit)
        parte_fracionaria -= bit
    return parte_inteira_bin + ("." + parte_fracionaria_bin if parte_fracionaria_bin else "")


def decimal_para_hexadecimal(valor):
    """
    Converte um número decimal para hexadecimal
    """
    if not validar_decimal(valor):
        return ("erro", "número introduzido não é decimal")
    
    parte_inteira = int(valor)
    parte_fracionaria = valor - parte_inteira
    parte_inteira_hex = ""
    while parte_inteira > 0:
        parte_inteira_hex = "0123456789ABCDEF"[parte_inteira % 16] + parte_inteira_hex
        parte_inteira //= 16
    parte_fracionaria_hex = ""
    while parte_fracionaria > 0 and len(parte_fracionaria_hex) < 23:
        parte_fracionaria *= 16
        digito = int(parte_fracionaria)
        parte_fracionaria_hex += "0123456789ABCDEF"[digito]
        parte_fracionaria -= digito
    return parte_inteira_hex + ("." + parte_fracionaria_hex if parte_fracionaria_hex else "")


def hexadecimal_para_binario(valor):
    """
    Converte de hexadecimal para binario
    """
    if not validar_hexadecimal(valor):
        return ("erro", "número introduzido não é hexadecimal")

    parte_inteira, parte_fracionaria = valor.split(".") if "." in valor else (valor, "0")
    hexadecimal_para_binario = {
        "0": "0000", "1": "0001", "2": "0010", "3": "0011",
        "4": "0100", "5": "0101", "6": "0110", "7": "0111",
        "8": "1000", "9": "1001", "A": "1010", "B": "1011",
        "C": "1100", "D": "1101", "E": "1110", "F": "1111"
    }
    binario = "".join(hexadecimal_para_binario[digito] for digito in parte_inteira.upper())
    binario_fracionario = "".join(hexadecimal_para_binario[digito] for digito in parte_fracionaria.upper())
    return binario + ("." + binario_fracionario if parte_fracionaria != "0" else "")


def hexadecimal_para_decimal(valor):
    """
    Converte de hexadecimal para decimal
    """
    if not validar_hexadecimal(valor):
        return ("erro", "número introduzido não é decimal")

    parte_inteira, parte_fracionaria = valor.split(".") if "." in valor else (valor, "0")
    parte_inteira = parte_inteira.upper()
    parte_fracionaria = parte_fracionaria.upper()
    decimal = 0
    for i in range(len(parte_inteira)):
        decimal += "0123456789ABCDEF".index(parte_inteira[i]) * (16 ** (len(parte_inteira) - i - 1))
    for i in range(len(parte_fracionaria)):
        decimal += "0123456789ABCDEF".index(parte_fracionaria[i]) * (16 ** -(i + 1))
    return decimal



def operar(base: str, valor1: str, valor2: str, operacao: str) -> str:
    resultado = ""
    vem_um = False
    virgula = False

    # Trocar , por . caso existir
    if "," in valor1:
        valor1 = valor1.replace(",", ".")
    if "," in valor2:
        valor2 = valor2.replace(",", ".")

    # Confirmação da operação
    if operacao not in ["+", "-"]:
        return "erro"

    # Verificar se tem Virgula
    if "." in valor1 or "." in valor2:
        virgula = True

    # Retornar o valor caso um deles for nulo
    if valor1 == "":
        if operacao == "-":
            valor2 = "-" + valor2
        return valor2
    if valor2 == "":
        return valor1

    # Diferenciação da base escolhida
    match base:
        # Caso for binário
        case "bin":
            # Validação de Binário
            if not validar_binario(valor1) or not validar_binario(valor2):
                return "erro"

            # Caso tiver Virgula
            if virgula:
                p_num = valor1.split(".")
                s_num = valor2.split(".")

                if len(p_num) < 2:
                    p_num.append("0")
                if len(s_num) < 2:
                    s_num.append("0")

                # Usar recursividade e repetir as contas para cada parte
                p_num_result = operar(base, p_num[0], s_num[0], operacao)
                s_num_result = operar(base, p_num[1], s_num[1], operacao)

                # Juntar as duas partes
                return p_num_result + "." + s_num_result

            # Caso for uma soma
            if operacao == "+":
                # Caso um número tiver mais dígitos que o outro, adicionar 0"s até terem o mesmo tamanho
                if len(valor1) > len(valor2):
                    while len(valor2) != len(valor1):
                        valor2 = "0" + valor2
                if len(valor1) < len(valor2):
                    while len(valor1) != len(valor2):
                        valor1 = "0" + valor1

                # O processo de soma dos valores
                for i in range(len(valor1)):
                    if vem_um:
                        if valor1[len(valor1)-1-i] == "0" and valor2[len(valor1)-1-i] == "0":
                            resultado = "1" + resultado
                            vem_um = False
                        elif valor1[len(valor1)-1-i] != valor2[len(valor1)-1-i]:
                            resultado = "0" + resultado
                        else:
                            resultado = "1" + resultado
                    else:
                        if valor1[len(valor1)-1-i] == "0" and valor2[len(valor1)-1-i] == "0":
                            resultado = "0" + resultado
                        elif valor1[len(valor1)-1-i] != valor2[len(valor1)-1-i]:
                            resultado = "1" + resultado
                        else:
                            resultado = "0" + resultado
                            vem_um = True
                if vem_um:
                    resultado = "1" + resultado
                return resultado

            # Caso for uma subtração
            if operacao == "-":
                # Caso um número tiver mais dígitos que o outro, adicionar 0"s até terem o mesmo tamanho
                if len(valor1) > len(valor2):
                    while len(valor2) != len(valor1):
                        valor2 = "0" + valor2
                if len(valor1) < len(valor2):
                    while len(valor1) != len(valor2):
                        valor1 = "0" + valor1

                # Fazer o complemento do valor2
                temp_var = ""
                for i in valor2:
                    if i == "0":
                        temp_var += "1"
                    else:
                        temp_var += "0"
                valor2 = temp_var

                # O processo de soma dos valores com o complemento
                vem_um = True # A soma do +1 do complemento
                for i in range(len(valor1)):
                    if vem_um:
                        if valor1[len(valor1)-1-i] == "0" and valor2[len(valor1)-1-i] == "0":
                            resultado = "1" + resultado
                            vem_um = False
                        elif valor1[len(valor1)-1-i] != valor2[len(valor1)-1-i]:
                            resultado = "0" + resultado
                        else:
                            resultado = "1" + resultado
                    else:
                        if valor1[len(valor1)-1-i] == "0" and valor2[len(valor1)-1-i] == "0":
                            resultado = "0" + resultado
                        elif valor1[len(valor1)-1-i] != valor2[len(valor1)-1-i]:
                            resultado = "1" + resultado
                        else:
                            resultado = "0" + resultado
                            vem_um = True
                if vem_um:
                    resultado = "1" + resultado
                return resultado

        # Caso for Decimal
        case "dec":
            # Validar se é decimal
            if not validar_decimal(valor1) or not validar_decimal(valor2):
                return "erro"

            if operacao == "+":
                return str(float(valor1) + float(valor2))
            elif operacao == "-":
                return str(float(valor1) - float(valor2))

        # Caso for Hexadecimal
        case "hex":
            lista_dec = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
            resultado = ""
            vem_um = False
            negativo = False

            # Validar se é hexadecimal
            if not validar_hexadecimal(valor1) or not validar_hexadecimal(valor2):
                return "erro"

            # Caso tiver virgula
            if virgula:
                p_num = valor1.split(".")
                s_num = valor2.split(".")

                if len(p_num) < 2:
                    p_num.append("")
                if len(s_num) < 2:
                    s_num.append("")

                # Usar recursividade e repetir as contas para cada parte
                p_num_result = operar(base, p_num[0], s_num[0], operacao)
                s_num_result = operar(base, p_num[1], s_num[1], operacao)

                # Juntar as duas partes
                return p_num_result + "." + s_num_result

            # Caso for soma
            if operacao == "+":
                for i in range(len(valor1)):
                    digit_sum = int(hexadecimal_para_decimal(valor1[len(valor1)-1-i])) + int(hexadecimal_para_decimal(valor2[len(valor2)-1-i]))
                    if vem_um:
                        digit_sum += 1
                    if digit_sum >= 16:
                        vem_um = True
                        digit_sum -= 16
                    else:
                        vem_um = False
                    resultado = lista_dec[digit_sum] + resultado
                if vem_um:
                    resultado = "1" + resultado
                return resultado

            # Caso for subtração
            elif operacao == "-":
                if len(valor1) < len(valor2):
                    valor1, valor2 = valor2, valor1
                    negativo = True
                elif len(valor1) == len(valor2):
                    if valor1 < valor2:
                        valor1, valor2 = valor2, valor1
                        negativo = True
                for i in range(len(valor1)):
                    digit_diff = int(hexadecimal_para_decimal(valor1[len(valor1)-1-i])) - int(hexadecimal_para_decimal(valor2[len(valor2)-1-i]))
                    if vem_um:
                        digit_diff -= 1
                    if digit_diff < 0:
                        vem_um = True
                        digit_diff += 16
                    else:
                        vem_um = False
                    resultado = lista_dec[digit_diff] + resultado
                if negativo:
                    return "-" + resultado
                return resultado
    return "erro"