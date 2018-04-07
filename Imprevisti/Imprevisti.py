
from Scritte import Scritte

class ImprevistiClass(object):
    
    def __init__(self, speed, sizeImpr):
    
        global imprevistiArray
        global imprevistiValoreDictionary
        
        self.speed = speed
        self.punteggio = 0
        self.sizeImpr = sizeImpr
        
        imprevistiArray = ['Banana-20.png','Razzo-100.png','BombaGameOver.png','Bonus100.png','Bonus50.png','Banana-60.png']
        imprevistiValoreDictionary = {'Banana-20.png': -20,'Razzo-100.png': -100,'BombaGameOver.png' : 0,'Bonus100.png' : 100,'Bonus50.png' : 50,'Banana-60.png' : -60}
        
        self.x = width-self.sizeImpr + random(500)
        self.y = random(height - self.sizeImpr) 
        
        self.createNewImprevisto()
        
    def moveImprevisto(self):
        self.x -= self.speed 
        
        if self.x < -self.sizeImpr:
            self.createNewImprevisto()
            if self.speed < 5:
                self.speed += 0.15
    
        colore = ''

        if self.punteggio < 0:
            colore = 'red'
        elif self.punteggio > 0:
            colore = 'green'
        else:
            self.punteggio = ''

        punteggioScritta = Scritte(self.punteggio, self.x + self.sizeImpr, self.y + self.sizeImpr, colore, 15)
        image(imprevisto, self.x, self.y, self.sizeImpr, self.sizeImpr) 

    
    def createNewImprevisto(self):
        global imprevisto
        
        self.x = width-self.sizeImpr + random(500)
        self.y = random(height - self.sizeImpr)
        
        imprevistoType = imprevistiArray[int(random(len(imprevistiArray)))]
        imprevisto = loadImage(imprevistoType)
        self.punteggio = imprevistiValoreDictionary[imprevistoType]
        
        
    def collisione(self):
        self.createNewImprevisto()
            
            
        
    
        
    
        
    
    
        
        
        
        
            
        
        
    
    
    
            
        
        
        
    
        
        
        
    
