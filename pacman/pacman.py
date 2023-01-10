import pygame
from board import boards
pygame.init()

WIDTH = 900
HEIGHT = 950
PI = 3.14
color = 'green'
screen = pygame.display.set_mode([WIDTH,HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf',20)
lvl = boards
player_x = 450
player_y = 663
player_images = []
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45)))
direction = 0
counter = 0
flicker = 0
#DASW
turns_allowed = (False,False,False,False)
direction_command = 0
player_speed = 2


def check_position(centerx, centery):
    turns = [False, False, False, False]
    Y = (HEIGHT - 50) // 32
    X = (WIDTH // 30)
    R = 14
    if centerx // 30 < 29:
        if direction == 0:
            if lvl[centery // Y][(centerx - R) // X] < 3:
                turns[1] = True
        if direction == 1:
            if lvl[centery // Y][(centerx + R) // X] < 3:
                turns[0] = True
        if direction == 2:
            if lvl[(centery + R) // Y][centerx // X] < 3:
                turns[3] = True
        if direction == 3:
            if lvl[(centery - R) // Y][centerx // X] < 3:
                turns[2] = True

        if direction == 2 or direction == 3:
            if 12 <= centerx % X <= 18:
                if lvl[(centery + R) // Y][centerx // X] < 3:
                    turns[3] = True
                if lvl[(centery - R) // Y][centerx // X] < 3:
                    turns[2] = True
            if 12 <= centery % Y <= 18:
                if lvl[centery // Y][(centerx - X) // X] < 3:
                    turns[1] = True
                if lvl[centery // Y][(centerx + X) // X] < 3:
                    turns[0] = True
        if direction == 0 or direction == 1:
            if 12 <= centerx % X <= 18:
                if lvl[(centery + Y) // Y][centerx // X] < 3:
                    turns[3] = True
                if lvl[(centery - Y) // Y][centerx // X] < 3:
                    turns[2] = True
            if 12 <= centery % Y <= 18:
                if lvl[centery // Y][(centerx - R) // X] < 3:
                    turns[1] = True
                if lvl[centery // Y][(centerx + R) // X] < 3:
                    turns[0] = True
    else:
        turns[0] = True
        turns[1] = True

    return turns


def draw_board(lvl):
    Y = ((HEIGHT - 50) // 32)
    X = (WIDTH // 30)
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            if lvl[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * X + (0.5 * X), i * Y + (0.5 * Y)), 4)
            if lvl[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, 'white', (j * X + (0.5 * X), i * Y + (0.5 * Y)), 10)
            if lvl[i][j] == 3:
                pygame.draw.line(screen, color, (j * X + (0.5 * X), i * Y),
                                 (j * X + (0.5 * X), i * Y + Y), 3)
            if lvl[i][j] == 4:
                pygame.draw.line(screen, color, (j * X, i * Y + (0.5 * Y)),
                                 (j * X + X, i * Y + (0.5 * Y)), 3)
            if lvl[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * X - (X * 0.4)) - 2, (i * Y + (0.5 * Y)), X, Y],
                                0, PI / 2, 3)
            if lvl[i][j] == 6:
                pygame.draw.arc(screen, color,
                                [(j * X + (X * 0.5)), (i * Y + (0.5 * Y)), X, Y], PI / 2, PI, 3)
            if lvl[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * X + (X * 0.5)), (i * Y - (0.4 * Y)), X, Y], PI,
                                3 * PI / 2, 3)
            if lvl[i][j] == 8:
                pygame.draw.arc(screen, color,
                                [(j * X - (X * 0.4)) - 2, (i * Y - (0.4 * Y)), X, Y], 3 * PI / 2,
                                2 * PI, 3)
            if lvl[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * X, i * Y + (0.5 * Y)),
                                 (j * X + X, i * Y + (0.5 * Y)), 3)


def draw_player():
    #DASW
    if direction == 0:
        screen.blit(player_images[counter // 5], (player_x, player_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))    
    
    if direction == 0:
        screen.blit(player_images[counter // 5], (player_x, player_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))


def move_player(player_x, player_y):
    # r, l, d, u
    if direction == 0 and turns_allowed[0]:
        player_x += player_speed
    elif direction == 1 and turns_allowed[1]:
        player_x -= player_speed
    if direction == 2 and turns_allowed[2]:
        player_y -= player_speed
    elif direction == 3 and turns_allowed[3]:
        player_y += player_speed
    return player_x, player_y

run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter += 1
        flicker = 0
    else:
        flicker = 1
        counter = 0
    screen.fill('black')
    draw_board(lvl)
    draw_player()

    center_x = player_x + 23
    center_y = player_y + 24
    turns_allowed = check_position(center_x,center_y) 
    player_x, player_y = move_player(player_x,player_y)
    print(player_x,player_y)
    if player_x > 900:
            player_x = -47
    elif player_x < -50:
            player_x = 897


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                direction_command = 0
            if event.key == pygame.K_a:
                direction_command = 1
            if event.key == pygame.K_w:
                direction_command = 2
            if event.key == pygame.K_s:
                direction_command = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d and direction_command == 0:
                direction_command = direction
            if event.key == pygame.K_a and direction_command == 1 :
                direction_command = direction
            if event.key == pygame.K_w and direction_command == 2:
                direction_command = direction
            if event.key == pygame.K_s and direction_command == 3:
                direction_command = direction

        for i in range(4):
            if direction_command == i and turns_allowed[i]:
                direction = i

    pygame.display.flip()
pygame.quit()