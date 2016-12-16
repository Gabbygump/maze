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
TITLE = "Hungry Piggy"
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

#images
img= pygame.image.load('splashscreen.jpg')
playerimg= pygame.image.load('player.png')
enemyimg= pygame.image.load ('enemy.png')
coinimg= pygame.image.load ('coin.png')
bottomright_switchimg= pygame.image.load ('switch.png')
topright_switchimg= pygame.image.load ('switch.png')
#Fonts
MY_FONT = pygame.font.Font(None, 50)

# stages
START = 0
PLAYING = 1
END = 2

def setup():
    global coins, stage,player,enemy,bottomright_doors,topright_doors,collidables,bottomright_switch,topright_switch,bottomright_doors_open,topright_doors_open
    coin1 = [58, 68, 25, 25]
    coin2 = [58, 157, 25, 25]
    coin3 = [58, 252, 25, 25]
    coin4 = [171,131,25,25]
    coin5 = [207,213,25,25]
    coin6 = [131,323,25,25]
    coin7 = [133,433,25,25]
    coin8 = [59,499,25,25]
    coin9 = [130,574,25,25]
    coin10 = [55,612,25,25]
    coin11 =[205,583,25,25]
    coin12 =[225,471,25,25]
    coin13=[285,401,25,25]
    coin14=[67,395,25,25]
    coin15=[214,362,25,25]
    coin16=[226,276,25,25]
    coin17=[301,185,25,25]
    coin18=[303,109,25,25]
    coin19=[224,56,25,25]
    coin20=[383,58,25,25]
    coin21=[462,101,25,25]
    coin22=[391,135,25,25]
    coin23=[459,174,25,25]
    coin24=[433,256,25,25]
    coin25=[537,262,25,25]
    coin26=[420,340,25,25]
    coin27=[541,387,25,25]
    coin28=[450,447,25,25]
    coin29=[359,515,25,25]
    coin30=[277,561,25,25]
    coin31=[272,635,25,25]
    coin32=[436,635,25,25]
    coin33=[430,551,25,25]
    coin34=[541,634,25,25]
    coin35=[535,499,25,25]
    coin36=[533,335,25,25]
    coin37=[361,374,25,25]
    coin38=[342,274,25,25]
    coin39=[661,554,25,25]
    coin40=[660,636,25,25]
    coin41=[712,524,25,25]
    coin42=[634,472,25,25]
    coin43=[630,399,25,25]
    coin44=[631,305,25,25]
    coin45=[714,234,25,25]
    coin46=[637,195,25,25]
    coin47=[622,104,25,25]
    coin48=[716,107,25,25]
    coin49=[660,55,25,25]
    coin50=[548,118,25,25]
    coin51=[545,53,25,25]
    coin52=[869,479,25,25]
    coin53=[791,468,25,25]
    coin54=[787,537,25,25]
    coin55=[927,570,25,25]
    coin56=[1006,634,25,25]
    coin57=[1049,558,25,25]
    coin58=[870,630,25,25]
    coin59=[1150,433,25,25]
    coin60=[948,404,25,25]
    coin61=[1179,630,25,25]
    coin62=[792,199,25,25]
    coin63=[851,185,25,25]
    coin64=[791,56,25,25]
    coin65=[891,48,25,25]
    coin66=[1030,57,25,25]
    coin67=[1044,163,25,25]
    coin68=[1143,114,25,25]
    coin69=[1137,238,25,25]
    coin70=[1206,331,25,25]
    coin71=[881,274,25,25]
    coin72=[953,329,25,25]
    coin73=[1029,272,25,25]
    coin74=[836,111,25,25]
    coin75=[1002,490,25,25]

    coins = [coin1, coin2, coin3,coin4,coin5,coin6,coin7,
             coin8,coin9,coin10,coin11,coin12,coin13,coin14,coin15,
             coin16,coin17,coin18,coin19,coin20,coin21,coin22,coin23,coin24,coin25,
             coin26,coin27,coin28,coin29,coin30,coin31,coin32,coin33,coin34,coin35,coin36,coin37,
             coin38,coin39,coin40,coin41,coin42,coin43,coin44,coin45,coin46,coin47,coin48,coin49,coin50,coin51,
             coin52,coin53,coin54,coin55,coin56,coin57,coin58,coin59,coin60,coin61,coin62,coin63,coin64,coin65,
             coin66,coin67,coin68,coin69,coin70,coin71,coin72,coin73,coin74,coin75]
    #make doors
    bottomright_door1 = [740, 520, 30, 60]
    bottomright_door2 = [830, 420, 70, 30]
    bottomright_doors = [bottomright_door1, bottomright_door2]
    
    #topright doors
    topright_door1 = [0, 300, 40, 80]
    topright_door2 = [770, 220,50,30]
    topright_door3 = [740, 130, 30, 30]
    topright_doors = [topright_door1, topright_door2 , topright_door3]
    
    # make switch
    bottomright_switch = [130, 636, 25, 25]
    topright_switch = [1146, 576,25, 25]

    #make collidables
    collidables = walls + bottomright_doors + topright_doors
    player =[748, 395, 25, 25]
    enemy =[756, 334, 25, 25]
    topright_doors_open = False
    bottomright_doors_open = False
    stage = START


# settings

player_speed = 5   
enemy_speed = 5

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
        if intersects.rect_rect(player, bottomright_switch):
            bottomright_doors_open = True
            collidables = [c for c in collidables if c not in bottomright_doors]

        if intersects.rect_rect(player, topright_switch):
            topright_doors_open = True
            collidables = [c for c in collidables if c not in topright_doors]
            
        '''get enemy'''
        if intersects.rect_rect(player,enemy):
            win = False
            stage = END
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(PURPLE)

    screen.blit(playerimg,(player[0], player[1]))

    screen.blit(enemyimg, (enemy[0], enemy[1]))
    
    for w in walls:
        pygame.draw.rect(screen, YELLOW, w)

    for c in coins:
        screen.blit(coinimg, (c[0], c[1]))

    screen.blit(bottomright_switchimg, (bottomright_switch[0],bottomright_switch[1]))
    screen.blit(topright_switchimg, (topright_switch[0],topright_switch[1]))
    
    if not bottomright_doors_open:
        for d in bottomright_doors:
            pygame.draw.rect(screen, YELLOW, d)
            
    if not topright_doors_open:
        for t in topright_doors:
            pygame.draw.rect(screen, YELLOW, t)
    ''' begin/end game text '''
    if stage == START:
        screen.blit(img,(0,0))
        text1 = MY_FONT.render("Hungry Pink Dot", True, BLUE)
        text2 = MY_FONT.render("(Press SPACE to play.)", True, BLUE)
        screen.blit(text1, [450, 300])
        screen.blit(text2, [430, 360])
    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, BLUE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, BLUE)
        screen.blit(text1, [500, 300])
        screen.blit(text2, [400, 360])
    
        if win:
            font = pygame.font.Font(None, 200)
            text = font.render("You Win!", 1, PINK)
            screen.blit(text, [310, 160])

        if win == False:
            font = pygame.font.Font(None, 200)
            text = font.render("You Lose!", 1, RED)
            screen.blit(text, [310, 160])
            
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
