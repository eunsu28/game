import pygame
import random
#remember commend d

pygame.init()
pygame.display.set_caption("game")
clock = pygame.time.Clock()

# 스크린
height = 750
width = 1000
screen = pygame.display.set_mode((width, height))
#

# 사진 불러오기
background = pygame.image.load("img/b.png")
charactor = pygame.image.load("img/c.jpg")
bad = pygame.image.load("img/bad.png")
#

# 캐릭터 설정
s_x = width / 2
s_y = 400
x = 0
y = 0
#

# 장애물 설정
b_s_x = random.randint(1, 1001)
b_s_y = random.randint(1, 751)
#

# 시간 설정
t_time = 2
start_ticks = pygame.time.get_ticks()
#

running = True
while running:

    time = (pygame.time.get_ticks() - start_ticks) / 1000
    get_time = t_time - time

    dt = clock.tick(60) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x -= 10
            elif event.key == pygame.K_d:
                x += 10
            elif event.key == pygame.K_w:
                y -= 10
            elif event.key == pygame.K_s:
                y += 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or pygame.K_d:
                x = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or pygame.K_s:
                y = 0

    s_x += x 
    s_y += y

    if s_x < 0:
        s_x = 0 
    elif s_x > width - 10:
        s_x = width - 10

    if s_y < 0:
        s_y = 0 
    elif s_y > height - 20:
        s_y = height - 20

    pygame.display.update()
#blit
    screen.blit(background, (0, 0))
    screen.blit(charactor, (s_x, s_y))
    screen.blit(bad, (b_s_x, b_s_y))
#blit

    print(get_time)

#무한반복
    if t_time - time < 0:
        b_s_x = random.randint(1, 901)
        b_s_y = random.randint(1, 725)
        start_ticks = pygame.time.get_ticks()
        time = (pygame.time.get_ticks() - start_ticks) / 1000
        get_time = t_time - time

pygame.quit()
#8/4 rect구하기