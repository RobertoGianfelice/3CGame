from oggettoVolante import OggettoVolante

class Imprevisto(OggettoVolante):
    
    def __init__(self,y,speedX,value):
        self.x=width
        self.y=y
        self.speedX=speedX
        self.speedY=0
        self.dirX=-1
        self.dirY=1
        self.value=value
        self.npoints=int(random(3,15))
        self.colpito=0
        self.delay=random(200)
        
    def star(self, x, y, radius1, radius2, npoints):
        angle = TWO_PI / npoints
        halfAngle = angle / 2.0
        with beginClosedShape():
            a = 0
            while a < TWO_PI:
                sx = x + cos(a) * radius2
                sy = y + sin(a) * radius2
                vertex(sx, sy)
                sx = x + cos(a + halfAngle) * radius1
                sy = y + sin(a + halfAngle) * radius1
                vertex(sx, sy)
                a += angle
                
    def display(self):
        if (self.delay>0):
            self.delay-=1
            print("Nascondo ", self.delay)
        else:
            if (self.value>0):
                fill(0,255,0)
            else:
                fill(255,0,0)
            self.star(self.x, self.y, 5, 30, self.npoints)
            text(self.value, self.x-20, self.y-30)
    
    def fly(self):
        if (self.delay<=0):
            self.x=self.x+self.speedX*self.dirX*OggettoVolante.gameSpeed
            self.y=self.y+self.speedY*self.dirY*OggettoVolante.gameSpeed
            if (self.x < 0):
                self.x=width 
                self.y=random(height)+30
                self.npoints=random(3,15)
                self.colpito=0
                self.value=int(random(-50,50))
                
    def getValue(self):
        return(self.value)
    
    def setColpito(self):
        self.colpito=1
        self.x=width
        self.colpito=0
        self.y=random(height)+30
        self.npoints=random(3,15)
        self.value=int(random(-50,50))
    
    def getColpito(self):
        return(self.colpito)