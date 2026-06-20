# ==========================================
# VÍRUS HUNTER
# fase.py
#
# Classe base para todas as fases
#
# Herança:
#
# Fase
#   ├── Fase1
#   ├── Fase2
#   └── Fase3
#
# ==========================================

import pygame


class Fase:

    def __init__(

        self,

        tela,

        audio,

        inventario

    ):

        # ==================================
        # REFERÊNCIAS PRINCIPAIS
        # ==================================

        self.tela = tela

        self.audio = audio

        self.inventario = inventario

        # ==================================
        # CONTROLE DE FASE
        # ==================================

        self.concluida = False

        self.game_over = False

        # ==================================
        # CONTROLE DE TEMPO
        # ==================================

        self.tempo_inicio = pygame.time.get_ticks()

        self.tempo_fase = 0

        # ==================================
        # MENSAGENS
        # ==================================

        self.mensagem = ""

        self.exibir_mensagem = False

        self.tempo_mensagem = 0

        # ==================================
        # TELA DE RECOMPENSA
        # ==================================

        self.recompensa_ativa = False

        self.tempo_recompensa = 0

    # ======================================
    # ATUALIZAR
    #
    # Sobrescrito por:
    # Fase1
    # Fase2
    # Fase3
    # ======================================

    def atualizar(self):

        pass

    # ======================================
    # DESENHAR
    #
    # Sobrescrito por:
    # Fase1
    # Fase2
    # Fase3
    # ======================================

    def desenhar(

        self,

        tela

    ):

        pass

    # ======================================
    # TEMPO DA FASE
    # ======================================

    def atualizar_tempo(self):

        agora = pygame.time.get_ticks()

        self.tempo_fase = (

            agora

            -

            self.tempo_inicio

        )

    # ======================================
    # EXIBIR MENSAGEM
    #
    # Exemplo:
    #
    # "VOCÊ OBTEVE A PEDRA DIGITAL"
    #
    # ======================================

    def mostrar_mensagem(

        self,

        texto,

        duracao=3000

    ):

        self.mensagem = texto

        self.exibir_mensagem = True

        self.tempo_mensagem = (

            pygame.time.get_ticks()

            +

            duracao

        )

    # ======================================
    # CONTROLE MENSAGEM
    # ======================================

    def atualizar_mensagem(self):

        if not self.exibir_mensagem:

            return

        if (

            pygame.time.get_ticks()

            >

            self.tempo_mensagem

        ):

            self.exibir_mensagem = False

    # ======================================
    # DESENHAR MENSAGEM
    # ======================================

    def desenhar_mensagem(

        self,

        tela

    ):

        if not self.exibir_mensagem:

            return

        fonte = pygame.font.SysFont(

            "arial",

            60,

            bold=True

        )

        texto = fonte.render(

            self.mensagem,

            True,

            (255, 255, 0)

        )

        rect = texto.get_rect(

            center=(

                tela.get_width() // 2,

                tela.get_height() // 2

            )

        )

        tela.blit(

            texto,

            rect

        )

    # ======================================
    # ATIVAR RECOMPENSA
    #
    # Pedra Digital
    # Tesoura
    # Papel
    #
    # ======================================

    def ativar_recompensa(self):

        self.recompensa_ativa = True

        self.tempo_recompensa = (

            pygame.time.get_ticks()

            +

            3000

        )

    # ======================================
    # CONTROLE RECOMPENSA
    # ======================================

    def atualizar_recompensa(self):

        if not self.recompensa_ativa:

            return

        if (

            pygame.time.get_ticks()

            >

            self.tempo_recompensa

        ):

            self.recompensa_ativa = False

    # ======================================
    # GAME OVER
    # ======================================

    def ativar_game_over(self):

        self.game_over = True

    # ======================================
    # STATUS
    # ======================================

    def fase_concluida(self):

        return self.concluida

    def houve_game_over(self):

        return self.game_over