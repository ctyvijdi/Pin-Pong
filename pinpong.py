from pygame import *

mixer.init()
font.init()

#mixer.music.load('space.ogg')
#kick = mixer.Sound("fire.ogg")
window = display.set_mode((800,700))
display.set_caption('PinPong')
bg = transform.scale(image.load('filld.jpg'),(800,700))
game = True
clock = time.Clock()
FPS = 120
finish = False
a = 0
b = 0
font2 = font.SysFont('calibri',36)
#!
class Game_Sprite(sprite.Sprite):
    def __init__(self,x,y,name,speed,waith,heigth):
        super().__init__()
        self.image = transform.scale(image.load(name),(waith,heigth))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = speed
        self.speed_x = speed

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    

class Player(Game_Sprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > -50:
            self.rect.y -= self.speed
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > -50:
            self.rect.y -= self.speed

class Sharic(Game_Sprite):
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y >= 625:
            self.speed_y = -self.speed_y
        if self.rect.y <= 100:
            self.speed_y = -self.speed_y
        if   
        



Sharic = Sharic(300,300,'sharic.png',1,100,100)
Player1 = Player(-85,300,'red_palka.png',10,300,300)
Player2 = Player(600,300,'blue_palka.png',10,300,300)
while game:
    clock.tick(FPS)
    for e in event.get():
            if e.type == QUIT:
                game = False
    if finish != True:
        window.blit(bg,(0,0))

        Sharic.update()
        Sharic.reset()

        Player1.update()
        Player1.reset()

        Player2.update1()
        Player2.reset()


    display.update()