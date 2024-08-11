import pgzrun
from random import randint

game_over = False

WIDTH = 600
HEIGHT = 500

count = 0

bee = Actor('bumble_bee')
flwr = Actor('y_flower')

flwr.pos = 250,250
bee.pos = 500,400

def draw():
    screen.blit('g_grass_background',(0,0))
    bee.draw()
    flwr.draw()
    screen.draw.text('Score: '+str(count),color = 'white',topleft=(10,10))
    if game_over:
        screen.fill('Orange')
        screen.draw.text('You Lost - Your Score: '+str(count), midtop=(WIDTH//2,10),fontsize=40,color=('red'))
        

def timeup():
    global game_over
    game_over = True

def flower():
    flwr.x = randint(100,450)
    flwr.y = randint(50,375)

def update():
    global count
    if keyboard.left:
        bee.x= bee.x-5
    if keyboard.right:
        bee.x= bee.x+5
    if keyboard.up:
        bee.y = bee.y-5
    if keyboard.down:
        bee.y = bee.y+5
    if bee.colliderect(flwr):
        count = count+1
        flower()
    
clock.schedule(timeup,15)

pgzrun.go()