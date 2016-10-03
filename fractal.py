#!/usr/local/bin/python3.5
import turtle
import math

def turns(L,n):
    """
    Find number of turns in a fractal.

    Keyword Arguments:
    L -- the number of turns in the base
    n -- the number of iterations
    """
    B=L
    for j in range(1,n+1):
        B=L+B*L+B
    return B

def fractalBounds(p,n,mir,init=0):
    """Find the bounding coordinates of the fractal."""
    x=0.0
    y=0.0
    # the initial direction
    d = init
    # the bounding coordinates
    b=[0,0,0,0]
    # length of the base pattern
    l=len(p)+1
    if mir:
        p+=[None]
        for i in range(l-2,-1,-1):
            p+=[-p[i]]
    for i in range(1,turns(l-1,n)+1):
        while not i%l:
            i//=l
        if mir:
            d+=p[i%(2*l)-1]
        else:
            d+=p[i%l-1]
        x+=math.cos(math.radians(d))
        y+=math.sin(math.radians(d))
        b[0]=min(b[0],x)
        b[1]=min(b[1],y)
        b[2]=max(b[2],x)
        b[3]=max(b[3],y)
    return [b[0]-1,b[1]-1,b[2]+1,b[3]+1]

def setupScreen(b,init):
    print(b)
    turtle.reset()
    ret=False
    turtle.setup(width=1670,height=1000, startx = 0, starty=0)
    R = float(turtle.window_height())/turtle.window_width()
    dy=b[3]-b[1]
    dx=b[2]-b[0]
    if not init and dy/dx>1 and R<1 or dy/dx<1 and R>1:
        b = [-b[3],b[0],-b[1],b[2]]
        ret=True
        dy=b[3]-b[1]
        dx=b[2]-b[0]
    ax=0.5*(b[0]+b[2])
    ay=0.5*(b[1]+b[3])
    if dy/dx>=R:
        turtle.setworldcoordinates(ax-0.5*dy/R,b[1],ax+0.5*dy/R,b[3])
    else:
        turtle.setworldcoordinates(b[0],ay-0.5*dx*R,b[2],ay+0.5*dx*R)
    turtle.hideturtle()
    return ret

def drawFractal(p,n,mir,init):
    """Draw the fractal"""
    if init:
        turtle.left(init)
    turtle.fd(1)
    if mir:
        l = int(0.5*(len(p)-1)+1)
    else:
        l = len(p)+1
    for i in range(1,turns(l-1,n)+1):
        while not i%l:
            i//=l
        if mir:
            turtle.left(p[i%(2*l)-1])
        else:
            turtle.left(p[i%l-1])
        turtle.fd(1)

def fractal(p,n,mir=False,init=0):
    """
    Draw fractal based on an initial shape.

    Keywords:
    p -- pattern, small array of turns in degrees
    n - number of iterations
    mir -- boolean, true if pattern is mirrored
    init -- initial angle
    """
    if setupScreen(fractalBounds(p,n,mir,init),init):
        turtle.left(90)
    turtle.tracer(0)
    drawFractal(p,n,mir,init)
    turtle.update()
    turtle.tracer(1)
    turtle.exitonclick()
