from Scritte import Scritte
class car (object):
                        #altezza macchina
    altezza=20
    larghezza=altezza*(3)             #larghezza macchina
    coloreM=color(204,255,0)      #colore corpo auto
    coloreR=color(0,0,0)          #colore ruote

    
    
    def __init__(self,x,y,speed,step,dimImpr=50,testo='3C'):
        self.x=x                  
        self.y=y
        self.step=step
        self.speed=speed
        self.c=car.coloreM
        self.r=car.coloreR
        self.testo=testo
        self.dimImpr=dimImpr
        
        self.scritta=Scritte(self.testo,"red",18)


        
    #visualizzazione macchina sul display
    def display(self):
        fill(self.c)
        rect(self.x,self.y,car.larghezza,car.altezza)
        fill(self.r)
        rect(self.x+car.altezza/(5),self.y-car.larghezza/(10),car.larghezza*(0.3),car.altezza*(0.3))  
        rect(self.x+car.altezza*(1.8),self.y-car.larghezza/(10),car.larghezza*(0.3),car.altezza*(0.3))
        rect(self.x+car.altezza/(5),self.y+car.larghezza/(3),car.larghezza*(0.3),car.altezza*(0.3))
        rect(self.x+car.altezza*(1.8),self.y+car.larghezza/(3),car.larghezza*(0.3),car.altezza*(0.3))
        self.scritta.setPos(self.x + 3,self.y + 17)
        self.scritta.display()

    def updateSpeed(newSpeed):
        self.speed=newSpeed

    
    
    #comandi            
    
    
    def comandi(self,comando):
        if (keyCode==UP and self.y>15):
            self.y=self.y-self.step*self.speed
        
        elif (keyCode==DOWN and self.y<height-30):
            self.y=self.y+self.step*self.speed
        
        elif (keyCode==LEFT and self.x>0):
            self.x=self.x-self.step*self.speed
        
        elif (keyCode==RIGHT and self.x<width-60):
            self.x=self.x+self.step*self.speed   
    
    #collisione
    def collisione (self,imprevisti):
        if(abs(self.x-imprevisti.x)<self.dimImpr and
           abs(self.y-imprevisti.y)<self.dimImpr):
            return True
        else:
            return False
     
