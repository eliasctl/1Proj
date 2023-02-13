# Import des modules et fichiers nécessaires
import pygame

# Test afin de voir si les fichiers sont bien reliers


def test():
    print("test")
# Fin de la fonction test

# fonction d'initialisation du nomre de joueur entre 2 et 4


# Début de la fonction d'initialisation du nombre de joueur qui retourne un entier corespondant au nombre de joueur compris entre 2 et 4
def initialisation_du_nombre_de_joueurs():
    nbJoueur = 0
    while nbJoueur <= 2 and nbJoueur >= 4:
        nbJoueur = int(
            input("Veuillez entrer le nombre de joueur (entre 2 et 4): "))
    return nbJoueur
# Fin de la fonction d'initialisation du nombre de joueur qui retourne le nombre de joueur
