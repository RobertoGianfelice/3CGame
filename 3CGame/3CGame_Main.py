from Mezzeria import mezz
from Imprevisti import Imprevisti
from Scritte import Scritte
from Macchina import car

larghezzaSchermo=800
altezzaSchermo=500
speed=4
dimImprevisto=larghezzaSchermo/20
mezzeria=mezz(0,1,speed,larghezzaSchermo*9.0/100,altezzaSchermo*4.0/100)
ListaImpr=[]
imprevisto=Imprevisti(speed,dimImprevisto)
ListaImpr.append(imprevisto)
punteggio=Scritte('0','green',18)

macchina=car(10,10,speed*2,1)

def setup():
  size(larghezzaSchermo,altezzaSchermo)
  for impr in ListaImpr:
      impr.createNewImprevisto()
  punteggio.setPos(larghezzaSchermo/2,15)
  frameRate(30)

def draw():
  background(255)
  
  punteggio.display()
  mezzeria.move()
  mezzeria.display()

  for impr in ListaImpr:
      impr.moveImprevisto()

  macchina.display()
  
  if (keyPressed):
      macchina.comandi(key)

  for impr in ListaImpr:
    if (macchina.collisione(impr)):
      punteggio.updateTesto(str(int(punteggio.testo)+impr.getValue()))
      impr.collisione()
      
  
  
  
  
