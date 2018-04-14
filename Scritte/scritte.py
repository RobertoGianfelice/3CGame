 class Scritte(object):
    
    def __init__(self,testo, colore, fontSize):   # quando inizializziamo una classe dobbiamo dire 'cosa volgiamo scrivere' il colore che gli vogliamo dare con 'red black or green' e la grandezza del testo
        self.testo=testo
        self.colore = colore 
        self.fontSize = fontSize

    def display(self):
        textSize(self.fontSize)
        
        if self.colore=='green':
            fill(135,255,84)
        elif self.colore== 'red':
            fill(255,7,7)
        elif self.colore== 'black':
            fill(0)
        text(self.testo,self.x,self.y)
    
    def updateTesto(self,testo):
        self.testo=testo
    
    def setPos(self,x,y):  # decidiamo dove posizionare la scritta 
        self.x=x
        self.y=y
        self.display()
