import pygame
import time

dimEcranX, dimEcranY = 400.0, 400.0     # Dimension de la grille
ecran = pygame.display.set_mode((dimEcranX, dimEcranY))

dimX, dimY = 40, 40


# fonction qui renvoie la casen où se trouve la souris
def getCase(posSouris):
    posCaseX = int((posSouris[0]) / dimX) + 1
    posCaseY = int((posSouris[1]) / dimY) + 1

    return (posCaseX, posCaseY)


while True:
    ev = pygame.event.poll()
    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
        break
    if ev.type == pygame.QUIT:
        break

    posSouris = pygame.mouse.get_pos()  # Récupérer la position du pointeur

    posCaseX, posCaseY = getCase(posSouris)

    print("Position x: " + str(posCaseX))
    print("Position y: " + str(posCaseY))

    # Dessiner la grille
    for y in range(0, 400, dimY):
        pygame.draw.line(ecran, 0xee0000, (0, y), (dimEcranX, y))

    for x in range(0, 400, dimX):
        pygame.draw.line(ecran, 0xee0000, (x, 0), (x, dimEcranY))

    pygame.display.flip()
    time.sleep(0.01)
