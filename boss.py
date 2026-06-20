# ==========================================
# VÍRUS HUNTER
# boss.py
#
# Boss Final
# TROJAN_BOSS.EXE
#
# O Boss só escolhe sua arma
# quando o jogador confirmar a jogada.
# ==========================================

import random

from classes.constantes import *


class Boss:

    def __init__(self):

        # ==================================
        # VIDA
        # ==================================

        self.vida = VIDA_BOSS

        # ==================================
        # ARMA ATUAL
        # ==================================

        self.arma_atual = None

    # ======================================
    # ESCOLHER ARMA
    # ======================================

    def escolher_arma(self):

        self.arma_atual = random.choice(

            [

                ARMA_PEDRA,

                ARMA_TESOURA,

                ARMA_PAPEL

            ]

        )

        return self.arma_atual

    # ======================================
    # RECEBER DANO
    # ======================================

    def receber_dano(self):

        self.vida -= 1

        if self.vida < 0:

            self.vida = 0

    # ======================================
    # STATUS
    # ======================================

    def esta_vivo(self):

        return self.vida > 0

    def get_arma(self):

        return self.arma_atual