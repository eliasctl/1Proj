# TODO : Le menu
# TODO : Le deplacement des joueurs
# TODO : Le fait de poser des barrières
# TODO : La fonction de victoire
# TODO : L'affichage des joueurs sur le plateau


# import des modules
import pygame
from fonctions import *


# un joueur (se deplacer, poser des barrières)
class Joueur:
    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur

    def deplacer(self):
        pass

    def pose_une_barrière(self, x, y):
        bariere_x = x
        bariere_y = y


# variables du jeux
t_fenetre = (800, 800)
pygame.display.set_caption("Quoridor")
nb_cases = 11
nb_barrieres = nb_cases - 1
t_cases = ((t_fenetre[0] // nb_cases) - nb_barrieres)
largeur_barriere = (t_fenetre[0] - (nb_cases * t_cases)) // nb_barrieres
hauteur_barriere = t_fenetre[0]

# définition des couleurs
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)


# pour le jeux
pygame.init()  # Initialisation de Pygame
screen = pygame.display.set_mode(t_fenetre)  # Création de la fenêtre
joueur = Joueur(0, 0, (255, 0, 0))  # on crée un joueur


# Boucle principale du jeu
running = True
while running:
    # Traitement des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x = 0
    y = 0

    # boucle pour l'affichage de la grille
    for i in range(nb_cases):
        for i in range(nb_cases - 1):
            # on affiche un carré
            pygame.draw.rect(screen, gray, pygame.Rect(x, y, t_cases, t_cases))
            # on decale la position x
            x += t_cases
            # on affiche une barrière
            pygame.draw.rect(screen, white, pygame.Rect(
                x, y, largeur_barriere, t_cases))
            # on decale la position x
            x += largeur_barriere
        # on decale la position x
        x = 0
        # on decale la position y
        y += t_cases
        for i in range(nb_cases // 2):
            # on affiche une barrière de la taille de deux cases
            pygame.draw.rect(screen, white, pygame.Rect(
                screen, white, pygame.Rect(x, y, t_cases * 2, largeur_barriere)))

    pygame.display.flip()  # maj de l'écran
pygame.quit()  # Arrêt de Pygame
