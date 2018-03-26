class mezz(object):
    coloreStriscia=color(128,128,128)
    def __init__(self,x,step,speed,larg):
        self.x = x
        self.step = step
        self.speed = speed
        self.larg = larg
        
    def move(self):
        self.x = self.x - self.step*self.speed
        
        if self.x < -120                                                                                                                                            :
            self.x = 0
                    
    def display(self):
        for i in  range(width/10):
            fill(mezz.coloreStriscia)
            
            rect(self.x + i*120,height/2,60,10)
            
        
        
        
   