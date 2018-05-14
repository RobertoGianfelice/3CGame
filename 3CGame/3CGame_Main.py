
from MEzzeria import mezz
from Imprevisti import Imprevisti
from Scritte import Scritte
from Macchina import car

larghezzaSchermo=800
altezzaSchermo=500
speed=4
dimImprevisto=larghezzaSchermo/20
testoMezzeria="3C LSA"

altezzaStriscia=500
larghezzaStriscia=800

mezzeria=mezz(0,1,spped,larghezzaStriscia,altezzaStriscia,testoMezzeria)
ListaImpr=[]
imprevisto=Imprevisti(speed,dimImprevisto,larghezzaSchermo,altezzaSchermo)
ListaImpr.append(imprevisto)
punteggio=Scritte('0','green',18)

macchina=car(10,10,speed*2,1)
fineGioco=0

def setup():
  size(larghezzaSchermo,altezzaSchermo)
  for impr in ListaImpr:
      impr.createNewImprevisto()
  punteggio.setPos(larghezzaSchermo/2,15)
  frameRate(30)

def draw():
  global fineGioco

  background(255)
  
  punteggio.display()
  mezzeria.move()
  mezzeria.display()

  for impr in ListaImpr:
      impr.moveImprevisto()

  macchina.display()
  
  if (keyPressed):
      macchina.comandi(key)

  if (fineGioco==0):

    for impr in ListaImpr:
        if (macchina.collisione(impr)):
            if (impr.getValue()==0):
                    fineGioco=True
            else:
                impr.collisione()
                punteggio.updateTesto(str(int(punteggio.testo)+impr.getValue()))
                if  len(ListaImpr) < 5:
                    imprevisto = Imprevisti(speed,dimImprevisto, larghezzaSchermo, altezzaSchermo)
                    ListaImpr.append(imprevisto)
  else:
        gameOver=Scritte('Game Over\nScore='+punteggio.testo,'red',100)
        gameOver.setPos(10,altezzaSchermo/2)
        gameOver.display()
