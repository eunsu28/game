import pygame

pygame.init()
pygame.display.set_caption("게임")
clock = pygame.time.Clock()

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
s_x = width / 2.25
s_y = 400
x = 0
y = 0

running = True
while running:
    dt = clock.tick(60) 
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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                x = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or pygame.K_DOWN:
                y = 0

    s_x += x 
    s_y += y 

    pygame.display.update()
#blit
    screen.blit(background, (0, 0))
    screen.blit(charactor, (s_x, s_y))
#blit


pygame.quit()