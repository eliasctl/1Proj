# Import des modules et fichiers nécessaires
import pygame
#Fin des imports

# Début de la fonction d'initialisation du nombre de joueur qui retourne un entier corespondant au nombre de joueurs compris entre 2 et 4
def initialisation_du_nombre_de_joueurs():
    nbJoueur = 0
    while nbJoueur < 2 or nbJoueur > 4:
        nbJoueur = int(
            input("Veuillez entrer le nombre de joueur (entre 2 et 4): "))
    return nbJoueur
# Fin de la fonction initialisation_du_nombre_de_joueurs

# Début de la fonction d'initialisation du nombre de barrière qui retourne un entier corespondant au nombre de barrières totales
def initialisation_du_nombre_de_barrieres():
    print("⚠️ ATTENTION ⚠️ Dev en cours")
# Fin de la fonction initialisation_du_nombre_de_barrieres

# Début de la fonction de création de la liste des joueurs qui retourne une liste de la forme (nom du joueur, nombre de barrières, position x, position y)
def creation_de_la_liste_des_joueurs(nombre_de_joueurs, nombre_de_barrieres_totales):
    liste_des_joueurs = []
    for i in range(nombre_de_joueurs):
        nom = input("Veuillez entrer le nom du joueur numéro " +
                    str(i + 1) + ": ")
        liste_des_joueurs.append(
            [nom, nombre_de_barrieres_totales/nombre_de_joueurs, 0, 0])
    return liste_des_joueurs
# Fin de la fonction creation_de_la_liste_des_joueurs

# Début de la fonction d'initialisation de la taille du plateau (5x5, 7x7, 9x9, 11x11) qui retourne un entier corespondant à la heuteur et la largeur de la grille
def initialisation_de_la_taille_du_plateau():
    print("⚠️ ATTENTION ⚠️ Dev en cours")
    taille = 0  # 9 de base
    while taille == 5 and taille == 7 and taille == 9 and taille == 11:
        taille = int(
            input("Entrez la taille du plateau il doit être égale à 5, 7, 9 ou 11 : "))
    return taille
# Fin de la fonction initialisation_de_la_taille_du_plateau

# Début de la fonction d'initialisation de la liste du plateau qui retourne une liste de la forme (mur_droit, mur_gauche, mur_haut, mur_bas) si il n'y a pas de mur alor la valeur est 0 et si il y a un mur la valeur est 1 à savoir que les bords auront des mur pour éviter la pose de mur à cette endroit
def creation_du_plateau():
    print("⚠️ ATTENTION ⚠️ Dev en cours")
# Fin de la fonction creation_du_plateau
