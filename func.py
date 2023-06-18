# Importation des libraries

import pygame
import time
import os

# Initialisation de Pygame
pygame.init()

# Création des couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)
bleu = (0, 0, 255)
vert = (19, 143, 0)
rouge = (143, 0, 0)
violet = (84, 0, 201)
gris = (150, 150, 150)
ombre = (50, 50, 50)

# Création des variables de jeu
nb_joueur = 0
taille_plateau = 0

# Céation des variables garphiques
Quadrillage_dx = 200  # position X du coin haut gauche du quadrillage
Quadrillage_dy = 100  # position Y du coin haut gauche du quadrillage
Quadrillage_lX = 400  # longueur du quadrillage
Quadrillage_ly = 400  # hauteur du quadrillage
Qpas_x = 1  # pas du quadrillage en X
Qpas_y = 1  # pas du quadrillage en Y
Quad_mur = 5  # largeur des murs du quadrillage


# Fonction qui affiche la page principale
def cree_page_principale():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Quoridor")  # titre de la fenetre
    return screen


# Création d'un bouton complet avec texte et ombre
def creation_bouton(screen, x, y, hauteur, largeur, couleurBoutton, couleurText, text, PossedeUneOmbre):
    
    # Affichage ombre
    if PossedeUneOmbre:
        button_rect = pygame.Rect(x+3, y+3, largeur, hauteur)
        button_color = pygame.Color(ombre)
        pygame.draw.rect(screen, button_color, button_rect)

    # Affichage du bouton
    button_rect = pygame.Rect(x, y, largeur, hauteur)
    button_color = pygame.Color(couleurBoutton)
    button_text = pygame.font.SysFont(None, 23).render(text, True, pygame.Color(couleurText))
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_rect.move(largeur/4, hauteur/2))

# Fonction d'affichage de texte
def affiche_text(screen, x, y, couleurText, text):
    font = pygame.font.Font(None, 36)
    text = font.render(text, 1, couleurText)
    screen.blit(text, (x, y))

# Affichage du menu de confirmation des choix
def afficher_confirmation_choix(fenetre, nb_joueur, taille_plateau, mode_jeu):
    fenetre.fill(noir)
    affiche_text(fenetre, 250, 50, blanc, "Confirmation de vos choix : ")
    affiche_text(fenetre, 15, 150, blanc, "Nombre de joueurs : " + str(nb_joueur))
    affiche_text(fenetre, 15, 300, blanc, "Taille du plateau : " + str(taille_plateau) + " x " + str(taille_plateau))
    affiche_text(fenetre, 15, 425, blanc, "Mode de jeu : " + str(mode_jeu))
    creation_bouton(fenetre, 250, 500, 100, 100, gris, blanc, "Valider", True)
    creation_bouton(fenetre, 400, 500, 100, 100, gris, blanc, "Retour", True)
    time.sleep(0.1)
    pygame.display.flip()

    choix_fait = 0
    while choix_fait == 0:
        # Tests de sortie
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
            pygame.quit()

        if ev.type == pygame.QUIT:
            pygame.quit()

        # Evennement de clic sur un bouton
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if pos[0] > 250 and pos[0] < 350 and pos[1] > 500 and pos[1] < 600:
                choix_fait = 1
                retour = True
            if pos[0] > 400 and pos[0] < 500 and pos[1] > 500 and pos[1] < 600:
                choix_fait = 1
                retour = False
    return retour


# Affichage des choix pour le mode de jeu et renvoie des choix sous forme de liste
def afficher_menu_jeu(fenetre):

    # Création de la liste des choix
    liste_choix = []

    # Clear fenetre & affichage Bienvenue
    fenetre.fill(noir)
    affiche_text(fenetre, 250, 50, blanc, "Bienvenue sur Quoridor")

    # Menu Choix Joueurs
    affiche_text(fenetre, 15, 150, blanc, "Choississez le nombre de joueurs : ")
    creation_bouton(fenetre, 470, 105, 100, 100, gris, blanc, "2 joueurs", True)
    creation_bouton(fenetre, 600, 105, 100, 100, gris, blanc, "4 joueurs", True)

    # Menu Choix Taille Plateau
    affiche_text(fenetre, 15, 300, blanc, "Choississez la taille du plateau : ")
    creation_bouton(fenetre, 400, 250, 90, 90, gris, blanc, "5 x 5", True)
    creation_bouton(fenetre, 500, 250, 90, 90, gris, blanc, "7 x 7", True)
    creation_bouton(fenetre, 600, 250, 90, 90, gris, blanc, "9 x 9", True)
    creation_bouton(fenetre, 700, 250, 90, 90, gris, blanc, "11 x 11", True)

    # Menu Choix Mode de Jeu
    affiche_text(fenetre, 15, 425, blanc, "Choississez le mode de jeu : ")
    creation_bouton(fenetre, 400, 375, 100, 115, gris, blanc, "Vs Humain", True)
    creation_bouton(fenetre, 600, 375, 100, 115, gris, blanc, "Vs Bot (2J)", True)

    creation_bouton(fenetre, 300, 500, 90, 200, vert, blanc, "Lancer la partie", True)

    # Afficher l'écran
    time.sleep(0.1)
    pygame.display.flip()

    # Attente des choix
    fin = 0
    taille_plateau = 0
    nb_joueur = 0
    mode_jeu = 0

    while fin == 0:
        # Tests de sortie
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
            pygame.quit()

        if ev.type == pygame.QUIT:
            pygame.quit()

        # Evennement de clic sur un bouton
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if pos[0] > 400 and pos[0] < 490 and pos[1] > 250 and pos[1] < 340:
                print("5")
                taille_plateau = 5
                print("taille_plateau")
                print(taille_plateau)
            if pos[0] > 500 and pos[0] < 590 and pos[1] > 250 and pos[1] < 340:
                print("7")
                taille_plateau = 7
                print("taille_plateau")
                print(taille_plateau)
            if pos[0] > 600 and pos[0] < 690 and pos[1] > 250 and pos[1] < 340:
                print("9")
                taille_plateau = 9
                print("taille_plateau")
                print(taille_plateau)
            if pos[0] > 700 and pos[0] < 790 and pos[1] > 250 and pos[1] < 340:
                print("11")
                taille_plateau = 11
                print("taille_plateau")
                print(taille_plateau)
            
            if pos[0] > 470 and pos[0] < 570 and pos[1] > 105 and pos[1] < 205:
                print("2")
                nb_joueur = 2
                print("nb_joueur")
                print(nb_joueur)
            if pos[0] > 600 and pos[0] < 700 and pos[1] > 105 and pos[1] < 205:
                print("4")
                nb_joueur = 4
                print("nb_joueur")
                print(nb_joueur)
            
            if pos[0] > 400 and pos[0] < 500 and pos[1] > 375 and pos[1] < 490:
                print("Humain")
                mode_jeu = 1
                print("mode_jeu")
                print(mode_jeu)
            if pos[0] > 600 and pos[0] < 700 and pos[1] > 375 and pos[1] < 490:
                print("Bot")
                mode_jeu = 2
                print("mode_jeu")
                print(mode_jeu)

            print ("----------")
            print (mode_jeu)
            print (nb_joueur)
            print (taille_plateau)
            print ("----------")

            if pos[0] > 300 and pos[0] < 500 and pos[1] > 500 and pos[1] < 590:
                if taille_plateau != 0 and nb_joueur != 0 and mode_jeu != 0:
                    fin = 1

    # Ajout des paramètres à la liste
    liste_choix.append(nb_joueur)
    liste_choix.append(taille_plateau)
    liste_choix.append(mode_jeu)

    conf_choix = afficher_confirmation_choix(fenetre, nb_joueur, taille_plateau, mode_jeu)
    if conf_choix == True:
        return liste_choix
    else:
        afficher_menu_jeu(fenetre)


# Affichage du plateau de jeu
def affichage_plateau(fenetre, nb_joueur, taille_plateau, joueur, joueur_actif, tableauMurH, tableauMurV):
    
    # Clear fenetre
    fenetre.fill(noir)

    # Initialisation du pas graphique
    Qpas_x = Quadrillage_lX / taille_plateau
    Qpas_y = Quadrillage_ly / taille_plateau

    # Affichage des textes
    affiche_text(fenetre, 250, 30, joueur[joueur_actif].couleur,
                 "Joueur en cours : Joueur "+str(joueur_actif+1))

    # Affichage du quadrillage
    for i in range(taille_plateau):
        for j in range(taille_plateau):
            creation_bouton(fenetre, Quadrillage_dx+Qpas_x*i, Quadrillage_dy +
                            Qpas_y*j, Qpas_x-Quad_mur, Qpas_y-Quad_mur, gris, gris, "", False)

    # Affichage des murs
    for i in range(taille_plateau-1):
        for j in range(taille_plateau-1):
            if tableauMurV[i][j] != 0:
                creation_bouton(fenetre, Quadrillage_dx+Qpas_x*(i+1), Quadrillage_dy +
                                Qpas_y*j, 2*Qpas_y, Quad_mur, tableauMurV[i][j], tableauMurV[i][j], "", False)  # mur vertical
            if tableauMurH[i][j] != 0:
                creation_bouton(fenetre, Quadrillage_dx+Qpas_x*i, Quadrillage_dy +
                                Qpas_y*(j+1), Quad_mur, 2*Qpas_x, tableauMurH[i][j], tableauMurH[i][j], "", False)  # mur horizontal

   # Affichage des boutons (pour le deplacement ou le placement de mur)
    creation_bouton(fenetre, 400, 510, 50, 150,
                    gris, blanc, "Se Deplacer", True)

    creation_bouton(fenetre, 615, 150, 50, 165, gris,
                    blanc, "mur Vertical", True)
    creation_bouton(fenetre, 615, 300, 50, 165, gris,
                    blanc, "mur Horizontal", True)

    # Affichage des joueurs
    joueur[0].affichage_joueur(fenetre, joueur[0].couleur,
                               joueur[0].x, joueur[0].y)
    joueur[1].affichage_joueur(fenetre, joueur[1].couleur,
                               joueur[1].x, joueur[1].y)
    if nb_joueur == 4:
        joueur[2].affichage_joueur(
            fenetre, joueur[2].couleur, joueur[2].x, joueur[2].y)
        joueur[3].affichage_joueur(
            fenetre, joueur[3].couleur, joueur[3].x, joueur[3].y)

    pygame.display.flip()


# Creation d'un tableau de mur
def initMurTabMur(taille_plateau):
    mur = []
    for i in range(taille_plateau):
        mur.append([])
        for j in range(taille_plateau):
            mur[i].append(0)
    return mur


# Affichage du tableau
def afficheTableau(tableau):
    for ligne in tableau:
        print(ligne)

# Vérification de victoire
def victoire(x, y, taille_plateau, couleur):
    if couleur==rouge :
        if y==taille_plateau:
            return True
    elif couleur==bleu :
        if y==1:
            return True
    elif couleur==violet :
        if x==1:
            return True
    elif couleur==vert :
        if x==taille_plateau:
            return True
        

# Affichage de la page de victoire
def afficher_victoire(fenetre, joueur_actif, nb_coups, python, sys_argv):
    
    # Clear fenetre
    fenetre.fill(noir)

    # Agrrandissement de la fenetre pour afficher le texte
    fenetre = pygame.display.set_mode((800, 700))
    # On récupère le nom du joueur actif
    if joueur_actif == rouge:
        joueur_actif = "rouge"
    elif joueur_actif == bleu:
        joueur_actif = "bleu"
    elif joueur_actif == violet:
        joueur_actif = "violet"
    elif joueur_actif == vert:
        joueur_actif = "vert"

    # Affichage des textes
    affiche_text(fenetre, 250, 100, blanc, "Victoire du joueur "+str(joueur_actif))
    affiche_text(fenetre, 250, 200, blanc, "Félicitation !")
    
    # Affichage du nombre de coups
    affiche_text(fenetre, 250, 300, blanc, "Nombre de coups : "+str(nb_coups))

    # Affichage des boutons pour rejouer ou quitter
    creation_bouton(fenetre, 100, 400, 200, 200, bleu, blanc, "Rejouer", True)
    creation_bouton(fenetre, 500, 400, 200, 200, bleu, blanc, "Quitter", True)

    pygame.display.flip()

    # Attente du choix de l'utilisateur
    while True:
        # test de sortie
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
            pygame.quit()
        if ev.type == pygame.QUIT:
            pygame.quit()

        # Evennement de clic sur un bouton
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if pos[0] > 100 and pos[0] < 400 and pos[1] > 400 and pos[1] < 500:
                
                # Relance du programme pour une nouvelle partie
                pygame.quit()
                os.execv(python, [python] + sys_argv)
            if pos[0] > 500 and pos[0] < 700 and pos[1] > 400 and pos[1] < 500:
                pygame.quit()