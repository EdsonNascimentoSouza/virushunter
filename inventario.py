# ==========================================
# VÍRUS HUNTER
# inventario.py
# ==========================================

from classes.constantes import *


class Inventario:

    def __init__(self):

        self.reiniciar()

    # ======================================
    # RESET COMPLETO
    # ======================================

    def reiniciar(self):

        # VIDA
        self.vida = VIDA_MAXIMA

        # ARMAS
        self.pedra = False
        self.tesoura = False
        self.papel = False

        # ITENS
        self.driver = False
        self.word = False

        # ARMA EQUIPADA
        self.arma_atual = None

    # ======================================
    # VIDA
    # ======================================

    def receber_dano(self):

        self.vida -= 1

        if self.vida < 0:
            self.vida = 0

    def recuperar_vida_total(self):

        self.vida = VIDA_MAXIMA

    def esta_vivo(self):

        return self.vida > 0

    # ======================================
    # PEDRA
    # ======================================

    def obter_pedra(self):

        self.pedra = True

        if self.arma_atual is None:
            self.arma_atual = ARMA_PEDRA

    def possui_pedra(self):

        return self.pedra

    # ======================================
    # TESOURA
    # ======================================

    def obter_tesoura(self):

        self.tesoura = True

        if self.arma_atual is None:
            self.arma_atual = ARMA_TESOURA

    def possui_tesoura(self):

        return self.tesoura

    # ======================================
    # PAPEL
    # ======================================

    def obter_papel(self):

        self.papel = True

        if self.arma_atual is None:
            self.arma_atual = ARMA_PAPEL

    def possui_papel(self):

        return self.papel

    # ======================================
    # DRIVER
    # ======================================

    def salvar_driver(self):

        self.driver = True

    def possui_driver(self):

        return self.driver

    # ======================================
    # WORD
    # ======================================

    def salvar_word(self):

        self.word = True

    def possui_word(self):

        return self.word

    # ======================================
    # ARMA EQUIPADA
    # ======================================

    def get_arma(self):

        return self.arma_atual

    # ======================================
    # TROCAR ARMA
    # ======================================

    def trocar_arma(self):

        armas = []

        if self.pedra:
            armas.append(ARMA_PEDRA)

        if self.tesoura:
            armas.append(ARMA_TESOURA)

        if self.papel:
            armas.append(ARMA_PAPEL)

        if len(armas) == 0:
            return

        if self.arma_atual is None:

            self.arma_atual = armas[0]

            return

        indice = armas.index(self.arma_atual)

        indice += 1

        if indice >= len(armas):
            indice = 0

        self.arma_atual = armas[indice]

    # ======================================
    # FASE 1
    # ======================================

    def fase1_completa(self):

        return self.pedra

    # ======================================
    # FASE 2
    # ======================================

    def fase2_completa(self):

        return (

            self.driver
            and
            self.word
            and
            self.pedra
            and
            self.tesoura
            and
            self.papel

        )

    # ======================================
    # STATUS
    # ======================================

    def resumo(self):

        return {

            "vida": self.vida,

            "pedra": self.pedra,

            "tesoura": self.tesoura,

            "papel": self.papel,

            "driver": self.driver,

            "word": self.word,

            "arma_atual": self.arma_atual

        }