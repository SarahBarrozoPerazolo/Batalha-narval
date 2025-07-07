def mostrar_menu():
    print("***** Batalha Naval *****\n")
    print("1 - Jogar")
    print("2 - Ver melhores Pontuações")
    print("3 - Sair")
    escolha = input("Escolha uma opção: ")
    return escolha


def mostrar_tabuleiro(tabuleiro, jogadas, navios_afundados, subs_afundados):
    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    print("\n    1 2 3 4 5 6")
    for i, linha in enumerate(tabuleiro):
        linha_formatada = ' '.join(str(c) for c in linha) # formata a linha do tabuleiro
        print(f"{letras[i]} | {linha_formatada}")
    
    print(f"\nJogadas até agora: {jogadas}")
    print(f"Afundados até agora = Navios {navios_afundados} de 5 | Submarinos {subs_afundados} de 3")


def mostrar_caracteres_usados():
    print("O caractere _ é usado para água")      
    print("O caractere X é usado para embarcação afundada")
    print("O caractere \u2316 é usado para embarcação parcialmente atingida")
    print("O caractere ■ é usado para posição ainda não explorada do tabuleiro")


def mostrar_vitoria():
    print("\n***** Você ganhou!!!! *****\n")


def mostrar_mensagem(msg):
    if msg == "AGUA":
        print("==> Você acertou água!")
    elif msg == "NAVIO":
        print("==> Você afundou um navio!")
    elif msg == "SUBMARINO AFUNDADO":
        print("==> Você afundou um submarino!")
    elif msg == "SUBMARINO PARCIAL":
        print("==> Você atingiu parte de um submarino!") 
    else:
        print(f"==> {msg}")


