# Imports
import pygame
import intersects
import math

# Initialize game engine
pygame.init()


# Window
WIDTH = 1250
HEIGHT = 700
SIZE = (WIDTH, HEIGHT)
TITLE = "The Hungry Pink Dot"
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
    global coins, stage,player,enemy,doors,topright_doors,collidables,switch,topright_switch,doors_open,topright_doors_open
    coin1 = [58, 68, 25, 25]
    coin2 = [58, 157, 25, 25]
    coin3 = [58, 252, 25, 25]
    coin4 = [58, 340, 25, 25]
    coin5 = [60, 463, 25, 25]
    coin6 = [299, 73, 25, 25]
    coin7 = [313, 195, 25, 25]
    coin8 = [514, 236, 25, 25]
    coin9 = [570, 55, 25, 25]
    coin10 = [713, 105, 25, 25]
    coin11 = [843, 94, 25, 25]
    coin12 = [904, 277, 25, 25]
    coin13 = [902, 334, 25, 25]
    coin14 = [999, 321, 25, 25]
    coin15 = [1001, 273, 25, 25]
    coin16 = [1142, 349, 25, 25]
    coin17 = [386, 356, 25, 25]
    coins = [coin1, coin2, coin3,coin4,coin5,
             coin6,coin7,coin8,coin9,coin10,coin11,coin12,coin13,coin14,
             coin15,coin16,coin17]
    #make doors
    door1 = [740, 520, 30, 60]
    door2 = [830, 420, 70, 30]
    doors = [door1, door2]
    #topright doors
    topright_door1 = [0, 300, 40, 80]
    topright_door2 = [770, 220,50,30]
    topright_door3 = [740, 130, 30, 30]
    topright_doors = [topright_door1, topright_door2 , topright_door3]
    # make switch
    switch = [130, 636, 25, 25]
    topright_switch = [1148, 586,25, 25]

    #make collidables
    collidables = walls + doors + topright_doors
    player =[748, 395, 25, 25]
    enemy =[756, 334, 25, 25]
    topright_doors_open = False
    doors_open = False
    stage = START


# settings

player_speed = 5   
enemy_speed = 6
# make walls
wall1 =  [0,660, 1350, 40]
wall2 =  [0,0, 1350, 40]
wall3 =  [0, 0, 40, 300]
wall4 = [0, 380, 40, 300]
wall5 = [1210, 0, 40, 300]
wall6 = [1210, 380, 40, 300]
wall7 = [90,80, 100, 30]
wall8 = [90, 80, 30, 100]
wall9 = [90,240, 100, 30]
wall10= [160, 240, 30, 150]
wall11 =[160,300, 100, 30]
wall12 =[90, 300, 30, 80]
wall13 =[90, 420, 30, 90]
wall14 =[90,480, 120, 30]
wall15 =[30,540, 80, 30]
wall16 =[90,600, 100, 30]
wall17 =[160, 540, 30, 90]
wall18 =[240, 90, 30, 170]
wall19 =[170,160, 100, 30]
wall20 =[240,230, 100, 30]
wall21 =[340, 680, 30, 90]
wall22 =[370, 230, 30, 170]
wall23 =[300,300, 100, 30]
wall24 =[390,370, 100, 30]
wall25 =[490, 820, 30, 90]
wall26 =[570, 360, 30, 170]
wall27=[490,425, 100, 30]
wall28 =[570,510, 100, 30]
wall29 =[230, 540, 30, 90]
wall30 =[230,600, 100, 30]
wall31 =[370, 540, 30, 90]
wall32 =[300,540, 100, 30]
wall33 =[250, 420, 30, 90]
wall34 =[160,420, 120, 30]
wall35 =[240,355, 100, 30]
wall36= [310, 355, 30, 150]
wall37 =[310,430, 100, 30]
wall38 =[380,485, 100, 30]
wall39= [460, 485, 30, 145]
wall40 =[460,565, 100, 30]
wall41 =[340, 90, 30, 90]
wall42 =[340, 160, 90, 30]
wall43 =[410, 90, 30, 30]
wall44 =[490, 290, 90, 30]
wall45 =[410, 90, 30, 30]
wall46 =[490, 40, 30, 90]
wall47 =[580, 90, 30, 170]
wall48 =[490,160, 100, 30]
wall49 =[580,230, 100, 30]
wall50 =[650, 90, 30, 30]
wall51 =[740, 40, 30, 90]
wall52 =[900, 80, 30, 170]
wall53 =[920,160, 100, 30]
wall54 =[820,220, 290, 30]
wall55 =[900, 370, 30, 170]
wall56 =[920,430, 100, 30]
wall57 =[820,510, 100, 30]
wall58 =[1080, 220, 30, 170]
wall59 =[1080,290, 100, 30]
wall60 =[920,370, 400, 30]
wall61 =[670,160,160,30]
wall62 =[740,160,30,100]
wall63 =[670,420,160,30]
wall64 =[740,420,30,100]
wall65 =[740, 580,30,90]
wall66 =[680,300,60,20]
wall67 =[784,300,40,20]
wall68 =[680,300,20,60]
wall69 =[820,300,20,60]
wall70 =[680,360,160,20]
wall71 =[650,590,30,30]
wall72 =[820,570,30,60]
wall73 =[820,570,90,30]
wall74 =[970,540,30,90]
wall75 =[970,600,90,30]
wall76 =[1100,540,30,90]
wall77 =[1100,600,120,30]
wall78 =[1100,540,80,30]
wall79 =[970,70,30,60]
wall80 =[970,100,90,30]
wall81 =[1100,80,30,90]
wall82 =[1100,140,120,30]
wall83 =[1100,80,80,30]
wall84 =[1090,460,30,30]
walls = [wall1, wall2,wall3,wall4,wall5,wall6,wall7,
         wall8,wall9,wall10,wall11,wall12,wall13,wall14,
         wall15,wall16,wall17,wall18,wall19,wall20,wall21,
         wall22,wall23,wall24,wall25,wall26,wall27,wall28,
         wall29,wall30,wall31,wall32,wall33,wall34,wall35,
         wall36,wall37,wall38,wall39,wall40,wall41,wall42,
         wall43,wall44,wall45,wall46,wall47,wall48,wall49,
         wall50,wall51,wall52,wall53,wall54,wall55,wall56,
         wall57,wall58,wall59,wall60,wall61,wall62,wall63,
         wall64,wall65,wall66,wall67,wall68,wall69,wall70,
         wall71,wall72,wall73,wall74,wall75,wall76,wall77,
         wall78,wall79,wall80,wall81,wall82,wall83,wall84]


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
        for c in collidables:
            if intersects.rect_rect(player, c):        
                if player_vx > 0:
                    player[0] = c[0] - player[2]
                elif player_vx < 0:
                    player[0] = c[0] + c[2]
            ''' resolve collisions horizontally '''
        for c in collidables:
            if intersects.rect_rect(enemy, c):        
                if enemy_vx > 0:
                    enemy[0] = c[0] - enemy[2]
                elif enemy_vx < 0:
                    enemy[0] = c[0] + c[2]

        ''' move the player in vertical direction '''
        player[1] += player_vy
        enemy[1] += enemy_vy
        ''' resolve collisions vertically '''
        for c in collidables:
            if intersects.rect_rect(player, c):                    
                if player_vy > 0:
                    player[1] = c[1] - player[3]
                if player_vy < 0:
                    player[1] = c[1] + c[3]

        ''' resolve collisions vertically '''
        for c in collidables:
            if intersects.rect_rect(enemy, c):                    
                if enemy_vy > 0:
                    enemy[1] = c[1] - enemy[3]
                if enemy_vy < 0:
                    enemy[1] = c[1] + c[3]

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

        ''' open door on switch contact '''
        if intersects.rect_rect(player, switch):
            doors_open = True
            collidables = [c for c in collidables if c not in doors]

        if intersects.rect_rect(player, topright_switch):
            topright_doors_open = True
            collidables = [c for c in collidables if c not in topright_doors]
            
        '''get enemy'''
        if intersects.rect_rect(player,enemy):
            win = False
            stage = END
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(PURPLE)

    pygame.draw.rect(screen, PINK, player)
    pygame.draw.rect(screen, RED, enemy)
    
    for w in walls:
        pygame.draw.rect(screen, YELLOW, w)

    for c in coins:
        pygame.draw.rect(screen, GREEN, c)

    pygame.draw.rect(screen, WHITE, switch)
    pygame.draw.rect(screen, WHITE, topright_switch)
    if not doors_open:
        for d in doors:
            pygame.draw.rect(screen, RED, d)
            
    if not topright_doors_open:
        for t in topright_doors:
            pygame.draw.rect(screen, BLUE, t)
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
