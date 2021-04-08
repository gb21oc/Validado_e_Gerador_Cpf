def functionValidator(cpf):
    cpf = str(cpf)
    cpfSemPontos = cpf.replace("+", "").replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%",
            "").replace("¨", "").replace("&", "").replace("*", "").replace("(", "").replace(")", "").replace("_",
                "").replace("=", "").replace("§", "").replace("´", "").replace("`", "").replace("{", "").replace("}",
                     "").replace("ª", "").replace("[", "").replace("]", "").replace("º", "").replace("~",
                           "").replace("^", "").replace(":", "").replace(";", "").replace("/", "").replace("?",
                                "").replace("°", "").replace(".", "").replace("-", "")
    cpfNew = cpfSemPontos[:-2]
    reverse = 1
    total_result = []
    soma_valor = 0

    if not cpfSemPontos.isdigit():
        print("Please enter only number")
        exit()

    for cpf in cpfSemPontos[:-2]:
        result = (int(cpf) * int(reverse))
        total_result.append(result)
        reverse += 1

    for valor in total_result:
        soma_valor += valor

    total_result = []

    account = (soma_valor % 11)
    if account == 10:
        cpfNew += "0"
    else:
        cpfNew += f"{account}"

    reverse = 0

    for cpf in cpfNew:
        result = (int(cpf) * int(reverse))
        total_result.append(result)
        reverse += 1

    soma_valor = 0
    for valor in total_result:
        soma_valor += valor

    account = (soma_valor % 11)
    cpfNew += f"{account}"

    sequence = cpfNew == str(cpfNew[0]) * 11

    if cpfNew == cpfSemPontos and not sequence:
        print("CPF I accept")
    else:
        print("CPF invalid")
