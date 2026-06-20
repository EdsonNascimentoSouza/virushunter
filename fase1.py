# ==========================================
# VÍRUS HUNTER
# fase1.py
#
# HD Corrompido
# ==========================================

import pygame

from classes.fase import Fase
from classes.constantes import *

from classes.jogador import Jogador
from classes.virus import Virus
from classes.arquivo_corrompido import ArquivoCorrompido
from classes.plataforma import Plataforma

from classes.audio import Audio
from classes.hud import HUD

from classes.colisao import Colisao


class Fase1(Fase):

    def __init__(self, tela, audio, inventario):

        super().__init__(
            tela,
            audio,
            inventario
        )   

        # ==================================
        # BACKGROUND
        # ==================================

        self.background = pygame.image.load(
            "assets/backgrounds/fase1.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            (
                LARGURA_TELA,
                ALTURA_TELA
            )
        )

        # ==================================
        # SISTEMAS
        # ==================================

        #self.audio = Audio()

        self.hud = HUD()

        # ==================================
        # JOGADOR
        # ==================================

        self.jogador = Jogador(inventario,audio)

        # ==================================
        # CONTADORES
        # ==================================

        self.virus_eliminados = 0

        self.arquivos_recuperados = 0

        # ==================================
        # LISTAS
        # ==================================

        self.plataformas = []

        self.virus_lista = []

        self.arquivos = []

        #self.pedras_virus = []#

        # ==================================
        # CRIAR OBJETOS
        # ==================================

        self.criar_plataformas()

        self.criar_virus()

        self.criar_arquivos()

        # ==================================
        # MÚSICA
        # ==================================

        self.audio.tocar_musica_fase1()

    # ======================================
    # CRIAR PLATAFORMAS
    # ======================================

    def criar_plataformas(self):

        self.plataformas = [

    # Chão
    Plataforma(
        0, 800,
        1350, 100,
        "assets/plataforms/hd_mec.png"
    ),

    # Plataforma esquerda
    Plataforma(
        180, 501,
        222, 40,
        "assets/plataforms/mem_ram.png"
    ),

    # Plataforma centro SSD arrumada
    Plataforma(
        685, 630,
        430, 40,
        "assets/plataforms/ssd.png"
    ),

    # Plataforma superior memória RAM
    Plataforma(
        627, 320,
        488, 40,
        "assets/plataforms/mem_ram.png"
    ),

    # Plataforma superior direita
    Plataforma(
        1265, 425,
        402, 40,
        "assets/plataforms/placa.png"
    ),

    # Plataforma SSD
    Plataforma(
        1190, 690,
        615, 40,
        "assets/plataforms/ssd.png"
    )
]

    # ======================================
    # CRIAR VÍRUS
    # ======================================

    def criar_virus(self):

        self.virus_lista = [
            Virus(385, 450, 150, 400), #virus2
            Virus(950, 570, 700, 1100), #virus3
            Virus(1700, 620, 1300, 1700), #virus4
            Virus(900, 265, 700, 1000), #virus5
            Virus(1600, 370, 1450, 1670,  ARMA_PEDRA, self.audio), #virus6
            Virus(1000, 720, 50, 1000) #virus1

        ]
# ==================================
    # FASE 1 NÃO POSSUI TIROS
    # ==================================

        for virus in self.virus_lista:

            virus.pode_atirar = False
        

    # ======================================
    # CRIAR ARQUIVOS
    # ======================================

    def criar_arquivos(self):

        self.arquivos = [

            ArquivoCorrompido(
                ARQUIVO_1_X,
                ARQUIVO_1_Y
            ),

            ArquivoCorrompido(
                ARQUIVO_2_X,
                ARQUIVO_2_Y
            ),

            ArquivoCorrompido(
                ARQUIVO_3_X,
                ARQUIVO_3_Y
            ),

            ArquivoCorrompido(
                ARQUIVO_4_X,
                ARQUIVO_4_Y
            ),

            ArquivoCorrompido(
                ARQUIVO_5_X,
                ARQUIVO_5_Y
            ),

            ArquivoCorrompido(
                ARQUIVO_6_X,
                ARQUIVO_6_Y
            )

        ]

    # ======================================
    # VERIFICAR ARQUIVOS
    # ======================================

    def verificar_arquivos(self):

        teclas = pygame.key.get_pressed()

        for arquivo in self.arquivos:

            if arquivo.foi_recuperado():
                continue

            if Colisao.jogador_arquivo(
                self.jogador,
                arquivo
            ):

                if teclas[pygame.K_d]:

                    arquivo.recuperar()

                    self.arquivos_recuperados += 1

                    self.audio.tocar_arquivo()

    # ======================================
    # VERIFICAR VÍRUS
    # ======================================
    def verificar_virus(self):

        resultado = Colisao.jogador_virus(

            self.jogador,

            self.virus_lista

        )

        if resultado == "virus_morto":

            self.virus_eliminados += 1

        elif resultado == "dano":

            pass

        Colisao.projetil_virus_jogador(

            self.jogador,

            self.virus_lista

        )

    # ======================================
    # REMOVER VÍRUS MORTOS
    # ======================================

    def remover_virus(self):

        for virus in self.virus_lista[:]:

            if virus.deve_remover():

                self.virus_lista.remove(
                    virus
                )

                self.virus_eliminados += 1

    # ======================================
    # VITÓRIA
    # ======================================

    def verificar_vitoria(self):

        if (

            self.virus_eliminados >= 6

            and

            self.arquivos_recuperados >= 6

        ):

            self.audio.parar_musica()

            self.audio.tocar_vitoria()

            self.inventario.obter_pedra()

            self.jogador.habilitar_ataque()

            self.inventario.recuperar_vida_total()

            self.concluida = True

            self.tempo_vitoria = pygame.time.get_ticks()

    # ======================================
    # GAME OVER
    # ======================================

    def verificar_game_over(self):

        if not self.jogador.esta_vivo():

            self.audio.parar_musica()

            self.audio.tocar_game_over()

            self.game_over = True

    # ======================================
    # ATUALIZAR
    # ======================================

    def atualizar(self):

        self.jogador.atualizar(
            self.plataformas
        )

        for virus in self.virus_lista:

            virus.atualizar(self.jogador)

        for arquivo in self.arquivos:

            arquivo.atualizar()

        self.verificar_arquivos()

        self.verificar_virus()

        self.remover_virus()

        self.verificar_vitoria()

        self.verificar_game_over()


    
    # ======================================
    # DESENHAR
    # ======================================

    def desenhar(self,tela):

        
        tela.blit(
            self.background,
            (0, 0)
        )

        # Plataformas
        for plataforma in self.plataformas:

            plataforma.desenhar(
                tela
            )
        # Arquivos
        for arquivo in self.arquivos:

            arquivo.desenhar(
                tela
            )

         # Vírus

        for virus in self.virus_lista:

            virus.desenhar(
                tela
            )    
        # Jogador

        self.jogador.desenhar(tela)

        # HUD

        self.hud.desenhar_fase1(tela, self.inventario, self.arquivos_recuperados, 6, self.virus_eliminados,6)