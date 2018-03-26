class car (object):
    altezza=10                    #altezza macchina
    larghezza=altezza*(3)             #larghezza macchina
    coloreM=color(204,255,0)      #colore corpo auto
    coloreR=color(0,0,0)          #colore ruote

    
    
    def __init__(self,x,y,speed,step):
        self.x=x                  
        self.y=y
        self.step=step
        self.speed=speed
        self.c=car.coloreM
        self.r=car.coloreR

        
    #visualizzazione macchina sul display
    def display(self):
        fill(self.c)
        rect(self.x,self.y,car.larghezza,car.altezza)
        fill(self.r)
        rect(self.x+car.altezza/(5),self.y-car.larghezza/(10),car.larghezza*(0.3),car.altezza*(0.3))  
        rect(self.x+car.altezza*(1.8),self.y-car.larghezza/(10),car.larghezza*(0.3),car.altezza*(0.3))
        rect(self.x+car.altezza/(5),self.y+car.larghezza/(3),car.larghezza*(0.3),car.altezza*(0.3))
        rect(self.x+car.altezza*(1.8),self.y+car.larghezza/(3),car.larghezza*(0.3),car.altezza*(0.3))


            
    #comandi            
    def comandi(self,comando):
        if (keyCode==UP and self.y>15):
            self.y=self.y-self.step*self.speed
        
        elif (keyCode==DOWN and self.y<485):
            self.y=self.y+self.step*self.speed
        
        elif (keyCode==LEFT and self.x>0):
            self.x=self.x-self.step*self.speed
        
        elif (keyCode==RIGHT and self.x<470):
            self.x=self.x+self.step*self.speed   
    