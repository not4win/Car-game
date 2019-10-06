import pygame
import time
import random
pygame.init()
display_width=600 #width of the screen display
display_height=1000 #height of the screen display
black=(0,0,0) #RGB values are 0 as darkest shades correspond to value 0
white=(255,255,255) #RGB values are 0 as white shades correspond to value 255
red=(255,0,0)

carImg=pygame.image.load('game.png') #load the car image
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('yolo')
clock=pygame.time.Clock()

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def things_dodged(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Dodged"+str(count),True,black)
    gameDisplay.blit(text,(0,0))
def text_objects(text,font):
    textSurface=font.render(text,True,red)
    return textSurface,textSurface.get_rect()

def message_display(text): #to display the message
    largeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
def crash():
    message_display('YOU CRASHED')
def game_loop():
    x=(display_width *0.45)
    y=(display_height *0.45)
    x_change=0
    thing_startx=random.randrange(0,display_width)
    thing_starty=-600
    thing_speed=7
    thing_width=50
    thing_height=50
    dodged=0
    crashed=False
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change= 5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
        x += x_change    
        gameDisplay.fill(white)
        things(thing_startx,thing_starty,thing_width,thing_height,black)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        if x > display_width-194 or x < 0:
            crash()
        if thing_starty > display_height:
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged*1.2)

        if y<thing_starty+thing_height:
            print('y crossover')
            if x> thing_startx and x<thing_startx + thing_width or x+75 > thing_startx and x+75<thing_startx+thing_width :
                print('x crossover')
                crash()
        pygame.display.update()
        clock.tick(30)
game_loop()
pygame.quit()
quit()
