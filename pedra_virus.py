# ==========================================
# VÍRUS HUNTER
# pedra_virus.py
#
# Projétil disparado pelos vírus
# ==========================================

import pygame

from classes.constantes import *


class PedraVirus:

    def __init__(
        self,
        x,
        y,
        direcao
    ):

        # ==================================
        # POSIÇÃO
        # ==================================

        self.x = x
        self.y = y

        # ==================================
        # DIREÇÃO
        # ==================================

        self.direcao = direcao

        # ==================================
        # VELOCIDADE
        # ==================================

        self.velocidade = (
            VELOCIDADE_PEDRA_VIRUS
        )

        # ==================================
        # ESTADO
        # ==================================

        self.ativa = True

        # ==================================
        # SPRITE
        # ==================================

        self.imagem_original = pygame.image.load(
            PEDRA_VIRUS_IMG
        ).convert_alpha()

        self.imagem_original = pygame.transform.scale(
            self.imagem_original,
            (
                LARGURA_PEDRA_VIRUS,
                ALTURA_PEDRA_VIRUS
            )
        )

        self.imagem = self.imagem_original

        # ==================================
        # COLISÃO
        # ==================================

        self.rect = self.imagem.get_rect(
            center=(x, y)
        )

        # ==================================
        # ROTAÇÃO
        # ==================================

        self.angulo = 0

    # ======================================
    # MOVIMENTO
    # ======================================

    def mover(self):

        self.rect.x += (
            self.velocidade *
            self.direcao
        )

    # ======================================
    # ROTAÇÃO VISUAL
    # ======================================

    def rotacionar(self):

        self.angulo += 15

        if self.angulo >= 360:

            self.angulo = 0

    # ======================================
    # VERIFICAR LIMITES
    # ======================================

    def verificar_limites(self):

        if self.rect.right < 0:

            self.ativa = False

        elif self.rect.left > LARGURA_TELA:

            self.ativa = False

    # ======================================
    # DESTRUIR
    # ======================================

    def destruir(self):

        self.ativa = False

    # ======================================
    # ATUALIZAR
    # ======================================

    def atualizar(self):

        if not self.ativa:

            return

        self.mover()

        self.rotacionar()

        self.verificar_limites()

    # ======================================
    # DESENHAR
    # ======================================

    def desenhar(
        self,
        tela
    ):

        if not self.ativa:

            return

        imagem_rotacionada = (
            pygame.transform.rotate(
                self.imagem_original,
                self.angulo
            )
        )

        novo_rect = (
            imagem_rotacionada.get_rect(
                center=self.rect.center
            )
        )

        tela.blit(
            imagem_rotacionada,
            novo_rect
        )

    # ======================================
    # ESTÁ ATIVA?
    # ======================================

    def esta_ativa(self):

        return self.ativa