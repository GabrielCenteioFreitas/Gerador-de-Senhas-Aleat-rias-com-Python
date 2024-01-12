import random
import string
import time
import os
MIN_CARAC_SENHA = 6
MAX_CARAC_SENHA = 15
MIN_QNTD = 0
MAX_QNTD = MAX_CARAC_SENHA

def pedindo_infos():
    pre_senha = ""
    qntd_total = 0
    min = MIN_QNTD
    max = MAX_QNTD - qntd_total
    while True:
        time.sleep(0.2)
        qntd_minusculas = input(f"Quantidade de letras minúsculas [{min}-{max}]: ")
        if qntd_minusculas.isdigit():
            qntd_minusculas = int(qntd_minusculas)
            if min <= qntd_minusculas <= max:
                qntd_total += qntd_minusculas
                max = MAX_QNTD - qntd_total
                for _ in range(qntd_minusculas):
                    random_minusc = random.choice(string.ascii_lowercase)
                    pre_senha += random_minusc
                break
            else: print("\033[31mInsira um número válido.\033[0m")
        else: print("\033[31mInsira um número.\033[0m")
    if max != 0:
        while True:
            time.sleep(0.2)
            qntd_maiusculas = input(f"Quantidade de letras maiúsculas [{min}-{max}]: ")
            if qntd_maiusculas.isdigit():
                qntd_maiusculas = int(qntd_maiusculas)
                if min <= qntd_maiusculas <= max:
                    qntd_total += qntd_maiusculas
                    max = MAX_QNTD - qntd_total
                    for _ in range(qntd_maiusculas):
                        random_maiusc = random.choice(string.ascii_uppercase)
                        pre_senha += random_maiusc
                    break
                else: print("\033[31mInsira um número válido.\033[0m")
            else: print("\033[31mInsira um número.\033[0m")
    else: print(f"A quantidade de letras maiúsculas deve ser 0. ")
    if max != 0:
        while True:
            time.sleep(0.2)
            qntd_numeros = input(f"Quantidade de números [{min}-{max}]: ")
            if qntd_numeros.isdigit():
                qntd_numeros = int(qntd_numeros)
                if min <= qntd_numeros <= max:
                    qntd_total += qntd_numeros
                    max = MAX_QNTD - qntd_total
                    for _ in range(qntd_numeros):
                        random_nums = random.choice(string.digits)
                        pre_senha += random_nums
                    break
                else: print("\033[31mInsira um número válido.\033[0m")
            else: print("\033[31mInsira um número.\033[0m")
    else: print(f"A quantidade de números deve ser 0. ")
    if qntd_total < MIN_CARAC_SENHA:
        min = MIN_CARAC_SENHA - qntd_total
    else:
        min = MIN_QNTD
    if max != 0:
        while True:
            time.sleep(0.2)
            qntd_especiais = input(f"Quantidade de caracteres especiais [{min}-{max}]: ")
            if qntd_especiais.isdigit():
                qntd_especiais = int(qntd_especiais)
                if min <= qntd_especiais <= max:
                    for _ in range(qntd_especiais):
                        random_especiais = random.choice(string.punctuation)
                        pre_senha += random_especiais
                    break
                else: print("\033[31mInsira um número válido.\033[0m")
            else: print("\033[31mInsira um número.\033[0m")
    else: print(f"A quantidade de números deve ser 0. ")
    return pre_senha

def gerador():
    pre_senha = pedindo_infos()
    senha = list(pre_senha)
    random.shuffle(senha)
    return senha

def main():
    os.system('cls')
    while True:
        print(f"\033[1m|{ '-'*65}|\033[0m")
        print(f"\033[1m| \033[1;40;32m>{'=-'*10}< GERADOR DE SENHAS >{'=-'*10}<\033[1;39m |\033[0m")
        print(f"\033[1m|{ '-'*65}|\033[0m")
        time.sleep(0.4) 
        print(f"\n - Este é um gerador de senhas aleatórias com um mínimo de {MIN_CARAC_SENHA} e máximo de {MAX_CARAC_SENHA} caracteres;")
        time.sleep(2.5) 
        print(f" - Você pode escolher a quantidade que deseja de letras minúsculas, maiúsculas, números e caracteres especiais.\n")
        time.sleep(3.5) 
        start_end = input("Deseja gerar? [S] [N] ")
        print()
        if start_end in ["N", "n"]:
            break
        time.sleep(0.3) 
        senha = gerador()
        senha = "".join(senha)
        time.sleep(0.4) 
        print(f"\n A senha gerada foi: \033[1;40;32m{senha}\033[0m\n")
        print(f"\033[1m|{ '-'*65}|\033[0m\n")
        time.sleep(10) 
main()
