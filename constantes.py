# ==========================================
# VÍRUS HUNTER
# constantes.py
# ==========================================

# ==========================================
# TELA
# ==========================================

LARGURA_TELA = 1800
ALTURA_TELA = 900

FPS = 30

TITULO_JOGO = "Virus Hunter"

# ==========================================
# CORES
# ==========================================

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 120, 255)

AMARELO = (255, 255, 0)

# ==========================================
# JOGADOR
# ==========================================

JOGADOR_X_INICIAL = 120
JOGADOR_Y_INICIAL = 700

VELOCIDADE_JOGADOR = 8

FORCA_PULO = -28

GRAVIDADE = 1.2

VIDA_MAXIMA = 4

TEMPO_DANO = 500

LARGURA_SPRITE_JOGADOR = 96
ALTURA_SPRITE_JOGADOR = 96

# ==========================================
# VIRUS
# ==========================================

VELOCIDADE_VIRUS = 2

TEMPO_ATAQUE_VIRUS = 10000

TEMPO_MORTE_VIRUS = 1000

LARGURA_SPRITE_VIRUS = 70
ALTURA_SPRITE_VIRUS = 70

TOTAL_VIRUS_FASE1 = 6

TOTAL_VIRUS_DOCUMENTOS = 2

TOTAL_VIRUS_DOWNLOADS = 6

# ==========================================
# FASE 1
# ==========================================

TOTAL_ARQUIVOS_FASE1 = 6

# ==========================================
# ARMAS
# ==========================================

ARMA_PEDRA = "PEDRA"

ARMA_TESOURA = "TESOURA"

ARMA_PAPEL = "PAPEL"

# ==========================================
# PROJETEIS
# ==========================================

VELOCIDADE_PROJETIL = 6

# ==========================================
# VOLUMES
# ==========================================

VOLUME_MUSICA = 0.5

VOLUME_EFEITOS = 0.8

VOLUME_VIRUS_ANDANDO = 0.3

# ==========================================
# PLAYER SPRITES
# ==========================================

CPU_IDLE = "assets/player/cpu_idle.png"

CPU_WALK_1 = "assets/player/cpu_walk_1.png"
CPU_WALK_2 = "assets/player/cpu_walk_2.png"

CPU_JUMP = "assets/player/cpu_jump.png"

CPU_DANO = "assets/player/cpu_dano.png"

# ==========================================
# VIRUS SPRITES
# ==========================================

VIRUS_IDLE = "assets/virus/virus_idle.png"

VIRUS_WALK_1 = "assets/virus/virus_walk_1.png"
VIRUS_WALK_2 = "assets/virus/virus_walk_2.png"

VIRUS_ATTACK = "assets/virus/virus_attack.png"

VIRUS_DEAD = "assets/virus/virus_dead.png"

# ==========================================
# ITENS
# ==========================================

ARQUIVO_CORROMPIDO_IMG = (
    "assets/itens/corrompido.png"
)

DRIVER_IMPRESSORA_IMG = (
    "assets/itens/driver.png"
)

WORD_IMG = (
    "assets/itens/word.png"
)

BATERIA_IMG = (
    "assets/hud/bat_cheia.png"
)

# ==========================================
# PLATAFORMAS
# ==========================================

PLATAFORMA_CHAO = (
    "assets/plataforms/chao.png"
)

PLATAFORMA_CIRCUITO = (
    "assets/plataforms/plataforma_fase1.png"
)

PLATAFORMA_PROCESSADOR = (
    "assets/plataforms/plataforma_fase1.png"
)

PLATAFORMA_MEMORIA = (
    "assets/plataforms/plataforma_fase1.png"
)

PLATAFORMA_HD = (
    "assets/plataforms/plataforma_fase1.png"
)

PLATAFORMA_SERVIDOR = (
    "assets/plataforms/plataforma_fase1.png"
)

PLATAFORMA_DOCUMENTOS = (
    "assets/plataforms/plataforma_fase1.png"
)

PLATAFORMA_DOWNLOADS = (
    "assets/plataforms/plataforma_fase1.png"
)

PLATAFORMA_LIXEIRA = (
    "assets/plataforms/plataforma_fase1.png"
)

PLATAFORMA_BOSS = (
    "assets/plataforms/plataforma_fase1.png"
)

LARGURA_PLATAFORMA = 320

ALTURA_PLATAFORMA = 40

# ==========================================
# PORTAS
# ==========================================

PORTA_DOCUMENTOS_IMG = (
    "assets/portas/documentos.png"
)

PORTA_DOWNLOADS_IMG = (
    "assets/portas/downloads.png"
)

PORTA_LIXEIRA_IMG = (
    "assets/portas/lixeira.png"
)

# ==========================================
# BACKGROUNDS
# ==========================================

FUNDO_FASE1 = (
    "assets/backgrounds/fase1.png"
)

FUNDO_FASE2_MAPA = (
    "assets/backgrounds/fase2_mapa.png"
)

FUNDO_DOCUMENTOS = (
    "assets/backgrounds/documentos.png"
)

FUNDO_DOWNLOADS = (
    "assets/backgrounds/downloads.png"
)

FUNDO_LIXEIRA = (
    "assets/backgrounds/lixeira.png"
)

FUNDO_FASE3 = (
    "assets/backgrounds/fase3.jpg"
)
# ==========================================
# PROJETEIS
# ==========================================

PROJETIL_PEDRA = (
    "assets/itens/pedra.png"
)

PROJETIL_TESOURA = (
    "assets/itens/tesoura.png"
)

PROJETIL_PAPEL = (
    "assets/itens/papel.png"
)
# ==========================================
# TELAS
# ==========================================

GAME_OVER_IMG = (
    "assets/telas/game_over.png"
)

TELA_PEDRA_DIGITAL = (
    "assets/telas/pedra_digital.png"
)

TELA_GANHOU_TESOURA = (
    "assets/telas/ganhou_tesoura.png"
)

TELA_GANHOU_PAPEL = (
    "assets/telas/ganhou_papel.png"
)

# ==========================================
# SONS
# ==========================================

SOM_ANDAR = (
    "assets/sounds/cpu_andando.mp3"
)

SOM_PULO = (
    "assets/sounds/cpu_pulo.mp3"
)

SOM_DANO = (
    "assets/sounds/dano.mp3"
)

SOM_PORTA = (
    "assets/sounds/portaAbrindo.mp3" 
)

SOM_VIRUS_ATAQUE = (
    "assets/sounds/virusAtacando.mp3"
)

SOM_VIRUS_MORTE = (
    "assets/sounds/virusMorrendo.mp3"
)

SOM_PEDRA = (
    "assets/sounds/virusAtacando.mp3"
)

SOM_TESOURA = (
    "assets/sounds/virusAtacando.mp3"
)

SOM_PAPEL = (
    "assets/sounds/virusAtacando.mp3"
)

SOM_TROCA_ARMA = (
    "assets/sounds/trocarArma.mp3"
)

SOM_ARQUIVO = (
    "assets/sounds/arquivoCorrompido.mp3"
)

SOM_DRIVER = (
    "assets/sounds/arquivoCorrompido.mp3"
)

SOM_WORD = (
    "assets/sounds/arquivoCorrompido.mp3"
)

SOM_VITORIA = (
    "assets/sounds/vitoriaFase.mp3"
)

SOM_GAME_OVER = (
    "assets/sounds/gameOver.mp3"
)

# ==========================================
# MÚSICAS
# ==========================================

MUSICA_FASE1 = (
    "assets/sounds/music/musicaFases.mp3"
)

MUSICA_FASE2 = (
    "assets/sounds/music/musicaFases.mp3"
)

MUSICA_FASE3 = (
    "assets/sounds/music/musicaFases.mp3"
)
# ==========================================
# POSIÇÕES DOS ARQUIVOS - FASE 1
# ==========================================

#arquivo 1
ARQUIVO_1_X = 180 # arquivo2
ARQUIVO_1_Y = 450

ARQUIVO_2_X = 850 #arquivo3
ARQUIVO_2_Y = 570

ARQUIVO_3_X = 1000 #arquivo4
ARQUIVO_3_Y = 265

ARQUIVO_4_X = 1500 #arquivo 5
ARQUIVO_4_Y = 370

ARQUIVO_5_X = 1450 #arquivo6
ARQUIVO_5_Y = 640

ARQUIVO_6_X = 250 #arquivo1 
ARQUIVO_6_Y = 730

# ==========================================
# DEBUG
# ==========================================

DEBUG_COLISAO = True #para visualizar a plataforma p ele sumir é só colocar false

# ==========================================
# BOSS FINAL
# ==========================================

VIDA_BOSS = 5

TEMPO_TROCA_ARMA_BOSS = 5000