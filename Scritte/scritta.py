class Scritta(object):
    def __init__(self,testo,x,y):
        self.testo=testo
        self.x=x
        self.y=y
    
    def display(self):
        text(self.testo, self.x, self.y)
    
    def updateTesto(self,testo):
        self.testo+=testo
        
    def setPos(self,x,y):
        self.x=x
        self.y=y