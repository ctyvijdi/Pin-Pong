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
Player1s = 0
Player2s = 0
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
        if keys_pressed[K_s] and self.rect.y < 550:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

class Sharic(Game_Sprite):
    
    def update(self):
        global Player1s
        global Player2s
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y > 615:
            self.speed_y *= -1
        if self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(Sharic,Player1) == True:
            self.speed_x = abs(self.speed_x)
        if sprite.collide_rect(Sharic,Player2) == True:
            self.speed_x = abs(self.speed_x)
            self.speed_x *= -1
        if self.rect.x > 900:
            Player1s += 1
            self.rect.x = 300 
            self.rect.y = 300
        if self.rect.x < -50:
            Player2s += 1
            self.rect.x = 300 
            self.rect.y = 300
            


font = font.Font(None, 70)
winP1 = font.render('Player1 was win!', True,(255, 0, 0))
winP2 = font.render('Player2 was win!', True,(0, 0, 255))

P1count = font.render('Score:', True,(255, 0, 0))
P2count = font.render('Score:', True,(0, 0, 255))

Sharic = Sharic(300,300,'sharic.png',5,100,100)
Player1 = Player(25,300,'red_palka.png',10,25,150)
Player2 = Player(750,300,'blue_palka.png',10,25,150)
while game:
    clock.tick(FPS)
    for e in event.get():
            if e.type == QUIT:
                game = False
    window.blit(bg,(0,0))
    window.blit(font.render(str(Player1s), True, (255, 0, 0)),(150, 0))
    window.blit(font.render(str(Player2s), True, (0, 0, 255)),(750, 0))            
    if finish != True:
        window.blit(P1count,(0, 0))
        window.blit(P2count,(600, 0))

        Sharic.update()
        Sharic.reset()

        Player1.update()
        Player1.reset()

        Player2.update1()
        Player2.reset()

    if Player1s >= 3:
        window.blit(winP1, (200, 300))
        finish = True
    if Player2s >= 3:
        window.blit(winP2, (200, 300))
        finish = True
    window.blit(P1count,(0, 0))
    window.blit(P2count,(600, 0))

    display.update()