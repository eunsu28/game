import pygame

pygame.init()
pygame.display.set_caption("게임")

#스크린
hight = 800
width = 1000
screen = pygame.display.set_mode((width, hight))
#스크린

#케릭터 불러오기
background = pygame.image.load("img/b.png")
charactor = pygame.image.load("img/c.png")
#불러오기

running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    pygame.display.update()

#blit
    screen.blit(charactor, ((width / 2), 800))
    screen.blit(background, (0, 0))
#blit

pygame.quit()