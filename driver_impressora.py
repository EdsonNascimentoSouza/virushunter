# ==========================================
# VÍRUS HUNTER
# driver_impressora.py
#
# Item especial da Fase 2
#
# Ao salvar o Driver:
#
# ✓ Ganha a Tesoura
# ✓ Exibe mensagem
# ✓ Atualiza Inventário
#
# ==========================================

import pygame

from classes.constantes import *


class DriverImpressora:

    def __init__(

        self,

        x,
        y

    ):

        # ==================================
        # SPRITE
        # ==================================

        self.imagem = pygame.image.load(
            DRIVER_IMPRESSORA_IMG
        ).convert_alpha()

        self.imagem = pygame.transform.scale(

            self.imagem,

            (
                70,
                70
            )

        )

        # ==================================
        # POSIÇÃO
        # ==================================

        self.rect = self.imagem.get_rect()

        self.rect.x = x

        self.rect.y = y

        # ==================================
        # ESTADO
        # ==================================

        self.salvo = False

        # ==================================
        # ANIMAÇÃO FLUTUANTE
        # ==================================

        self.direcao = 1

        self.offset = 0

        self.velocidade_animacao = 0.3

    # ======================================
    # SALVAR DRIVER
    # ======================================

    def salvar(self):

        self.salvo = True

    # ======================================
    # STATUS
    # ======================================

    def foi_salvo(self):

        return self.salvo

    # ======================================
    # ANIMAÇÃO
    #
    # Faz o item flutuar
    # ======================================

    def atualizar(self):

        if self.salvo:

            return

        self.offset += (

            self.direcao

            *

            self.velocidade_animacao

        )

        if self.offset >= 5:

            self.direcao = -1

        elif self.offset <= -5:

            self.direcao = 1

    # ======================================
    # DESENHAR
    # ======================================

    def desenhar(

        self,

        tela

    ):

        if self.salvo:

            return

        tela.blit(

            self.imagem,

            (

                self.rect.x,

                self.rect.y + self.offset

            )

        )

    # ======================================
    # POSIÇÃO
    # ======================================

    def get_x(self):

        return self.rect.x

    def get_y(self):

        return self.rect.y

    # ======================================
    # CENTRO
    # ======================================

    def centro(self):

        return (

            self.rect.centerx,

            self.rect.centery

        )