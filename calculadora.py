#! /bin/zsh

import re

historico = []
conta_atual = ""

print("\033[1;93mBem vindo a calculadora python\033[0m\n")

nome = input("Qual seu nome? ").strip()

print(f"\n\033[1;93mOlá, {nome}! Vamos calcular, mas antes conheça alguns comandos básicos.\033[0m\n")

print("\033[1;93mComandos:\033[0m\n")
print("Para deletar ultimo número e calcular de novo, digite D")
print("Para acessar o histórico, digite H")
print("Para apagar historico, digite A")
print("Para encerrar sair, digite S")
print("Atenção: Para divisão use // -> exemplo.: 10 // 2")
print("Para porcentagem use 'de' -> exemplo.: 5% de 6")
print("\n")

while True:
    entrada = input("O que deseja calcular? ").strip()

    # SAIR
    if entrada.lower() == "sair" or entrada.upper() == "S":
        confirmacao = input("Tem certeza que deseja sair? (sim/não): ").strip().lower()
        if confirmacao == "sim":
            print("\033[1;93mObrigada por usar a calculadora Python.\033[0m")
            break
        elif confirmacao == "não" or confirmacao == "nao": # Fixed line
            print("\033[1;93mVoltando para a calculadora...\033[0m\n")
        else:
            print("Digite apenas 'sim' ou 'não'.")

    # APAGAR HISTÓRICO
    elif entrada.upper() == "A":
        historico.clear()
        print("\033[1;93mHistórico apagado com sucesso!\033[0m")

    # DELETAR
    elif entrada.upper() == "D":
        # remove último número com operador (tipo -4, +9, *3)
        conta_atual = re.sub(r'[\+\-\*\/]?\d+$', '', conta_atual)

        print(f"Conta atual: {conta_atual}")

        if conta_atual:
            try:
                resultado = eval(conta_atual)
                print(f"\033[92mResultado: {resultado}\033[0m")
            except:
                pass  # não mostra erro se estiver incompleto

        continue  # MUITO IMPORTANTE: evita duplicar resultado

    # HISTÓRICO
    elif entrada.upper() == "H":
        print("\n\033[92mHistórico:\033[0m")
        if not historico:
            print("\033[92mNenhum cálculo feito ainda.\033[0m")
        else:
            for item in historico:
                print(f"\033[92m{item}\033[0m")
        print()


    # CÁLCULO
    else:
        conta_atual = entrada

        try:
            conta_tratada = conta_atual.lower().replace("de", "*").replace("%", "/100")
            resultado = eval(conta_tratada)

            print(f"\033[92mResultado: {resultado}\033[0m")
            historico.append(f"{conta_atual} = {resultado}")

        except Exception:
            print("\033[91m[Opa, tivemos um erro inesperado, por favor tente de novo]\033[0m")
            historico.append(f"{conta_atual} = [erro]")
