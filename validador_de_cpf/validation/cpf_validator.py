import os

def start_validation( user_cpf):

    os.system("cls")

    #remove a pontuação caso tenha
    user_cpf = str(user_cpf)
    user_cpf = user_cpf.replace(".", "").replace("-", "")

    #verifica se o usuario digitou um cpf com 11 numeros
    if len(user_cpf) !=11:
        input("Erro: o CPF precisa conter 11 numeros")
        os.system("cls")
        return
        
    
    #metodo que valida o primeiro digito
    first_digit = validation_first_digit(user_cpf)

    #caso o resultado seja igual ao 10 numero caso não seja o cpf é invalido
    if first_digit != int(user_cpf[9]):
        input("CPF invalido" )
        return
    
    #metodo que valido o segundo digito
    second_digit = validation_second_digit(user_cpf)

    #caso o resultado do segundo digito seja igual ao 11 numero o cpf é valido
    if second_digit != int(user_cpf[10]):
        input("CPF invalido" )

    #caso seja verdadeira ambas operaçoes o CPF é valido
    input("CPF valido ")
    
#metodo que valida o primeiro digito
def validation_first_digit(user_cpf):

    #pega os 9 primeiro nuimeros do cpf
    cpf_9_numbers = user_cpf[:9]

    multiplied = 10

    cpf_number_sum = 0

    #multiplica e soma os numeros da esquerda para a direita de forma decressente começando do 10(de acordo com a regra de geração de cpf)
    for number in cpf_9_numbers:
        number = int(number)
        cpf_number_sum += (number * multiplied)
        multiplied -= 1

    #multiplica o reltado por 10 e depois tira o resto de 11
    cpf_number_sum = (cpf_number_sum * 10) % 11

    #caso o resto seja > 10 o numero se torna 0
    if cpf_number_sum > 9:
        cpf_number_sum = 0

   
    
    return cpf_number_sum


#metodo que valida o sefundo digito do cpf
def validation_second_digit(user_cpf):

    #pega os 10 primeiro nuimeros do cpf
    cpf_10_numbers = user_cpf[:10]

    multiplied = 11

    cpf_number_sum = 0

    #multiplica e soma os numeros da esquerda para a direita de forma decressente começando do 10(de acordo com a regra de geração de cpf)
    for number in cpf_10_numbers:
        number = int(number)
        cpf_number_sum += (number * multiplied)
        multiplied -= 1

    #multiplica o reltado por 10 e depois tira o resto de 11
    cpf_number_sum = (cpf_number_sum * 10) % 11

    #caso o resto seja > 10 o numero se torna 0
    if cpf_number_sum > 10:
        cpf_number_sum = 0

    return cpf_number_sum