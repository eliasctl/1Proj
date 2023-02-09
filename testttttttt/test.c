

#include <SDL2/SDL.h>

int main(int argc, char *argv[])
{
    // Initialisation de la SDL
    if (SDL_Init(SDL_INIT_VIDEO) != 0)
    {
        SDL_Log("Unable to initialize SDL: %s", SDL_GetError());
        return 1;
    }

    // Définir la taille de chaque case
    int case_size = 50;

    // Création de la fenêtre
    SDL_Window *window = SDL_CreateWindow("Checkerboard", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, case_size * 10, case_size * 10, 0);
    if (!window)
    {
        SDL_Log("Unable to create window: %s", SDL_GetError());
        return 1;
    }
    // Création du rendu
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, 0);
    if (!renderer)
    {
        SDL_Log("Unable to create renderer: %s", SDL_GetError());
        return 1;
    }

    // Boucle pour dessiner les cases du damier
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            // Définir la couleur de la case en fonction de sa position
            if ((i + j) % 2 == 0)
            {
                SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
            }
            else
            {
                SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
            }

            // Dessiner la case
            SDL_Rect rect = {j * case_size, i * case_size, case_size, case_size};
            SDL_RenderFillRect(renderer, &rect);
        }
    }

    // Présenter les modifications
    SDL_RenderPresent(renderer);

    // Attente de l'événement de fermeture de fenêtre
    SDL_Event event;
    while (SDL_WaitEvent(&event) && event.type != SDL_QUIT)
        ;

    // Nettoyage de la mémoire
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}