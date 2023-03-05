import pygame
import time


# on definis une classe pour les joueurs
class Joueur:
    def __init__(self, nom, nb_barriere, position_x, position_y):
        self.nom = nom
        self.nb_barriere = nb_barriere
        self.position_x = position_x
        self.position_y = position_y

    def deplacement(self, direction):
        if direction == "haut":
            self.position_y -= 1
        elif direction == "bas":
            self.position_y += 1
        elif direction == "gauche":
            self.position_x -= 1
        elif direction == "droite":
            self.position_x += 1
        else:
            print("Erreur de direction")
        return self.position_x, self.position_y

    def pose_barriere(self, direction, position_x, position_y):
        if direction == "haut":
            position_y -= 1
        elif direction == "bas":
            position_y += 1
        elif direction == "gauche":
            position_x -= 1
        elif direction == "droite":
            position_x += 1
        else:
            print("Erreur de direction")
        return position_x, position_y


# Initialisation de Pygame
pygame.init()

# couleur
noir = (0, 0, 0)
blanc = (255, 255, 255)
bleu = (0, 0, 255)
vert = (0, 255, 0)
rouge = (255, 0, 0)
gris = (150, 150, 150)
ombre = (50, 50, 50)

# variables du jeux
nb_joueur = 0
taille_plateau = 0


def cree_page_principale():
    # Création d'une surface pour la fenêtre principale
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Quoridor")  # titre de la fenetre
    return screen


def creation_bouton(screen, x, y, hauteur, largeur, couleurBoutton, couleurText, text):
    # Création d'un bouton complet
    # affichage ombre
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
    creation_bouton(fenetre, 100, 300, 200, 200, bleu, blanc, "2 joueurs")
    creation_bouton(fenetre, 500, 300, 200, 200, bleu, blanc, "4 joueurs")

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
    creation_bouton(fenetre, 100, 300, 100, 100, gris, blanc, "5 x 5")
    creation_bouton(fenetre, 500, 300, 100, 100, gris, blanc, "7 x 7")
    creation_bouton(fenetre, 100, 450, 100, 100, gris, blanc, "9 x 9")
    creation_bouton(fenetre, 500, 450, 100, 100, gris, blanc, "11 x 11")
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


# initialisation graphiques
fenetre_jeu = cree_page_principale()

# if nb_joueur == 0:
nb_joueur = afficher_menu_nb_joueur(fenetre_jeu)
print(nb_joueur)

# if taille_plateau == 0:
taille_plateau = afficher_menu_taille_plateau(fenetre_jeu)
print(taille_plateau)


# initialisation des joueurs
if nb_joueur == 2:
    joueur1 = Joueur("Joueur 1", 10, int(taille_plateau/2), 1)
    joueur2 = Joueur("Joueur 2", 10, int(taille_plateau/2), taille_plateau)
else:
    joueur1 = Joueur("Joueur 1", 5, int(taille_plateau/2), 1)
    joueur2 = Joueur("Joueur 2", 5, taille_plateau, int(taille_plateau/2))
    joueur3 = Joueur("Joueur 3", 5, int(taille_plateau/2), taille_plateau)
    joueur4 = Joueur("Joueur 4", 5, 1, int(taille_plateau/2))
