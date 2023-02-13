import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
window_size = (400, 300)

# Création de la fenêtre
screen = pygame.display.set_mode(window_size)

# Boucle principale du jeu
running = True
while running:
    # Traitement des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            # Récupération de la position de la souris
            mouse_pos = pygame.mouse.get_pos()
            # Exécution d'une action si le clic a été effectué dans la zone définie
            print("Clic détecté dans la zone définie")

            # Mise à jour de l'écran
            screen.fill((random.randint(0, 255),
                         random.randint(0, 255),
                         random.randint(0, 255)))
    # Mise à jour de l'écran
    pygame.display.update()

# Nettoyage
pygame.quit()
