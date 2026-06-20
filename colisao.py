# ==========================================
# VÍRUS HUNTER
# colisao.py
#
# Centraliza todas as colisões do jogo
#
# Utilizado por:
# - Fase 1
# - Fase 2
# - Fase 3
# ==========================================

import pygame


class Colisao:

    # ======================================
    # JOGADOR x PLATAFORMAS
    # ======================================
    @staticmethod
    def jogador_plataformas(
        jogador,
        plataformas
    ):

        jogador.no_chao = False

        for plataforma in plataformas:

            if jogador.rect.colliderect(
                plataforma.rect
            ):

                # CAINDO SOBRE A PLATAFORMA
                if (
                    jogador.vel_y > 0
                    and
                    jogador.rect.bottom - jogador.vel_y
                    <= plataforma.rect.top
                ):

                    jogador.rect.bottom = (
                        plataforma.rect.top
                    )

                    jogador.vel_y = 0

                    jogador.no_chao = True

                # BATENDO A CABEÇA
                elif (
                    jogador.vel_y < 0
                    and
                    jogador.rect.top - jogador.vel_y
                    >= plataforma.rect.bottom
                ):

                    jogador.rect.top = (
                        plataforma.rect.bottom
                    )

                    jogador.vel_y = 0

    # ======================================
    # JOGADOR x VÍRUS
    # ======================================
    @staticmethod
    def jogador_virus(
        jogador,
        virus_lista
    ):

        for virus in virus_lista:

            if not virus.esta_vivo():
                continue

            if jogador.rect.colliderect(
                virus.rect
            ):

                # Está caindo?
                if (
                    jogador.vel_y > 0
                    and
                    jogador.rect.bottom
                    <
                    virus.rect.centery
                ):

                    virus.morrer()

                    jogador.quicar()

                    return "virus_morto"

                else:

                    jogador.receber_dano()

                    return "dano"

        return None

    # ======================================
    # PROJETIL JOGADOR x VÍRUS
    #
    # Fase 2:
    # Pedra
    # Tesoura
    # Papel
    # ======================================
    @staticmethod
    def projetil_jogador_virus(
        projeteis,
        virus_lista
    ):

        mortos = 0

        for projetil in projeteis:

            for virus in virus_lista:

                if not virus.esta_vivo():
                    continue

                if projetil.rect.colliderect(
                    virus.rect
                ):

                    virus.morrer()

                    projetil.destruir()

                    mortos += 1

                    break

        return mortos

    # ======================================
    # PROJETIL JOGADOR x VÍRUS
    # APENAS TESOURA
    #
    # Sala Downloads
    # ======================================
    @staticmethod
    def projetil_tesoura_virus(
        projeteis,
        virus_lista
    ):

        mortos = 0

        for projetil in projeteis:

            if not projetil.eh_tesoura():
                continue

            for virus in virus_lista:

                if not virus.esta_vivo():
                    continue

                if projetil.rect.colliderect(
                    virus.rect
                ):

                    virus.morrer()

                    projetil.destruir()

                    mortos += 1

                    break

        return mortos

    # ======================================
    # PROJETIL VÍRUS x JOGADOR
    # ======================================
    @staticmethod
    def projetil_virus_jogador(
        jogador,
        virus_lista
    ):

        for virus in virus_lista:

            for projetil in virus.projeteis:

                if projetil.rect.colliderect(
                    jogador.rect
                ):

                    jogador.receber_dano()

                    projetil.destruir()

                    return True

        return False

    # ======================================
    # JOGADOR x ARQUIVO
    # ======================================
    @staticmethod
    def jogador_arquivo(
        jogador,
        arquivo
    ):

        if arquivo.foi_recuperado():
            return False

        return jogador.rect.colliderect(
            arquivo.rect
        )

    # ======================================
    # JOGADOR x DRIVER
    # ======================================
    @staticmethod
    def jogador_driver(
        jogador,
        driver
    ):

        if driver.foi_salvo():
            return False

        return jogador.rect.colliderect(
            driver.rect
        )

    # ======================================
    # JOGADOR x WORD
    # ======================================
    @staticmethod
    def jogador_word(
        jogador,
        word
    ):

        if word.foi_salvo():
            return False

        return jogador.rect.colliderect(
            word.rect
        )

    # ======================================
    # JOGADOR x PORTA
    # ======================================
    @staticmethod
    def jogador_porta(
        jogador,
        porta
    ):

        return jogador.rect.colliderect(
            porta.rect
        )

    # ======================================
    # DISTÂNCIA ENTRE OBJETOS
    #
    # Utilizado para:
    #
    # Pressione D
    # Abrir porta
    # Salvar driver
    # Recuperar word
    # Recuperar arquivo
    # ======================================
    @staticmethod
    def proximo(
        jogador,
        objeto,
        distancia=100
    ):

        centro_jogador = (
            jogador.rect.centerx,
            jogador.rect.centery
        )

        centro_objeto = (
            objeto.rect.centerx,
            objeto.rect.centery
        )

        dx = abs(
            centro_jogador[0]
            -
            centro_objeto[0]
        )

        dy = abs(
            centro_jogador[1]
            -
            centro_objeto[1]
        )

        return (

            dx <= distancia

            and

            dy <= distancia

        )

    # ======================================
    # BOSS x JOGADOR
    # ======================================
    @staticmethod
    def boss_jogador(
        jogador,
        boss
    ):

        if boss.rect.colliderect(
            jogador.rect
        ):

            jogador.receber_dano()

            return True

        return False

    # ======================================
    # PROJETIL x BOSS
    # ======================================
    @staticmethod
    def projetil_boss(
        projeteis,
        boss
    ):

        dano = 0

        for projetil in projeteis:

            if projetil.rect.colliderect(
                boss.rect
            ):

                projetil.destruir()

                dano += 1

        return dano

    # ======================================
    # JOGADOR DENTRO DA TELA
    # ======================================
    @staticmethod
    def limitar_jogador(
        jogador,
        largura_tela
    ):

        if jogador.rect.left < 0:

            jogador.rect.left = 0

        if jogador.rect.right > largura_tela:

            jogador.rect.right = largura_tela

    # ======================================
    # JOGADOR CAIU NO VAZIO
    # ======================================
    @staticmethod
    def caiu_da_tela(
        jogador,
        altura_tela
    ):

        return jogador.rect.top > altura_tela