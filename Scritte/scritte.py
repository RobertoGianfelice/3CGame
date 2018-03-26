class Scritte(object):
    
    def __init__(self,testo,x,y, colore, fontSize):
        self.testo=testo
        self.x = x
        self.y=y
        self.colore = colore 
        self.fontSize = fontSize

    def display(self):
        textSize(self.fontSize)
        fill(self.colore)
        text(self.testo,self.x,self.y)
    
    def updateTesto(self,testo):
        self.testo=testo
        
        
    
    
    def setPass(self,x,y):
        self.x=x
        self.y=y