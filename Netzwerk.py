#Autor:     Tim Behnke
#           Tobias Schüler
#Datum:     03.03.2016
#Zweck:     Netzwerkanbindung Schiffe versenken

#IMPORTIEREN
from Spielfeld import*
from Kanaele import*
from Schiffe import*
from Stecker import *
from Koord2Feld import *
from turtle import *
from time import *

#-----------------------------------------------------------------------------------------------

class Netzwerk():
    
    def __init__(self,ip,port,schiffe):
        k1=Kanaele(ip,port)
        self.__schiffe=schiffe
        self.__k1=k1

    def erster(self):
        #Vor:   keine
        #Eff:   True ist geliefert, wenn man erster ist, andernfalls False
        
        if self.__k1.erster():
            return True
        return False

    def __stecken(self,k,x,y):
        #Vor:   -k- ist vom Typ list
        #       -x- und -y- sind vom Typ Integer
        #Eff:   Der Stecker ist an den Koordinaten gesetzt
        
        t=Stecker(k,x,y)

    def verschicken(self,feld):
        #Vor:   -feld- ist vom Typ Integer
        #Erg:   Die Variablen sind geliefert, ob beim gegnerischen Feld ein Schiff
        #       getroffen ist und ob ein Schiff versenkt ist.
        
        trefferliste=[]
        self.__k1.senden(str(feld))
        trefferstring=self.__k1.empfangen()
        trefferliste=[]
        for i in trefferstring:
            if i=="1":
                trefferliste.append(True)
            if i=="0":
                trefferliste.append(False)
        b=Koord2Feld()
        x,y=b.eckkoord(feld,False)
        self.__stecken(trefferliste[0],x,y)

        return trefferliste[1]
        
    def empfang(self):
        #Vor:   keine
        #Eff:   Es ist makiert, ob der Gegner ein Schiff getroffen hat.
        #       Der Information ist dem Gegner gesendet
        
        trefferliste=[]
        n=self.__k1.empfangen()
        feld=int(n)
        a,b=self.__schiffe.treffer(feld)
        trefferliste=[a,b]
        erg=""
        for i in trefferliste:
            if i:
                erg=erg+"1"
            if i==False:
                erg=erg+"0"
        h=Koord2Feld()
        x,y=h.eckkoord(feld,True)
        self.__stecken(trefferliste[0],x,y)
        self.__k1.senden(erg)
        

        
        
        

    
