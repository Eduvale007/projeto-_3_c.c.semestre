

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


'''
import pygame
import chess
import chess.engine
import time

# Configurações do tabuleiro
TAMANHO = 600
CASA = TAMANHO // 8

# Cores do tabuleiro
BRANCO = (240, 217, 181)
PRETO = (181, 136, 99)
PRETO_PECA = (0, 0, 0)
BRANCO_PECA = (255, 255, 255)

pygame.init()
pygame.mixer.init()  # Inicializa o mixer de áudio
som_movimento = pygame.mixer.Sound("sounds/move.wav")
som_start = pygame.mixer.Sound("sounds/game-start.wav")
som_board_start = pygame.mixer.Sound('sounds/board-start.wav')


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
        som_start.play()
        tela.fill((0, 0, 0))  # fundo preto
        texto = fonte.render(str(i), True, (255, 255, 255))
        texto_rect = texto.get_rect(center=(TAMANHO // 2, TAMANHO // 2))
        tela.blit(texto, texto_rect)
        pygame.display.flip()
        pygame.time.delay(1000)  # espera 1 segundo
     
    som_board_start.play()
 

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
        time.sleep(1)
        if jogo_ativo:
            if not board.is_game_over():
                result = engine.play(board, chess.engine.Limit(time=1.0))
                board.push(result.move)
                som_movimento.play()  #  Toca o som após cada jogada
                desenhar_tabuleiro(board)
            else:
                resultado = board.result()
                if resultado == "1-0":
                    msg = "Brancas ganharam!"
                elif resultado == "0-1":
                    msg = "Pretas ganharam!"
                else:
''                    msg = "Empate!"
                mostrar_resultado(msg)
                jogo_ativo = False

jogo()
pygame.quit()
engine.quit()

'''


import pygame
import chess
import chess.engine
import time

# Configurações do tabuleiro
TAMANHO = 600
CASA = TAMANHO // 8

# Cores do tabuleiro
BRANCO = (240, 217, 181)
PRETO = (181, 136, 99)
PRETO_PECA = (0, 0, 0)
BRANCO_PECA = (255, 255, 255)

pygame.init()
pygame.mixer.init()

# Sons
som_movimento = pygame.mixer.Sound("sounds/move.wav")
som_start = pygame.mixer.Sound("sounds/game-start.wav")
som_board_start = pygame.mixer.Sound('sounds/board-start.wav')

# Fontes
tela = pygame.display.set_mode((TAMANHO, TAMANHO))
pygame.display.set_caption("IA de Xadrez")
fonte = pygame.font.Font("DejaVuSans.ttf", CASA)
fonte_menor = pygame.font.Font("DejaVuSans.ttf", 30)

# Unicode das peças
pecas_unicode = {
    'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔',
    'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚'
}

# Função de desenhar o tabuleiro
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

# Mostrar resultado
def mostrar_resultado(texto):
    tela.fill((0, 0, 0))
    mensagem = fonte.render(texto, True, (255, 255, 255))
    mensagem_rect = mensagem.get_rect(center=(TAMANHO // 2, TAMANHO // 2 - 50))
    tela.blit(mensagem, mensagem_rect)

    instrucoes = fonte_menor.render("Pressione R para reiniciar ou Q para sair", True, (255, 255, 255))
    instrucoes_rect = instrucoes.get_rect(center=(TAMANHO // 2, TAMANHO // 2 + 20))
    tela.blit(instrucoes, instrucoes_rect)
    pygame.display.flip()

# Menu inicial
def menu_inicial():
    escolhendo = True
    while escolhendo:
        tela.fill((0, 0, 0))
        titulo = fonte_menor.render("Escolha um modo:", True, (255, 255, 255))
        opcao1 = fonte_menor.render("1 - Jogar contra a IA", True, (255, 255, 255))
        opcao2 = fonte_menor.render("2 - Assistir IA vs IA", True, (255, 255, 255))
        opcao3 = fonte_menor.render("3 - Jogar sozinho", True, (255, 255, 255))
        
        tela.blit(titulo, (TAMANHO // 2 - titulo.get_width() // 2, 150))
        tela.blit(opcao1, (TAMANHO // 2 - opcao1.get_width() // 2, 250))
        tela.blit(opcao2, (TAMANHO // 2 - opcao2.get_width() // 2, 300))
        tela.blit(opcao3, (TAMANHO // 2 - opcao3.get_width() // 2, 350))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return "vs_ia"
                elif evento.key == pygame.K_2:
                    return "ia_vs_ia"
                elif evento.key == pygame.K_3:
                    return "solo"

# Caminho do Stockfish
STOCKFISH_PATH = "C:/Users/Eduardo/Desktop/3_semestre/Stockfish/stockfish-windows-x86-64-sse41-popcnt.exe"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
def jogo(modo):
    board = chess.Board()
    rodando = True
    jogo_ativo = True
    jogador_cor = chess.WHITE  # Jogador joga de brancas

    desenhar_tabuleiro(board)
    som_board_start.play()

    selecionado = None  # Para armazenar o quadrado de origem

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if not jogo_ativo:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        board.reset()
                        jogo_ativo = True
                        desenhar_tabuleiro(board)
                        som_board_start.play()
                    elif evento.key == pygame.K_q:
                        rodando = False

        time.sleep(0.1)

        if jogo_ativo:
            if not board.is_game_over():
                if modo == "ia_vs_ia" or (modo == "vs_ia" and board.turn != jogador_cor):
                    # IA joga
                    result = engine.play(board, chess.engine.Limit(time=1.0))
                    board.push(result.move)
                    som_movimento.play()
                    desenhar_tabuleiro(board)
                elif modo == "solo" or (modo == "vs_ia" and board.turn == jogador_cor):
                    # Jogador humano joga
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            rodando = False
                        elif evento.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            coluna = pos[0] // CASA
                            linha = 7 - (pos[1] // CASA)
                            square = chess.square(coluna, linha)

                            if selecionado is None:
                                # Seleciona o quadrado de origem
                                peca = board.piece_at(square)
                                if peca and peca.color == board.turn:
                                    selecionado = square
                            else:
                                # Seleciona o quadrado de destino
                                move = chess.Move(selecionado, square)
                                if move in board.legal_moves:
                                    board.push(move)
                                    som_movimento.play()
                                    desenhar_tabuleiro(board)
                                selecionado = None  # Reseta a seleção

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
# Fluxo principal
modo = menu_inicial()
jogo(modo)

pygame.quit()
engine.quit()

