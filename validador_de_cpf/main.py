"""
Algoritmo que valida se o CPF do usuario digitado é valido ou não
"""
import os

from validation.cpf_validator import start_validation

while True:
    os.system("cls")    
    print("Digite [sair] para encerrar o programa.")
    user_cpf = input("Digite o CPF: ")

    if user_cpf.lower() == "sair":
        os.system("cls")
        print("Obrigado por usar")
        break
    else:
        start_validation(user_cpf)
    
    
    