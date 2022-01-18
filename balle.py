import random
import pygame
from pygame import Vector2
import core

class Balle:
    """ Classe pour la balle du jeu Pong. """

    def __init__(self):
        self.position = (Vector2(540, 360))
        self.couleur = (255, 255, 255)
        self.rayon = 5
        self.rayon_max = 150

        self.vitesse = 1
        self.vitessemax = 5
        self.direction = Vector2(random.choice([-3, 3]), random.choice([-2, 2]))

        self.spawn = Vector2(540, 360)

    def draw(self, ecran):
        """ Méthode qui dessine la balle. """
        pygame.draw.circle(ecran, self.couleur, self.position, self.rayon)

    def deplacer(self, h, l, joueur1, joueur2):
        """ Méthode qui permet à la balle de se déplacer. """

        self.position += self.direction

        # Collisions joueurs
        if self.position.x == 50 and joueur1.position.y < self.position.y < joueur1.position.y + joueur1.longueur:
            self.direction = Vector2(self.direction.x * -1, self.direction.y * -1)

        if self.position.x == 1030 and joueur2.position.y < self.position.y < joueur2.position.y + joueur2.longueur:
            self.direction = Vector2(self.direction.x * -1, self.direction.y * -1)

        # Bords fenêtre
        if self.position.y < 0 or self.position.y > h:
            self.position = self.spawn

        if self.position.x < 0 or self.position.x > l:
            self.position = self.spawn


