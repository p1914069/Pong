import pygame
import core

from Joueur1 import JoueurUn
from Joueur2 import JoueurDeux
from balle import Balle


def setup():
    core.fps = 60
    core.WINDOW_SIZE = [1080, 720]

    # Joueurs
    core.memory("Joueur1", JoueurUn())
    core.memory("Joueur2", JoueurDeux())

    # Balle
    core.memory("Balle", Balle())

    # Scores
    core.memory("Score_J1", 0)
    core.memory("Score_J2", 0)


def run():
    core.cleanScreen()

    # Écriture des scores
    core.Draw.text((255, 255, 255), f'Joueur 1: {core.memory("Score_J1")}', (210, 0))
    core.Draw.text((255, 255, 255), f'Joueur 2: {core.memory("Score_J2")}', (730, 0))

    # Bloc déplacements
    # Balle
    core.memory("Balle").deplacer(720, 1080, core.memory("Joueur1"), core.memory("Joueur2"))

    core.memory("Joueur1").deplacer(720)
    core.memory("Joueur2").deplacer(720, 1080)

    # Bloc dessins
    pygame.draw.rect(core.screen, (255, 255, 255), ((540, 0), (1, 720)), 10)

    core.memory("Joueur1").draw(core.screen)
    core.memory("Joueur2").draw(core.screen)

    core.memory("Balle").draw(core.screen)

    print(core.memory("Balle").position)
    print(core.memory("Joueur1").position)
    print(core.memory("Joueur2").position)
    print("\n")


core.main(setup, run)
