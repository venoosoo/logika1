from pygame import *

display.set_caption("My first geame")
screen = display.set_mode((700, 500))
background = transform.scale(image.load('download.png'), (700, 500))
yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)
class Card(sprite.Sprite):
    def __init__(self,width,height,x,y,color):
        self.rect = Rect(x,y,width,height)
        self.fill_color = color
    def draw(self):
        draw.rect(screen, self.fill_color, self.rect)

class Pic(sprite.Sprite):
    def __init__(self,width,height,x,y):
        self.image = transform.scale(image.load('sf-removebg-preview.png'), (width,height))
        self.x = x
        self.y = y
    def reset(self):
        screen.blit(self.image,(self.x,self.y))

player1 = Card(80,80,100,200,black)
player2 = Pic(100,100,500,200)
false = True
while false:
    time.delay(25)
    screen.blit(background,(0,0))
    player1.draw()
    player2.reset()
    for e in event.get():
        if e.type == QUIT:
            false = False
        if e.type == MOUSEBUTTONDOWN:
            false = False
        run = False
    display.update()