class OggettoVolante(object):
    gameSpeed=1
    MAXSPEED=2
    SPEEDSTEP=0.01
    def __init__(self, x,y,speedX,speedY,dirX,dirY):
        self.x=x
        self.y=y
        self.speedX=speedX
        self.speedY=speedY
        self.dirX=dirX
        self.dirY=dirY
        
    def display(self):       
        ellipse(self.x,self.y,2,2)

    def fly(self):
        self.x=self.x+self.speedX*self.dirX*OggettoVolante.gameSpeed
        self.y=self.y+self.speedY*self.dirY*OggettoVolante.gameSpeed
        if (self.x > (width-20) or self.x < 0):
            self.dirX=-self.dirX        
        if (self.y > (height-40) or self.y < 0):
            self.dirY=-self.dirY        
    
    def comandi(self,comando):
        if (comando=='u'):
            self.dirY=-1
        elif (comando=='d'):
            self.dirY=1    
        elif (comando=='+'and OggettoVolante.gameSpeed<3):
            OggettoVolante.gameSpeed+=0.1
        elif (comando=='-' and OggettoVolante.gameSpeed>1):
            OggettoVolante.gameSpeed-=0.1
    
    def updateGameSpeed(self):
        OggettoVolante.gameSpeed+=OggettoVolante.SPEEDSTEP
        print(OggettoVolante.gameSpeed)
