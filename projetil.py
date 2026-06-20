# ==========================================
# VÍRUS HUNTER
# projetil.py
#
# Sistema único de projéteis
# ==========================================

import pygame

from classes.constantes import *


class Projetil:

    def __init__(
        self,
        x,
        y,
        tipo,
        direcao
    ):

        # ==================================
        # TIPO DO PROJÉTIL
        # ==================================

        self.tipo = tipo

        # ==================================
        # SPRITE
        # ==================================

        if self.tipo == ARMA_PEDRA:

            self.imagem = pygame.image.load(
                PROJETIL_PEDRA
            ).convert_alpha()

        elif self.tipo == ARMA_TESOURA:

            self.imagem = pygame.image.load(
                PROJETIL_TESOURA
            ).convert_alpha()

        elif self.tipo == ARMA_PAPEL:

            self.imagem = pygame.image.load(
                PROJETIL_PAPEL
            ).convert_alpha()

        self.imagem = pygame.transform.scale(
            self.imagem,
            (
                40,
                40
            )
        )

        # ==================================
        # POSIÇÃO
        # ==================================

        self.rect = self.imagem.get_rect()

        self.rect.centerx = x

        self.rect.centery = y

        # ==================================
        # MOVIMENTO
        # ==================================

        self.direcao = direcao

        self.velocidade = VELOCIDADE_PROJETIL

        # ==================================
        # CONTROLE
        # ==================================

        self.ativo = True

    # ======================================
    # MOVIMENTAÇÃO
    # ======================================

    def atualizar(self):

        self.rect.x += (

            self.velocidade

            *

            self.direcao

        )

        # Saiu da tela

        if self.rect.right < 0:

            self.ativo = False

        if self.rect.left > LARGURA_TELA:

            self.ativo = False

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
    # REMOVER
    # ======================================

    def destruir(self):

        self.ativo = False

    # ======================================
    # STATUS
    # ======================================

    def esta_ativo(self):

        return self.ativo

    # ======================================
    # TIPO
    # ======================================

    def eh_pedra(self):

        return self.tipo == ARMA_PEDRA

    def eh_tesoura(self):

        return self.tipo == ARMA_TESOURA

    def eh_papel(self):

        return self.tipo == ARMA_PAPEL