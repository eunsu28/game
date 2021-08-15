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
character = pygame.image.load("img/c.jpg")
bad = pygame.image.load("img/bad.png")
gameover = pygame.image.load("img/gameover.png")
#

# 캐릭터 설정
s_x = width / 2 #starting x position
s_y = 400 # y position 
x = 0
y = 0
#

# 장애물 설정
b_s_x = random.randint(1, 1001)
b_s_y = random.randint(1, 751)

b_s_x2 = random.randint(1, 1001)
b_s_y2 = random.randint(1, 751)
#

# 시간 설정
t_time = 2
start_ticks = pygame.time.get_ticks()
#

running = True
run = True
while run:

    time = (pygame.time.get_ticks() - start_ticks) / 1000
    get_time = t_time - time

    dt = clock.tick(60) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
        
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

#rect
    c_r = character.get_rect()
    c_r.left = s_x
    c_r.top = s_y

    b_r = bad.get_rect()
    b_r.left = b_s_x 
    b_r.top = b_s_y

    b_r2 = bad.get_rect()
    b_r2.left = b_s_x2 
    b_r2.top = b_s_y2
#rect

#충돌
    if c_r.colliderect(b_r):
        print("1번에 충돌했어요^^")
        screen.blit(gameover, (0, 0))
        running = False

    if c_r.colliderect(b_r2):
        print("2번에 충돌했어요^^")
        screen.blit(gameover, (0, 0))
        running = False
#충돌

    pygame.display.update()
#blit
    screen.blit(background, (0, 0))
    screen.blit(character, (s_x, s_y))
    screen.blit(bad, (b_s_x, b_s_y))
    screen.blit(bad, (b_s_x2, b_s_y2))
#blit

#무한반복
    if t_time - time < 0:
        b_s_x = random.randint(1, 901)
        b_s_y = random.randint(1, 725)
        b_s_x2 = random.randint(1, 1001)
        b_s_y2 = random.randint(1, 751)
        start_ticks = pygame.time.get_ticks()
        time = (pygame.time.get_ticks() - start_ticks) / 1000
        get_time = t_time - time
#

#replaying
    if running == False:
        pygame.time.delay(1000)
        b_s_x = random.randint(1, 901)
        b_s_y = random.randint(1, 725)
        b_s_x2 = random.randint(1, 1001)
        b_s_y2 = random.randint(1, 751)
        s_x = width / 2 #starting x position
        s_y = 400 # y position 
        start_ticks = pygame.time.get_ticks()
        time = (pygame.time.get_ticks() - start_ticks) / 1000
        get_time = t_time - time
        print("replay")
        running = True

pygame.quit()
#8/4 rect구하기