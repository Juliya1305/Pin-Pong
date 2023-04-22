#Создай собственный Шутер!
from pygame import *
from random import randint
from time import time as timer

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

    
        
window = display.set_mode((700, 500))
display.set_caption('Пин-Понг')

#задай фон сцены
#background = transform.scale(image.load('galaxy.jpg'), (700,500))

font.init()
font1 = font.Font(None, 30)
font2 = font.Font(None, 70)
win = font2.render('YOU WIN!', True, (255, 215, 0))
lose = font2.render('YOU LOSE!', True, (255, 0, 0))

count = 0
counts = font1.render('Счет:' + str(count), True, (255, 255, 255))

mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()

#fire = mixer.Sound('fire.ogg')
clock = time.Clock()

player = Player('left.png', 0, 250, 10, 90, 90)

run = True
finish = False

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

        if e.type == KEYDOWN:
            if e.key == K_SPACE and energy:
                player.fire()
                num_fire += 1
                if num_fire % 5 == 0:
                    energy = False
                    time1 =  timer()
            

    if finish != True: 
       # window.blit(background,(0, 0))

        player.reset()

        player.update_l()
        

        if  count >= 5:
            window.blit(win, (245, 250))
            finish = True

        
        counts = font1.render('Счет:' + str(count), True, (255, 255, 255))


        #sprites_list = sprite.spritecollide(player, monsters, False)
        #asteroid_list = sprite.spritecollide(player, asteroids, False)

        #sprites_list2  = sprites_list
        #asteroid_list2  = asteroid_list

        
        window.blit(counts,(0, 30))
        
    clock.tick(60)
    display.update()