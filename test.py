# import des modules
import pygame
import time
from fonctions import *


# un joueur (se deplacer, poser des barrières)
class Joueur:
    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur


# variables du jeux
t_fenetre = (700, 700)
pygame.display.set_caption("Quoridor")
nb_cases = 11
nb_barrieres = nb_cases - 1
t_cases = ((t_fenetre[0] // nb_cases) - nb_barrieres)
l_barrière = (t_fenetre[0] - (nb_cases * t_cases)) // nb_barrieres
hauteur_barriere = t_fenetre[0]


# pour le jeux
pygame.init()  # Initialisation de Pygame
screen = pygame.display.set_mode(t_fenetre)  # Création de la fenêtre
joueur = Joueur(0, 0, (255, 0, 0))  # on crée un joueur


# Boucle principale du jeu
while True:
    ev = pygame.event.poll()
    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
        break
    if ev.type == pygame.QUIT:
        break

    x = 0
    y = 0

    # affichage de la grille
    for w in range(nb_cases):
        # si on est a la premiere ou derniere ligne
        if (w == 0 or w == nb_cases - 1):
            colorCase = (0, 0, 205)
        else:
            colorCase = (65, 105, 225)

        # boucle qui dessine une case et une barrière
        for i in range(nb_cases - 1):
            # on affiche un carré
            pygame.draw.rect(screen, colorCase, pygame.Rect(
                x, y, t_cases, t_cases))
            x += t_cases  # on decale la position x
            # on affiche une barrière
            pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(
                x, y, l_barrière, t_cases))
            x += l_barrière  # on decale la position x

        # on affiche le dernier carré
        pygame.draw.rect(screen, colorCase, pygame.Rect(
            x, y, t_cases, t_cases))
        # on update x, y
        x = 0
        y += t_cases

        # si on est pas a la derniere ligne
        if w != nb_cases - 1:
            # on affiche une barrière de la taille de la fenêtre
            pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(
                x, y, t_fenetre[0], l_barrière))
            # update de la position y
            y += l_barrière

    pygame.display.flip()
    time.sleep(0.1)
