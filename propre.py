import pygame

# Initialisation de Pygame
pygame.init()


def cree_page_principale():
    # Création d'une surface pour la fenêtre principale
    screen = pygame.display.set_mode((400, 300))
    return screen


def create_second_window():
    # Création de la deuxième fenêtre
    second_screen = pygame.display.set_mode((200, 100))
    second_screen.fill(pygame.Color('white'))
    pygame.display.set_caption('Deuxième fenêtre')
    return second_screen


def creation_bouton(screen, x, y, hauteur, largeur, couleurBoutton, couleurText, text):
    # Création d'un bouton complet
    button_rect = pygame.Rect(x, y, largeur, hauteur)
    button_color = pygame.Color(couleurBoutton)
    button_text = pygame.font.SysFont(None, 24).render(
        text, True, pygame.Color(couleurText))

    # Affichage du bouton
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_rect.move(10, hauteur/2))


def main_loop():
    # Création de la fenêtre principale
    screen = cree_page_principale()
    pygame.display.set_caption('Fenêtre principale')

    # Boucle principale
    running = True
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Vérification si le clic est sur le bouton
                button_rect = pygame.Rect(150, 100, 100, 50)
                if button_rect.collidepoint(event.pos):
                    # Création de la deuxième fenêtre
                    second_screen = create_second_window()
                    pygame.display.flip()

        # Affichage de la fenêtre principale et du bouton
        screen.fill(pygame.Color('white'))
        creation_bouton(screen)
        pygame.display.flip()

    # Fermeture de Pygame
    pygame.quit()


# Appel de la fonction pour exécuter la boucle principale
main_loop()
