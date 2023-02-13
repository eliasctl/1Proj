# Import des modules et fichiers nécessaires
import pygame

# Test afin de voir si les fichiers sont bien reliers


def test():
    print("test")
# Fin de la fonction test


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
