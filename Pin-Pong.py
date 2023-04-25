from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, player_x, player_y, speed_x, speed_y, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (wight, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y

        if key_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed_y
    
    def update_r(self):
        key_pressed = key.get_pressed()
        
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y

        if key_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed_y

class Ball(GameSprite):

    def update(self):
        global count1
        global count2

        
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y
        if sprite.collide_rect(ball, player1):
            self.speed_x *= -1

        if sprite.collide_rect(ball, player2):
            self.speed_x *= -1

        if self.rect.x <= 0:
            self.speed_x *= -1
            count2 += 1
        
        if self.rect.x >= 500:
            self.speed_x *= -1
            count1 += 1
    
        if self.rect.y == 0 or self.rect.y == 500:
            self.speed_y *= -1
        
window = display.set_mode((600, 600))
display.set_caption('Пин-Понг')

#задай фон сцены
background = transform.scale(image.load('background.png'), (600,600))

font.init()
font1 = font.SysFont('Arial', 30)
font2 = font.SysFont('Arial', 70)

win1 = font2.render('Player1 win!', True, (255, 215, 0))
win2 = font2.render('Player2 win!', True, (255, 215, 0))

count1 = 0
count2 = 0
counts = font1.render('Счет: ' + str(count1) + ' : ' + str(count2), True, (255, 255, 255))

clock = time.Clock()

player1 = Player('left.png', 0, 250, 10, 10, 50, 200)
player2 = Player('right.png', 550, 250, 10, 10, 50, 200)
ball = Ball('ball.png', 325, 340, 5, 5,100, 100)

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

        

        if count1 >= 5:
            window.blit(win1,(120, 250))
            finish = True
        
        if count2 >= 5:
            window.blit(win2,(120, 250))
            finish = True
        

        counts = font1.render('Счет: ' + str(count1) + ' : ' + str(count2), True, (255, 255, 255))

        window.blit(counts,(0, 30))
        
    clock.tick(60)
    display.update()
