import pygame
import sys
from game import *
import os



pygame.init()


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("EdenGarden")
# Police de texte
font = pygame.font.Font(None, 36)

game_title = font.render("EdenGarden", True, BLACK)
solo_text = font.render("Play", True, BLACK)
git_text = font.render("Github", True, BLACK)
credit_text = font.render("Credits", True, BLACK)

solo_rect = solo_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
multi_rect = git_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
menu_running = True

while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if solo_rect.collidepoint(mouse_x, mouse_y):
                print("Lancement du mode Solo") 
                start_game()
                pygame.quit()
            elif multi_rect.collidepoint(mouse_x, mouse_y):
                os.system('start https://github.com/clochettes/edengarden')


    # Affichage du menu
    screen.blit(background_image, (0, 0))
    screen.blit(game_title, (SCREEN_WIDTH // 2 - game_title.get_width() // 2, 50))

    screen.blit(solo_text, solo_rect.topleft)
    screen.blit(git_text, multi_rect.topleft)
    pygame.display.flip()

pygame.quit()
sys.exit()
