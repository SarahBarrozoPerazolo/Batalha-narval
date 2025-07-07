import os

ARQUIVO_RANKING = "ranking.txt"


def ler_ranking():
    ranking = []
    if not os.path.exists(ARQUIVO_RANKING):
        return ranking

    with open(ARQUIVO_RANKING, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                try:
                    nome, jogadas = linha.split(',')
                    ranking.append((nome.strip(), int(jogadas)))
                except ValueError:
                    continue

    ranking.sort(key=lambda x: x[1])  # Ordena pelo número de jogadas (menor é melhor)
    return ranking


def salvar_ranking(nome, jogadas):
    ranking = ler_ranking()
    ranking.append((nome, jogadas))
    ranking.sort(key=lambda x: x[1])

    with open(ARQUIVO_RANKING, 'w', encoding='utf-8') as f:
        for nome, jogadas in ranking:
            f.write(f"{nome},{jogadas}\n")


def mostrar_ranking():
    ranking = ler_ranking()
    print("\n=== Melhores Pontuações ===\n")

    if not ranking:
        print("Nenhuma pontuação registrada ainda.\n")
        return

    print(f"{'Posição':<8}{'Nome':<15}{'Jogadas':<8}")
    print("-" * 35) # Separador para melhor visualização

    for i, (nome, jogadas) in enumerate(ranking[:3], start=1):
        print(f"{i:<8}{nome:<15}{jogadas:<8}")

    print()

