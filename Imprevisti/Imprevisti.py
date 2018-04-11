
from Scritte import Scritte

class Imprevisti(object):
    def __init__(self, speed, sizeImpr):
        global imprevistiArray
        self.speed = speed
        self.punteggio = 0
        self.sizeImpr = sizeImpr
        
        imprevistiArray = ['-20.png','-100.png','0.png','100.png','50.png','-60.png']
    
        
    
        
    def moveImprevisto(self):
        
        self.x -= self.speed 
        
        if self.x < -self.sizeImpr:
            self.createNewImprevisto()
            if self.speed < 5:
                self.speed += 0.15
                
        image(imprevisto, self.x, self.y, self.sizeImpr, self.sizeImpr)
        punteggioScritta.move(self.x + self.sizeImpr, self.y + (self.sizeImpr + 15)/2)
        
    def createNewImprevisto(self):
        global imprevisto
        global punteggioScritta
        
        self.x = width-self.sizeImpr + random(500)
        self.y = random(height - self.sizeImpr) 
        
        numeroImprevisto = int(random(len(imprevistiArray))) # Posizione dell'imprevisto all'interno di imprevistiArray
        imprevisto = loadImage(imprevistiArray[numeroImprevisto]) #carica l'immagine dell'imprevisto
        self.punteggio = imprevistiArray[numeroImprevisto].replace('.png', '') #siccome il  nome di ogni immagina rappresenta il punteggio dell'imprevisto, prendo il nome dell'imprevisto e rimuovo .png
        punteggioScritta = Scritte(self.punteggio, self.x + self.sizeImpr, self.y + (self.sizeImpr + 15)/2, self.coloreScritta(), 15)
        
        
        
        
    def coloreScritta(self):  #sceglie il colore della scritta in base al punteggio, se e' negativo il colore e' rosso altrimenti il punteggio e' verde
        if self.punteggio < 0:
            return 'red'
        elif self.punteggio > 0:
            return 'green'
        else:
            return 'transparente'    
        
        
    def collisione(self):
        if self.punteggio == '':
            return 'Game Over'
        else: 
            self.createNewImprevisto()
            
        

            
            
        
    
        
    
        
    
    
        
        
        
        
            
        
        
    
    
    
            
        
        
        
    
        
        
        
    
