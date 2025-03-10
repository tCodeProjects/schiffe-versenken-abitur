#Autor:     Tobias Schüler
#Datum:     25.02.2016
#Zweck:     Schiffeversenken

#IMPORTIEREN
from turtle import*

#---------------------------------------------------------------------------

class Stecker():
    
    def __init__(self,treffer,x,y):
        #Vor:   -treffer- ist vom Typ boolean
        #       -x-,-y- sind vom Typ Integer
        #Eff:   Das entsprechende Feld ist mit einem Stecker makiert, dieser
        #       signalisiert entweder einen Treffer oder einen Nicht-Treffer
        
        t=Turtle()
        self.__treffer=treffer
        t.speed(0)
        t.hideturtle()
        farbe="darkblue"
        if treffer:farbe="orange"
        t.penup()
        t.fillcolor(farbe)
        t.pencolor(farbe)
        t.goto(x,y)
        t.fd(30)
        t.pendown()
        t.begin_fill()
        t.right(180)
        t.circle(30)
        t.end_fill()
        t.right(180)

