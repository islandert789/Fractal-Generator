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
        if mirrored:
            self.pattern += [None]
            for i in range(len(self.pattern)-2, -1, -1):
                self.pattern += [-self.pattern[i]]
        self.angle = angle
        self.bounds = self.getBounds()
    def turns(self):
        baseTurns = len(self.pattern)
        turnN = baseTurns
        for j in range(1,self.iterations+1):
            turnN = baseTurns + turnN*baseTurns + turnN
        return turnN
    def getBounds(self):
        x=0.0
        y=0.0
        # the initial direction
        direction = self.angle
        # the bounding coordinates
        bounds=[0,0,0,0]
        # length of the base pattern
        l=len(self.pattern)//2+1
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
    def setupScreen(self):
        print(self.bounds)
        turtle.setup(width=1670,height=1000, startx = 0, starty=0)
        R = float(turtle.window_height())/turtle.window_width()
        dy=self.bounds[3]-self.bounds[1]
        dx=self.bounds[2]-self.bounds[0]
        ax=0.5*(self.bounds[0]+self.bounds[2])
        ay=0.5*(self.bounds[1]+self.bounds[3])
        if dy/dx>=R:
            turtle.setworldcoordinates(ax-0.5*dy/R,self.bounds[1],ax+0.5*dy/R,self.bounds[3])
        else:
            turtle.setworldcoordinates(self.bounds[0],ay-0.5*dx*R,self.bounds[2],ay+0.5*dx*R)
        turtle.hideturtle()
    def draw(self):
        turtle.tracer(0)

        turtle.left(self.angle)
        turtle.fd(1)
        if self.mirrored:
            l = (len(self.pattern)-1)//2+1
            print(len(self.pattern))
        else:
            l = len(self.pattern)+1
        for i in range(1,self.turns()+1):
            while not i%l:
                i//=l
            if self.mirrored:
                turtle.left(self.pattern[i%(2*l)-1])
            else:
                turtle.left(self.pattern[i%l-1])
            turtle.fd(1)
        turtle.tracer(1)
        turtle.exitonclick()
    def disp(self):
        self.setupScreen()
        self.draw()


F = Fractal([90],5,True, 15)
print(F.disp())
