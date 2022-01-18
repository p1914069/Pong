import random
import pygame
from pygame import Vector2
import core


class JoueurUn:
    """ Classe pour le joueur 1 (de gauche) du jeu PONG. """

    def __init__(self):
        self.couleur = (255, 0, 0)
        self.position = Vector2(50, random.randint(50, 680))
        self.largeur = 15
        self.longueur = 40
        self.taille = (self.largeur, self.longueur)
        self.vitesse = 4

    def draw(self, screen):
        """ Méthode qui dessine le joueur 1. """
        pygame.draw.rect(screen, self.couleur, (self.position, self.taille), 10)

    def deplacer(self, h):
        """ Méthode qui permet au joueur 1 de se déplacer. """

        if core.getKeyPressList("q"):
            if self.position.y + self.longueur < 720:
                self.position.y = self.position.y + self.vitesse

        if core.getKeyPressList("a"):
            if self.position.y > 0:
                self.position.y = self.position.y - self.vitesse
