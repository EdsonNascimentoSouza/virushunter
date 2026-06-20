# ==========================================
# VÍRUS HUNTER
# virus.py
# ==========================================

import pygame

from classes.constantes import *
from classes.projetil import Projetil


class Virus:

    def __init__(

        self,

        x,
        y,

        limite_esquerda,
        limite_direita,

        arma=ARMA_PEDRA,

        audio=None

    ):

        self.audio = audio
        self.pode_atirar = True

        # ==================================
        # SPRITES
        # ==================================

        self.sprite_idle = pygame.image.load(
            VIRUS_IDLE
        ).convert_alpha()

        self.sprite_walk_1 = pygame.image.load(
            VIRUS_WALK_1
        ).convert_alpha()

        self.sprite_walk_2 = pygame.image.load(
            VIRUS_WALK_2
        ).convert_alpha()

        self.sprite_attack = pygame.image.load(
            VIRUS_ATTACK
        ).convert_alpha()

        self.sprite_dead = pygame.image.load(
            VIRUS_DEAD
        ).convert_alpha()

        self.sprite_idle = pygame.transform.scale(
            self.sprite_idle,
            (
                LARGURA_SPRITE_VIRUS,
                ALTURA_SPRITE_VIRUS
            )
        )

        self.sprite_walk_1 = pygame.transform.scale(
            self.sprite_walk_1,
            (
                LARGURA_SPRITE_VIRUS,
                ALTURA_SPRITE_VIRUS
            )
        )

        self.sprite_walk_2 = pygame.transform.scale(
            self.sprite_walk_2,
            (
                LARGURA_SPRITE_VIRUS,
                ALTURA_SPRITE_VIRUS
            )
        )

        self.sprite_attack = pygame.transform.scale(
            self.sprite_attack,
            (
                LARGURA_SPRITE_VIRUS,
                ALTURA_SPRITE_VIRUS
            )
        )

        self.sprite_dead = pygame.transform.scale(
            self.sprite_dead,
            (
                LARGURA_SPRITE_VIRUS,
                ALTURA_SPRITE_VIRUS
            )
        )

        self.imagem = self.sprite_idle

        self.rect = self.imagem.get_rect()

        # ==================================
        # POSIÇÃO
        # ==================================

        self.rect.x = x
        self.rect.y = y

        # ==================================
        # MOVIMENTO
        # ==================================

        self.velocidade = VELOCIDADE_VIRUS

        self.direcao = 1

        self.limite_esquerda = limite_esquerda
        self.limite_direita = limite_direita

        # ==================================
        # ARMA
        # ==================================

        self.arma = arma

        # ==================================
        # PROJÉTEIS
        # ==================================

        self.projeteis = []

        self.ultimo_ataque = pygame.time.get_ticks()

        # ==================================
        # VIDA
        # ==================================

        self.vivo = True

        self.remover = False

        self.tempo_morte = 0

        # ==================================
        # ANIMAÇÃO
        # ==================================

        self.frame = 0

        self.contador_animacao = 0

    # ======================================
    # DIREÇÃO DO JOGADOR
    # ======================================

    def direcao_jogador(self, jogador):

        if jogador.rect.centerx < self.rect.centerx:
            return -1

        return 1

    # ======================================
    # PATRULHA
    # ======================================

    def patrulhar(self):

        if not self.vivo:
            return

        self.rect.x += (

            self.velocidade

            *

            self.direcao

        )

        if self.rect.left <= self.limite_esquerda:

            self.direcao = 1

        if self.rect.right >= self.limite_direita:

            self.direcao = -1

    # ======================================
    # ATAQUE
    # ======================================

    def atacar(self, jogador):

        if not self.vivo:
            return

        agora = pygame.time.get_ticks()

        if (

            agora

            -

            self.ultimo_ataque

            <

            TEMPO_ATAQUE_VIRUS

        ):

            return

        self.ultimo_ataque = agora

        direcao = self.direcao_jogador(
            jogador
        )

        projetil = Projetil(

            self.rect.centerx,

            self.rect.centery,

            self.arma,

            direcao

        )

        self.projeteis.append(
            projetil
        )

        if self.audio:

            self.audio.tocar_virus_ataque()

    # ======================================
    # PROJÉTEIS
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
    # MORTE
    # ======================================

    def morrer(self):

        if not self.vivo:
            return

        self.vivo = False

        self.imagem = self.sprite_dead

        self.tempo_morte = pygame.time.get_ticks()

        if self.audio:

            self.audio.tocar_virus_morte()

    # ======================================
    # CONTROLE MORTE
    # ======================================

    def atualizar_morte(self):

        if self.vivo:
            return

        agora = pygame.time.get_ticks()

        if (

            agora

            -

            self.tempo_morte

            >

            TEMPO_MORTE_VIRUS

        ):

            self.remover = True

    # ======================================
    # ANIMAÇÃO
    # ======================================

    def animar(self):

        if not self.vivo:

            self.imagem = self.sprite_dead

            return

        self.contador_animacao += 1

        if self.contador_animacao >= 15:

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
    # ATUALIZAR
    # ======================================

    def atualizar(self, jogador):

        self.patrulhar()

        if self.pode_atirar:

            self.atacar(
                jogador
        )

   
    # PROJÉTEIS

        self.atualizar_projeteis()

    # MORTE

        self.atualizar_morte()

    # ANIMAÇÃO

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

            projetil.desenhar(
                tela
            )

    # ======================================
    # STATUS
    # ======================================

    def esta_vivo(self):

        return self.vivo

    def esta_morto(self):

        return not self.vivo

    def deve_remover(self):

        return self.remover