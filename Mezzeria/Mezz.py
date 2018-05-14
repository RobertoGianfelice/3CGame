from Scritte import Scritte

class mezz(object):
    coloreStriscia=color(100,100,190)#128

    def __init__(self,x,step,speed,larghezzaSchermo,altezzaSchermo,testo="3C"):
        self.x = x
        self.step = step
        self.speed = speed
        self.larg = ((larghezzaSchermo*9.0)/100.0)
        self.altezza= ((altezzaSchermo*4.0)/100.0)
        self.scritta=Scritte(testo,"green",self.altezza-(1/2))
                            
    def move(self):
        self.x = self.x - self.step*self.speed
        
        if self.x < -120:
            self.x = 0
                    
    def display(self):
        
        for i in  range(width/10):
            fill(mezz.coloreStriscia)
            rect(self.x + i*120,height/2,self.larg,self.altezza)
      
            self.scritta.setPos(self.x + i*120 + (7/2),height/2+self.altezza-2)
            self.scritta.display()
            
    def updateSpeed(self,newSpeed):
        self.speed=newSpeed        
