from Mezzeria import mezz
from Imprevisti import Imprevisti
from Scritte import Scritte
from Car import car

larghezzaSchermo=800
altezzaSchermo=500
speed=1.5
dimImprevisto=larghezzaSchermo/20
SCRITTA_MACCHINA="3CLSA"
SCRITTA_MEZZERIA="CDS.18"

altezzaStriscia=500
larghezzaStriscia=800

mezzeria=mezz(0,1,speed,larghezzaStriscia,altezzaStriscia,SCRITTA_MEZZERIA)
ListaImpr=[]
imprevisto=Imprevisti(speed,dimImprevisto,larghezzaSchermo,altezzaSchermo)
ListaImpr.append(imprevisto)
punteggio=Scritte('0','black',18)

macchina=car(10,10,speed*2,1,50,SCRITTA_MACCHINA)
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
  newSpeed=min(8,int(int(punteggio.testo)/100+2))
  mezzeria.updateSpeed(newSpeed)
  macchina.updateSpeed(newSpeed+2)


  mezzeria.move()
  mezzeria.display()

  for impr in ListaImpr:
      impr.updateSpeed(newSpeed)

      impr.moveImprevisto()

  macchina.display()
  

  if (keyPressed):
        macchina.comandi(key)

  if (fineGioco==0 and int(punteggio.testo)>=0):

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
