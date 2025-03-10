#Autor:     Tim Behnke
#Datum:     25.02.2016
#Zweck:     Schiffe versenken

#IMPORTIEREN
from turtle import *
from Koord2Feld import *

#----------------------------------------------------------------------------------------

class Schiffe:
    
    class __Schiff:
        
        def __init__(self,senkrecht,waagerecht,groesse):

            self.isWaagerecht=True
            self.senkrechtSchiff=senkrecht
            self.waagerechtSchiff=waagerecht
            self.groesse=groesse
            self.turtle=Turtle()
            self.turtle.penup()
            self.felderliste=[]
            self.aktuellesFeld=-1
            self.turtle.shape(self.waagerechtSchiff)
            
            
    def __init__(self,screen):

        self.__bewegbar=True
        self.__screen=screen
        self.__setVisual()
        self.__schiffsliste=[self.__Schiff("fztraeger_senkrecht.gif","fztraeger_waagerecht.gif",5),
           self.__Schiff("sschiff_senkrecht.gif","sschiff_waagerecht.gif",4),
           self.__Schiff("kreuzer_senkrecht.gif","kreuzer_waagerecht.gif",3),
           self.__Schiff("uboot_senkrecht.gif","uboot_waagerecht.gif",3),
           self.__Schiff("zerstoerer_senkrecht.gif","zerstoerer_waagerecht.gif",2)]

    def __setVisual(self):
        #Vor:   keine
        #Eff:   Die GIF'S sind im screen registiert
        
        self.__screen.register_shape("fztraeger_senkrecht.gif")
        self.__screen.register_shape("fztraeger_waagerecht.gif")
        self.__screen.register_shape("sschiff_senkrecht.gif")
        self.__screen.register_shape("sschiff_waagerecht.gif")
        self.__screen.register_shape("kreuzer_senkrecht.gif")
        self.__screen.register_shape("kreuzer_waagerecht.gif")
        self.__screen.register_shape("uboot_senkrecht.gif")
        self.__screen.register_shape("uboot_waagerecht.gif")
        self.__screen.register_shape("zerstoerer_senkrecht.gif")
        self.__screen.register_shape("zerstoerer_waagerecht.gif")

    def bewegen(self,feld,schiff):
        #Vor:   -feld- ist vom Typ Integer und im Bereich von 0 bis 99
        #       -schiff- ist vom Typ Integer und im Bereich 0 bis 4
        #Eff:   Das entsprechende Schiff ist zu den Feld bewegt.
        
        if self.__bewegbar:
            x=0;y=0;
            k=Koord2Feld()
            x,y=k.eckkoord(feld,True)
            if self.__schiffsliste[schiff].groesse%2==0:
                a=60
            if self.__schiffsliste[schiff].groesse%2==1:
                a=30
            if self.__schiffsliste[schiff].isWaagerecht:
                self.__schiffsliste[schiff].turtle.goto(x+a,y+30)
            if self.__schiffsliste[schiff].isWaagerecht==False:
                self.__schiffsliste[schiff].turtle.goto(x+30,y+a)
            self.__schiffsliste[schiff].aktuellesFeld=feld

    def bewegenspez(self,schiff,x,y):
        #Vor:   -schiff- ist vom Typ Integer und im Bereich 0 bis 4
        #       -x- und -y- sind vom Typ Integer
        #Eff:   Das entsprechende Schiff ist zu den Koordinaten bewegt
        
        self.__schiffsliste[schiff].turtle.goto(x,y)
        
            
    def drehen(self,schiff):
        #Vor:   -schiff- ist vom Typ Integer und im Bereich 0 bis 4.
        #Eff:   Das entsprechende Schiff ist um 90 Grad gedreht
        
        if self.__bewegbar:
            if self.__schiffsliste[schiff].isWaagerecht:
                self.__schiffsliste[schiff].turtle.shape(self.__schiffsliste[schiff].senkrechtSchiff)
                self.__schiffsliste[schiff].isWaagerecht=False
            else:
                self.__schiffsliste[schiff].turtle.shape(self.__schiffsliste[schiff].waagerechtSchiff)
                self.__schiffsliste[schiff].isWaagerecht=True
            return self.__schiffsliste[schiff].isWaagerecht

    def bestätigen(self):
        #Vor:   -keine-
        #Eff:   Die besetzten Felder sind abgespeichert.
        
        if self.__bewegbar:
            self.__bewegbar=False
            for i in range(5):
                if self.__schiffsliste[i].groesse%2==0:
                    faktor=10
                    if self.__schiffsliste[i].isWaagerecht:
                        faktor=1
                    if self.__schiffsliste[i].groesse==4:
                        if self.__schiffsliste[i].isWaagerecht:
                            self.__schiffsliste[i].felderliste.append(self.__schiffsliste[i].aktuellesFeld+(-1))
                            self.__schiffsliste[i].felderliste.append(self.__schiffsliste[i].aktuellesFeld+(0))
                            self.__schiffsliste[i].felderliste.append(self.__schiffsliste[i].aktuellesFeld+(+1))
                            self.__schiffsliste[i].felderliste.append(self.__schiffsliste[i].aktuellesFeld+(2))
                        if self.__schiffsliste[i].isWaagerecht==False:
                            self.__schiffsliste[i].felderliste.append(self.__schiffsliste[i].aktuellesFeld+(+10))
                            self.__schiffsliste[i].felderliste.append(self.__schiffsliste[i].aktuellesFeld)
                            self.__schiffsliste[i].felderliste.append(self.__schiffsliste[i].aktuellesFeld+(-10))
                            self.__schiffsliste[i].felderliste.append(self.__schiffsliste[i].aktuellesFeld+(-20))
                    if self.__schiffsliste[i].groesse==2:
                            if self.__schiffsliste[i].isWaagerecht==False:
                                self.__schiffsliste[i].felderliste.append(self.__schiffsliste[i].aktuellesFeld-(10))
                                self.__schiffsliste[i].felderliste.append(self.__schiffsliste[i].aktuellesFeld-(0))
                                g=-1
                            if self.__schiffsliste[i].isWaagerecht:
                                self.__schiffsliste[i].felderliste.append(self.__schiffsliste[i].aktuellesFeld+(1))
                                self.__schiffsliste[i].felderliste.append(self.__schiffsliste[i].aktuellesFeld-(0))
                if self.__schiffsliste[i].groesse%2==1:
                    faktor=10
                    if self.__schiffsliste[i].isWaagerecht:
                        faktor=1
                    self.__schiffsliste[i].felderliste.append(self.__schiffsliste[i].aktuellesFeld)
                    d=1
                    for b in range((self.__schiffsliste[i].groesse-1)//2):
                        self.__schiffsliste[i].felderliste.append((self.__schiffsliste[i].aktuellesFeld+(d+b)*faktor))
                    d=-1
                    for b in range(((self.__schiffsliste[i].groesse-1)//2)):
                        self.__schiffsliste[i].felderliste.append((self.__schiffsliste[i].aktuellesFeld+(b+d)*faktor))
                        d=d-2
            
            

    def treffer(self,feld):
        #Vor:   keine
        #Erg:   Zwei Variablen sind geliefert, der erste gibt an ob ein Schiff getroffen wurde
        #       die zweite gibt an ob ein Schiff versenkt wurde
        
        for i in range(5):
            try:
                bizeps=self.__schiffsliste[i].felderliste.index(feld)
                self.__schiffsliste[i].felderliste.pop(bizeps)
                if len(self.__schiffsliste[i].felderliste)!=0:
                    return True,False
                return True,True
            except:
                continue
        return False,False


    
#flugzeugträger 5
#schlachtschiff 4 
#kreuzer 3
#uboot 3 
#zerstörer 2
