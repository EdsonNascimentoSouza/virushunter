# ==========================================
# VÍRUS HUNTER
# fase3.py
#
# BOSS FINAL
# ==========================================

import pygame

from classes.fase import Fase

from classes.jogador import Jogador

from classes.boss import Boss

from classes.hud import HUD

from classes.constantes import *


class Fase3(Fase):

    def __init__(

        self,

        tela,

        audio,

        inventario

    ):

        super().__init__(

            tela,

            audio,

            inventario

        )

        # ==================================
        # SISTEMAS
        # ==================================

        self.hud = HUD()

        self.audio = audio

        # ==================================
        # FUNDO
        # ==================================

        self.background = pygame.image.load(

            FUNDO_FASE3

        ).convert()

        self.background = pygame.transform.scale(

            self.background,

            (

                LARGURA_TELA,

                ALTURA_TELA

            )

        )

        # ==================================
        # JOGADOR
        # ==================================

        self.jogador = Jogador(

            inventario,

            audio

        )

        self.jogador.rect.x = 500

        self.jogador.rect.y = 650

        # ==================================
        # BOSS
        # ==================================

        self.boss = Boss()

        # ==================================
        # CONTROLE
        # ==================================

        self.tecla_f_pressionada = False

        # ==================================
# ESCOLHA DO JOGADOR
# ==================================

        self.escolha_jogador = ARMA_PEDRA

# ==================================
# RESULTADO DA RODADA
# ==================================

        self.resultado = ""

        self.arma_boss_rodada = ""

        self.tempo_resultado = 0

# ======================================
# ESCOLHER ARMA
# ======================================

    def verificar_escolha_arma(self):

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_1]:

            self.escolha_jogador = ARMA_PEDRA

        elif teclas[pygame.K_2]:

            self.escolha_jogador = ARMA_TESOURA

        elif teclas[pygame.K_3]:

            self.escolha_jogador = ARMA_PAPEL        


        # ==================================
        # MÚSICA
        # ==================================

        #self.audio.tocar_musica_fase3()

    # ======================================
# JOGAR RODADA
# ======================================

    def verificar_ataque(self):

        teclas = pygame.key.get_pressed()

        if not teclas[pygame.K_f]:

            self.tecla_f_pressionada = False

            return

        if self.tecla_f_pressionada:

            return

        self.tecla_f_pressionada = True

        arma_jogador = self.escolha_jogador

        arma_boss = self.boss.escolher_arma()

        self.arma_boss_rodada = arma_boss

    # ==============================
    # EMPATE
    # ==============================

        if arma_jogador == arma_boss:

            self.resultado = "EMPATE"

            self.tempo_resultado = pygame.time.get_ticks()

            return

    # ==============================
    # VITÓRIA OU DERROTA
    # ==============================

        venceu = (

            (arma_jogador == ARMA_PEDRA and arma_boss == ARMA_TESOURA)

            or

            (arma_jogador == ARMA_TESOURA and arma_boss == ARMA_PAPEL)

            or

            (arma_jogador == ARMA_PAPEL and arma_boss == ARMA_PEDRA)

        )

        if venceu:

            self.boss.receber_dano()

            self.resultado = "VOCE VENCEU"

        else:

            self.inventario.receber_dano()

            self.resultado = "VOCE PERDEU"

        self.tempo_resultado = pygame.time.get_ticks()  

# ======================================
# VITÓRIA
# ======================================        
    def verificar_vitoria(self):

        if not self.boss.esta_vivo():

            self.audio.tocar_vitoria()

            self.concluida = True
   
   
    # ======================================
    # GAME OVER
    # ======================================

    def verificar_game_over(self):

        if not self.inventario.esta_vivo():

            self.audio.tocar_game_over()

            self.game_over = True

    # ======================================
    # ATUALIZAR
    # ======================================

    def atualizar(self):

        self.verificar_escolha_arma()

        self.verificar_ataque()

        self.verificar_vitoria()

        self.verificar_game_over()

    # ======================================
    # DESENHAR
    # ======================================

    def desenhar(self, tela):

        tela.blit(

            self.background,

            (0, 0)

        )

        self.hud.desenhar_fase3(
            tela,

            self.inventario,

            self.boss.vida,

            VIDA_BOSS

        )

# ==================================
# ARMA ESCOLHIDA
# ==================================

        fonte = pygame.font.SysFont("arial",40,bold=True)

        texto = fonte.render( f"SUA ARMA: {self.escolha_jogador}",True,BRANCO)

        tela.blit(texto,(50, 300))

# ==================================
# INSTRUCOES
# ==================================

        texto = fonte.render("1=PEDRA  2=TESOURA  3=PAPEL",True,AMARELO)

        tela.blit(texto,(50, 350))

        texto = fonte.render("F = JOGAR",True,AMARELO)

        tela.blit(texto,(50, 400))
        if self.resultado != "":

            texto = fonte.render( f"BOSS: {self.arma_boss_rodada}",True,VERMELHO)

            tela.blit(texto,(700, 300))

            texto = fonte.render(self.resultado,True,AMARELO)

            tela.blit(texto,(700, 360))