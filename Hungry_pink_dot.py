# Imports
import pygame
import intersects
import math

# Initialize game engine
pygame.init()


# Window
WIDTH = 1200
HEIGHT = 700
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 198, 0)
GREEN = (153, 255, 0)
PURPLE = (64,0,128)
PINK = (255, 149, 213)
BLUE = (22,64, 252)

#Fonts
MY_FONT = pygame.font.Font(None, 50)

# stages
START = 0
PLAYING = 1
END = 2

def setup():
    global coins, stage
    coin1 = [680, 232, 25, 25]
    coin2 = [950, 330, 25, 25]
    coin3 = [200, 400, 25, 25]
    coin4 = [320, 541, 25, 25]
    coin5 = [535, 221, 25, 25]
    coin6 = [575, 603, 25, 25]
    coin7 = [552, 490, 25, 25]
    coin8 = [1029, 598, 25, 25]
    coin9 = [1107, 112, 25, 25]
    coin10 = [288, 211, 25, 25]
    coin11 = [97, 143, 25, 25]
    coin12 = [97, 494, 25, 25]
    coin13 = [1084, 324, 25, 25]
    coin14 = [845, 460, 25, 25]
    coin15 = [907, 602, 25, 25]
    coin16 = [906, 75, 25, 25]
    coin17 = [386, 356, 25, 25]
    coins = [coin1, coin2, coin3,coin4,coin5,
             coin6,coin7,coin8,coin9,coin10,coin11,coin12,coin13,coin14,
             coin15,coin16,coin17]    

    stage = START


# Make a player
player =  [200, 150, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# Make enemy
enemy =[500, 150, 25, 25]
enemy_vx = 0
enemy_vy = 0
enemy_speed = 6

# make walls
wall1 =  [0,640, 1200, 60]
wall2 =  [0,0, 1200, 60]
wall3 =  [0, 0, 60, 300]
wall4 =  [0, 350, 60, 300]
wall5 =  [1140, 0, 60, 300]
wall6 =  [1140, 350, 60, 300]
wall7 =  [130, 120, 50, 200]
wall8 =  [130, 100, 200, 50]
wall9 =  [130, 400, 50, 180]
wall10 = [260, 290, 50, 200]
wall11 = [260, 280, 200, 50]
wall12 = [410, 100, 50, 200]
wall13 = [360, 400, 50, 400]
wall14 = [220,580, 170, 60]
wall15 = [470,525, 170, 50]
wall16 = [470,400, 180, 50]
wall17 = [600, 100, 50, 340]
wall18 = [750, 100, 50, 150]
wall19 = [750, 300, 50, 150]
wall20 = [750, 500, 50, 150]
wall21 = [880, 380, 50, 200]
wall22 = [880, 100, 50, 200]
wall23 = [1000, 150, 50, 400]

walls = [wall1, wall2, wall3,wall4,
         wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,
         wall14,wall15,wall16,wall17,wall18,wall19,
         wall20,wall21,wall22,wall23]



# Game loop
win = False
done = False
setup()
while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            print (event.pos)
        if event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()

    if stage == PLAYING:
        pressed = pygame.key.get_pressed()

        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]

        if up:
            player_vy = -player_speed
        elif down:
            player_vy = player_speed
        else:
            player_vy = 0
            
        if left:
            player_vx = -player_speed
        elif right:
            player_vx = player_speed
        else:
            player_vx = 0

    if stage == PLAYING:
        pressed = pygame.key.get_pressed()

        up = pressed[pygame.K_e]
        down = pressed[pygame.K_d]
        left = pressed[pygame.K_s]
        right = pressed[pygame.K_f]

        if up:
            enemy_vy = -enemy_speed
        elif down:
           enemy_vy = enemy_speed
        else:
            enemy_vy = 0
            
        if left:
            enemy_vx = -enemy_speed
        elif right:
            enemy_vx = enemy_speed
        else:
            enemy_vx = 0


        
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING :
        ''' move the player and enemy in horizontal direction '''
        player[0] += player_vx
        enemy[0] += enemy_vx
        ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]
            ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(enemy, w):        
                if enemy_vx > 0:
                    enemy[0] = w[0] - enemy[2]
                elif enemy_vx < 0:
                    enemy[0] = w[0] + w[2]

        ''' move the player in vertical direction '''
        player[1] += player_vy
        enemy[1] += enemy_vy
        ''' resolve collisions vertically '''
        for w in walls:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]

        ''' resolve collisions vertically '''
        for w in walls:
            if intersects.rect_rect(enemy, w):                    
                if enemy_vy > 0:
                    enemy[1] = w[1] - enemy[3]
                if enemy_vy < 0:
                    enemy[1] = w[1] + w[3]

        ''' here is where you should resolve player collisions with screen edges '''
        if player[1] + player[3] < 0:
                player[1] = HEIGHT
        elif player[1] > HEIGHT:
                player[1] = 0 -player[3]

        if player[0] > WIDTH:
                player[0] = 0 - player[2]
        elif player[0] + player[2] < 0:
                player[0] = WIDTH

        ''' here is where you should resolve player collisions with screen edges '''
        if enemy[1] + enemy[3] < 0:
                enemy[1] = HEIGHT
        elif enemy[1] > HEIGHT:
                player[1] = 0 -player[3]

        if enemy[0] > WIDTH:
                enemy[0] = 0 - enemy[2]
        elif enemy[0] + enemy[2] < 0:
                enemy[0] = WIDTH
            
        

        ''' get the coins '''
        coins = [c for c in coins if not intersects.rect_rect(player, c)]

        if len(coins) == 0:
            win = True
            stage = END
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(PURPLE)

    pygame.draw.rect(screen, PINK, player)
    pygame.draw.rect(screen, RED, enemy)
    
    for w in walls:
        pygame.draw.rect(screen, YELLOW, w)

    for c in coins:
        pygame.draw.rect(screen, GREEN, c)

    ''' begin/end game text '''
    if stage == START:
        text1 = MY_FONT.render("Hungry Pink Dot", True, BLUE)
        text2 = MY_FONT.render("(Press SPACE to play.)", True, BLUE)
        screen.blit(text1, [450, 300])
        screen.blit(text2, [430, 360])
    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, BLUE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, BLUE)
        screen.blit(text1, [490, 300])
        screen.blit(text2, [400, 360])



    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
