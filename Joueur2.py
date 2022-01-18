import random
import pygame
from pygame import Vector2
import core


class JoueurDeux:
    """ Classe pour le joueur 2 (de gauche) du jeu PONG. """

    def __init__(self):
        self.couleur = (0, 255, 0)
        self.position = Vector2(1030, random.randint(50, 680))
        self.largeur = 15
        self.longueur = 40
        self.taille = (self.largeur, self.longueur)
        self.vitesse = 4

    def draw(self, screen):
        """ Méthode qui dessine le joueur 2. """
        pygame.draw.rect(screen, self.couleur, (self.position, self.taille), 10)

    def deplacer(self, h, l):
        """ Méthode qui permet au joueur 2 de se déplacer. """

        if core.getKeyPressList("m"):
            if self.position.y + self.longueur < 720:
                self.position.y = self.position.y + self.vitesse

        if core.getKeyPressList("p"):
            if self.position.y > 0:
                self.position.y = self.position.y - self.vitesse
