import pygame as py
import math
WIDTH = 600
HEIGHT = 600
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption('Battleships')
py.display.set_icon(py.image.load('beam.png'))
running = True
# Scores


py.init()
py.font.init()
#Player1
image1 = py.image.load('spaceship2.png')
player_x = 32
player_y = 284
player_x_change = 0
player_y_change = 0
def Playerimg(x, y):
    screen.blit(image1, (x, y))

#Player2
image2 = py.image.load('ufo.png')
player2_x = 536
player2_y = 284
player2_x_change = 0
player2_y_change = 0
def Player2img(x, y):
    screen.blit(image2, (x, y))


#Bullet
image3 = py.image.load('bullet.png')
bullet_x = 364
bullet_y = 464
bulletx_change = 0.2
bullety_change = -0.2
bullet_state = "ready"
def bulletimg(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(image3, (x, y))
#Beam
image4 = py.image.load('beam.png')
beam_x = 536
beam_y = 284
beamx_change = 0.2
beamy_change = -0.2
beam_state = "ready"
def beamimg(x, y):
    global beam_state
    beam_state = "fire"
    screen.blit(image4, (x, y))


#collisiondetection

def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    if distance <= 27:
        return True
    else:
        return False


score1 = 0  # Player 1 (left)
score2 = 0  # Player 2 (right)

# Font for score display
font = py.font.Font(None, 36)  # Default font, size 36

def show_score():
    text1 = font.render(f"Player 1: {score1}", True, (255, 255, 255))
    text2 = font.render(f"Player 2: {score2}", True, (255, 255, 255))
    screen.blit(screen, text1, (10, 10))
    screen.blit(screen, text2, (WIDTH - text2.get_width() - 10, 10))

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type==py.KEYDOWN:         #KEYDOWN CHECK
            if event.key == py.K_w:
                player_y_change = -0.5
            if event.key == py.K_s:
                player_y_change = 0.5
            if event.key == py.K_a:
                player_x_change = -0.5
            if event.key == py.K_d:
                player_x_change = 0.5
            if event.key == py.K_UP:
                player2_y_change = -0.5
            if event.key == py.K_DOWN:
                player2_y_change = 0.5
            if event.key == py.K_LEFT:
                player2_x_change = -0.5
            if event.key == py.K_RIGHT:
                player2_x_change = 0.5
            if event.key == py.K_g:
                if bullet_state == "ready":
                    bullet_x = player_x
                    bullet_y = player_y
                    bulletimg(bullet_x, bullet_y)
            if event.key == py.K_l:
                if beam_state == "ready":
                    beam_x = player2_x
                    beam_y = player2_y
                    beamimg(beam_x, beam_y)
            
        if event.type==py.KEYUP:           #KEYUP CHECK
            if event.key == py.K_w:
                player_y_change =0
            if event.key == py.K_s:
                player_y_change = 0
            if event.key == py.K_a:
                player_x_change = 0
            if event.key == py.K_d:
                player_x_change =0
            if event.key == py.K_UP:
                player2_y_change =0
            if event.key == py.K_DOWN:
                player2_y_change = 0
            if event.key == py.K_LEFT:
                player2_x_change = 0
            if event.key == py.K_RIGHT:
                player2_x_change =0
    
    #BOUND CHECKS
    if player_x >= 258:
        player_x = 258
    if player_x <=0:
        player_x = 0
    if player_y >= 568:
        player_y = 568
    if player_y <= 0:
        player_y = 0
    if player2_x >= 568:
        player2_x = 568
    if player2_x <=310:
        player2_x = 310
    if player2_y >= 568:
        player2_y = 568
    if player2_y <= 0:
        player2_y = 0
        
    screen.fill((20, 80, 165))
    py.draw.rect(screen, (0,0,0), (290,0,20,600))
    Playerimg(player_x, player_y) 
    Player2img(player2_x,player2_y) 
    player_x += player_x_change
    player_y += player_y_change
    player2_x += player2_x_change
    player2_y += player2_y_change
    
    coll1 = isCollision(player2_x, player2_y, bullet_x, bullet_y)
    if coll1:
            bullet_y = player_y
            bullet_state = "ready"
            player2_x = 536
            player2_y = 284
            score1+=1
    coll2 = isCollision(player_x, player_y, beam_x, beam_y)
    if coll2:
            beam_y = beam_y
            beam_state = "ready"
            player_x = 32
            player_y = 284        
            score2+=1
    
    
    if bullet_state == "fire":
        bulletimg(bullet_x, bullet_y)
        bullet_x -= bullety_change
    if bullet_x >= 600:
        bullet_x = player_x
        bullet_state = "ready"
    if beam_state == "fire":
        beamimg(beam_x, beam_y)
        beam_x += beamy_change
    if beam_x <= 0:
        beam_x = player2_x
        beam_state = "ready"
    
    
    py.display.update()
            
