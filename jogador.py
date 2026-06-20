# ==========================================
# VÍRUS HUNTER
# jogador.py
# ==========================================

import pygame

from classes.constantes import *
from classes.projetil import Projetil


class Jogador:

    def __init__(

        self,

        inventario,

        audio

    ):

        self.inventario = inventario

        self.audio = audio

        # ==================================
        # SPRITES
        # ==================================

        self.carregar_sprites()

        self.imagem = self.sprite_idle

        self.rect = self.imagem.get_rect()

        # ==================================
        # POSIÇÃO
        # ==================================

        self.rect.x = JOGADOR_X_INICIAL

        self.rect.y = JOGADOR_Y_INICIAL

        # ==================================
        # MOVIMENTO
        # ==================================

        self.vel_x = 0

        self.vel_y = 0

        self.direcao = 1

        self.no_chao = False

        # ==================================
        # ANIMAÇÃO
        # ==================================

        self.frame = 0

        self.contador_animacao = 0

        # ==================================
        # DANO
        # ==================================

        self.recebendo_dano = False

        self.tempo_dano = 0

        # ==================================
        # PROJETEIS
        # ==================================

        self.projeteis = []
# ==================================
# RECARGA DO TIRO
# ==================================

        self.ultimo_tiro = 0

        self.tempo_recarga_tiro = 500

        # ==================================
        # CONTROLES
        # ==================================

        self.tecla_f_liberada = True

        self.tecla_s_liberada = True

        # ==================================
        # FASE
        # ==================================

        self.ataque_habilitado = False

    # ======================================
    # SPRITES
    # ======================================

    def carregar_sprites(self):

        self.sprite_idle = pygame.image.load(
            CPU_IDLE
        ).convert_alpha()

        self.sprite_walk_1 = pygame.image.load(
            CPU_WALK_1
        ).convert_alpha()

        self.sprite_walk_2 = pygame.image.load(
            CPU_WALK_2
        ).convert_alpha()

        self.sprite_jump = pygame.image.load(
            CPU_JUMP
        ).convert_alpha()

        self.sprite_dano = pygame.image.load(
            CPU_DANO
        ).convert_alpha()

        self.sprite_idle = pygame.transform.scale(
            self.sprite_idle,
            (
                LARGURA_SPRITE_JOGADOR,
                ALTURA_SPRITE_JOGADOR
            )
        )

        self.sprite_walk_1 = pygame.transform.scale(
            self.sprite_walk_1,
            (
                LARGURA_SPRITE_JOGADOR,
                ALTURA_SPRITE_JOGADOR
            )
        )

        self.sprite_walk_2 = pygame.transform.scale(
            self.sprite_walk_2,
            (
                LARGURA_SPRITE_JOGADOR,
                ALTURA_SPRITE_JOGADOR
            )
        )

        self.sprite_jump = pygame.transform.scale(
            self.sprite_jump,
            (
                LARGURA_SPRITE_JOGADOR,
                ALTURA_SPRITE_JOGADOR
            )
        )

        self.sprite_dano = pygame.transform.scale(
            self.sprite_dano,
            (
                LARGURA_SPRITE_JOGADOR,
                ALTURA_SPRITE_JOGADOR
            )
        )

    # ======================================
    # HABILITAR ATAQUE
    # ======================================

    def habilitar_ataque(self):

        self.ataque_habilitado = True

        self.tempo_recarga_tiro = 500

    # ======================================
    # MOVIMENTO
    # ======================================

    def mover(self):

        teclas = pygame.key.get_pressed()

        self.vel_x = 0

        if teclas[pygame.K_LEFT]:

            self.vel_x = -VELOCIDADE_JOGADOR

            self.direcao = -1

        elif teclas[pygame.K_RIGHT]:

            self.vel_x = VELOCIDADE_JOGADOR

            self.direcao = 1

        self.rect.x += self.vel_x

    # ======================================
    # PULO
    # ======================================

    def pular(self):

        if self.no_chao:

            self.vel_y = FORCA_PULO

            self.no_chao = False

            self.audio.tocar_pulo()

    # ======================================
    # GRAVIDADE
    # ======================================

    def aplicar_gravidade(self):

        self.vel_y += GRAVIDADE

        self.rect.y += self.vel_y

    # ======================================
    # TROCA DE ARMA
    # ======================================

    def trocar_arma(self):

        self.inventario.trocar_arma()

        self.audio.tocar_troca_arma()

    # ======================================
    # ATIRAR
    # ======================================

    def atirar(self):

        if not self.ataque_habilitado:

            return

        agora = pygame.time.get_ticks()

        if (

            agora

            -

            self.ultimo_tiro

            <

            self.tempo_recarga_tiro

        ):

            return

        self.ultimo_tiro = agora

        arma = self.inventario.get_arma()

        if arma is None:

            return

        projetil = Projetil(

            self.rect.centerx,

            self.rect.centery,

            arma,

            self.direcao

        )

        self.projeteis.append(
            projetil
        )

        if arma == ARMA_PEDRA:

            self.audio.tocar_pedra()

        elif arma == ARMA_TESOURA:

            self.audio.tocar_tesoura()

        elif arma == ARMA_PAPEL:

            self.audio.tocar_papel()

    # ======================================
    # PROJETEIS
    # ======================================

    def atualizar_projeteis(self):

        for projetil in self.projeteis:

            projetil.atualizar()

        self.projeteis = [

            p

            for p in self.projeteis

            if p.esta_ativo()

        ]

    # ======================================
    # DANO
    # ======================================

    def receber_dano(self):

        if self.recebendo_dano:

            return

        self.inventario.receber_dano()

        self.recebendo_dano = True

        self.tempo_dano = pygame.time.get_ticks()

        self.audio.tocar_dano()

    # ======================================
    # ATUALIZA DANO
    # ======================================

    def atualizar_dano(self):

        if not self.recebendo_dano:

            return

        agora = pygame.time.get_ticks()

        if (

            agora - self.tempo_dano

            >

            TEMPO_DANO

        ):

            self.recebendo_dano = False

    # ======================================
    # QUICAR
    # ======================================

    def quicar(self):

        self.vel_y = -12

    # ======================================
    # LIMITES DA TELA
    # ======================================

    def limitar_tela(self):

        if self.rect.left < 0:

            self.rect.left = 0

        if self.rect.right > LARGURA_TELA:

            self.rect.right = LARGURA_TELA

    # ======================================
    # COLISÃO PLATAFORMAS
    # ======================================

    def verificar_colisao_plataformas(

        self,

        plataformas

    ):

        self.no_chao = False

        for plataforma in plataformas:

            # CAINDO

            if (

                self.vel_y > 0

                and

                self.rect.bottom >= plataforma.rect.top

                and

                self.rect.bottom - self.vel_y
                <= plataforma.rect.top

                and

                self.rect.right > plataforma.rect.left

                and

                self.rect.left < plataforma.rect.right

            ):

                self.rect.bottom = plataforma.rect.top

                self.vel_y = 0

                self.no_chao = True

            # SUBINDO

            elif (

                self.vel_y < 0

                and

                self.rect.top <= plataforma.rect.bottom

                and

                self.rect.top - self.vel_y
                >= plataforma.rect.bottom

                and

                self.rect.right > plataforma.rect.left

                and

                self.rect.left < plataforma.rect.right

            ):

                self.rect.top = plataforma.rect.bottom

                self.vel_y = 0

    # ======================================
    # ANIMAÇÃO
    # ======================================

    def animar(self):

        if self.recebendo_dano:

            sprite = self.sprite_dano

        elif not self.no_chao:

            sprite = self.sprite_jump

        elif self.vel_x == 0:

            sprite = self.sprite_idle

        else:

            self.contador_animacao += 1

            if self.contador_animacao >= 10:

                self.frame += 1

                self.contador_animacao = 0

            if self.frame % 2 == 0:

                sprite = self.sprite_walk_1

            else:

                sprite = self.sprite_walk_2

        if self.direcao == -1:

            sprite = pygame.transform.flip(

                sprite,

                True,

                False

            )

        self.imagem = sprite

    # ======================================
    # EVENTOS
    # ======================================

    def processar_eventos(self):

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_s]:

            if self.tecla_s_liberada:

                self.trocar_arma()

                self.tecla_s_liberada = False

        else:

            self.tecla_s_liberada = True

        if teclas[pygame.K_f]:

            if self.tecla_f_liberada:

                self.atirar()

                self.tecla_f_liberada = False

        else:

            self.tecla_f_liberada = True

    # ======================================
    # ATUALIZAR
    # ======================================

    def atualizar(

        self,

        plataformas

    ):

        self.processar_eventos()

        self.mover()

        self.aplicar_gravidade()

        self.atualizar_dano()

        self.atualizar_projeteis()

        self.limitar_tela()

        self.verificar_colisao_plataformas(
            plataformas
        )

        self.animar()

    # ======================================
    # DESENHAR
    # ======================================

    def desenhar(self, tela):

        tela.blit(

            self.imagem,

            self.rect

        )

        for projetil in self.projeteis:

            projetil.desenhar(tela)

    # ======================================
    # AUXILIARES
    # ======================================

    def esta_vivo(self):

        return self.inventario.esta_vivo()

    def obter_pedra(self):

        self.inventario.obter_pedra()

    def obter_tesoura(self):

        self.inventario.obter_tesoura()

    def obter_papel(self):

        self.inventario.obter_papel()