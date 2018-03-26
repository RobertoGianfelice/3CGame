
class ImprevistiClass(object):
    
    
    
    def __init__(self, speed):
        
        global imprevistiArray
        global imprevistiValoreDictionary
        global imprevistoSize
        global canvaHeight
        global canvaWidth
        
        canvaWidth = width
        canvaHeight = height
        
        
        self.speed = speed
        self.punteggio = 0
        self.isItUsed = False 
        
        imprevistoSize = 75
        imprevistiArray = ['Banana-20.png','Razzo-100.png','BombaGameOver.png','Bonus100.png','Bonus50.png','Banana-60.png']
        imprevistiValoreDictionary = {'Banana-20.png': -20,'Razzo-100.png': -100,'BombaGameOver.png' : 0,'Bonus100.png' : 100,'Bonus50.png' : 50,'Banana-60.png' : -60}
        
        self.x = canvaWidth-imprevistoSize + random(500)
        self.y = random(canvaHeight - imprevistoSize) 
        
        self.createNewImprevisto()
        
    def moveImprevisto(self):
        global imprevistoSize 
        global canvaHeight
        global canvaWidth
        
        self.x -= self.speed 
        
        if self.x < -imprevistoSize:
            self.createNewImprevisto()
            if self.speed < 7:
                self.speed += 0.50
        
        image(imprevisto, self.x, self.y, imprevistoSize, imprevistoSize)
            
        textSize(15)
        
        if self.punteggio < 0:
            fill(255, 7,7)
        elif self.punteggio > 0:
            fill(135, 255, 84)
        else:
            self.punteggio = '' 

        text(self.punteggio, self.x + imprevistoSize, self.y + imprevistoSize)
        
        
    def createNewImprevisto(self):
        global imprevisto 
        global imprevistiValoreDictionary
        
        self.x = canvaWidth-imprevistoSize + random(500)
        self.y = random(canvaHeight - imprevistoSize)
        
        imprevistoType = imprevistiArray[int(random(len(imprevistiArray)))]
        imprevisto = loadImage(imprevistoType)
        self.punteggio = imprevistiValoreDictionary[imprevistoType]
        self.isItUsed = False
        
    def collisione(self):
        self.isItUsed = True
        self.createNewImprevisto()
            
        
    
        
    
        
    
    
        
        
        
        
            
        
        
    
    
    
            
        
        
        
    
        
        
        
    