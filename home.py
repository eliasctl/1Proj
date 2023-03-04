import pygame

# pour pygame
pygame.init()  # Initialisation de Pygame
t_fenetre = (800, 600)
fenetre = pygame.display.set_mode(t_fenetre)  # Création de la fenêtre
pygame.display.set_caption("Quoridor")  # titre de la fenetre

# couleur
noir = (0, 0, 0)
blanc = (255, 255, 255)
bleu = (0, 0, 255)
vert = (0, 255, 0)
rouge = (255, 0, 0)
gris = (50, 50, 50)

# variables du jeux
nb_joueur = 0
taille_plateau = 0


def afficher_menu_nb_joueur():
    # texte de bienvenue
    font = pygame.font.Font(None, 36)
    text = font.render("Bienvenue sur Quoridor", 1, blanc)
    textpos = text.get_rect()
    textpos.centerx = fenetre.get_rect().centerx
    fenetre.blit(text, (250, 100))

    text = font.render("Choississez le nombre de joueurs", 1, blanc)
    textpos = text.get_rect()
    textpos.centerx = fenetre.get_rect().centerx
    fenetre.blit(text, (250, 200))

    # boutons pour choisir le nombre de joueur
    pygame.draw.rect(fenetre, gris, pygame.Rect(100, 300, 200, 200))
    pygame.draw.rect(fenetre, gris, pygame.Rect(500, 300, 200, 200))

    # texte pour choisir le nombre de joueur
    font = pygame.font.Font(None, 36)
    text = font.render("2 joueur", 1, blanc)
    textpos = text.get_rect()
    textpos.centerx = fenetre.get_rect().centerx
    fenetre.blit(text, (150, 350))

    font = pygame.font.Font(None, 36)
    text = font.render("4 joueurs", 1, blanc)
    textpos = text.get_rect()
    textpos.centerx = fenetre.get_rect().centerx
    fenetre.blit(text, (550, 350))
    pygame.display.flip()

    nb_joueur = 0

    while nb_joueur == 0:
        # si on clique sur un bouton
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if pos[0] > 100 and pos[0] < 300 and pos[1] > 300 and pos[1] < 500:
                nb_joueur = 2
            if pos[0] > 500 and pos[0] < 700 and pos[1] > 300 and pos[1] < 500:
                nb_joueur = 4
    return nb_joueur


def afficher_menu_taille_plateau():
    # texte de bienvenue
    font = pygame.font.Font(None, 36)
    text = font.render("Bienvenue sur Quoridor", 1, blanc)
    textpos = text.get_rect()
    textpos.centerx = fenetre.get_rect().centerx
    fenetre.blit(text, (250, 100))

    text = font.render("Choississez la taille du plateau", 1, blanc)
    textpos = text.get_rect()
    textpos.centerx = fenetre.get_rect().centerx
    fenetre.blit(text, (250, 200))

    # boutons pour choisir le nombre de joueur
    pygame.draw.rect(fenetre, gris, pygame.Rect(100, 300, 100, 100))
    pygame.draw.rect(fenetre, gris, pygame.Rect(500, 300, 100, 100))
    pygame.draw.rect(fenetre, gris, pygame.Rect(100, 500, 100, 100))
    pygame.draw.rect(fenetre, gris, pygame.Rect(500, 500, 100, 100))

    # texte pour choisir le nombre de joueur
    font = pygame.font.Font(None, 36)
    text = font.render("5 x 5", 1, blanc)
    textpos = text.get_rect()
    textpos.centerx = fenetre.get_rect().centerx
    fenetre.blit(text, (120, 325))

    font = pygame.font.Font(None, 36)
    text = font.render("7 x 7", 1, blanc)
    textpos = text.get_rect()
    textpos.centerx = fenetre.get_rect().centerx
    fenetre.blit(text, (525, 325))

    font = pygame.font.Font(None, 36)
    text = font.render("9 x 9", 1, blanc)
    textpos = text.get_rect()
    textpos.centerx = fenetre.get_rect().centerx
    fenetre.blit(text, (120, 525))

    font = pygame.font.Font(None, 36)
    text = font.render("11 x 11", 1, blanc)
    textpos = text.get_rect()
    textpos.centerx = fenetre.get_rect().centerx
    fenetre.blit(text, (525, 525))
    pygame.display.flip()

    taille_plateau = 0

    while taille_plateau == 0:
        # si on clique sur un bouton
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if pos[0] > 100 and pos[0] < 200 and pos[1] > 300 and pos[1] < 350:
                taille_plateau = 5
            if pos[0] > 500 and pos[0] < 600 and pos[1] > 300 and pos[1] < 350:
                taille_plateau = 7
            if pos[0] > 100 and pos[0] < 200 and pos[1] > 500 and pos[1] < 550:
                taille_plateau = 9
            if pos[0] > 500 and pos[0] < 600 and pos[1] > 500 and pos[1] < 550:
                taille_plateau = 11
    return taille_plateau


while True:
    ev = pygame.event.poll()
    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
        break
    if ev.type == pygame.QUIT:
        break

    if nb_joueur == 0:
        nb_joueur = afficher_menu_nb_joueur()
        print(nb_joueur)

    if taille_plateau == 0:
        taille_plateau = afficher_menu_taille_plateau()
        print(taille_plateau)

    fenetre.fill(noir)
    pygame.display.flip()
