import pgzrun
import random 

WIDTH=300
HEIGHT=300
TITLE="random lines"





def draw() :
    screen.fill("black")
    WIDTH=100
    HEIGHT=50

    r=200
    g=100
    b=100
    screen.draw.filled_circle((100,200),60,(r,g,b))
    screen.draw.line((140,100),(140,150),(r,g,b))

    
    







pgzrun.go()