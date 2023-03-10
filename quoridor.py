import pygame
from func import *


# classe joueur
class Joueur:
    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur

    def affichage_joueur(self, fenetre, couleur, x, y, rayon):
        pygame.draw.circle(fenetre, couleur, (x, y), rayon, 0)


# Programme principal
# initialisation graphiques
fenetre_jeu = cree_page_principale()

# if nb_joueur == 0:
nb_joueur = afficher_menu_nb_joueur(fenetre_jeu)
print(nb_joueur)

# if taille_plateau == 0:
taille_plateau = afficher_menu_taille_plateau(fenetre_jeu)
print(taille_plateau)

# fonction de creation de nb de joueurs qui renvoie une liste contenant les coueurs
player1 = Joueur((taille_plateau+1)/2, 1, rouge)
if nb_joueur == 2:
    player2 = Joueur((taille_plateau+1)/2, taille_plateau, bleu)
    player3 = 0
    player4 = 0
else:
    player2 = Joueur(taille_plateau, (taille_plateau+1)/2, bleu)
    player3 = Joueur((taille_plateau+1)/2, taille_plateau, violet)
    player4 = Joueur(1, (taille_plateau+1)/2, vert)


# initialisation du plateau et des données
affichage_plateau(fenetre_jeu, nb_joueur, taille_plateau,
                  player1, player2, player3, player4)
