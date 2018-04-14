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
        
        
        if self.colore=='green':
            fill(135,255,84)
        elif self.colore== 'red':
            fill(255,7,7)
        else:
            fill(0)
        text(self.testo,self.x,self.y)
    
    def updateTesto(self,testo):
        self.testo=testo
