from tabuleiro import Tabuleiro
import exibicao
import persistencia


def converter_coordenada(coord_str):
    coord_str = coord_str.strip().upper()
    if coord_str == '-1':
        return -1, -1
    if len(coord_str) < 2 or len(coord_str) > 3:
        return None

    linha_letra = coord_str[0]
    if linha_letra not in "ABCDEF":
        return None

    try:
        coluna_num = int(coord_str[1:])
    except ValueError:
        return None

    if coluna_num < 1 or coluna_num > 6:
        return None

    linha = ord(linha_letra) - ord('A')
    coluna = coluna_num - 1
    return linha, coluna


def jogar():
    tabuleiro = Tabuleiro()

    while True:
        exibicao.mostrar_tabuleiro(
            tabuleiro.tabuleiro,
            tabuleiro.jogadas,
            tabuleiro.afundados_navios,
            tabuleiro.afundados_submarinos
        )

        coord_str = input("Digite a posição (ex: A1, C3) ou -1 para sair: ")
        coords = converter_coordenada(coord_str)

        if coords == (-1, -1):
            print("Voltando ao menu principal...")
            input("Pressione Enter para continuar...")
            break

        if coords is None:
            print("Coordenada inválida! Use o formato LetraNúmero (ex: A1 até F6).")
            input("Pressione Enter para tentar novamente...")
            continue

        linha, coluna = coords
        valor = tabuleiro.tabuleiro[linha][coluna]

        if valor in ['X', '_', '\u2316']:
            print("Você já jogou nessa posição. Tente outra.")
            input("Pressione Enter para continuar...")
            continue

        resultado = tabuleiro.realizar_jogada(linha, coluna)
        exibicao.mostrar_mensagem(resultado)

        input("Pressione Enter para continuar...")

        if tabuleiro.verificar_vitoria():
            exibicao.mostrar_tabuleiro(
                tabuleiro.tabuleiro,
                tabuleiro.jogadas,
                tabuleiro.afundados_navios,
                tabuleiro.afundados_submarinos
            )
            exibicao.mostrar_vitoria()
            nome = input("Digite seu nome: ")
            persistencia.salvar_ranking(nome, tabuleiro.jogadas)
            persistencia.mostrar_ranking()
            break


def main():
    while True:
        escolha = exibicao.mostrar_menu()
        if escolha == '1':
            jogar()
        elif escolha == '2':
            persistencia.mostrar_ranking()
            input("Pressione Enter para voltar ao menu...")
        elif escolha == '3':
            print("Finalizando programa...")
            break
        else:
            print("Opção inválida! Digite 1, 2 ou 3.")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
