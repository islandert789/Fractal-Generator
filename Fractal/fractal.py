import turtle
import math

class Fractal:
    def __init__(self, pattern, iterations, mirrored, angle):
        """
        Initialize a Fractal object.

        Arguments:
            pattern -- an array of angles that form the base of the fractal

            iterations -- number of iterations of the fractal

            mirrored -- boolean if the pattern is mirrored

            angle -- initial angle, leave blank to find optimal angle

        Example:
            myFractal = Fractal([90], 15, True)
                define a fractal with base [90] for 15 iterations using mirroring
        """
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
        bounds=[0,0,0,0]
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
            bounds[0]=min(bounds[0],x)
            bounds[1]=min(bounds[1],y)
            bounds[2]=max(bounds[2],x)
            bounds[3]=max(bounds[3],y)
        return [bounds[0]-1,bounds[1]-1,bounds[2]+1,bounds[3]+1]

F = Fractal([90],10,True, 15)
print(F.bounds())
