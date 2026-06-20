# ==========================================
# VÍRUS HUNTER
# plataforma.py
#
# Classe responsável pelas plataformas
#
# Utilizada em:
# - Fase 1
# - Fase 2
# - Fase 3
#
# Pode utilizar:
# - Imagem
# - Plataforma invisível
#
# ==========================================

import pygame

from classes.constantes import *


class Plataforma:

    def __init__(

        self,

        x,
        y,

        largura,
        altura,

        imagem=None

    ):

        # ==================================
        # POSIÇÃO
        # ==================================

        self.x = x

        self.y = y

        # ==================================
        # TAMANHO
        # ==================================

        self.largura = largura

        self.altura = altura

        # ==================================
        # COLISÃO
        # ==================================

        self.rect = pygame.Rect(

            self.x,
            self.y,

            self.largura,
            self.altura

        )

        # ==================================
        # IMAGEM OPCIONAL
        # ==================================

        self.imagem = None

        if imagem:

            self.imagem = pygame.image.load(
                imagem
            ).convert_alpha()

            self.imagem = pygame.transform.scale(

                self.imagem,

                (
                    self.largura,
                    self.altura
                )

            )

    # ======================================
    # ATUALIZAR
    # ======================================

    def atualizar(self):

        pass

    # ======================================
    # DESENHAR
    # ======================================

    def desenhar(

        self,

        tela

    ):

        # ==============================
        # COM IMAGEM
        # ==============================

        if self.imagem:

            tela.blit(

                self.imagem,

                (
                    self.rect.x,
                    self.rect.y
                )

            )

        # ==============================
        # DEBUG DE COLISÃO
        # ==============================

        if DEBUG_COLISAO:

            pygame.draw.rect(

                tela,

                (255, 0, 0),

                self.rect,

                2

            )

    # ======================================
    # DESENHAR COLISÃO
    #
    # Utilizado apenas para testes
    # ======================================

    def desenhar_colisao(

        self,

        tela

    ):

        pygame.draw.rect(

            tela,

            (255, 0, 0),

            self.rect,

            2

        )