# ==========================================
# VÍRUS HUNTER
# arquivo_corrompido.py
#
# Arquivos perdidos da Fase 1
# ==========================================

import pygame

from classes.constantes import *


class ArquivoCorrompido:

    def __init__(self, x, y):

        # ==============================
        # SPRITE
        # ==============================

        self.imagem = pygame.image.load(
            ARQUIVO_CORROMPIDO_IMG
        ).convert_alpha()

        self.imagem = pygame.transform.scale(
            self.imagem,
            (60, 60)
        )

        # ==============================
        # POSIÇÃO
        # ==============================

        self.rect = self.imagem.get_rect()

        self.rect.x = x

        self.rect.y = y

        # ==============================
        # ESTADO
        # ==============================

        self.coletado = False

        # ==============================
        # ANIMAÇÃO
        # ==============================

        self.offset = 0

        self.subindo = True

    # ======================================
    # RECUPERAR ARQUIVO
    # ======================================

    def recuperar(self):

        self.coletado = True

    # ======================================
    # STATUS
    # ======================================

    def foi_recuperado(self):

        return self.coletado

    # ======================================
    # ANIMAÇÃO
    # ======================================

    def animar(self):

        if self.coletado:

            return

        if self.subindo:

            self.offset += 0.2

            if self.offset >= 5:

                self.subindo = False

        else:

            self.offset -= 0.2

            if self.offset <= -5:

                self.subindo = True

    # ======================================
    # ATUALIZAR
    # ======================================

    def atualizar(self):

        self.animar()

    # ======================================
    # DESENHAR
    # ======================================

    def desenhar(self, tela):

        if self.coletado:

            return

        tela.blit(

            self.imagem,

            (
                self.rect.x,
                self.rect.y + self.offset
            )

        )

    # ======================================
    # MENSAGEM
    # ======================================

    def desenhar_interacao(

        self,

        tela,

        fonte

    ):

        if self.coletado:

            return

        texto = fonte.render(

            "Pressione D",

            True,

            BRANCO

        )

        texto_rect = texto.get_rect(

            center=(

                self.rect.centerx,

                self.rect.y - 30

            )

        )

        tela.blit(

            texto,

            texto_rect

        )