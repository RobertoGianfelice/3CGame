class mezz(object):
    coloreStriscia=color(128,128,128)
    def __init__(self,x,step,speed,larg,altez,testo=''):
        self.x = x
        self.step = step
        self.speed = speed
        self.larg = larg
        self.altezza= altez
        self.testo=testo
        self.scritta=Scritte(self.testo,self.x,250,0,18)       
        
        
    def move(self):
        self.x = self.x - self.step*self.speed
        
        if self.x < -120                                                                                                                                            :
            self.x = 0
                    
    def display(self):
        for i in  range(width/10):
            fill(mezz.coloreStriscia)            
            rect(self.x + i*120,height/2,self.larg,self.altezza)
            #self.scritta.SetPos(self.x + i*120+10,height/2+13)
            self.scritta.x=self.x + i*120+17
            self.scritta.y=height/2+17
            self.scritta.display()
            
        
        
        
   
