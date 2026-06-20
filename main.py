# ==========================================
# VÍRUS HUNTER
# main.py
#
# Arquivo principal do jogo
# ==========================================

import pygame

from classes.jogo import Jogo

def main():

    # ======================================
    # INICIALIZA PYGAME
    # ======================================

    pygame.init()

    # Inicializa mixer de áudio
    pygame.mixer.init()

    # ======================================
    # CRIA O JOGO
    # ======================================

    jogo = Jogo()

    # ======================================
    # EXECUTA LOOP PRINCIPAL
    # ======================================

    jogo.executar()

    # ======================================
    # ENCERRA PYGAME
    # ======================================

    pygame.quit()


# ==========================================
# PONTO DE ENTRADA
# ==========================================

if __name__ == "__main__":

    main()