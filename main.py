from typing_extensions import runtime
import pygame

pygame.init()
pygame.display.set_caption("게임")

hight = 800
width = 1000
screen = pygame.display.set_mode((width, hight))
background = pygame.image.load("img/b.png")

running = True

while running:


    pygame.display.update()

    screen.blit(background, (0, 0))

pygame.quit()