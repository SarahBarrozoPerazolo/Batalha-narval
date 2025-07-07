## 🐋 Batalha Narval
Um jogo de **batalha naval com temática de narvais**, criado em Python.  
A proposta é simples: explore o tabuleiro e tente afundar todos os navios e submarinos inimigos com o menor número possível de jogadas!

---
## Pré-requisitos

- Python 3.x instalado no sistema
- Rodar arquivos pelo terminal

---
## Como executar o jogo
   No terminal, digite: python FrontEnd.py

---
## Mecânica do jogo

- Tabuleiro: 6x6
- Navios: 5 (ocupa 1 célula cada)
- Submarinos: 3 (ocupam 2 células cada, posicionados aleatoriamente na horizontal ou vertical)
- Símbolos no tabuleiro:

     ■ área não explorada /  _ água / ⌖ parte de submarino atingida / X navio ou submarino afundado 
---
## Estrutura do projeto
📁 batalha-narval
-├── exibicao.py          # Exibe o menu, tabuleiro, mensagens e símbolos
-├── FrontEnd.py          # Interface principal com menu e lógica de jogo
-├── main.py              # Exibe legenda dos símbolos usados
-├── persistencia.py      # Salva e exibe o ranking de jogadores
-├── ranking.txt          # Arquivo local com os melhores resultados
-└── tabuleiro.py         # Lógica de jogo: criação, jogadas e verificação


---
##  Autoria
Desenvolvido por Sarah Barrozo Perazolo
Estudante de Análise e Desenvolvimento de Sistemas


