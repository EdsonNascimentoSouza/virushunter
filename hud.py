# ==========================================
# VÍRUS HUNTER
# hud.py
# ==========================================

import pygame

from classes.constantes import *


class HUD:

    def __init__(self):

        # ==================================
        # FONTES
        # ==================================

        self.fonte_titulo = pygame.font.SysFont(
            "arial",
            28,
            bold=True
        )

        self.fonte_texto = pygame.font.SysFont(
            "arial",
            22
        )

        self.fonte_pequena = pygame.font.SysFont(
            "arial",
            18
        )

        # ==================================
        # BATERIA
        # ==================================

        self.img_bateria = pygame.image.load(
            BATERIA_IMG
        ).convert_alpha()

        self.img_bateria = pygame.transform.scale(
            self.img_bateria,
            (40, 40)
        )

    # ======================================
    # VIDA
    # ======================================

    def desenhar_vida(

        self,

        tela,

        inventario

    ):

        x = 20
        y = 20

        for i in range(inventario.vida):

            tela.blit(

                self.img_bateria,

                (x, y)

            )

            x += 50

    # ======================================
    # ARMA ATUAL
    # ======================================

    def desenhar_arma(

        self,

        tela,

        inventario

    ):

        arma = inventario.get_arma()

        if arma is None:

            arma = "NENHUMA"

        texto = self.fonte_texto.render(

            f"ARMA: {arma}",

            True,

            BRANCO

        )

        tela.blit(

            texto,

            (20, 80)

        )

    # ======================================
    # INVENTÁRIO
    # ======================================

    def desenhar_inventario(

        self,

        tela,

        inventario

    ):

        itens = []

        if inventario.possui_pedra():
            itens.append("PEDRA")

        if inventario.possui_tesoura():
            itens.append("TESOURA")

        if inventario.possui_papel():
            itens.append("PAPEL")

        if inventario.possui_driver():
            itens.append("DRIVER")

        if inventario.possui_word():
            itens.append("WORD")

        texto = self.fonte_texto.render(

            "ITENS: " + ", ".join(itens),

            True,

            BRANCO

        )

        tela.blit(

            texto,

            (20, 120)

        )

    # ======================================
    # FASE 1
    # ======================================

    def desenhar_fase1(

        self,

        tela,

        inventario,

        arquivos_recuperados,

        total_arquivos,

        virus_mortos,

        total_virus

    ):

        self.desenhar_vida(
            tela,
            inventario
        )

        texto_arquivos = self.fonte_texto.render(

            f"ARQUIVOS: {arquivos_recuperados}/{total_arquivos}",

            True,

            BRANCO

        )

        tela.blit(

            texto_arquivos,

            (20, 90)

        )

        texto_virus = self.fonte_texto.render(

            f"VIRUS: {virus_mortos}/{total_virus}",

            True,

            BRANCO

        )

        tela.blit(

            texto_virus,

            (20, 130)

        )

    # ======================================
    # FASE 2
    # ======================================

    def desenhar_fase2(

        self,

        tela,

        inventario,

        virus_mortos,

        total_virus

    ):

        self.desenhar_vida(
            tela,
            inventario
        )

        self.desenhar_arma(
            tela,
            inventario
        )

        self.desenhar_inventario(
            tela,
            inventario
        )

        texto_virus = self.fonte_texto.render(

            f"VIRUS: {virus_mortos}/{total_virus}",

            True,

            BRANCO

        )

        tela.blit(

            texto_virus,

            (20, 160)

        )

        texto_driver = self.fonte_texto.render(

            f"DRIVER: {'SIM' if inventario.possui_driver() else 'NAO'}",

            True,

            BRANCO

        )

        tela.blit(

            texto_driver,

            (20, 200)

        )

        texto_word = self.fonte_texto.render(

            f"WORD: {'SIM' if inventario.possui_word() else 'NAO'}",

            True,

            BRANCO

        )

        tela.blit(

            texto_word,

            (20, 240)

        )

    # ======================================
    # FASE 3
    # ======================================

    def desenhar_fase3(

        self,

        tela,

        inventario,

        vida_boss,

        vida_maxima_boss

    ):

        self.desenhar_vida(
            tela,
            inventario
        )

        self.desenhar_arma(
            tela,
            inventario
        )

        self.desenhar_inventario(
            tela,
            inventario
        )

        texto_boss = self.fonte_texto.render(

            f"BOSS: {vida_boss}/{vida_maxima_boss}",

            True,

            VERMELHO

        )

        tela.blit(

            texto_boss,

            (20, 170)

        )

        largura_barra = 300

        altura_barra = 30

        pygame.draw.rect(

            tela,

            BRANCO,

            (

                20,
                210,

                largura_barra,
                altura_barra

            ),

            2

        )

        vida_atual = (

            vida_boss

            /

            vida_maxima_boss

        )

        pygame.draw.rect(

            tela,

            VERMELHO,

            (

                20,
                210,

                largura_barra * vida_atual,
                altura_barra

            )

        )

    # ======================================
    # GAME OVER
    # ======================================

    def desenhar_game_over(

        self,

        tela

    ):

        fonte = pygame.font.SysFont(

            "arial",

            72,

            bold=True

        )

        texto = fonte.render(

            "GAME OVER",

            True,

            VERMELHO

        )

        rect = texto.get_rect(

            center=(

                LARGURA_TELA // 2,

                ALTURA_TELA // 2

            )

        )

        tela.blit(

            texto,

            rect

        )

    # ======================================
    # MENSAGEM CENTRAL
    # ======================================

    def mensagem_central(

        self,

        tela,

        mensagem,

        cor=BRANCO

    ):

        fonte = pygame.font.SysFont(

            "arial",

            64,

            bold=True

        )

        texto = fonte.render(

            mensagem,

            True,

            cor

        )

        rect = texto.get_rect(

            center=(

                LARGURA_TELA // 2,

                ALTURA_TELA // 2

            )

        )

        tela.blit(

            texto,

            rect

        )

    # ======================================
    # TELA DE RECOMPENSA
    # ======================================

    def mostrar_recompensa(

        self,

        tela,

        mensagem

    ):

        overlay = pygame.Surface(

            (

                LARGURA_TELA,

                ALTURA_TELA

            )

        )

        overlay.set_alpha(180)

        overlay.fill(PRETO)

        tela.blit(

            overlay,

            (0, 0)

        )

        fonte = pygame.font.SysFont(

            "arial",

            60,

            bold=True

        )

        texto = fonte.render(

            mensagem,

            True,

            AMARELO

        )

        rect = texto.get_rect(

            center=(

                LARGURA_TELA // 2,

                ALTURA_TELA // 2

            )

        )

        tela.blit(

            texto,

            rect

        )