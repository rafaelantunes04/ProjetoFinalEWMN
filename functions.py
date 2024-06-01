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