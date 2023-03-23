from pygame import *
from random import randint
from time import time as timer
life = 3 
lost = 0
maxl = 10
score = 0
goal = 10
rel = False
nuf = 0
font.init()
font2 = font.Font(None,36)
win = font2.render('YOU WIN!', True, (255, 255, 255))
lose = font2.render('YOU LOSE!', True, (180, 0, 0))


class useless(sprite.Sprite):
    
    def __init__(self,ima,x,y,w,h,speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(ima),(w,h))
        self.h = h
        self.w = w
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def undissepear(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class player(useless):
    
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x >= 10 :
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x <= 690:
            self.rect.x += self.speed
    
    def fire(self):
        bullet = rocket("bullet.png",self.rect.centerx,self.rect.top,10,10,-5)
        bull.add(bullet)

class Enemy(useless):
    
    def update(self):
        self.rect.y += self.speed
        global lost
        
        if self.rect.y > h:
            self.rect.x = randint(80,h-80)
            self.rect.y = 0
            lost += 1

class rocket(useless):
    
    def update(self):
        self.rect.y += self.speed
        
        if self.rect.y < 0:
            self.kill()
    
    



mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fires = mixer.Sound("fire.ogg")

w = 700
h = 500

window = display.set_mode((w,h))
display.set_caption("jet go brrrr")
back = transform.scale(image.load("background.jpg"),(w,h))

Game = False
finish = False
clock = time.Clock()
fps = 60

enemy = sprite.Group()
bull = sprite.Group()
asti = sprite.Group()

for i in range(3):
    ast = Enemy("asteroid.png",randint(80,h-80),40,70,70,randint(1,5))
    asti.add(ast)

jet = player("jet.png",300,440,50,55,20)

for i in range(5):
    ene = Enemy("ufo.png",randint(80,h-80),40,50,50,randint(1,3))
    enemy.add(ene)
    
while Game == False:
    
    for j in event.get():
        
        if j.type == QUIT:
            Game = True
        
        elif j.type == KEYDOWN:
            
            if j.key == K_SPACE:
                
                if nuf < 5 and rel == False:
                    jet.fire()
                    nuf += 1
                    fires.play()
            
            if nuf >= 5 and rel == False:
                rel = True
                last = timer()
    
    if not finish:
        
        collide = (sprite.groupcollide(enemy,bull,True,True))
        
        window.blit(back,(0,0))
        
        if rel == True :
            now = timer()
            if now - last < 3:
                relo = font2.render("Reloding.Cover me!",1,(255,0,0))
                window.blit(relo,(200,450))
            else:
                nuf = 0
                rel = False
        

        for c in collide:
            score += 1
            ene = Enemy("ufo.png",randint(80,w-80),40,50,50,randint(1,3))
            enemy.add(ene)
        
        if sprite.spritecollide(jet,enemy,False) or sprite.spritecollide(jet,asti,False):
            sprite.spritecollide(jet,enemy,True)
            sprite.spritecollide(jet,asti,True)
            life -= 1
        if life == 0 or lost >= maxl:
            finish = True
            window.blit(lose,(200,200))
        
        if score >= goal:
            finish = True
            window.blit(win,(200,200))
        
        text = font2.render("Missed:"+str(lost),1,(255,0,0))
        window.blit(text,(10,50))
        text2 = font2.render("Scored:"+str(score),1,(255,0,0))
        window.blit(text2,(10,25))
        text4 = font2.render("Life:"+str(life),1,(255,0,0))
        window.blit(text4,(600,50))
        jet.move()
        enemy.update()
        bull.update()
        asti.update()
        
        
        jet.undissepear()
        bull.draw(window)
        enemy.draw(window)
        asti.draw(window)

        clock.tick(fps)
        display.update()
    else:
        finish = False
        score = 0
        lost = 0 
        nuf = 0
        life = 3
        for b in bull:
            b.kill()
        for j in asti:
            j.kill()
        for g in enemy:
            g.kill()
        time.delay(3000)
        for i in range(1,6):
            ene = Enemy("ufo.png",randint(80,h-80),40,50,50,randint(1,3))
            enemy.add(ene)
        for i in range(1,3):
            ast = Enemy("asteroid.png",randint(80,h-80),40,70,70,randint(1,5))
            asti.add(ast)





