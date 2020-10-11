import pgzrun
from random import randint


WIDTH = 800
HEIGHT = 800

# prick = Actor("dot")
# prick.pos = [100, 100]

prickar = []
linjer = []

for prick in range(0, 10):
    aktor = Actor("dot")
    aktor.pos = randint(20, WIDTH-20), randint(20, HEIGHT-20)
    prickar.append(aktor)


def draw():
    screen.fill("black")

    siffra = 1
    for prick in prickar:
        screen.draw.text(str(siffra), (prick.pos[0], prick.pos[1] + 12))
        prick.draw()
        siffra = siffra + 1





# def update():
#    print('update')


pgzrun.go()
