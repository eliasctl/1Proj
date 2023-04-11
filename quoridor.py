import pygame
from func import *


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
        # on créé un tableau de tuples
        # chaque tuple contient les coordonnées d'une case ou le joueur peut se deplacer
        deplace_possible = []

        # on affiche les cercles sur les cases ou le joueur peut se deplacer
        if self.x > 1:
            # on vérifie qu'il n'y a pas de joueur sur la case
            presence_joueur = False
            for i in range(nb_joueur):
                if self.x-1 == joueurs[i].x and self.y == joueurs[i].y:
                    presence_joueur = True
            if presence_joueur == False:
                self.affichage_joueur(fenetre, blanc, self.x-1, self.y)
                # on ajoute les coordonnées de la case dans le tableau
                deplace_possible.append((self.x-1, self.y))
            elif self.x > 2:
                presence_joueur_case2 = False
                for j in range(nb_joueur):
                    if self.x-2 == joueurs[j].x and self.y == joueurs[j].y:
                        presence_joueur_case2 = True
                if presence_joueur_case2 == False:
                    self.affichage_joueur(fenetre, blanc, self.x-2, self.y)
                    deplace_possible.append((self.x-2, self.y))

        if self.x < taille_plateau:
            presence_joueur = False
            for i in range(nb_joueur):
                if self.x+1 == joueurs[i].x and self.y == joueurs[i].y:
                    presence_joueur = True
            if presence_joueur == False:
                self.affichage_joueur(fenetre, blanc, self.x+1, self.y)
                deplace_possible.append((self.x+1, self.y))
            elif self.x+2 < taille_plateau:
                presence_joueur_case2 = False
                for i in range(nb_joueur):
                    if self.x+2 == joueurs[i].x and self.y == joueurs[i].y:
                        presence_joueur_case2 = True
                if presence_joueur_case2 == False:
                    self.affichage_joueur(
                        fenetre, blanc, self.x+2, self.y)
                    deplace_possible.append((self.x+2, self.y))

        if self.y > 1:
            presence_joueur = False
            for i in range(nb_joueur):
                if self.x == joueurs[i].x and self.y-1 == joueurs[i].y:
                    presence_joueur = True
            if presence_joueur == False:
                self.affichage_joueur(fenetre, blanc, self.x, self.y-1)
                deplace_possible.append((self.x, self.y-1))
            elif self.y-2 > 0:
                presence_joueur_case2 = False
                for i in range(nb_joueur):
                    if self.x == joueurs[i].x and self.y-2 == joueurs[i].y:
                        presence_joueur_case2 = True
                if presence_joueur_case2 == False:
                    self.affichage_joueur(
                        fenetre, blanc, self.x, self.y-2)
                    deplace_possible.append((self.x, self.y-2))

        if self.y < taille_plateau:
            presence_joueur = False
            for i in range(nb_joueur):
                if self.x == joueurs[i].x and self.y+1 == joueurs[i].y:
                    presence_joueur = True
            if presence_joueur == False:
                self.affichage_joueur(fenetre, blanc, self.x, self.y+1)
                deplace_possible.append((self.x, self.y+1))
            elif self.y+2 < taille_plateau:
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
        # on affiche les milieux de murs possibles
        for i in range(taille_plateau-1):
            for j in range(taille_plateau-1):
                if tableauMurV[i][j] == 0:
                    pygame.draw.circle(fenetre, blanc, (Quadrillage_dx+Qpas_x*(i+1)-Quad_mur/2,
                                                        Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2), 6, 0)
        pygame.display.flip()

        # on attend que le joueur clique sur un neoud de mur
        mur_choisi = False
        while mur_choisi == False:
            ev = pygame.event.poll()
            # si on clique
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if pos[0] > Quadrillage_dx and pos[0] < Quadrillage_dx+Quadrillage_lX and pos[1] > Quadrillage_dy and pos[1] < Quadrillage_dy+Quadrillage_ly:
                    # on cherche la case ou le joueur a clique
                    for i in range(taille_plateau-1):
                        for j in range(taille_plateau-1):
                            # print("test des valeurs de i et j : ", i, j)
                            if tableauMurV[i][j] == 0:
                                distance = (Quadrillage_dx+Qpas_x*(i+1)-Quad_mur/2-pos[0])**2+(
                                    Quadrillage_dy+Qpas_y*(j+1)-Quad_mur/2-pos[1])**2
                                if distance < 36:
                                    print("poser murV")
                                    tableauMurV[i][j] = self.couleur
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

# debug
# afficheTableau(tableauMurH)
# print("\n")
# afficheTableau(tableauMurV)

# init du pas graphique
Qpas_x = Quadrillage_lX / taille_plateau
Qpas_y = Quadrillage_ly / taille_plateau

# creation des joueurs
# on créé et rempli le tableau des joueurs
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
while not partie_finie:

    for i in range(nb_joueur):

        # initialisation du plateau et des données
        affichage_plateau(fenetre_jeu, nb_joueur, taille_plateau, joueurs, i)

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
                # print("pos = " + str(pos))
                # Position bouton deplacement 400, 510, 50, 150,
                if pos[0] > 400 and pos[0] < 550 and pos[1] > 510 and pos[1] < 660:
                    joueurs[i].deplacer(fenetre_jeu, nb_joueur, taille_plateau)
                    pygame.display.flip()
                    break
                # Position bouton mur 615, 150, 50, 165
                if pos[0] > 615 and pos[0] < 780 and pos[1] > 150 and pos[1] < 200:
                    joueurs[i].poser_murV(
                        fenetre_jeu, tableauMurV, taille_plateau)
                    pygame.display.flip()
                    break

    # pause 0.25 seconde
    pygame.time.wait(250)
