
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, player_x, player_y, speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (wight, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update_l(self):
        key_pressed = key.get_pressed()
        
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if key_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
    
    def update_r(self):
        key_pressed = key.get_pressed()
        
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if key_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

class Ball(GameSprite):
    global count1
    global count2

    def update(self):
        if self.rect.x == 0:
            self.speed = self.speed *(-1)
            count2 += 1
        
        if self.rect.x == 600:
            self.speed = self.speed *(-1)
            count1 += 1
    
        if self.rect.y == 0 or self.rect.y == 700:
            self.speed = self.speed *(-1) 
        
window = display.set_mode((700, 750))
display.set_caption('Пин-Понг')

#задай фон сцены
background = transform.scale(image.load('background.png'), (700,750))

font.init()
font1 = font.Font(None, 30)
font2 = font.Font(None, 70)
win = font2.render('YOU WIN!', True, (255, 215, 0))
lose = font2.render('YOU LOSE!', True, (255, 0, 0))

count1 = 0
count2 = 0
counts = font1.render('Счет: ' + str(count1) + ' : ' + str(count2), True, (255, 255, 255))

clock = time.Clock()

player1 = Player('left.png', 0, 250, 10, 50, 250)
player2 = Player('right.png', 650, 250, 10, 50, 250)
ball = Ball('ball.png', 325, 340, 5, 100, 100)

players = sprite.Group()
players.add(player1)
players.add(player2)

run = True
finish = False
list_player1 = list()
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True: 
        window.blit(background,(0, 0))

        player1.reset()
        player2.reset()
        ball.reset()

        player1.update_l()
        player2.update_r()
        ball.update()

        ball.rect.x += ball.speed
        ball.rect.y += ball.speed

        if  count1 or count2 >= 5:
            window.blit(win, (245, 250))
            finish = True
        
        list_player = len(list_player1)
        list_player1 = sprite.spritecollide(ball, players, False)
        
        if len(list_player1) - list_player >= 1:
            ball.speed = ball.speed * (-1)
            
        counts = font1.render('Счет: ' + str(count1) + ' : ' + str(count2), True, (255, 255, 255))

        window.blit(counts,(0, 30))
        
    clock.tick(60)
    display.update()