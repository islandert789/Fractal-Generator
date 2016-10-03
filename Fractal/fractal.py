import turtle
import math

class Fractal:
    def __init__(self, pattern, iterations, mirrored, angle):
        self.pattern = pattern
        self.iterations = iterations
        self.mirrored = mirrored
        self.angle = angle
    def turns(self):
        baseTurns = len(self.pattern)
        turnN = baseTurns
        for j in range(1,self.iterations+1):
            turnN = baseTurns + turnN*baseTurns + turnN
        return turnN
    def bounds(self):
        x=0.0
        y=0.0
        # the initial direction
        direction = self.angle
        # the bounding coordinates
        b=[0,0,0,0]
        # length of the base pattern
        l=len(self.pattern)+1
        tempPattern = self.pattern.copy()
        if self.mirrored:
            tempPattern+=[None]
            for i in range(l-2,-1,-1):
                tempPattern+=[-tempPattern[i]]
        for i in range(1,self.turns()+1):
            while not i%l:
                i//=l
            if self.mirrored:
                direction+=tempPattern[i%(2*l)-1]
            else:
                direction+=tempPattern[i%l-1]
            x+=math.cos(math.radians(direction))
            y+=math.sin(math.radians(direction))
            b[0]=min(b[0],x)
            b[1]=min(b[1],y)
            b[2]=max(b[2],x)
            b[3]=max(b[3],y)
        return [b[0]-1,b[1]-1,b[2]+1,b[3]+1]

F = Fractal([90],10,True, 15)
print(F.bounds())
