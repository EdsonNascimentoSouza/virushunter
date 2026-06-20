# ==========================================
# VÍRUS HUNTER
# jogo.py
#
# Gerenciador principal do jogo
# ==========================================

import pygame

from classes.constantes import *

from classes.audio import Audio
from classes.inventario import Inventario

from classes.fase1 import Fase1
from classes.fase2 import Fase2

# Descomente quando criar
from classes.fase3 import Fase3


class Jogo:

    def __init__(self):

        # ==================================
        # TELA
        # ==================================

        self.tela = pygame.display.set_mode(

            (
                LARGURA_TELA,
                ALTURA_TELA
            )

        )

        pygame.display.set_caption(
            TITULO_JOGO
        )

        # ==================================
        # RELÓGIO
        # ==================================

        self.clock = pygame.time.Clock()

        # ==================================
        # CONTROLE
        # ==================================

        self.rodando = True

        # ==================================
        # SISTEMAS
        # ==================================

        self.audio = Audio()

        self.inventario = Inventario()

        # ==================================
        # FASE ATUAL
        # ==================================

        self.fase_atual = 1

        # ==================================
        # CARREGA FASE 1
        # ==================================

        self.carregar_fase1()

    # ======================================
    # FASE 1
    # ======================================

    def carregar_fase1(self):

        self.fase_atual = 1

        self.fase = Fase1(

            self.tela,

            self.audio,

            self.inventario

        )

        self.audio.tocar_musica_fase1()

    # ======================================
    # FASE 2
    # ======================================

    def carregar_fase2(self):

        self.fase_atual = 2

        self.fase = Fase2(

            self.tela,

            self.audio,

            self.inventario

        )

        self.audio.tocar_musica_fase2()

    # ======================================
    # FASE 3
    # ======================================

    def carregar_fase3(self):

        self.fase_atual = 3

        self.fase = Fase3(

            self.tela,

            self.audio,

            self.inventario

        )

        self.audio.tocar_musica_fase3()
      
    # ======================================
    # GAME OVER
    # ======================================
    def tela_vitoria(self):

        self.audio.parar_musica()

        self.audio.tocar_vitoria()

        fonte = pygame.font.SysFont(

            "arial",

            80,

            bold=True

        )

        self.tela.fill((0,0,0))

        texto = fonte.render(

        "SISTEMA RECUPERADO!",

            True,

        (0,255,0)

    )

        rect = texto.get_rect(

            center=(

                LARGURA_TELA//2,

                ALTURA_TELA//2

            )

        )

        self.tela.blit(

            texto,

            rect

        )

        pygame.display.flip()

        pygame.time.delay(5000)

        self.rodando = False
    
    def game_over(self):

        self.audio.parar_musica()

        self.audio.tocar_game_over()

        try:

            imagem = pygame.image.load(
                GAME_OVER_IMG
            ).convert()

            imagem = pygame.transform.scale(

                imagem,

                (
                    LARGURA_TELA,
                    ALTURA_TELA
                )

            )

            self.tela.blit(

                imagem,

                (0, 0)

            )

            pygame.display.flip()

        except:

            print(
                "Imagem GAME OVER não encontrada."
            )

        pygame.time.delay(3000)

        # Reinicia inventário

        self.inventario.reiniciar()

        # Volta para a Fase 1

        self.carregar_fase1()

    # ======================================
    # EVENTOS
    # ======================================

    def processar_eventos(self):

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                self.rodando = False

            if evento.type == pygame.KEYDOWN:

                # ----------------------
                # PULO
                # ----------------------

                if evento.key == pygame.K_SPACE:

                    self.fase.jogador.pular()

    # ======================================
    # TROCA DE FASE
    # ======================================

    def verificar_transicoes(self):

        if not self.fase.concluida:

            return

        # ------------------------------
        # FASE 1 -> FASE 2
        # ------------------------------

        if self.fase_atual == 1:

            self.carregar_fase2()

        # ------------------------------
        # FASE 2 -> FASE 3
        # ------------------------------

        elif self.fase_atual == 2:

            self.carregar_fase3()

        elif self.fase_atual == 3:

            self.tela_vitoria()

    # ======================================
    # LOOP PRINCIPAL
    # ======================================
    def executar(self):

        while self.rodando:

            #print("loop")
            self.clock.tick(FPS)

            # ==========================
            # EVENTOS
            # ==========================

            self.processar_eventos()
            

            # ==========================
            # ATUALIZA
            # ==========================

            self.fase.atualizar()
           
            # ==========================
            # DESENHA
            # ==========================
            
            #self.fase.desenhar(self.tela)

            #pygame.display.flip()

            #print(type(self.fase))
            #print(self.fase)
            #print(self.fase.desenhar)

            self.fase.desenhar(self.tela)

            pygame.display.flip()
            
        
            # ==========================
            # GAME OVER
            # ==========================

            if not self.inventario.esta_vivo():

                self.game_over()

            # ==========================
            # TROCA DE FASE
            # ==========================

            self.verificar_transicoes()

        pygame.quit()
    def verificar_vitoria(self):

        if not self.boss.esta_vivo():

            self.concluida = True