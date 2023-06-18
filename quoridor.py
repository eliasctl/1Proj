import pygame
import sys
from func import *
from pygame import mixer

# Possibilité de relancer la partie
    

# mettre en place la musique
mixer.init()
mixer.music.load('Bloons TD battles music Monkeys and Bloons!.mp3')
mixer.music.set_volume(1)
mixer.music.play(-1)

# classe joueur
class Joueur:
    def __init__(self, x, y, couleur, nb_murs):
        self.x = x
        self.y = y
        self.couleur = couleur
        self.nb_mur = nb_murs

    def affichage_joueur(self, fenetre, couleur, indx, indy):
        pygame.draw.circle(fenetre, couleur, (Quadrillage_dx+Qpas_x*(indx-0.5)-Quad_mur/2,
                                              Quadrillage_dy+Qpas_y*(indy-0.5)-Quad_mur/2), Qpas_x/3, 0)

    def deplacer(self, fenetre, nb_joueur, taille_plateau):
        deplace_possible = []

        # on check les murs
        if self.x > 1:  # si le joueur n'est pas sur la premiere colonne mouv vers le gauche
            presence_mur = False
            if self.y > 1:
                # print("valeur X = " + str(self.x) + " Valeur Y=" + str(self.y))
                if tableauMurV[int(self.x-2)][int(self.y-2)] != 0:
                    presence_mur = True
            if self.y < taille_plateau:
                if tableauMurV[int(self.x-2)][int(self.y-1)] != 0:
                    presence_mur = True

            # on check les joueurs
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
                    if tableauMurV[int(self.x-2)][int(self.y)] == 0 and tableauMurV[int(self.x-2)][int(self.y-1)] == 0:
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

        if self.x < taille_plateau:  # si le joueur n'est pas sur la derniere colonne mouv vers le la droite
            presence_mur = False
            if self.y > 1:
                if tableauMurV[int(self.x-1)][int(self.y-2)] != 0:
                    presence_mur = True
            if self.y < taille_plateau:
                if tableauMurV[int(self.x-1)][int(self.y-1)] != 0:
                    presence_mur = True

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
                    if tableauMurV[int(self.x+1)][int(self.y)] == 0 and tableauMurV[int(self.x+1)][int(self.y-1)] == 0:
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

        if self.y > 1:  # verifie que le joueur n'est pas sur la premiere colonne pour dep vers haut
            presence_mur = False
            if self.x > 1:
                if tableauMurH[int(self.x-2)][int(self.y-2)] != 0:
                    presence_mur = True
            if self.x < taille_plateau:
                if tableauMurH[int(self.x-1)][int(self.y-2)] != 0:
                    presence_mur = True

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
                    if tableauMurV[int(self.x)][int(self.y-2)] == 0 and tableauMurV[int(self.x-1)][int(self.y-2)] == 0:
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

        if self.y < taille_plateau:  # verifie que le joueur n'est pas sur la derniere colonne pour dep vers bas
            presence_mur = False
            if self.x > 1:
                if tableauMurH[int(self.x-2)][int(self.y-1)] != 0:
                    presence_mur = True
            if self.x < taille_plateau:
                if tableauMurH[int(self.x-1)][int(self.y-1)] != 0:
                    presence_mur = True

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
                    if tableauMurV[int(self.x)][int(self.y+1)] == 0 and tableauMurV[int(self.x-1)][int(self.y+1)] == 0:
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

        # on attend que le joueur clique sur une case
        while True:
            ev = pygame.event.poll()
            # si on clique sur un bouton
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if pos[0] > Quadrillage_dx and pos[0] < Quadrillage_dx+Quadrillage_lX and pos[1] > Quadrillage_dy and pos[1] < Quadrillage_dy+Quadrillage_ly:
                    # on recupere la case ou le joueur a clique
                    indx = int((pos[0]-Quadrillage_dx)/Qpas_x)+1
                    indy = int((pos[1]-Quadrillage_dy)/Qpas_y)+1
                    # on vérifie que la case est dans le tableau
                    if (indx, indy) in deplace_possible:
                        # on deplace le joueur
                        self.x = indx
                        self.y = indy
                        break

    def poser_murV(self, fenetre, tableauMurV, taille_plateau):
        # on init un tableau avec les coordonnées des murs possibles
        mur_possible = [[False for i in range(
            taille_plateau-1)] for j in range(taille_plateau-1)]

        # on affiche les milieux de murs possibles
        for i in range(taille_plateau-1):
            for j in range(taille_plateau-1):
                if tableauMurV[i][j] == 0 and tableauMurH[i][j] == 0:
                    if j > 0:  # si on est pas sur la premiere ligne
                        if j < taille_plateau-2:  # si on est pas sur la derniere ligne
                            # si il n'y a pas de mur au dessus et en dessous
                            if tableauMurV[i][j-1] == 0 and tableauMurV[i][j+1] == 0:
                                pygame.draw.circle(fenetre, blanc, (Quadrillage_dx+Qpas_x*(
                                    i+1)-Quad_mur/2, Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2), 6, 0)
                                mur_possible[i][j] = True
                        else:  # si on est sur la derniere ligne
                            if tableauMurV[i][j-1] == 0:
                                pygame.draw.circle(fenetre, blanc, (Quadrillage_dx+Qpas_x*(
                                    i+1)-Quad_mur/2, Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2), 6, 0)
                                mur_possible[i][j] = True
                    else:  # si on est sur la premiere ligne
                        if tableauMurV[i][j+1] == 0:
                            pygame.draw.circle(fenetre, blanc, (Quadrillage_dx+Qpas_x*(
                                i+1)-Quad_mur/2, Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2), 6, 0)
                            mur_possible[i][j] = True
        pygame.display.flip()
        mur_choisi = False  # on attend que le joueur clique sur un neoud de mur
        while mur_choisi == False:
            ev = pygame.event.poll()
            if pygame.mouse.get_pressed()[0]:  # si on clique
                pos = pygame.mouse.get_pos()
                if pos[0] > Quadrillage_dx and pos[0] < Quadrillage_dx+Quadrillage_lX and pos[1] > Quadrillage_dy and pos[1] < Quadrillage_dy+Quadrillage_ly:
                    # on cherche la case ou le joueur a clique
                    for i in range(taille_plateau-1):
                        for j in range(taille_plateau-1):
                            if tableauMurV[i][j] == 0 and tableauMurH[i][j] == 0 and mur_possible[i][j] == True:
                                distance = (Quadrillage_dx+Qpas_x*(i+1)-Quad_mur/2-pos[0])**2+(
                                    Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2-pos[1])**2
                                if distance < 36:
                                    # print("poser murV")
                                    tableauMurV[i][j] = self.couleur
                                    mur_choisi = True
                                    break

    def poser_murH(self, fenetre, tableauMurH, taille_plateau):
        # on init un tableau avec les coordonnées des murs possibles
        mur_possible = [[False for i in range(
            taille_plateau-1)] for j in range(taille_plateau-1)]

        # on affiche les milieux de murs possibles
        for i in range(taille_plateau-1):
            for j in range(taille_plateau-1):
                if tableauMurH[i][j] == 0 and tableauMurV[i][j] == 0:
                    if i > 0:
                        if i < taille_plateau-2:
                            if tableauMurH[i-1][j] == 0 and tableauMurH[i+1][j] == 0:
                                pygame.draw.circle(fenetre, blanc, (Quadrillage_dx+Qpas_x*(
                                    i+1)-Quad_mur/2, Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2), 6, 0)
                                mur_possible[i][j] = True
                        else:
                            if tableauMurH[i-1][j] == 0:
                                pygame.draw.circle(fenetre, blanc, (Quadrillage_dx+Qpas_x*(
                                    i+1)-Quad_mur/2, Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2), 6, 0)
                                mur_possible[i][j] = True
                    else:
                        if tableauMurH[i+1][j] == 0:
                            pygame.draw.circle(fenetre, blanc, (Quadrillage_dx+Qpas_x*(
                                i+1)-Quad_mur/2, Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2), 6, 0)
                            mur_possible[i][j] = True
        pygame.display.flip()
        mur_choisi = False
        while mur_choisi == False:
            ev = pygame.event.poll()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if pos[0] > Quadrillage_dx and pos[0] < Quadrillage_dx+Quadrillage_lX and pos[1] > Quadrillage_dy and pos[1] < Quadrillage_dy+Quadrillage_ly:
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
# initialisation graphiques
fenetre_jeu = cree_page_principale()

# if nb_joueur == 0:
nb_joueur = afficher_menu_nb_joueur(fenetre_jeu)
print(nb_joueur)

# if taille_plateau == 0:
taille_plateau = afficher_menu_taille_plateau(fenetre_jeu)
print(taille_plateau)

# initialisation des tableaux de mur
tableauMurH = initMurTabMur(taille_plateau)
tableauMurV = initMurTabMur(taille_plateau)

# init du pas graphique
Qpas_x = Quadrillage_lX / taille_plateau
Qpas_y = Quadrillage_ly / taille_plateau

# init des joueurs
joueurs = []

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


partie_finie = False
nb_coups = 0
while not partie_finie:
    nb_coups += 1
    print(partie_finie)
    for i in range(nb_joueur):
        # initialisation du plateau et des données
        affichage_plateau(fenetre_jeu, nb_joueur, taille_plateau,
                          joueurs, i, tableauMurH, tableauMurV)
        pygame.display.flip()

        while True:
            # test de sortie
            ev = pygame.event.poll()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                pygame.quit()
            if ev.type == pygame.QUIT:
                pygame.quit()

            # si on clique sur un bouton
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                # si on clique sur deplacer
                if pos[0] > 400 and pos[0] < 550 and pos[1] > 510 and pos[1] < 660:
                    joueurs[i].deplacer(fenetre_jeu, nb_joueur, taille_plateau)
                    pygame.display.flip()
                    break

                # si on clique sur pose mur vertical en 615, 150, 50, 165
                if pos[0] > 615 and pos[0] < 780 and pos[1] > 150 and pos[1] < 200:
                    joueurs[i].poser_murV(
                        fenetre_jeu, tableauMurV, taille_plateau)
                    pygame.display.flip()
                    break

                # si on clique sur pose mur horizontal en 615, 300, 50, 165
                if pos[0] > 615 and pos[0] < 780 and pos[1] > 300 and pos[1] < 350:
                    joueurs[i].poser_murH(
                        fenetre_jeu, tableauMurH, taille_plateau)
                    pygame.display.flip()
                    break
        #test de victoire
        if victoire(joueurs[i].x, joueurs[i].y, taille_plateau, joueurs[i].couleur)==True:

            # Recupération du chemin vers python
            python = sys.executable

            # Affichage de la victoire avec possibilité de relancer la partie
            afficher_victoire(fenetre_jeu, joueurs[i].couleur, nb_coups, python, sys.argv)
            partie_finie = True
            break

    # pause 0.1s
    pygame.time.wait(100)




