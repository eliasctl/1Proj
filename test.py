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
        # on recupere les touches enfoncées
        touches = pygame.key.get_pressed()

    def pose_une_barrière(self, x, y):
        bariere_x = x
        bariere_y = y


# pour le jeux
pygame.init()  # Initialisation de Pygame
window_size = (400, 300)  # Définition de la taille de la fenêtre
screen = pygame.display.set_mode(window_size)  # Création de la fenêtre
joueur = Joueur(0, 0, (255, 0, 0))  # on crée un joueur

# Boucle principale du jeu
running = True
while running:
    # Traitement des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()  # Mise à jour de l'écran
pygame.quit()  # Nettoyage

# TODO : Une grille sur le plateau de jeux
# TODO : Le deplacement des joueurs
# TODO : Le fait de poser des barrières
# TODO : La fonction de victoire
# TODO : L'affichage des joueurs sur le plateau
