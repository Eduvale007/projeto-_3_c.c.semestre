
"""

import chess
import chess.engine

# Caminho para o Stockfish (ajuste conforme necessário)
STOCKFISH_PATH = "C:/Users/Eduardo/Desktop/C.C_3/Stockfish/stockfish-windows-x86-64-sse41-popcnt.exe"



  # Se estiver no mesmo diretório

# Inicializa o motor de xadrez
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

# Cria o tabuleiro
board = chess.Board()

# Executa jogadas até o jogo acabar
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=1.0))  # IA pensa por 1s
    board.push(result.move)  # Faz a jogada no tabuleiro
    print(board)  # Mostra o tabuleiro no console
    print("\n")

# Mostra o resultado do jogo
print("Resultado:", board.result())

engine.quit()
"""

### O código acima já é funcional e pode ser executado no seu terminal 



### O código abaixo é funcional mas precisa ser baixado as imagens e criar uma pasta chamada "images" para poder executar o tabuleiro


"""
import pygame
import chess
import chess.engine

# Configurações do tabuleiro
TAMANHO = 600
CASA = TAMANHO // 8

# Cores do tabuleiro
BRANCO = (240, 217, 181)
PRETO = (181, 136, 99)

# Inicializa o Pygame
pygame.init()
tela = pygame.display.set_mode((TAMANHO, TAMANHO))
pygame.display.set_caption("IA de Xadrez")

# Carregar as imagens das peças
pecas = {}
for peca in "prnbqkPRNBQK":
    pecas[peca] = pygame.transform.scale(
        pygame.image.load(f"images/{peca}.png"), (CASA, CASA)
    )

# Função para desenhar o tabuleiro
def desenhar_tabuleiro(board):
    for linha in range(8):
        for coluna in range(8):
            cor = BRANCO if (linha + coluna) % 2 == 0 else PRETO
            pygame.draw.rect(tela, cor, (coluna * CASA, linha * CASA, CASA, CASA))

            # Desenha peças
            peca = board.piece_at(chess.square(coluna, 7 - linha))
            if peca:
                tela.blit(pecas[str(peca)], (coluna * CASA, linha * CASA))

    pygame.display.flip()

# Configuração da engine Stockfish
STOCKFISH_PATH = "C:/Users/Eduardo/Desktop/C.C_3/Stockfish/stockfish-windows-x86-64-sse41-popcnt.exe"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
board = chess.Board()

# Loop do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    if not board.is_game_over():
        result = engine.play(board, chess.engine.Limit(time=1.0))
        board.push(result.move)
        desenhar_tabuleiro(board)

pygame.quit()
engine.quit()
"""