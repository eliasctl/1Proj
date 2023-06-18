# Description : Jeu Quoridor
# Auteurs : William Bergue, Paul Mareschi, Elias Moussa-Osman, Clovis Kouoi
# Date : 18/06/2023

# Importation des libraries
import pygame
import sys
import random
from func import *
from pygame import mixer


# Mise en place la musique
mixer.init()
mixer.music.load('Bloons TD battles music Monkeys and Bloons!.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# Initialisation de la classe joueur


class Joueur:
    def __init__(self, x, y, couleur, nb_murs):
        self.x = x
        self.y = y
        self.couleur = couleur
        self.nb_mur = nb_murs

    # Affichage du joueur
    def affichage_joueur(self, fenetre, couleur, indx, indy):
        pygame.draw.circle(fenetre, couleur, (Quadrillage_dx+Qpas_x*(indx-0.5)-Quad_mur/2,
                                              Quadrillage_dy+Qpas_y*(indy-0.5)-Quad_mur/2), Qpas_x/3, 0)

    # Déplacement du joueur
    def deplacer(self, fenetre, nb_joueur, taille_plateau , bot = False):
        deplace_possible = []

        # Vérification des murs
        if self.x > 1:  # Si le joueur n'est pas sur la premiere colonne déplacement vers la gauche
            presence_mur = False
            if self.y > 1:
                if tableauMurV[int(self.x-2)][int(self.y-2)] != 0:
                    presence_mur = True
            if self.y < taille_plateau:
                if tableauMurV[int(self.x-2)][int(self.y-1)] != 0:
                    presence_mur = True

            # Vérification des joueurs
            if not presence_mur:
                presence_joueur = False

                for i in range(nb_joueur):

                    if self.x-1 == joueurs[i].x and self.y == joueurs[i].y:
                        presence_joueur = True

                if not presence_joueur:

                    if tableauMurV[int(self.x-2)][int(self.y-1)] == 0:
                        self.affichage_joueur(fenetre, blanc, self.x-1, self.y)
                        deplace_possible.append((self.x-1, self.y))

                elif self.x > 2:
                    presence_mur_case2 = False

                    if tableauMurV[int(self.x-2)][int(self.y)] != 0 or tableauMurV[int(self.x-2)][int(self.y-1)] != 0:
                        presence_mur_case2 = True

                    if not presence_mur_case2:
                        presence_joueur_case2 = False

                        for j in range(nb_joueur):

                            if self.x-2 == joueurs[j].x and self.y == joueurs[j].y:
                                presence_joueur_case2 = True

                        if presence_joueur_case2 == False:
                            self.affichage_joueur(
                                fenetre, blanc, self.x-2, self.y)
                            deplace_possible.append((self.x-2, self.y))

        # Vérification des murs
        if self.x < taille_plateau:  # Si le joueur n'est pas sur la derniere colonne déplacement vers la droite
            presence_mur = False
            if self.y > 1:

                if tableauMurV[int(self.x-1)][int(self.y-2)] != 0:
                    presence_mur = True

            if self.y < taille_plateau:

                if tableauMurV[int(self.x-1)][int(self.y-1)] != 0:
                    presence_mur = True
            # Vérification des joueurs
            if not presence_mur:
                presence_joueur = False

                for i in range(nb_joueur):

                    if self.x+1 == joueurs[i].x and self.y == joueurs[i].y:
                        presence_joueur = True

                if not presence_joueur:

                    if tableauMurV[int(self.x-1)][int(self.y-1)] == 0:
                        self.affichage_joueur(fenetre, blanc, self.x+1, self.y)
                        deplace_possible.append((self.x+1, self.y))

                elif self.x+2 < taille_plateau:
                    presence_mur_case2 = False

                    if tableauMurV[int(self.x+1)][int(self.y)] != 0 or tableauMurV[int(self.x+1)][int(self.y-1)] != 0:
                        presence_mur_case2 = True

                    if not presence_mur_case2:
                        presence_joueur_case2 = False

                        for i in range(nb_joueur):

                            if self.x+2 == joueurs[i].x and self.y == joueurs[i].y:
                                presence_joueur_case2 = True

                        if presence_joueur_case2 == False:
                            self.affichage_joueur(
                                fenetre, blanc, self.x+2, self.y)
                            deplace_possible.append((self.x+2, self.y))

        # Vérification des murs
        if self.y > 1:  # Si le joueur n'est pas sur la derniere colonne déplacement vers le haut
            presence_mur = False

            if self.x > 1:

                if tableauMurH[int(self.x-2)][int(self.y-2)] != 0:
                    presence_mur = True

            if self.x < taille_plateau:

                if tableauMurH[int(self.x-1)][int(self.y-2)] != 0:
                    presence_mur = True
            # Vérification des joueurs
            if not presence_mur:
                presence_joueur = False

                for i in range(nb_joueur):

                    if self.x == joueurs[i].x and self.y-1 == joueurs[i].y:
                        presence_joueur = True

                if not presence_joueur:
                    self.affichage_joueur(fenetre, blanc, self.x, self.y-1)
                    deplace_possible.append((self.x, self.y-1))

                elif self.y-2 > 0:
                    presence_mur_case2 = False

                    if tableauMurV[int(self.x)][int(self.y-2)] != 0 or tableauMurV[int(self.x-1)][int(self.y-2)] != 0:
                        presence_mur_case2 = True

                    if not presence_mur_case2:
                        presence_joueur_case2 = False

                        for i in range(nb_joueur):

                            if self.x == joueurs[i].x and self.y-2 == joueurs[i].y:
                                presence_joueur_case2 = True

                        if presence_joueur_case2 == False:
                            self.affichage_joueur(
                                fenetre, blanc, self.x, self.y-2)
                            deplace_possible.append((self.x, self.y-2))

        # Vérification des murs
        if self.y < taille_plateau:  # Si le joueur n'est pas sur la derniere colonne déplacement vers le bas
            presence_mur = False

            if self.x > 1:

                if tableauMurH[int(self.x-2)][int(self.y-1)] != 0:
                    presence_mur = True

            if self.x < taille_plateau:

                if tableauMurH[int(self.x-1)][int(self.y-1)] != 0:
                    presence_mur = True

            # Vérification des joueurs
            if not presence_mur:
                presence_joueur = False

                for i in range(nb_joueur):

                    if self.x == joueurs[i].x and self.y+1 == joueurs[i].y:
                        presence_joueur = True

                if not presence_joueur:

                    if tableauMurH[int(self.x-1)][int(self.y-1)] == 0:
                        self.affichage_joueur(fenetre, blanc, self.x, self.y+1)
                        deplace_possible.append((self.x, self.y+1))

                elif self.y+2 < taille_plateau:
                    presence_mur_case2 = False

                    if tableauMurV[int(self.x)][int(self.y+1)] != 0 or tableauMurV[int(self.x-1)][int(self.y+1)] != 0:
                        presence_mur_case2 = True

                    if not presence_mur_case2:
                        presence_joueur_case2 = False

                        for i in range(nb_joueur):

                            if self.x == joueurs[i].x and self.y+2 == joueurs[i].y:
                                presence_joueur_case2 = True

                        if presence_joueur_case2 == False:
                            self.affichage_joueur(
                                fenetre, blanc, self.x, self.y+2)
                            deplace_possible.append((self.x, self.y+2))
        pygame.display.flip()

        if not bot :
            # Attente du clic du joueur
            while True:
                ev = pygame.event.poll()

                # Evennement de clic
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    # Son du clic
                    click = pygame.mixer.Sound("Click.mp3")
                    click.set_volume(0.5)
                    click.play()

                    if pos[0] > Quadrillage_dx and pos[0] < Quadrillage_dx+Quadrillage_lX and pos[1] > Quadrillage_dy and pos[1] < Quadrillage_dy+Quadrillage_ly:
                        # Récupération de la case cliquée
                        indx = int((pos[0]-Quadrillage_dx)/Qpas_x)+1
                        indy = int((pos[1]-Quadrillage_dy)/Qpas_y)+1

                        # Vérification que la case cliquée est dans le tableau
                        if (indx, indy) in deplace_possible:
                            # Déplacement du joueur
                            self.x = indx
                            self.y = indy
                            break
        else :

            # Pause de 1 s pour laisser le temps au joueur de voir le déplacement du bot
            pygame.time.wait(1000)

            # Déplacement du bot de maniere aléatoire
            self.x, self.y = deplace_possible[random.randint(0, len(deplace_possible)-1)]

    # Fonction pour poser un mur vertical
    def poser_murV(self, fenetre, tableauMurV, taille_plateau):
        # Initialisation d'un tableau avec les coordonnées des murs possibles
        mur_possible = [[False for i in range(
            taille_plateau-1)] for j in range(taille_plateau-1)]
        # son pour bouton mur
        click = pygame.mixer.Sound("Click.mp3")
        click.set_volume(0.5)
        click.play()

        # Affichage des milieux de murs possibles
        for i in range(taille_plateau-1):

            for j in range(taille_plateau-1):

                if tableauMurV[i][j] == 0 and tableauMurH[i][j] == 0:

                    if j > 0:  # Si le murs n'est pas sur la premiere ligne

                        if j < taille_plateau-2:  # Si le mur n'est pas sur la derniere ligne

                            # Si il n'y a pas de mur au dessus et en dessous
                            if tableauMurV[i][j-1] == 0 and tableauMurV[i][j+1] == 0:
                                pygame.draw.circle(fenetre, blanc, (Quadrillage_dx+Qpas_x*(
                                    i+1)-Quad_mur/2, Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2), 6, 0)
                                mur_possible[i][j] = True

                        else:  # Si on est sur la derniere ligne

                            if tableauMurV[i][j-1] == 0:
                                pygame.draw.circle(fenetre, blanc, (Quadrillage_dx+Qpas_x*(
                                    i+1)-Quad_mur/2, Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2), 6, 0)
                                mur_possible[i][j] = True

                    else:  # Si on est sur la premiere ligne

                        if tableauMurV[i][j+1] == 0:
                            pygame.draw.circle(fenetre, blanc, (Quadrillage_dx+Qpas_x*(
                                i+1)-Quad_mur/2, Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2), 6, 0)
                            mur_possible[i][j] = True

        pygame.display.flip()

        mur_choisi = False  # Attente que le joueur clique sur un neoud de mur

        while mur_choisi == False:
            ev = pygame.event.poll()

            # Evennement de clic
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                if pos[0] > Quadrillage_dx and pos[0] < Quadrillage_dx+Quadrillage_lX and pos[1] > Quadrillage_dy and pos[1] < Quadrillage_dy+Quadrillage_ly:

                    # Récupération de la case cliquée
                    for i in range(taille_plateau-1):

                        for j in range(taille_plateau-1):

                            if tableauMurV[i][j] == 0 and tableauMurH[i][j] == 0 and mur_possible[i][j] == True:
                                distance = (Quadrillage_dx+Qpas_x*(i+1)-Quad_mur/2-pos[0])**2+(
                                    Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2-pos[1])**2

                                if distance < 36:
                                    tableauMurV[i][j] = self.couleur
                                    mur_choisi = True
                                    break

    # Fonction pour poser un mur horizontal
    def poser_murH(self, fenetre, tableauMurH, taille_plateau):
        # Initialisation d'un tableau avec les coordonnées des murs possibles
        mur_possible = [[False for i in range(taille_plateau-1)] for j in range(taille_plateau-1)]
        # Son du bouton mur horizontal
        click = pygame.mixer.Sound("Click.mp3")
        click.set_volume(0.5)
        click.play()

        # Affichage des milieux de murs possibles
        for i in range(taille_plateau-1):

            for j in range(taille_plateau-1):

                if tableauMurH[i][j] == 0 and tableauMurV[i][j] == 0:

                    if i > 0:  # Si le murs n'est pas sur la premiere colonne

                        if i < taille_plateau-2:  # Si le mur n'est pas sur la derniere colonne

                            # Si il n'y a pas de mur à gauche et à droite
                            if tableauMurH[i-1][j] == 0 and tableauMurH[i+1][j] == 0:
                                pygame.draw.circle(fenetre, blanc, (Quadrillage_dx+Qpas_x*(
                                    i+1)-Quad_mur/2, Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2), 6, 0)
                                mur_possible[i][j] = True

                        else:  # Si on est sur la derniere colonne

                            if tableauMurH[i-1][j] == 0:
                                pygame.draw.circle(fenetre, blanc, (Quadrillage_dx+Qpas_x*(
                                    i+1)-Quad_mur/2, Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2), 6, 0)
                                mur_possible[i][j] = True
                    
                    else:  # Si on est sur la premiere colonne
                        if tableauMurH[i+1][j] == 0:
                            pygame.draw.circle(fenetre, blanc, (Quadrillage_dx+Qpas_x*(
                                i+1)-Quad_mur/2, Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2), 6, 0)
                            mur_possible[i][j] = True

        pygame.display.flip()

        mur_choisi = False  # Attente que le joueur clique sur un neoud de mur

        while mur_choisi == False:
            ev = pygame.event.poll()

            # Evennement de clic
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                if pos[0] > Quadrillage_dx and pos[0] < Quadrillage_dx+Quadrillage_lX and pos[1] > Quadrillage_dy and pos[1] < Quadrillage_dy+Quadrillage_ly:

                    # Récupération de la case cliquée
                    for i in range(taille_plateau-1):

                        for j in range(taille_plateau-1):

                            if tableauMurH[i][j] == 0 and tableauMurV[i][j] == 0 and mur_possible[i][j] == True:
                                distance = (Quadrillage_dx+Qpas_x*(i+1)-Quad_mur/2-pos[0])**2+(
                                    Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2-pos[1])**2

                                if distance < 36:
                                    # print("poser murH")
                                    tableauMurH[i][j] = self.couleur
                                    mur_choisi = True
                                    break


# Programme principal

# Initialisation graphiques
fenetre_jeu = cree_page_principale()

# Récupération des paramètres de la partie
choix_jeu = afficher_menu_jeu(fenetre_jeu)
# Nombre de joueurs
nb_joueur = choix_jeu[0]

# Taille du plateau
taille_plateau = choix_jeu[1]

# Initialisation des tableaux de mur
tableauMurH = initMurTabMur(taille_plateau)
tableauMurV = initMurTabMur(taille_plateau)

# Initialisation du pas graphique
Qpas_x = Quadrillage_lX / taille_plateau
Qpas_y = Quadrillage_ly / taille_plateau

# Initalisation des joueurs
joueurs = []

# Récupération du nombre de joueur
if nb_joueur == 2:
    joueurs.append(Joueur((taille_plateau+1)/2, 1, rouge, 10))
    joueurs.append(Joueur((taille_plateau+1)/2, taille_plateau, bleu, 10))
    joueurs.append(Joueur(0, 0, 0, 0))
    joueurs.append(Joueur(0, 0, 0, 0))
else:
    joueurs.append(Joueur((taille_plateau+1)/2, 1, rouge, 5))
    joueurs.append(Joueur(taille_plateau, (taille_plateau+1)/2, bleu, 5))
    joueurs.append(Joueur((taille_plateau+1)/2, taille_plateau, violet, 5))
    joueurs.append(Joueur(1, (taille_plateau+1)/2, vert, 5))

# Jeu classique sans bot
if choix_jeu[2] == 1:

    # Boucle de jeu
    partie_finie = False  # Variable pour savoir si la partie est finie
    nb_coups = 0  # Variable pour compter le nombre de coups

    while not partie_finie:
        nb_coups += 1
        for i in range(nb_joueur):
            # Initialisation du plateau et des données
            affichage_plateau(fenetre_jeu, nb_joueur, taille_plateau,
                            joueurs, i, tableauMurH, tableauMurV)
            pygame.display.flip()

            while True:
                # Test de sortie
                ev = pygame.event.poll()
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                    pygame.quit()

                if ev.type == pygame.QUIT:
                    pygame.quit()

                # Evennement de clic sur un bouton
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()

                    # Clic sur le bouton de déplacement (400, 510, 150, 150)
                    if pos[0] > 400 and pos[0] < 550 and pos[1] > 510 and pos[1] < 660:
                        joueurs[i].deplacer(fenetre_jeu, nb_joueur, taille_plateau)
                        pygame.display.flip()
                        break

                    # Clic sur le bouton de pose de mur vertical (615, 150, 50, 165)
                    if pos[0] > 615 and pos[0] < 780 and pos[1] > 150 and pos[1] < 200:
                        joueurs[i].poser_murV(
                            fenetre_jeu, tableauMurV, taille_plateau)
                        pygame.display.flip()
                        break

                    # Clic sur le bouton de pose de mur horizontal (615, 300, 50, 165)
                    if pos[0] > 615 and pos[0] < 780 and pos[1] > 300 and pos[1] < 350:
                        joueurs[i].poser_murH(
                            fenetre_jeu, tableauMurH, taille_plateau)
                        pygame.display.flip()
                        break
            
            # Test de victoire
            if victoire(joueurs[i].x, joueurs[i].y, taille_plateau, joueurs[i].couleur) == True:

                # Recupération du chemin vers python
                python = sys.executable

                # ajout du son de victoire
                pygame.mixer.music.load("Victory.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play()

                # Affichage de la victoire avec possibilité de relancer la partie
                afficher_victoire(fenetre_jeu, joueurs[i].couleur, nb_coups, python, sys.argv)

                # Sortie de la boucle de jeu
                partie_finie = True
                break

        # Pause de 1 s pour éviter de surcharger le processeur
        pygame.time.wait(1)

# Jeu avec bot
else:

    # Boucle de jeu
    partie_finie = False
    nb_coups = 0

    while not partie_finie:
        nb_coups += 1
        for i in range(nb_joueur):
            if i == 0:
                # Initialisation du plateau et des données
                affichage_plateau(fenetre_jeu, nb_joueur, taille_plateau,
                                joueurs, i, tableauMurH, tableauMurV)
                pygame.display.flip()

                while True:
                    # Test de sortie
                    ev = pygame.event.poll()
                    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                        pygame.quit()

                    if ev.type == pygame.QUIT:
                        pygame.quit()

                    # Evennement de clic sur un bouton
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()

                        # Clic sur le bouton de déplacement (400, 510, 150, 150)
                        if pos[0] > 400 and pos[0] < 550 and pos[1] > 510 and pos[1] < 660:
                            joueurs[i].deplacer(fenetre_jeu, nb_joueur, taille_plateau)
                            pygame.display.flip()
                            break

                        # Clic sur le bouton de pose de mur vertical (615, 150, 50, 165)
                        if pos[0] > 615 and pos[0] < 780 and pos[1] > 150 and pos[1] < 200:
                            joueurs[i].poser_murV(
                                fenetre_jeu, tableauMurV, taille_plateau)
                            pygame.display.flip()
                            break

                        # Clic sur le bouton de pose de mur horizontal (615, 300, 50, 165)
                        if pos[0] > 615 and pos[0] < 780 and pos[1] > 300 and pos[1] < 350:
                            joueurs[i].poser_murH(
                                fenetre_jeu, tableauMurH, taille_plateau)
                            pygame.display.flip()
                            break

                # Test de victoire
                if victoire(joueurs[i].x, joueurs[i].y, taille_plateau, joueurs[i].couleur) == True:

                    # Recupération du chemin vers python
                    python = sys.executable

                    # Affichage de la victoire avec possibilité de relancer la partie
                    afficher_victoire(fenetre_jeu, joueurs[i].couleur, nb_coups, python, sys.argv)

                    # Sortie de la boucle de jeu
                    partie_finie = True
                    break

            # Pause de 1 s pour éviter de surcharger le processeur
            pygame.time.wait(1)
    
        # Tour du bot
        if partie_finie == False:
            # Initialisation du plateau et des données
            affichage_plateau(fenetre_jeu, nb_joueur, taille_plateau,
                            joueurs, i, tableauMurH, tableauMurV, True)
            pygame.display.flip()

            # Déplacement du bot
            joueurs[i].deplacer(fenetre_jeu, nb_joueur, taille_plateau, True)
            pygame.display.flip()

            # Test de victoire
            if victoire(joueurs[i].x, joueurs[i].y, taille_plateau, joueurs[i].couleur) == True:

                # Recupération du chemin vers python
                python = sys.executable

                # ajout du son de victoire
                pygame.mixer.music.load("Victory.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play()

                # Affichage de la victoire avec possibilité de relancer la partie
                afficher_victoire(fenetre_jeu, joueurs[i].couleur, nb_coups, python, sys.argv, bot = True)

                # Sortie de la boucle de jeu
                partie_finie = True
                break

            # Pause de 1 s pour éviter de surcharger le processeur
            pygame.time.wait(1000)