from oggettoVolante import OggettoVolante
from imprevisto import Imprevisto
from scritta import Scritta

from mezzeria import Mezzeria
from car import Car

punteggio=0
timer=0.0
imprevisti=[]
mezzeria=Mezzeria(100,0,1,0,-1,0)
macchina=Car(100,100)
scritta=Scritta(punteggio,200,10)




def setup():
  size(800,500)
  scritta.setPos(width/2,10)
  imprevisti.append(Imprevisto(50,random(1,3),int(random(-50,50))))

  

def draw():
  background(255)
  
  scritta.display()
  print(OggettoVolante.gameSpeed, int(OggettoVolante.gameSpeed))
  if (int(OggettoVolante.gameSpeed*10-10)>=len(imprevisti)):
      imprevisti.append(Imprevisto(random(width),random(1,3),int(random(-50,50))))
      
  for i in range(0,len(imprevisti)):
      imprevisti[i].display()
      imprevisti[i].fly()
      if(not(imprevisti[i].getColpito()) and macchina.collisione(imprevisti[i])):
        scritta.updateTesto(imprevisti[i].getValue())
        imprevisti[i].setColpito()
      
  mezzeria.display()
  mezzeria.fly()
  macchina.display()


  if (keyPressed):
      macchina.comandi(keyCode)
      
      
