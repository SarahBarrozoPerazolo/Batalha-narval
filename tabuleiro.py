import random

class Tabuleiro:
    def __init__(self):
        self.tamanho = 6 # tamanho do tabuleiro (6x6)
        self.tabuleiro = [['■' for _ in range(self.tamanho)] for _ in range(self.tamanho)]  # matriz do tabuleiro (preenchida com '■') para indicar posições vazias
        self.navios = []  
        self.submarinos = [] # duas posições são ocupadas por submarinos
        self.jogadas = 0 
        self.afundados_navios = 0 
        self.afundados_submarinos = 0   
        self.submarinos_danificados = []    

        self.gerar_navios()
        self.gerar_submarinos()

    def gerar_navios(self):
        while len(self.navios) < 5:  # sorteia 5 navios
            l = random.randint(0, 5)  # linha
            c = random.randint(0, 5)  # coluna
            if (l, c) not in self.navios:  # evita repetição de posição
                self.navios.append((l, c))
  
    def gerar_submarinos(self):
        tentativas = 0
        while len(self.submarinos) < 3 and tentativas < 100: # sorteia 3 submarinos e limita tentativas para evitar loop infinito
            l = random.randint(0, 4)  # até 4 para evitar ultrapassar o limite do tabuleiro
            c = random.randint(0, 4)  
            direcao = random.choice(['H', 'V'])  # sorteia direção horizontal ou vertical

            # Define as duas posições ocupadas pelo submarino
            if direcao == 'H':
                pos = [(l, c), (l, c + 1)]
            else:
                pos = [(l, c), (l + 1, c)]

            # Lista todas posições já ocupadas
            pos_ocupadas = [p for sub in self.submarinos for p in sub] + self.navios  
            if all(p not in pos_ocupadas for p in pos):  # Adiciona submarino se as duas posições estiverem livres
                self.submarinos.append(pos) 

            tentativas += 1 

    def realizar_jogada(self, linha, coluna): 
        if self.tabuleiro[linha][coluna] in ['X', '_', '\u2316']: 
            return "JA_JOGADO"

        self.jogadas += 1 # incrementa jogadas

        # Se acertar navio
        if (linha, coluna) in self.navios:
            self.tabuleiro[linha][coluna] = 'X'
            self.navios.remove((linha, coluna))
            self.afundados_navios += 1
            return "NAVIO"

        # Se acertar parte de submarino
        for submarino in self.submarinos:
            if (linha, coluna) in submarino:
                self.tabuleiro[linha][coluna] = '\u2316'  # marca parte atingida
                # Se todas as partes do submarino estiverem atingidas
                if all(self.tabuleiro[l][c] == '\u2316' for l, c in submarino):
                    for l, c in submarino:
                        self.tabuleiro[l][c] = 'X' # Marca submarino afundado
                    self.submarinos.remove(submarino)
                    self.afundados_submarinos += 1
                    return "SUBMARINO AFUNDADO"
                return "SUBMARINO PARCIAL"

        # Se acertar água
        self.tabuleiro[linha][coluna] = '_'
        return "AGUA"
    
    def verificar_vitoria(self):
        return len(self.navios) == 0 and len(self.submarinos) == 0




