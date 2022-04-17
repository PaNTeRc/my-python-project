#create a Maze game!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < a - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < b - 80:
            self.rect.y += self.speed


class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= a -85:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite) :
    def __init__(self,r,g,b,x,y,w,h):
        super().__init__()
        self.color=r,g,b
        self.width=w
        self.height=h
        self.image=Surface((self.width,self.height))
        self.image.fill(self.color)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

wall1=Wall(200,0,0,450,350,150,20)
wall2=Wall(200,0,0,150,210,900,20)          
wall3=Wall(200,0,0,150,210,20,200)
wall4=Wall(200,0,0,250,370,20,200)
wall5=Wall(200,0,0,450,350,20,150)
wall6=Wall(200,0,0,350,210,20,200)
a=700
b=500
window = display.set_mode((700,500))
display.set_caption("Maze")
player = Player("hero.png",5,b - 100,5)
enemy = Enemy("cyborg.png",600,b - 220,3)
treasure = GameSprite("treasure.png",600,b - 100,0)
background = transform.scale(image.load("background.jpg"),(a,b))

clock = time.Clock()
fps = 60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

game = True
finish=False
font.init()
font=font.Font(None,70)
win=font.render('YOU WIN!',True,(255,215,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        player.reset()
        enemy.reset()
        treasure.reset()
        player.update()
        enemy.update()
        clock.tick(fps)
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        if sprite.collide_rect(player, treasure) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6):
            finish=True
            mixer.music.load('money.ogg')
            mixer.music.play()

    display.update()