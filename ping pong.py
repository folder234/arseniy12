from pygame import *


'''class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed =player_speed
        self.rect = self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -=self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 88:
            self.rect.x += self.speed
    def fire(self):
        bullet=Bullet(img_bullet,self.rect.centerx,self.rect.top,15,20,-15)
        bullets.add(bullet)'''




win_width=700
win_height=500
window = display.set_mode((win_width, win_height))
display.set_caption("ping pong")
background=transform.scale(image.load("fon.jpg"),(win_width,win_height))
clock=time.Clock()
FPS=60
game = True
while game:
    for e in event.get():
        if e.type==QUIT:
            game = False
img.ball="ball.png"
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed =player_speed
        self.rect = self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -=self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 88:
            self.rect.x += self.speed
    def fire(self):
        bullet=Bullet(img.ball,self.rect.centerx,self.rect.top,15,20,-15)
        bullets.add(bullet)

    window.blit(background,(0,0))
    display.update()
    clock.tick(FPS)

    
    