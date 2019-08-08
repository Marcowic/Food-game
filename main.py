import pygame,sys,time,random
from pygame.locals import *

#CREATE THE FUNCTIONS
def terminate():
    pygame.quit()
    sys.exit()

def Player_Press_Key():
    while True:
        for event in pygame.event.get():

            if event.type==KEYDOWN:
                return

def drawText(text,font,surface,x,y):
    textobj=font.render(text,1,TEXTCOLOUR)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

#SET UP THE COLOURS
BLACK=(0,0,0)
WHITE=(255,255,255)
TEXTCOLOUR=(255,255,255)
BACKGROUNDCOLOUR=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)


#SET UP THE  VARIABLES (PLAYER MOVEMENT,WINDOW SIZE, ETC.)
move_Left=False
move_Right=False
move_Down=False
move_Up=False
direction='right'
direction2='right'
direction3='right'
direction4='right'
V_direction='down'
V_direction2='down'
V_direction3='down'
V_direction4='down'


Player_Move_Speed=3
Move_Speed=4
Lives_Left=3
FPS=60
Window_Height=500
Window_Width=500

#SET UP PYGAME
pygame.init()
mainClock=pygame.time.Clock()

#SET UP THE WINDOW
window_Surface=pygame.display.set_mode((Window_Width,Window_Height))
pygame.display.set_caption("Food Game")

#SET UP THE FONTS
font=pygame.font.SysFont(None,48)
font2=pygame.font.SysFont(None,30)

#SHOW THE "START" SCREEN (IMPORTANT)
drawText('Welcome',font,window_Surface,(175),(0))
drawText('Press any key to start!',font,window_Surface,(70),(450))
drawText("-Use the arrow keys or 'wasd' to move.",font2,window_Surface,(0),(100))
drawText("-Collect all the green blocks to earn points.",font2,window_Surface,(0),(150))
drawText("-Avoid touching the red blocks.",font2,window_Surface,(0),(200))
drawText("-Have Fun.",font2,window_Surface,(0),(250))
pygame.display.update()
Player_Press_Key()

#CREATING THE OBJECTS
player=pygame.Rect(240,240,30,30)
Danger_block=pygame.Rect(360,95,70,10)
Danger_block2=pygame.Rect(0,195,70,10)
Danger_block3=pygame.Rect(430,295,70,10)
Danger_block4=pygame.Rect(220,395,70,10)
V_Danger_block=pygame.Rect(95,120,10,70)
V_Danger_block2=pygame.Rect(195,430,10,70)
V_Danger_block3=pygame.Rect(295,220,10,70)
V_Danger_block4=pygame.Rect(395,0,10,70)

#CREATING THE FOOD
food=[]
for count in range(25):
    x=random.randint(1,480)
    y=random.randint(1,480)
    block=pygame.Rect(x,y,20,20)
    food.append(block)

for block in food:
    pygame.draw.rect(window_Surface,GREEN,block)

#DRAW THE WINDOW ONTO THE SCREEN
pygame.display.update()

score=0
top_Score=0

#SET UP THE MUSIC
gameOver_Sound=pygame.mixer.Sound('gameover.wav')
score_Sound=pygame.mixer.Sound('score.wav')
congratulations_Sound=pygame.mixer.Sound('Congratulations Sound.wav')
pygame.mixer.music.load('Background.wav')
pygame.mixer.music.play(-1,0.0)
music_Playing=True

#MAIN GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
        #ASSIGNING THE KEYS
            if event.key == K_LEFT or event.key == ord('a'):
                move_Right = False
                move_Left = True
            if event.key == K_RIGHT or event.key == ord('d'):
                move_Left = False
                move_Right = True
            if event.key == K_UP or event.key == ord('w'):
                move_Down = False
                move_Up = True
            if event.key == K_DOWN or event.key == ord('s'):
                move_Up = False
                move_Down = True
            if event.key == ord('m'):
                if music_Playing==True:
                    pygame.mixer.music.stop()
                    music_Playing=False
                elif music_Playing==False:
                    pygame.mixer.music.play()
                    music_Playing=True

        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == ord('a'):
                move_Left = False
            if event.key == K_RIGHT or event.key == ord('d'):
                move_Right = False
            if event.key == K_UP or event.key == ord('w'):
                move_Up = False
            if event.key == K_DOWN or event.key == ord('s'):
                move_Down = False

    #MOVEMENT IN ALL DIRECTIONS
    if move_Down and player.bottom < Window_Height:
            player.bottom += Player_Move_Speed
    if move_Up and player.top > 0:
            player.top -= Player_Move_Speed
    if move_Left and player.left > 0:
            player.left = player.left - Player_Move_Speed
    if move_Right and player.right < Window_Width:
            player.right = player.right + Player_Move_Speed

    #HORIZONTALLY MOVING DANGER BLOCKS
    if direction == 'right':
        Danger_block.left=Danger_block.left +Move_Speed
        if Danger_block.left >=430:
            direction = 'left'
    if direction == 'left':
        Danger_block.left=Danger_block.left -Move_Speed
        if Danger_block.left<=0:
            direction='right'
    if direction2 == 'right':
        Danger_block2.left=Danger_block2.left +Move_Speed
        if Danger_block2.left >=430:
            direction2 = 'left'
    if direction2 == 'left':
        Danger_block2.left=Danger_block2.left -Move_Speed
        if Danger_block2.left<=0:
            direction2='right'
    if direction3 == 'right':
        Danger_block3.left=Danger_block3.left +Move_Speed
        if Danger_block3.left >=430:
            direction3 = 'left'
    if direction3 == 'left':
        Danger_block3.left=Danger_block3.left -Move_Speed
        if Danger_block3.left<=0:
            direction3='right'
    if direction4 == 'right':
        Danger_block4.left=Danger_block4.left +Move_Speed
        if Danger_block4.left >=430:
            direction4 = 'left'
    if direction4 == 'left':
        Danger_block4.left=Danger_block4.left -Move_Speed
        if Danger_block4.left<=0:
            direction4='right'

    #VERTICALLY MOVING DANGER BLOCKS
    if V_direction == 'down':
        V_Danger_block.top=V_Danger_block.top +Move_Speed
        if V_Danger_block.top >= 430:
            V_direction='up'
    if V_direction == 'up':
        V_Danger_block.top=V_Danger_block.top -Move_Speed
        if V_Danger_block.top <= 0:
            V_direction = 'down'
    if V_direction2 == 'down':
        V_Danger_block2.top=V_Danger_block2.top +Move_Speed
        if V_Danger_block2.top >= 430:
            V_direction2='up'
    if V_direction2 == 'up':
        V_Danger_block2.top=V_Danger_block2.top -Move_Speed
        if V_Danger_block2.top <= 0:
            V_direction2 = 'down'
    if V_direction3 == 'down':
        V_Danger_block3.top=V_Danger_block3.top +Move_Speed
        if V_Danger_block3.top >= 430:
            V_direction3='up'
    if V_direction3 == 'up':
        V_Danger_block3.top=V_Danger_block3.top -Move_Speed
        if V_Danger_block3.top <= 0:
            V_direction3 = 'down'
    if V_direction4 == 'down':
        V_Danger_block4.top=V_Danger_block4.top +Move_Speed
        if V_Danger_block4.top >= 430:
            V_direction4='up'
    if V_direction4 == 'up':
        V_Danger_block4.top=V_Danger_block4.top -Move_Speed
        if V_Danger_block4.top <= 0:
            V_direction4 = 'down'

    #DRAW THE BACKGROUND ONTO THE SCREEN
    window_Surface.fill(BACKGROUNDCOLOUR)



    #DRAW THE SCORE
    drawText('Score: %s' % (score),font,window_Surface,10,0)

    #DRAW THE LIVES
    drawText('Lives Left:%s'%(Lives_Left),font,window_Surface,300,0)

    #Drawing the food
    for block in food:                                      #Loop 25 Times
        if player.colliderect(block):                       #Conditon if the "player" object collides with the object "block" object (proves True)
            food.remove(block)                              #The specific block which has collided with the player will be removed from the list and not drawn onto the window anymore
            score=score+1                                   #The score counter is increased by 1        READ:::::Win Condition:::::
            score_Sound.play()                              #A specific sound will play
        else:                                               #If no "block" object has collided with the player
            pygame.draw.rect(window_Surface,GREEN,block)    #Keep drawing all the "block" objects in the list (food)

    #IF THE PLAYER OVERLAP ANY OF THE DANGER BLOCKS/OBJECTS(GAME OVER)
    if player.colliderect(Danger_block) or player.colliderect(Danger_block2) or player.colliderect(Danger_block3) or player.colliderect(Danger_block4) or player.colliderect(V_Danger_block) or player.colliderect(V_Danger_block2) or player.colliderect(V_Danger_block3) or player.colliderect(V_Danger_block4):
        window_Surface.fill(BACKGROUNDCOLOUR)
        Lives_Left=Lives_Left-1
        if Lives_Left==0:
            drawText("GAME OVER-YOU LOST",font,window_Surface,(60),(100))
            drawText('Your Final Score is: %s' %(score),font,window_Surface,(85),(200))
            drawText('Press any key to quit.',font,window_Surface,(85),(300))
            pygame.mixer.music.stop()
            pygame.display.update()
            gameOver_Sound.play()
            Player_Press_Key()
            terminate()

    #DRAW THE PLAYER&DANGER OBJECTS ONTO THE SURFACE
    pygame.draw.rect(window_Surface,BLUE,player)
    pygame.draw.rect(window_Surface,RED,Danger_block)
    pygame.draw.rect(window_Surface,RED,Danger_block2)
    pygame.draw.rect(window_Surface,RED,Danger_block3)
    pygame.draw.rect(window_Surface,RED,Danger_block4)
    pygame.draw.rect(window_Surface,RED,V_Danger_block)
    pygame.draw.rect(window_Surface,RED,V_Danger_block2)
    pygame.draw.rect(window_Surface,RED,V_Danger_block3)
    pygame.draw.rect(window_Surface,RED,V_Danger_block4)

    #RENDER THE window_Surface OBJECT
    pygame.display.update()

    #WIN CONDITON
    if score==25:
        window_Surface.fill(BACKGROUNDCOLOUR)
        drawText("YOU WIN!",font,window_Surface,(170),(100))
        drawText("You have collected",font,window_Surface,(90),(200))
        drawText("all the green blocks!",font,window_Surface,(90),(250))
        drawText("Press any key to exit",font,window_Surface,(80),(400))
        pygame.mixer.music.stop()
        congratulations_Sound.play()
        pygame.display.update()
        Player_Press_Key()
        terminate()

    mainClock.tick(FPS)

