import pygame
import time

pygame.init()

clock = pygame.time.Clock()
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
car_width = 150
carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('wedgie.ttf',80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

driving = True

def crash(state):
    message_display('You Crashed')
    pygame.time.wait(1000)
    print "debug crashed"
    return state


def game_loop(state):
    x =  (display_width * 0.4)
    y = (display_height * 0.45)
    x_change = 0
    print "debug loop"

    while state:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print "debug eventquit"
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    print "debug left"
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        car(x,y)

        if x > display_width - car_width or x < 0:
            print "debug crash initiation"
            crash(state)

        pygame.display.update()
        clock.tick(60)

game_loop(driving)
pygame.quit()
quit()