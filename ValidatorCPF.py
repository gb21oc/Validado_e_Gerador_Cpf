from random import randint
from functionValidator import functionValidator

def validarCpf():
    gerarCpf = input("Do you want to generate a CPF?(Y/N)")
    if gerarCpf.upper() == 'Y':
        cpf = randint(10000000000, 99999999900)
        print(f"CPF generate: {cpf}")
        functionValidator(cpf)
    elif gerarCpf.upper() == "N":
        cpf = input("Enter the cpf: ")
        functionValidator(cpf)
    else:
        print("Type only y(ysm) or N(no)")


validarCpf()