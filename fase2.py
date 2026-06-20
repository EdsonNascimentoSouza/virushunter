# ==========================================
# VÍRUS HUNTER
# fase2.py
#
# FASE 2
# O WORD PERDIDO
#
# Objetivos:
#
# ✓ Recuperar Driver
# ✓ Recuperar Word
# ✓ Eliminar 8 vírus
#
# Recompensas:
#
# ✓ Tesoura
# ✓ Papel
#
# ==========================================

import pygame

from classes.fase import Fase
from classes.constantes import *

from classes.jogador import Jogador
from classes.virus import Virus

from classes.driver_impressora import DriverImpressora
from classes.word import Word

from classes.plataforma import Plataforma

from classes.colisao import Colisao

from classes.hud import HUD


class Fase2(Fase):

    def __init__(

        self,

        tela,

        audio,

        inventario

    ):

        super().__init__(

            tela,

            audio,

            inventario

        )

        # ==================================
        # BACKGROUND
        # ==================================

        self.background = pygame.image.load(
            FUNDO_FASE2_MAPA
        ).convert()

        self.background = pygame.transform.scale(

            self.background,

            (
                LARGURA_TELA,
                ALTURA_TELA
            )

        )

        # ==================================
        # HUD
        # ==================================

        self.hud = HUD()

        # ==================================
        # JOGADOR
        # ==================================

        self.jogador = Jogador(

            inventario,

            audio

        )

        self.jogador.rect.x = 100
        self.jogador.rect.y = 700

        # ==================================
        # CONTADORES
        # ==================================

        self.virus_mortos = 0

        # ==================================
        # LISTAS
        # ==================================

        self.plataformas = []

        self.virus_lista = []

        # ==================================
        # OBJETOS
        # ==================================

        self.driver = None

        self.word = None

        # ==================================
        # CRIAÇÃO
        # ==================================

        self.criar_plataformas()

        self.criar_itens()

        self.criar_virus()

        # ==================================
        # MÚSICA
        # ==================================

        self.audio.tocar_musica_fase2()

    # ======================================
    # PLATAFORMAS
    # ======================================

    def criar_plataformas(self):

        self.plataformas = [

            # CHÃO

            Plataforma(
                0,
                800,
                1800,
                100
            ),

            # AUXILIAR

            Plataforma(
                250,
                550,
                250,
                40
            ),

            # CENTRAL

            Plataforma(
                650,
                600,
                500,
                40
            ),

            # DOWNLOADS

            Plataforma(
                1150,
                450,
                500,
                40
            ),

            # DOCUMENTOS

            Plataforma(
                150,
                350,
                550,
                40
            )

        ]

    # ======================================
    # ITENS
    # ======================================

    def criar_itens(self):

        self.driver = DriverImpressora(

            420,
            270

        )

        self.word = Word(

            250,
            720

        )

    # ======================================
    # VÍRUS
    # ======================================

    def criar_virus(self):

        self.virus_lista = [

            # DOCUMENTOS

            Virus(
                220,
                280,
                180,
                450,
                ARMA_PEDRA,
                self.audio
            ),

            Virus(
                520,
                280,
                350,
                650,
                ARMA_PEDRA,
                self.audio
            ),

            # DOWNLOADS

            Virus(
                1180,
                380,
                1150,
                1300,
                ARMA_PEDRA,
                self.audio
            ),

            Virus(
                1260,
                380,
                1200,
                1400,
                ARMA_PEDRA,
                self.audio
            ),

            Virus(
                1340,
                380,
                1250,
                1500,
                ARMA_PEDRA,
                self.audio
            ),

            Virus(
                1420,
                380,
                1300,
                1550,
                ARMA_PEDRA,
                self.audio
            ),

            Virus(
                1500,
                380,
                1400,
                1600,
                ARMA_PEDRA,
                self.audio
            ),

            Virus(
                1580,
                380,
                1450,
                1650,
                ARMA_PEDRA,
                self.audio
            )
            

        ]
        self.pode_atirar = True

    # ======================================
    # DRIVER
    # ======================================

    def verificar_driver(self):

        teclas = pygame.key.get_pressed()

        if self.driver.foi_salvo():
            return

        if Colisao.jogador_driver(

            self.jogador,

            self.driver

        ):

            if teclas[pygame.K_d]:

                self.driver.salvar()

                self.inventario.salvar_driver()

                self.inventario.obter_tesoura()

                self.audio.tocar_driver()

    # ======================================
    # WORD
    # ======================================

    def verificar_word(self):

        teclas = pygame.key.get_pressed()

        if self.word.foi_salvo():
            return

        if Colisao.jogador_word(

            self.jogador,

            self.word

        ):

            if teclas[pygame.K_d]:

                self.word.salvar()

                self.inventario.salvar_word()

                self.inventario.obter_papel()

                self.audio.tocar_word()

    # ======================================
    # VÍRUS
    # ======================================

    def verificar_virus(self):

        resultado = Colisao.jogador_virus(

            self.jogador,

            self.virus_lista

        )

        if resultado == "virus_morto":

            self.virus_mortos += 1

    # ======================================
    # REMOVER VÍRUS
    # ======================================

    def remover_virus(self):

        for virus in self.virus_lista[:]:

            if virus.deve_remover():

                self.virus_lista.remove(
                    virus
                )

    # ======================================
    # VITÓRIA
    # ======================================

    def verificar_vitoria(self):

        if (

            self.inventario.possui_driver()

            and

            self.inventario.possui_word()

            and

            self.virus_mortos >= 8

        ):

            self.audio.parar_musica()

            self.audio.tocar_vitoria()

            self.inventario.recuperar_vida_total()

            self.concluida = True

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

            virus.atualizar(
                self.jogador
            )

        self.driver.atualizar()

        self.word.atualizar()

        self.verificar_driver()

        self.verificar_word()

        self.verificar_virus()

        self.remover_virus()

        self.verificar_vitoria()

        self.verificar_game_over()

    # ======================================
    # DESENHAR
    # ======================================

    def desenhar(

        self,

        tela

    ):

        tela.blit(

            self.background,

            (0, 0)

        )

        for plataforma in self.plataformas:

            plataforma.desenhar(
                tela
            )

        self.driver.desenhar(
            tela
        )

        self.word.desenhar(
            tela
        )

        for virus in self.virus_lista:

            virus.desenhar(
                tela
            )

        self.jogador.desenhar(
            tela
        )

        self.hud.desenhar_fase2(

            tela,

            self.inventario,

            self.virus_mortos,

            8

        )