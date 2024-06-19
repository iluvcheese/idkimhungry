import pgzrun
import random
from time import time

WIDTH = 800
HEIGHT = 600

satellites = []
lines = []

nextwasteofelectricity = 0

start_time = 0
total_time = 0
end_time = 0

numberofflyingthingies = 8

def draw():
    screen.blit("sattelite",(0, 0))
    number = 1
    for i in satellites:
        i.draw()
        screen.draw.text(str(number), (i.pos[0], i.pos[1]+20))
        number = number+1

def launchflyingthingies():
    global start_time
    for i in range(8):
        satellite = Actor("space")
        satellite.pos = random.randint(40, 760), random.randint(40, 589)
        satellites.append(satellite)
        
        
    start_time = time()

def update():
    pass
launchflyingthingies()
pgzrun.go()