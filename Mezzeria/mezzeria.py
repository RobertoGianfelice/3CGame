from oggettoVolante import OggettoVolante

class Mezzeria(OggettoVolante):
    def display(self):
        fill(0)
        for i in range (width/10):
           rect(self.x+i*120,(height/2)-3,60,6)

    def fly(self):
        self.x=self.x+self.speedX*self.dirX*OggettoVolante.gameSpeed
        if (self.x < -120):
            self.x=0
            self.updateGameSpeed()  
                    