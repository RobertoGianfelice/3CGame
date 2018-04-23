
from Scritte import Scritte

class Imprevisti(object):
    
    def __init__(self, speed, sizeImpr):
      
        self.speed = speed
        self.punteggio = 0
        self.sizeImpr = sizeImpr
        self.imprevistiArray = ['-20.png','-100.png','0.png','100.png','50.png','-60.png']
        
        self.punteggioScritta = Scritte(self.punteggio,'', 15)
        
    
        
    def moveImprevisto(self):
        
        self.x -= self.speed 
        if self.x < -self.sizeImpr:
            self.createNewImprevisto()
            if self.speed < 5:
                self.speed += 0.15
                
        image(imprevisto, self.x, self.y, self.sizeImpr, self.sizeImpr)
        
        colore = color(255)
        
        if int(self.punteggio) > 0:
           colore = color(135,255,84)
        elif int(self.punteggio) < 0:
           colore = color(255, 7,7)
        else:
            colore = color(255)
            
        self.punteggioScritta.colore = colore
        self.punteggioScritta.updateTesto(self.punteggio)
        self.punteggioScritta.setPos(self.x + self.sizeImpr, self.y + (self.sizeImpr + 15)/2)   
        
        
        
    def createNewImprevisto(self):
        global imprevisto
        
        self.x = width-self.sizeImpr + random(500)
        self.y = random(height - self.sizeImpr) 
        
        numeroImprevisto = int(random(len(self.imprevistiArray))) # Posizione dell'imprevisto all'interno di imprevistiArray
        imprevisto = loadImage(self.imprevistiArray[numeroImprevisto]) #carica l'immagine dell'imprevisto
        self.punteggio = self.imprevistiArray[numeroImprevisto].replace('.png', '') #siccome il  nome di ogni immagina rappresenta il punteggio dell'imprevisto, prendo il nome dell'imprevisto e rimuovo .png
        
        
    def collisione(self):
        if self.punteggio == '':
            return 'Game Over'
        else: 
            self.createNewImprevisto()
            
        

            
            
        
    
        
    
        
    
    
        
        
        
        
            
        
        
    
    
    
            
        
        
        
    
        
        
        
    
