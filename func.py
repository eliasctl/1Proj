import pygame
import time

# Initialisation de Pygame
pygame.init()

# couleur
noir = (0, 0, 0)
blanc = (255, 255, 255)
bleu = (0, 0, 255)
vert = (19, 143, 0)
rouge = (143, 0, 0)
violet = (84, 0, 201)
gris = (150, 150, 150)
ombre = (50, 50, 50)

# variables du jeux
nb_joueur = 0
taille_plateau = 0

# variables graphiques
Quadrillage_dx = 200  # position X du coin haut gauche du quadrillage
Quadrillage_dy = 100  # position Y du coin haut gauche du quadrillage
Quadrillage_lX = 400  # longueur du quadrillage
Quadrillage_ly = 400  # hauteur du quadrillage
Qpas_x = 1  # pas du quadrillage en X
Qpas_y = 1  # pas du quadrillage en Y
Quad_mur = 5  # largeur des murs du quadrillage


# fonction qui affiche la page principale
def cree_page_principale():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Quoridor")  # titre de la fenetre
    return screen


# Création d'un bouton complet avec texte et ombre
def creation_bouton(screen, x, y, hauteur, largeur, couleurBoutton, couleurText, text, PossedeUneOmbre):
    # affichage ombre
    if PossedeUneOmbre:
        button_rect = pygame.Rect(x+3, y+3, largeur, hauteur)
        button_color = pygame.Color(ombre)
        pygame.draw.rect(screen, button_color, button_rect)

    # Affichage du bouton
    button_rect = pygame.Rect(x, y, largeur, hauteur)
    button_color = pygame.Color(couleurBoutton)
    button_text = pygame.font.SysFont(None, 24).render(
        text, True, pygame.Color(couleurText))
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_rect.move(largeur/4, hauteur/2))


# fonction qui affiche du texte
def affiche_text(screen, x, y, couleurText, text):
    font = pygame.font.Font(None, 36)
    text = font.render(text, 1, couleurText)
    screen.blit(text, (x, y))


# fonction qui affiche le menu du nombre de joueur
def afficher_menu_nb_joueur(fenetre):
    # Clear fenetre
    fenetre.fill(noir)

    # Affichage des textes
    affiche_text(fenetre, 250, 100, blanc, "Bienvenue sur Quoridor")
    affiche_text(fenetre, 250, 200, blanc, "Choississez le nombre de joueurs")

    # boutons pour choisir le nombre de joueur
    creation_bouton(fenetre, 100, 300, 200, 200,
                    bleu, blanc, "2 joueurs", True)
    creation_bouton(fenetre, 500, 300, 200, 200,
                    bleu, blanc, "4 joueurs", True)

    pygame.display.flip()

    nb_joueur = 0
    while nb_joueur == 0:
        # test de sortie
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
            pygame.quit()
        if ev.type == pygame.QUIT:
            pygame.quit()
        # si on clique sur un bouton
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if pos[0] > 100 and pos[0] < 300 and pos[1] > 300 and pos[1] < 500:
                nb_joueur = 2
            if pos[0] > 500 and pos[0] < 700 and pos[1] > 300 and pos[1] < 500:
                nb_joueur = 4

    return nb_joueur


def afficher_menu_taille_plateau(fenetre):
    # Clear fenetre
    fenetre.fill(noir)

    # Affichage des textes
    affiche_text(fenetre, 250, 100, blanc, "Bienvenue sur Quoridor")
    affiche_text(fenetre, 250, 200, blanc, "Choississez la taille du plateau")

    # on dessine les 4 boutons
    creation_bouton(fenetre, 100, 300, 100, 100, gris, blanc, "5 x 5", True)
    creation_bouton(fenetre, 500, 300, 100, 100, gris, blanc, "7 x 7", True)
    creation_bouton(fenetre, 100, 450, 100, 100, gris, blanc, "9 x 9", True)
    creation_bouton(fenetre, 500, 450, 100, 100, gris, blanc, "11 x 11", True)
    time.sleep(1)
    pygame.display.flip()

    taille_plateau = 0
    while taille_plateau == 0:
        ev = pygame.event.poll()
        # si on clique sur un bouton
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if pos[0] > 100 and pos[0] < 200 and pos[1] > 300 and pos[1] < 400:
                taille_plateau = 5
            if pos[0] > 500 and pos[0] < 600 and pos[1] > 300 and pos[1] < 400:
                taille_plateau = 7
            if pos[0] > 100 and pos[0] < 200 and pos[1] > 450 and pos[1] < 550:
                taille_plateau = 9
            if pos[0] > 500 and pos[0] < 600 and pos[1] > 450 and pos[1] < 550:
                taille_plateau = 11
    # pygame.quit()
    return taille_plateau


def affichage_plateau(fenetre, nb_joueur, taille_plateau, player1, player2, player3, player4):
    # Clear fenetre
    fenetre.fill(noir)

    # init du pas graphique
    Qpas_x = Quadrillage_lX / taille_plateau
    Qpas_y = Quadrillage_ly / taille_plateau

    # Affichage des textes
    affiche_text(fenetre, 250, 30, blanc, "A qui de jouer ?")
    affiche_text(fenetre, 250, 50, blanc, "tableau")

    # boutons pour choisir le nombre de joueur
    for i in range(taille_plateau):
        for j in range(taille_plateau):
            creation_bouton(fenetre, Quadrillage_dx+Qpas_x*i, Quadrillage_dy +
                            Qpas_y*j, Qpas_x-Quad_mur, Qpas_y-Quad_mur, gris, gris, "", False)

    # affichage des boutons (pour le deplacement ou le placement de mur)
    creation_bouton(fenetre, 200, 510, 50, 150,
                    gris, blanc, "Se Deplacer", True)
    creation_bouton(fenetre, 450, 510, 50, 150, gris,
                    blanc, "Poser un mur", True)
    print("Tableau affiché")

    # affichage des joueurs
    player1.affichage_joueur(fenetre, player1.couleur,
                             player1.x, player1.y)
    player2.affichage_joueur(fenetre, player2.couleur,
                             player2.x, player2.y)
    if nb_joueur == 4:
        player3.affichage_joueur(
            fenetre, player3.couleur, player3.x, player3.y)
        player4.affichage_joueur(
            fenetre, player4.couleur, player4.x, player4.y)
    print("Joueurs affichés")

    pygame.display.flip()


def initMurTabMur(taille_plateau):
    mur = []
    for i in range(taille_plateau-1):
        mur.append([])
        for j in range(taille_plateau-1):
            mur[i].append(0)
    return mur


def afficheTableau(tableau):
    for ligne in tableau:
        print(ligne)
