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

# classe joueur


class Joueur:
    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur

    def affichage_joueur(self, fenetre, couleur, x, y, rayon):
        pygame.draw.circle(fenetre, couleur, (x, y), rayon, 0)


def cree_page_principale():
    # Création d'une surface pour la fenêtre principale
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Quoridor")  # titre de la fenetre
    return screen


# Création d'un bouton complet
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


def affiche_text(screen, x, y, couleurText, text):
    font = pygame.font.Font(None, 36)
    text = font.render(text, 1, couleurText)
    screen.blit(text, (x, y))


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


def affichage_plateau(fenetre, nb_joueur, taille_plateau):
    # Clear fenetre
    fenetre.fill(noir)

    # Affichage des textes
    affiche_text(fenetre, 250, 30, blanc, "A qui de jouer ?")
    affiche_text(fenetre, 250, 50, blanc, "tableau")

    Quadrillage_dx = 200  # position X du coin haut gauche du quadrillage
    Quadrillage_dy = 100  # position Y du coin haut gauche du quadrillage
    Quadrillage_lX = 400  # longueur du quadrillage
    Quadrillage_ly = 400  # hauteur du quadrillage
    Qpas_x = Quadrillage_lX / taille_plateau  # pas du quadrillage en X
    Qpas_y = Quadrillage_ly / taille_plateau  # pas du quadrillage en Y
    Quad_mur = 5  # largeur des murs du quadrillage

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

    # affichage des joueurs
    player1.affichage_joueur(fenetre, player1.couleur, Quadrillage_dx+Qpas_x*(player1.x-0.5)-Quad_mur/2,
                             Quadrillage_dy+Qpas_y*(player1.y-0.5)-Quad_mur/2, Qpas_x/3)
    player2.affichage_joueur(fenetre, player2.couleur, Quadrillage_dx+Qpas_x*(player2.x-0.5)-Quad_mur/2,
                             Quadrillage_dy+Qpas_y*(player2.y-0.5)-Quad_mur/2, Qpas_x/3)

    if nb_joueur == 4:
        player3.affichage_joueur(fenetre, player3.couleur, Quadrillage_dx+Qpas_x*(player3.x-0.5)-Quad_mur/2,
                                 Quadrillage_dy+Qpas_y*(player3.y-0.5)-Quad_mur/2, Qpas_x/3)
        player4.affichage_joueur(fenetre, player4.couleur, Quadrillage_dx+Qpas_x*(player4.x-0.5)-Quad_mur/2,
                                 Quadrillage_dy+Qpas_y*(player4.y-0.5)-Quad_mur/2, Qpas_x/3)

    pygame.display.flip()

    # # gestion des clics
    # action = False
    # while action == False:
    #     ev = pygame.event.poll()
    #     # si on clique sur un des boutons
    #     if pygame.mouse.get_pressed()[0]:
    #         pos = pygame.mouse.get_pos()
    #         if pos[0] > 200 and pos[0] < 250 and pos[1] > 510 and pos[1] < 660:
    #             action = "deplacement"
    #             print("deplacement")
    #             pygame.quit()
    #         if pos[0] > 450 and pos[0] < 500 and pos[1] > 510 and pos[1] < 660:
    #             action = "mur"
    #             print("mur")
    #             pygame.quit()

    while True:
        # test de sortie
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
            pygame.quit()
        if ev.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if pos[0] > 200 and pos[0] < 250 and pos[1] > 510 and pos[1] < 660:
                action = "deplacement"
                print("deplacement")
                pygame.quit()
            if pos[0] > 450 and pos[0] < 500 and pos[1] > 510 and pos[1] < 660:
                action = "mur"
                print("mur")
                pygame.quit()


# Programme principal
# initialisation graphiques
fenetre_jeu = cree_page_principale()

# if nb_joueur == 0:
nb_joueur = afficher_menu_nb_joueur(fenetre_jeu)
print(nb_joueur)

# if taille_plateau == 0:
taille_plateau = afficher_menu_taille_plateau(fenetre_jeu)
print(taille_plateau)

player1 = Joueur((taille_plateau+1)/2, 1, rouge)
if nb_joueur == 2:
    player2 = Joueur((taille_plateau+1)/2, taille_plateau, bleu)
else:
    player2 = Joueur(taille_plateau, (taille_plateau+1)/2, bleu)
    player3 = Joueur((taille_plateau+1)/2, taille_plateau, violet)
    player4 = Joueur(1, (taille_plateau+1)/2, vert)


# initialisation du plateau et des données
affichage_plateau(fenetre_jeu, nb_joueur, taille_plateau)
