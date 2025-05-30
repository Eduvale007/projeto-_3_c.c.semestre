

'''
import chess
import chess.engine

# Caminho para o Stockfish (ajuste conforme necessário)
STOCKFISH_PATH = "C:/Users/Eduardo/Desktop/3_semestre/Stockfish/stockfish-windows-x86-64-sse41-popcnt.exe"



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

'''
### O código acima já é funcional e pode ser executado no seu terminal 



### O código abaixo é funcional mas precisa ser baixado as imagens e criar uma pasta chamada "images" para poder executar o tabuleiro


'''
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
STOCKFISH_PATH = "C:/Users/Eduardo/Desktop/3_semestre/Stockfish/stockfish-windows-x86-64-sse41-popcnt.exe"
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
'''

'''
import pygame
import chess
import chess.engine

# Configurações do tabuleiro
TAMANHO = 600
CASA = TAMANHO // 8

# Cores do tabuleiro
BRANCO = (240, 217, 181)
PRETO = (181, 136, 99)
PRETO_PECA = (0, 0, 0)
BRANCO_PECA = (255, 255, 255)

# Símbolos Unicode para as peças
pecas_unicode = {
    'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔',
    'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚'
}

# Inicializa o Pygame
pygame.init()
tela = pygame.display.set_mode((TAMANHO, TAMANHO))
pygame.display.set_caption("IA de Xadrez")

# Fonte para desenhar as peças
fonte = pygame.font.Font("DejaVuSans.ttf", CASA)



# Função para desenhar o tabuleiro
def desenhar_tabuleiro(board):
    for linha in range(8):
        for coluna in range(8):
            cor = BRANCO if (linha + coluna) % 2 == 0 else PRETO
            pygame.draw.rect(tela, cor, (coluna * CASA, linha * CASA, CASA, CASA))

            # Desenha peças usando Unicode
            peca = board.piece_at(chess.square(coluna, 7 - linha))
            if peca:
                simbolo = pecas_unicode[str(peca)]
                cor_texto = PRETO_PECA if peca.color == chess.WHITE else BRANCO_PECA
                texto = fonte.render(simbolo, True, cor_texto)
                tela.blit(texto, (coluna * CASA + CASA//4, linha * CASA + CASA//8))

    pygame.display.flip()

# Configuração da engine Stockfish
STOCKFISH_PATH = "C:/Users/Eduardo/Desktop/3_semestre/Stockfish/stockfish-windows-x86-64-sse41-popcnt.exe"
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
'''

'''
import pygame
import chess
import chess.engine

# Configurações do tabuleiro
TAMANHO = 600
CASA = TAMANHO // 8

# Cores do tabuleiro
BRANCO = (240, 217, 181)
PRETO = (181, 136, 99)
PRETO_PECA = (0, 0, 0)
BRANCO_PECA = (255, 255, 255)

# Símbolos Unicode para as peças
pecas_unicode = {
    'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔',
    'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚'
}

# Inicializa o Pygame
pygame.init()
tela = pygame.display.set_mode((TAMANHO, TAMANHO))
pygame.display.set_caption("IA de Xadrez")

# Fonte para desenhar as peças
fonte = pygame.font.Font("DejaVuSans.ttf", CASA)

# Função para desenhar o tabuleiro
def desenhar_tabuleiro(board):
    for linha in range(8):
        for coluna in range(8):
            cor = BRANCO if (linha + coluna) % 2 == 0 else PRETO
            pygame.draw.rect(tela, cor, (coluna * CASA, linha * CASA, CASA, CASA))

            # Desenha peças usando Unicode
            peca = board.piece_at(chess.square(coluna, 7 - linha))
            if peca:
                simbolo = pecas_unicode[str(peca)]
                cor_texto = PRETO_PECA if peca.color == chess.WHITE else BRANCO_PECA
                texto = fonte.render(simbolo, True, cor_texto)
                
                # Centraliza o texto na casa
                texto_rect = texto.get_rect(center=(coluna * CASA + CASA // 2, linha * CASA + CASA // 2))
                tela.blit(texto, texto_rect)

    pygame.display.flip()

# Configuração da engine Stockfish
STOCKFISH_PATH = "C:/Users/Eduardo/Desktop/3_semestre/Stockfish/stockfish-windows-x86-64-sse41-popcnt.exe"
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
'''

'''

import pygame
import chess
import chess.engine

# Configurações do tabuleiro
TAMANHO = 600
CASA = TAMANHO // 8

# Cores do tabuleiro
BRANCO = (240, 217, 181)
PRETO = (181, 136, 99)
PRETO_PECA = (0, 0, 0)
BRANCO_PECA = (255, 255, 255)

# Símbolos Unicode para as peças
pecas_unicode = {
    'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔',
    'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚'
}

# Inicializa o Pygame
pygame.init()
tela = pygame.display.set_mode((TAMANHO, TAMANHO))
pygame.display.set_caption("IA de Xadrez")

# Fonte para desenhar as peças e mensagens
fonte_pecas = pygame.font.Font("DejaVuSans.ttf", CASA)
fonte_msg = pygame.font.Font("DejaVuSans.ttf", 40)

# Função para desenhar o tabuleiro
def desenhar_tabuleiro(board):
    for linha in range(8):
        for coluna in range(8):
            cor = BRANCO if (linha + coluna) % 2 == 0 else PRETO
            pygame.draw.rect(tela, cor, (coluna * CASA, linha * CASA, CASA, CASA))

            # Desenha peças usando Unicode
            peca = board.piece_at(chess.square(coluna, 7 - linha))
            if peca:
                simbolo = pecas_unicode[str(peca)]
                cor_texto = PRETO_PECA if peca.color == chess.WHITE else BRANCO_PECA
                texto = fonte_pecas.render(simbolo, True, cor_texto)
                
                # Centraliza o texto na casa
                texto_rect = texto.get_rect(center=(coluna * CASA + CASA // 2, linha * CASA + CASA // 2))
                tela.blit(texto, texto_rect)

    pygame.display.flip()

# Função para mostrar mensagem no centro da tela
def mostrar_mensagem(texto):
    tela.fill((0, 0, 0))  # Limpa a tela com preto
    msg = fonte_msg.render(texto, True, (255, 255, 255))
    msg_rect = msg.get_rect(center=(TAMANHO // 2, TAMANHO // 2))
    tela.blit(msg, msg_rect)
    pygame.display.flip()

# Configuração da engine Stockfish
STOCKFISH_PATH = "C:/Users/Eduardo/Desktop/3_semestre/Stockfish/stockfish-windows-x86-64-sse41-popcnt.exe"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
board = chess.Board()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    if not board.is_game_over():
        result = engine.play(board, chess.engine.Limit(time=1.0))
        board.push(result.move)
        desenhar_tabuleiro(board)
    else:
        # Jogo terminou, mostra resultado
        resultado = board.result()  # ex: "1-0", "0-1", "1/2-1/2"
        if resultado == "1-0":
            mostrar_mensagem("Brancas venceram!")
        elif resultado == "0-1":
            mostrar_mensagem("Pretas venceram!")
        else:
            mostrar_mensagem("Empate!")

pygame.quit()
engine.quit()

'''

'''
import pygame
import chess
import chess.engine

# Configurações do tabuleiro
TAMANHO = 600
CASA = TAMANHO // 8

# Cores do tabuleiro
BRANCO = (240, 217, 181)
PRETO = (181, 136, 99)
PRETO_PECA = (0, 0, 0)
BRANCO_PECA = (255, 255, 255)

pecas_unicode = {
    'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔',
    'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚'
}

pygame.init()
tela = pygame.display.set_mode((TAMANHO, TAMANHO))
pygame.display.set_caption("IA de Xadrez")
fonte = pygame.font.Font("DejaVuSans.ttf", CASA)
fonte_menor = pygame.font.Font("DejaVuSans.ttf", 30)  # pra texto menor

def desenhar_tabuleiro(board):
    for linha in range(8):
        for coluna in range(8):
            cor = BRANCO if (linha + coluna) % 2 == 0 else PRETO
            pygame.draw.rect(tela, cor, (coluna * CASA, linha * CASA, CASA, CASA))

            peca = board.piece_at(chess.square(coluna, 7 - linha))
            if peca:
                simbolo = pecas_unicode[str(peca)]
                cor_texto = PRETO_PECA if peca.color == chess.WHITE else BRANCO_PECA
                texto = fonte.render(simbolo, True, cor_texto)
                texto_rect = texto.get_rect(center=(coluna * CASA + CASA // 2, linha * CASA + CASA // 2))
                tela.blit(texto, texto_rect)

    pygame.display.flip()

def mostrar_resultado(texto):
    tela.fill((0,0,0))
    mensagem = fonte.render(texto, True, (255, 255, 255))
    mensagem_rect = mensagem.get_rect(center=(TAMANHO//2, TAMANHO//2 - 50))
    tela.blit(mensagem, mensagem_rect)

    instrucoes = fonte_menor.render("Pressione R para reiniciar ou Q para sair", True, (255, 255, 255))
    instrucoes_rect = instrucoes.get_rect(center=(TAMANHO//2, TAMANHO//2 + 20))
    tela.blit(instrucoes, instrucoes_rect)
    pygame.display.flip()

STOCKFISH_PATH = "C:/Users/Eduardo/Desktop/3_semestre/Stockfish/stockfish-windows-x86-64-sse41-popcnt.exe"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

def jogo():
    board = chess.Board()
    rodando = True
    jogo_ativo = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if not jogo_ativo:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:  # Reiniciar jogo
                        board.reset()
                        jogo_ativo = True
                        desenhar_tabuleiro(board)
                    elif evento.key == pygame.K_q:  # Sair do jogo
                        rodando = False

        if jogo_ativo:
            if not board.is_game_over():
                result = engine.play(board, chess.engine.Limit(time=1.0))
                board.push(result.move)
                desenhar_tabuleiro(board)
            else:
                resultado = board.result()
                if resultado == "1-0":
                    msg = "Brancas ganharam!"
                elif resultado == "0-1":
                    msg = "Pretas ganharam!"
                else:
                    msg = "Empate!"
                mostrar_resultado(msg)
                jogo_ativo = False

jogo()
pygame.quit()
engine.quit()
'''


import pygame
import chess
import chess.engine

# Configurações do tabuleiro
TAMANHO = 600
CASA = TAMANHO // 8

# Cores do tabuleiro
BRANCO = (240, 217, 181)
PRETO = (181, 136, 99)
PRETO_PECA = (0, 0, 0)
BRANCO_PECA = (255, 255, 255)

pecas_unicode = {
    'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔',
    'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚'
}

pygame.init()
tela = pygame.display.set_mode((TAMANHO, TAMANHO))
pygame.display.set_caption("IA de Xadrez")
fonte = pygame.font.Font("DejaVuSans.ttf", CASA)
fonte_menor = pygame.font.Font("DejaVuSans.ttf", 30)  # pra texto menor

def desenhar_tabuleiro(board):
    for linha in range(8):
        for coluna in range(8):
            cor = BRANCO if (linha + coluna) % 2 == 0 else PRETO
            pygame.draw.rect(tela, cor, (coluna * CASA, linha * CASA, CASA, CASA))

            peca = board.piece_at(chess.square(coluna, 7 - linha))
            if peca:
                simbolo = pecas_unicode[str(peca)]
                cor_texto = PRETO_PECA if peca.color == chess.WHITE else BRANCO_PECA
                texto = fonte.render(simbolo, True, cor_texto)
                texto_rect = texto.get_rect(center=(coluna * CASA + CASA // 2, linha * CASA + CASA // 2))
                tela.blit(texto, texto_rect)

    pygame.display.flip()

def mostrar_resultado(texto):
    tela.fill((0,0,0))
    mensagem = fonte.render(texto, True, (255, 255, 255))
    mensagem_rect = mensagem.get_rect(center=(TAMANHO//2, TAMANHO//2 - 50))
    tela.blit(mensagem, mensagem_rect)

    instrucoes = fonte_menor.render("Pressione R para reiniciar ou Q para sair", True, (255, 255, 255))
    instrucoes_rect = instrucoes.get_rect(center=(TAMANHO//2, TAMANHO//2 + 20))
    tela.blit(instrucoes, instrucoes_rect)
    pygame.display.flip()

def contagem_regressiva(tela, fonte, tempo=3):
    for i in range(tempo, 0, -1):
        tela.fill((0, 0, 0))  # fundo preto
        texto = fonte.render(str(i), True, (255, 255, 255))
        texto_rect = texto.get_rect(center=(TAMANHO // 2, TAMANHO // 2))
        tela.blit(texto, texto_rect)
        pygame.display.flip()
        pygame.time.delay(1000)  # espera 1 segundo

STOCKFISH_PATH = "C:/Users/Eduardo/Desktop/3_semestre/Stockfish/stockfish-windows-x86-64-sse41-popcnt.exe"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

def jogo():
    board = chess.Board()
    rodando = True
    jogo_ativo = True

    desenhar_tabuleiro(board)
    contagem_regressiva(tela, fonte, 3)  # Contagem regressiva antes de começar

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if not jogo_ativo:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:  # Reiniciar jogo
                        board.reset()
                        jogo_ativo = True
                        desenhar_tabuleiro(board)
                        contagem_regressiva(tela, fonte, 3)  # Contagem ao reiniciar
                    elif evento.key == pygame.K_q:  # Sair do jogo
                        rodando = False

        if jogo_ativo:
            if not board.is_game_over():
                result = engine.play(board, chess.engine.Limit(time=1.0))
                board.push(result.move)
                desenhar_tabuleiro(board)
            else:
                resultado = board.result()
                if resultado == "1-0":
                    msg = "Brancas ganharam!"
                elif resultado == "0-1":
                    msg = "Pretas ganharam!"
                else:
                    msg = "Empate!"
                mostrar_resultado(msg)
                jogo_ativo = False

jogo()
pygame.quit()
engine.quit()


