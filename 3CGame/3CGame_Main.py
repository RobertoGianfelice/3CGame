from Mezzeria import mezz
from Imprevisti import ImprevistiClass
from Scritte import Scritte
from Macchina import car

larghezzaSchermo=800
altezzaSchermo=500
mezzeria=mezz(0,1,1,60,20)
imprevisto=ImprevistiClass(1)
punteggio=Scritte(0,larghezzaSchermo/2,15,0,18)
macchina=car(10,10,1,2)

def setup():
  size(larghezzaSchermo,altezzaSchermo)
  imprevisto.inizializza(1)

def draw():
  background(255)
  
  punteggio.display()
  mezzeria.move()
  mezzeria.display()

  imprevisto.moveImprevisto()  #Sposta e visualizza
  macchina.display()
  
  if (keyPressed):
      macchina.comandi(key)
  
