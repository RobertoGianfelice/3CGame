from Scritte import Scritte

class mezz(object):
    coloreStriscia=color(128,128,128)
    def __init__(self,x,step,speed,larg,altez,testo="3C"):
        self.x = x
        self.step = step
        self.speed = speed
        self.larg = larg
        self.altezza= altez
        #self.colore=colore
        #self.fontSize=fontSize
        
        self.scritta=Scritte(testo,"red",self.altezza-1)
                            
        
    def move(self):
        self.x = self.x - self.step*self.speed
        
        if self.x < -120:
            self.x = 0
                    
    def display(self):
        
        
        for i in  range(width/10):
            fill(mezz.coloreStriscia)
            rect(self.x + i*120,height/2,self.larg,self.altezza)
      
            self.scritta.setPos(self.x + i*120 + 3,height/2+self.altezza-2)
            self.scritta.display()
        
        
   
