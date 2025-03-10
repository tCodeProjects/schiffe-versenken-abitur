#Autor:     Sophie Baudach
#Datum:     03.03.2016
#Zweck:     Schiffe versenken

#IMPORTIEREN
from turtle import *
from time import clock
from Spielfeld import *

#--------------------------------------------------------------------------

#HP
reset()
s=Spielfeld(55599)
s.getTheScreen().onclick(s.klick,1)
