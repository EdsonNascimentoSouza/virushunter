# ==========================================
# VÍRUS HUNTER
# sala.py
#
# Classe base para salas da Fase 2
# ==========================================

import pygame


class Sala:

    def __init__(

        self,

        nome,

        fundo

    ):

        # ==================================
        # IDENTIFICAÇÃO
        # ==================================

        self.nome = nome

        # ==================================
        # BACKGROUND
        # ==================================

        self.fundo = pygame.image.load(
            fundo
        ).convert()

        # ==================================
        # OBJETOS DA SALA
        # ==================================

        self.plataformas = []

        self.virus = []

        self.itens = []

        # ==================================
        # CONTROLE
        # ==================================

        self.concluida = False

    # ======================================
    # ATUALIZAR
    # ======================================

    def atualizar(self):

        for virus in self.virus:

            virus.atualizar()

        for item in self.itens:

            item.atualizar()

    # ======================================
    # DESENHAR
    # ======================================

    def desenhar(

        self,

        tela

    ):

        tela.blit(

            self.fundo,

            (0, 0)

        )

        for plataforma in self.plataformas:

            plataforma.desenhar(
                tela
            )

        for item in self.itens:

            item.desenhar(
                tela
            )

        for virus in self.virus:

            virus.desenhar(
                tela
            )

    # ======================================
    # ADICIONAR
    # ======================================

    def adicionar_virus(

        self,

        virus

    ):

        self.virus.append(
            virus
        )

    def adicionar_item(

        self,

        item

    ):

        self.itens.append(
            item
        )

    def adicionar_plataforma(

        self,

        plataforma

    ):

        self.plataformas.append(
            plataforma
        )

    # ======================================
    # STATUS
    # ======================================

    def total_virus(self):

        return len(self.virus)

    def virus_vivos(self):

        total = 0

        for virus in self.virus:

            if virus.esta_vivo():

                total += 1

        return total