# ==========================================
# VÍRUS HUNTER
# porta.py
#
# Portas da Fase 2
# ==========================================

import pygame

from classes.constantes import *


class Porta:

    def __init__(

        self,

        x,
        y,

        imagem,

        nome,

        destino

    ):

        # ==================================
        # IDENTIFICAÇÃO
        # ==================================

        self.nome = nome

        self.destino = destino

        # ==================================
        # IMAGEM
        # ==================================

        self.imagem = pygame.image.load(
            imagem
        ).convert_alpha()

        self.imagem = pygame.transform.scale(

            self.imagem,

            (120, 120)

        )

        # ==================================
        # POSIÇÃO
        # ==================================

        self.rect = self.imagem.get_rect()

        self.rect.x = x

        self.rect.y = y

    # ======================================
    # DESENHAR
    # ======================================

    def desenhar(

        self,

        tela

    ):

        tela.blit(

            self.imagem,

            self.rect

        )

    # ======================================
    # TEXTO
    # ======================================

    def desenhar_nome(

        self,

        tela,

        fonte

    ):

        texto = fonte.render(

            self.nome,

            True,

            BRANCO

        )

        rect = texto.get_rect(

            center=(

                self.rect.centerx,

                self.rect.bottom + 20

            )

        )

        tela.blit(

            texto,

            rect

        )

    # ======================================
    # INTERAÇÃO
    # ======================================

    def desenhar_interacao(

        self,

        tela,

        fonte

    ):

        texto = fonte.render(

            "Pressione D",

            True,

            AMARELO

        )

        rect = texto.get_rect(

            center=(

                self.rect.centerx,

                self.rect.y - 30

            )

        )

        tela.blit(

            texto,

            rect

        )