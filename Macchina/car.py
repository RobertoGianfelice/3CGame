
class Car(object):
    
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.speedX=2
        self.speedY=2

        self.c = color(random(255),0,0)


    def display(self):
        fill(self.c)
        rect(self.x,self.y,30,10)
        rect(self.x+2,self.y-3,10,3)
        rect(self.x+18,self.y-3,10,3)
        rect(self.x+2,self.y+10,10,3)
        rect(self.x+18,self.y+10,10,3)
    
    def comandi(self,comando):
        if (comando == UP and self.y>0):
            self.y-=self.speedY
        elif (comando == DOWN and self.y<(height-30)):
            self.y+=self.speedY
        elif (comando == LEFT and self.x>0):
            self.x-=self.speedX
        elif (comando == RIGHT and self.x<(width-30)):
            self.x+=self.speedX
        
    def comandiMouse(self,incrX,incrY):
        if (incrY<0 and self.y>0):
            self.y-=1
        elif (incrY>0 and self.y<(height-30)):
            self.y+=1
        elif (incrX<0 and self.x>0):
            self.x-=1
        elif (incrX>0 and self.x<(width-30)):
            self.x+=1
    
    def collisione(self,imprevisto):
        if (abs(self.x-imprevisto.x)<50 and 
            abs(self.y-imprevisto.y)<50):
            print("collisione")
            return(1)
        else:
            return(0)