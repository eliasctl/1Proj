import pygame
from func import *


# classe joueur
class Joueur:
    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur

    def affichage_joueur(self, fenetre, couleur, indx, indy):
        pygame.draw.circle(fenetre, couleur, (Quadrillage_dx+Qpas_x*(indx-0.5)-Quad_mur/2,
                                              Quadrillage_dy+Qpas_y*(indy-0.5)-Quad_mur/2), Qpas_x/3, 0)

    def deplacer(self, fenetre, nb_joueur, taille_plateau):
        # on créé un tableau de tuples
        # chaque tuple contient les coordonnées d'une case ou le joueur peut se deplacer
        deplace_possible = []

        # on affiche les cercles sur les cases ou le joueur peut se deplacer
        if self.x > 1:
            self.affichage_joueur(fenetre, blanc, self.x-1, self.y)
            # on ajoute les coordonnées de la case dans le tableau
            deplace_possible.append((self.x-1, self.y))
        if self.x < taille_plateau:
            self.affichage_joueur(fenetre, blanc, self.x+1, self.y)
            deplace_possible.append((self.x+1, self.y))
        if self.y > 1:
            self.affichage_joueur(fenetre, blanc, self.x, self.y-1)
            deplace_possible.append((self.x, self.y-1))
        if self.y < taille_plateau:
            self.affichage_joueur(fenetre, blanc, self.x, self.y+1)
            deplace_possible.append((self.x, self.y+1))
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


# Programme principal
# initialisation graphiques
fenetre_jeu = cree_page_principale()

# if nb_joueur == 0:
nb_joueur = afficher_menu_nb_joueur(fenetre_jeu)
print(nb_joueur)

# if taille_plateau == 0:
taille_plateau = afficher_menu_taille_plateau(fenetre_jeu)
print(taille_plateau)

# init du pas graphique
Qpas_x = Quadrillage_lX / taille_plateau
Qpas_y = Quadrillage_ly / taille_plateau
print(" init var graphique " + str(Qpas_x) + " " + str(Qpas_y))

# creation des joueurs
# on créé et rempli le tableau des joueurs
joueurs = []

joueurs.append(Joueur((taille_plateau+1)/2, 1, rouge))
if nb_joueur == 2:
    joueurs.append(Joueur((taille_plateau+1)/2, taille_plateau, bleu))
    joueurs.append(Joueur(0, 0, 0))
    joueurs.append(Joueur(0, 0, 0))
else:
    joueurs.append(Joueur(taille_plateau, (taille_plateau+1)/2, bleu))
    joueurs.append(Joueur((taille_plateau+1)/2, taille_plateau, violet))
    joueurs.append(Joueur(1, (taille_plateau+1)/2, vert))


parie_finie = False
while not parie_finie:

    for i in range(nb_joueur):

        # initialisation du plateau et des données
        affichage_plateau(fenetre_jeu, nb_joueur, taille_plateau,
                          joueurs[0], joueurs[1], joueurs[2], joueurs[3])

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
                # Position bouton deplacement 200, 510, 50, 150
                if pos[0] > 200 and pos[0] < 350 and pos[1] > 510 and pos[1] < 660:
                    joueurs[i].deplacer(fenetre_jeu, nb_joueur, taille_plateau)
                    pygame.display.flip()
                    break

    # pause 0.5 seconde
    pygame.time.wait(500)
