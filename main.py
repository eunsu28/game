import pygame

pygame.init()
pygame.display.set_caption("게임")

#스크린
hight = 600
width = 1000
screen = pygame.display.set_mode((width, hight))
#스크린

#케릭터 불러오기
background = pygame.image.load("img/b.png")
charactor = pygame.image.load("img/c.png")
#불러오기

#캐릭터 관련 정보
x = width / 2.25
y = 400

running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10  
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_UP:
                y -= 10
            elif event.key == pygame.K_DOWN:
                y += 10

    pygame.display.update()

#blit
    screen.blit(background, (0, 0))
    screen.blit(charactor, ((width / 2.25), 400))
#blit

pygame.quit()