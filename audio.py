# ==========================================
# VÍRUS HUNTER
# audio.py
# ==========================================

import pygame

from classes.constantes import *


class Audio:

    def __init__(self):

        # ==================================
        # INICIALIZA MIXER
        # ==================================

        if not pygame.mixer.get_init():
            pygame.mixer.init()

        # ==================================
        # SONS DO JOGADOR
        # ==================================

        self.som_andar = pygame.mixer.Sound(
            SOM_ANDAR
        )

        self.som_pulo = pygame.mixer.Sound(
            SOM_PULO
        )

        self.som_dano = pygame.mixer.Sound(
            SOM_DANO
        )

        # ==================================
        # PORTAS
        # ==================================

        self.som_porta = pygame.mixer.Sound(
            SOM_PORTA
        )

        # ==================================
        # VIRUS
        # ==================================

        self.som_virus_ataque = pygame.mixer.Sound(
            SOM_VIRUS_ATAQUE
        )

        self.som_virus_morte = pygame.mixer.Sound(
            SOM_VIRUS_MORTE
        )

        # ==================================
        # ARMAS
        # ==================================

        self.som_pedra = pygame.mixer.Sound(
            SOM_PEDRA
        )

        self.som_tesoura = pygame.mixer.Sound(
            SOM_TESOURA
        )

        self.som_papel = pygame.mixer.Sound(
            SOM_PAPEL
        )

        self.som_troca_arma = pygame.mixer.Sound(
            SOM_TROCA_ARMA
        )

        # ==================================
        # ITENS
        # ==================================

        self.som_arquivo = pygame.mixer.Sound(
            SOM_ARQUIVO
        )

        self.som_driver = pygame.mixer.Sound(
            SOM_DRIVER
        )

        self.som_word = pygame.mixer.Sound(
            SOM_WORD
        )

        # ==================================
        # SISTEMA
        # ==================================

        self.som_vitoria = pygame.mixer.Sound(
            SOM_VITORIA
        )

        self.som_game_over = pygame.mixer.Sound(
            SOM_GAME_OVER
        )

        # ==================================
        # CONFIGURA VOLUMES
        # ==================================

        self.configurar_volumes()

    # ======================================
    # VOLUMES
    # ======================================

    def configurar_volumes(self):

        self.som_andar.set_volume(
            VOLUME_EFEITOS
        )

        self.som_pulo.set_volume(
            VOLUME_EFEITOS
        )

        self.som_dano.set_volume(
            VOLUME_EFEITOS
        )

        self.som_porta.set_volume(
            VOLUME_EFEITOS
        )

        self.som_virus_ataque.set_volume(
            VOLUME_EFEITOS
        )

        self.som_virus_morte.set_volume(
            VOLUME_EFEITOS
        )

        self.som_pedra.set_volume(
            VOLUME_EFEITOS
        )

        self.som_tesoura.set_volume(
            VOLUME_EFEITOS
        )

        self.som_papel.set_volume(
            VOLUME_EFEITOS
        )

        self.som_troca_arma.set_volume(
            VOLUME_EFEITOS
        )

        self.som_arquivo.set_volume(
            VOLUME_EFEITOS
        )

        self.som_driver.set_volume(
            VOLUME_EFEITOS
        )

        self.som_word.set_volume(
            VOLUME_EFEITOS
        )

        self.som_vitoria.set_volume(
            VOLUME_EFEITOS
        )

        self.som_game_over.set_volume(
            VOLUME_EFEITOS
        )

    # ======================================
    # MUSICAS
    # ======================================

    def tocar_musica_fase1(self):

        pygame.mixer.music.load(
            MUSICA_FASE1
        )

        pygame.mixer.music.set_volume(
            VOLUME_MUSICA
        )

        pygame.mixer.music.play(-1)

    def tocar_musica_fase2(self):

        pygame.mixer.music.load(
            MUSICA_FASE2
        )

        pygame.mixer.music.set_volume(
            VOLUME_MUSICA
        )

        pygame.mixer.music.play(-1)

    def tocar_musica_fase3(self):

        pygame.mixer.music.load(
            MUSICA_FASE3
        )

        pygame.mixer.music.set_volume(
            VOLUME_MUSICA
        )

        pygame.mixer.music.play(-1)

    # ======================================
    # CONTROLE MUSICA
    # ======================================

    def parar_musica(self):

        pygame.mixer.music.stop()

    def pausar_musica(self):

        pygame.mixer.music.pause()

    def continuar_musica(self):

        pygame.mixer.music.unpause()

    # ======================================
    # JOGADOR
    # ======================================

    def tocar_andar(self):

        self.som_andar.play()

    def tocar_pulo(self):

        self.som_pulo.play()

    def tocar_dano(self):

        self.som_dano.play()

    # ======================================
    # PORTA
    # ======================================

    def tocar_porta(self):

        self.som_porta.play()

    # ======================================
    # VIRUS
    # ======================================

    def tocar_virus_ataque(self):

        self.som_virus_ataque.play()

    def tocar_virus_morte(self):

        self.som_virus_morte.play()

    # ======================================
    # ARMAS
    # ======================================

    def tocar_pedra(self):

        self.som_pedra.play()

    def tocar_tesoura(self):

        self.som_tesoura.play()

    def tocar_papel(self):

        self.som_papel.play()

    def tocar_troca_arma(self):

        self.som_troca_arma.play()

    # ======================================
    # ITENS
    # ======================================

    def tocar_arquivo(self):

        self.som_arquivo.play()

    def tocar_driver(self):

        self.som_driver.play()

    def tocar_word(self):

        self.som_word.play()

    # ======================================
    # SISTEMA
    # ======================================

    def tocar_vitoria(self):

        self.som_vitoria.play()

    def tocar_game_over(self):

        self.som_game_over.play()

    # ======================================
    # PARAR TODOS
    # ======================================

    def parar_todos(self):

        pygame.mixer.stop()

        pygame.mixer.music.stop()