#Autoren:   Alexandra Kuhls
#           Tim Behnke 
#Datum:     25.02.2016
#Zweck:     Spielfeld Grafik

#IMPORTIEREN
from turtle import*
from Schiffe import *
from Koord2Feld import*
from Netzwerk import*

#-----------------------------------------------------------------------------

class Spielfeld:
    
    def __init__(self,port):
        
        self.__ip=input("Die IP deines Gegners:")
        self.__x=0
        self.__y=0
        self.__a=0
        self.__dran=False
        self.__screen=getscreen()
        self.__screen.setup(1600,1000)
        self.spielfeldzeichnen()
        self.__dubistdran(False)
        self.__schiffe=Schiffe(self.__screen)
        self.__netzwerk=Netzwerk(self.__ip,port,self.__schiffe)
        a=self.__netzwerk.erster()
        self.__screen.title("Schiffe versenken")
        if a:
            self.__dran=True
        self.__aktuellesSchiff=-1
        self.__gesetzt=False
        self.__schiffe.bewegenspez(0,161,-250)
        self.__schiffe.bewegenspez(1,440,-250)
        self.__schiffe.bewegenspez(2,100,-320)
        self.__schiffe.bewegenspez(3,290,-320)
        self.__schiffe.bewegenspez(4,70,-390)
        self.__dubistdran(self.__dran)
        
    def aktuellesSchiff(self,x,y):
        #Vor: -x- und -y- sind vom Typ Integer.
        #Erg: Wenn die Koordinaten mit der Grundposition eines Schiffes übereinstimmen, dann ist das aktuelle Schiff bestimmt.

        if -280<=y<=-220:
            if 10<=x<=310:
                self.__aktuellesSchiff=0
            if 320<=x<=560:
                self.__aktuellesSchiff=1
        if -350<=y<=-290:
            if 10<=x<=190:
                self.__aktuellesSchiff=2
            if 200<=x<=380:
                self.__aktuellesSchiff=3
        if -420<=y<=-360 and 10<=x<=130:
            self.__aktuellesSchiff=4
            
    def getTheScreen(self):
        #Vor: keine
        #Erg: Die Instanz des getscreen() ist geliefert.

        return self.__screen
    def klick(self,x,y):
        #Vor: -x- und -y- sind vom Typ Integer
        #Erg: Je nach den gegeben Koordinaten ist das aktuelle Schiff bestimmt, das Schiff zu der gegeben position bewegt, das aktuelle Schiff gedreht oder das angegriffene Feld geliefert.

        if 0<=x<=600 and -420<=y<=-210:
            self.aktuellesSchiff(x,y)
        if 0<=x<=600 and -200<=y<=400 and self.__aktuellesSchiff!=-1 and self.__gesetzt==False:
            k=Koord2Feld()
            feldzahl=k.XY2Feld(x,y)
            self.__schiffe.bewegen(feldzahl,self.__aktuellesSchiff)
        if -10>=x>=-80:
            if -430<=y<=-360:
                self.__schiffe.bestätigen()
                self.__gesetzt=True
                if self.__dran==False:
                    self.__netzwerk.empfang()
                    self.__dran=True
            if -355<=y<=-285 and self.__gesetzt==False:
                self.__schiffe.drehen(self.__aktuellesSchiff)
        if self.__gesetzt==True:  ##Nach dem Setzten der Schiffe
            if -620<=x<=-20 and -200<=y<=400:
                k=Koord2Feld()
                feldzahl=k.XY2Feld(x,y)
                b=None
                if self.__dran:
                    b=self.__netzwerk.verschicken(feldzahl)
                    if b:
                        self.__schiff_makieren()
                    self.__dran=False
                    self.__dubistdran(False)
                    self.__netzwerk.empfang()
                    self.__dubistdran(True)
                    self.__dran=True

    def __schiff_makieren(self):
        #Vor:   keine
        #Eff:   Es ist makiert auf dem Spielfeld, das ein Schiff versenkt wurde.
        #       Makier das einfach mit einem grünen Kreis unter dem Spielfeld 

        penup()
        goto(-350+(self.__a*40),-295)
        pendown()
        pencolor("green")
        fillcolor("green")
        begin_fill()
        circle(20)
        end_fill()
        self.__a=self.__a+1

    def __dubistdran(self,dran):
        #Vor:   keine
        #Eff:   Der Raketenstatus ist entsprechend der Variable -dran- verändert

        if dran==True:
            Farbe="green"
        if dran==False:
            Farbe="red"
        penup()
        goto(-220,-390)
        pendown()
        pencolor(Farbe)
        fillcolor(Farbe)
        begin_fill()
        circle(30)
        end_fill()

    def spielfeldzeichnen(self):
        #Vor:   keine
        #Eff:   Das GUI ist ausgegeben.

        speed(0)
        hideturtle()
        penup()
        goto(0,-200)
        pendown()
        pencolor("lightblue")
        fillcolor("lightblue")
        begin_fill()
        right(90)
        for i in range(4):
            fd(600)
            left(90)
        end_fill()
        penup()
        goto(-620,-200)
        pendown()
        begin_fill()
        for i in range(4):
            fd(600)
            left(90)
        end_fill()
        for i in range(11):
            pencolor("black")
            penup()
            goto(0,-200+i*60)
            pendown()
            fd(600)
        left(90)
        for i in range(11):
            penup()
            goto(0+60*i,-200)
            pendown()
            fd(600)
        right(90)
        for i in range(11):
            penup()
            goto(-620,-200+i*60)
            pendown()
            fd(600)
        left(90)
        for i in range(11):
            penup()
            goto(-620+i*60,-200)
            pendown()
            fd(600)
        penup()
        home()
        goto(0,-430)
        pendown()
        fillcolor("Slate Gray")
        pencolor("Slate Gray")
        begin_fill()
        for i in range(2):
            fd(220)
            right(90)
            fd(600)
            right(90)
        end_fill()
        ###Platz der Schiffe
        pencolor("black")
        fillcolor("black")
        penup()
        goto(10,-220)
        pendown()
        begin_fill()
        for i in range(2):
            right(90)
            fd(300)
            right(90)
            fd(60)
        end_fill()
        penup()
        goto(320,-220)
        pendown()
        begin_fill()
        for i in range(2):
            right(90)
            fd(240)
            right(90)
            fd(60)
        end_fill()
        penup()
        goto(10,-290)
        pendown()
        begin_fill()
        for i in range(2):
            right(90)
            fd(180)
            right(90)
            fd(60)
        end_fill()
        penup()
        goto(200,-290)
        pendown()
        begin_fill()
        for i in range(2):
            right(90)
            fd(180)
            right(90)
            fd(60)
        end_fill()
        penup()
        goto(10,-360)
        pendown()
        begin_fill()
        for i in range(2):
            right(90)
            fd(120)
            right(90)
            fd(60)
        end_fill()
        for i in range(2):
            if i==0:
                farbe="green"
            if i==1:
                farbe="yellow"
            fillcolor(farbe)
            pencolor(farbe)
            penup()
            goto(-20,-430+i*75)
            pendown()
            begin_fill()
            for i in range(4):
                fd(70)
                left(90)
            end_fill()
        pencolor("black")
        penup()
        goto(-600,-420)
        pendown()
        pencolor("black")
        write("Raketenstatus",font=('Arial',35,'normal'))
        penup()
        goto(-600,-320)
        pendown()
        write("Versenkt",font=('Arial',35,'normal'))
        for i in range(5):
            penup()
            goto(-350+(i*40),-295)
            pendown()
            circle(20)
        
