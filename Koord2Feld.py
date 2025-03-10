#Autoren:   Tobias Schüler
#           Tim Behnke
#Datum:     26.02.2016
#Zweck:     Koordinaten in Feld umwandeln

#----------------------------------------------------------------------------

class Koord2Feld:
    
    def __init__(self):
        pass

    def XY2Feld(self,x,y):
        #Vor:   -x- und -y- sind vom Typ Integer
        #Erg:   Das Feld, welches bei diesen Koordinaten liegt, ist als Integer geliefert.

        #Radar Feld
        #Spalte 1
        if x>=-620 and x<-560:
            if y<=400 and y>=340:
                self.__feld=0
            if y<340 and y>=280:
                self.__feld=10
            if y<280 and y>=220:
                self.__feld=20
            if y<220 and y>=160:
                self.__feld=30
            if y<160 and y>=100:
                self.__feld=40
            if y<100 and y>=40:
                self.__feld=50
            if y<40 and y>=-20:
                self.__feld=60
            if y<-20 and y>=-80:
                self.__feld=70
            if y<-80 and y>=-140:
                self.__feld=80
            if y<-140 and y>=-200:
                self.__feld=90

        #Spalte 2
        if x>=-560 and x<-500:
            if y<=400 and y>=340:
                self.__feld=1
            if y<340 and y>=280:
                self.__feld=11
            if y<280 and y>=220:
                self.__feld=21
            if y<220 and y>=160:
                self.__feld=31
            if y<160 and y>=100:
                self.__feld=41
            if y<100 and y>=40:
                self.__feld=51
            if y<40 and y>=-20:
                self.__feld=61
            if y<-20 and y>=-80:
                self.__feld=71
            if y<-80 and y>=-140:
                self.__feld=81
            if y<-140 and y>=-200:
                self.__feld=91

        #Spalte 3
        if x>=-500 and x<-440:
            if y<=400 and y>=340:
                self.__feld=2
            if y<340 and y>=280:
                self.__feld=12
            if y<280 and y>=220:
                self.__feld=22
            if y<220 and y>=160:
                self.__feld=32
            if y<160 and y>=100:
                self.__feld=42
            if y<100 and y>=40:
                self.__feld=52
            if y<40 and y>=-20:
                self.__feld=62
            if y<-20 and y>=-80:
                self.__feld=72
            if y<-80 and y>=-140:
                self.__feld=82
            if y<-140 and y>=-200:
                self.__feld=92

        #Spalte 4
        if x>=-440 and x<-380:
            if y<=400 and y>=340:
                self.__feld=3
            if y<340 and y>=280:
                self.__feld=13
            if y<280 and y>=220:
                self.__feld=23
            if y<220 and y>=160:
                self.__feld=33
            if y<160 and y>=100:
                self.__feld=43
            if y<100 and y>=40:
                self.__feld=53
            if y<40 and y>=-20:
                self.__feld=63
            if y<-20 and y>=-80:
                self.__feld=73
            if y<-80 and y>=-140:
                self.__feld=83
            if y<-140 and y>=-200:
                self.__feld=93

        #Spalte 5
        if x>=-380 and x<-320:
            if y<=400 and y>=340:
                self.__feld=4
            if y<340 and y>=280:
                self.__feld=14
            if y<280 and y>=220:
                self.__feld=24
            if y<220 and y>=160:
                self.__feld=34
            if y<160 and y>=100:
                self.__feld=44
            if y<100 and y>=40:
                self.__feld=54
            if y<40 and y>=-20:
                self.__feld=64
            if y<-20 and y>=-80:
                self.__feld=74
            if y<-80 and y>=-140:
                self.__feld=84
            if y<-140 and y>=-200:
                self.__feld=94

        #Spalte 6
        if x>=-320 and x<-260:
            if y<=400 and y>=340:
                self.__feld=5
            if y<340 and y>=280:
                self.__feld=15
            if y<280 and y>=220:
                self.__feld=25
            if y<220 and y>=160:
                self.__feld=35
            if y<160 and y>=100:
                self.__feld=45
            if y<100 and y>=40:
                self.__feld=55
            if y<40 and y>=-20:
                self.__feld=65
            if y<-20 and y>=-80:
                self.__feld=75
            if y<-80 and y>=-140:
                self.__feld=85
            if y<-140 and y>=-200:
                self.__feld=95

        #Spalte 7
        if x>=-260 and x<-200:
            if y<=400 and y>=340:
                self.__feld=6
            if y<340 and y>=280:
                self.__feld=16
            if y<280 and y>=220:
                self.__feld=26
            if y<220 and y>=160:
                self.__feld=36
            if y<160 and y>=100:
                self.__feld=46
            if y<100 and y>=40:
                self.__feld=56
            if y<40 and y>=-20:
                self.__feld=66
            if y<-20 and y>=-80:
                self.__feld=76
            if y<-80 and y>=-140:
                self.__feld=86
            if y<-140 and y>=-200:
                self.__feld=96

        #Spalte 8
        if x>=-200 and x<-140:
            if y<=400 and y>=340:
                self.__feld=7
            if y<340 and y>=280:
                self.__feld=17
            if y<280 and y>=220:
                self.__feld=27
            if y<220 and y>=160:
                self.__feld=37
            if y<160 and y>=100:
                self.__feld=47
            if y<100 and y>=40:
                self.__feld=57
            if y<40 and y>=-20:
                self.__feld=67
            if y<-20 and y>=-80:
                self.__feld=77
            if y<-80 and y>=-140:
                self.__feld=87
            if y<-140 and y>=-200:
                self.__feld=97

        #Spalte 9
        if x>=-140 and x<-80:
            if y<=400 and y>=340:
                self.__feld=8
            if y<340 and y>=280:
                self.__feld=18
            if y<280 and y>=220:
                self.__feld=28
            if y<220 and y>=160:
                self.__feld=38
            if y<160 and y>=100:
                self.__feld=48
            if y<100 and y>=40:
                self.__feld=58
            if y<40 and y>=-20:
                self.__feld=68
            if y<-20 and y>=-80:
                self.__feld=78
            if y<-80 and y>=-140:
                self.__feld=88
            if y<-140 and y>=-200:
                self.__feld=98

        #Spalte 10
        if x>=-80 and x<20:
            if y<=400 and y>=340:
                self.__feld=9
            if y<340 and y>=280:
                self.__feld=19
            if y<280 and y>=220:
                self.__feld=29
            if y<220 and y>=160:
                self.__feld=39
            if y<160 and y>=100:
                self.__feld=49
            if y<100 and y>=40:
                self.__feld=59
            if y<40 and y>=-20:
                self.__feld=69
            if y<-20 and y>=-80:
                self.__feld=79
            if y<-80 and y>=-140:
                self.__feld=89
            if y<-140 and y>=-200:
                self.__feld=99



        #Schiffe Feld
        #Spalte 1 (0;10;20;30;40;50;60;70;80;90)
        if x>=0 and x<60:
            if y<=400 and y>=340:
                self.__feld=0
            if y<340 and y>=280:
                self.__feld=10
            if y<280 and y>=220:
                self.__feld=20
            if y<220 and y>=160:
                self.__feld=30
            if y<160 and y>=100:
                self.__feld=40
            if y<100 and y>=40:
                self.__feld=50
            if y<40 and y>=-20:
                self.__feld=60
            if y<-20 and y>=-80:
                self.__feld=70
            if y<-80 and y>=-140:
                self.__feld=80
            if y<-140 and y>=-200:
                self.__feld=90
                
        #Spalte 2 (1;11;21;31;41;51;61;71;81;91)
        if x>=60 and x<120:
            if y<=400 and y>=340:
                self.__feld=1
            if y<340 and y>=280:
                self.__feld=11
            if y<280 and y>=220:
                self.__feld=21
            if y<220 and y>=160:
                self.__feld=31
            if y<160 and y>=100:
                self.__feld=41
            if y<100 and y>=40:
                self.__feld=51
            if y<40 and y>=-20:
                self.__feld=61
            if y<-20 and y>=-80:
                self.__feld=71
            if y<-80 and y>=-140:
                self.__feld=81
            if y<-140 and y>=-200:
                self.__feld=91

        #Spalte 3
        if x>=120 and x<180:
            if y<=400 and y>=340:
                self.__feld=2
            if y<340 and y>=280:
                self.__feld=12
            if y<280 and y>=220:
                self.__feld=22
            if y<220 and y>=160:
                self.__feld=32
            if y<160 and y>=100:
                self.__feld=42
            if y<100 and y>=40:
                self.__feld=52
            if y<40 and y>=-20:
                self.__feld=62
            if y<-20 and y>=-80:
                self.__feld=72
            if y<-80 and y>=-140:
                self.__feld=82
            if y<-140 and y>=-200:
                self.__feld=92

        #Spalte 4
        if x>=180 and x<240:
            if y<=400 and y>=340:
                self.__feld=3
            if y<340 and y>=280:
                self.__feld=13
            if y<280 and y>=220:
                self.__feld=23
            if y<220 and y>=160:
                self.__feld=33
            if y<160 and y>=100:
                self.__feld=43
            if y<100 and y>=40:
                self.__feld=53
            if y<40 and y>=-20:
                self.__feld=63
            if y<-20 and y>=-80:
                self.__feld=73
            if y<-80 and y>=-140:
                self.__feld=83
            if y<-140 and y>=-200:
                self.__feld=93

        #Spalte 5
        if x>=240 and x<300:
            if y<=400 and y>=340:
                self.__feld=4
            if y<340 and y>=280:
                self.__feld=14
            if y<280 and y>=220:
                self.__feld=24
            if y<220 and y>=160:
                self.__feld=34
            if y<160 and y>=100:
                self.__feld=44
            if y<100 and y>=40:
                self.__feld=54
            if y<40 and y>=-20:
                self.__feld=64
            if y<-20 and y>=-80:
                self.__feld=74
            if y<-80 and y>=-140:
                self.__feld=84
            if y<-140 and y>=-200:
                self.__feld=94

        #Spalte 6
        if x>=300 and x<360:
            if y<=400 and y>=340:
                self.__feld=5
            if y<340 and y>=280:
                self.__feld=15
            if y<280 and y>=220:
                self.__feld=25
            if y<220 and y>=160:
                self.__feld=35
            if y<160 and y>=100:
                self.__feld=45
            if y<100 and y>=40:
                self.__feld=55
            if y<40 and y>=-20:
                self.__feld=65
            if y<-20 and y>=-80:
                self.__feld=75
            if y<-80 and y>=-140:
                self.__feld=85
            if y<-140 and y>=-200:
                self.__feld=95

        #Spalte 7
        if x>=360 and x<420:
            if y<=400 and y>=340:
                self.__feld=6
            if y<340 and y>=280:
                self.__feld=16
            if y<280 and y>=220:
                self.__feld=26
            if y<220 and y>=160:
                self.__feld=36
            if y<160 and y>=100:
                self.__feld=46
            if y<100 and y>=40:
                self.__feld=56
            if y<40 and y>=-20:
                self.__feld=66
            if y<-20 and y>=-80:
                self.__feld=76
            if y<-80 and y>=-140:
                self.__feld=86
            if y<-140 and y>=-200:
                self.__feld=96

        #Spalte 8
        if x>=420 and x<480:
            if y<=400 and y>=340:
                self.__feld=7
            if y<340 and y>=280:
                self.__feld=17
            if y<280 and y>=220:
                self.__feld=27
            if y<220 and y>=160:
                self.__feld=37
            if y<160 and y>=100:
                self.__feld=47
            if y<100 and y>=40:
                self.__feld=57
            if y<40 and y>=-20:
                self.__feld=67
            if y<-20 and y>=-80:
                self.__feld=77
            if y<-80 and y>=-140:
                self.__feld=87
            if y<-140 and y>=-200:
                self.__feld=97

        #Spalte 9
        if x>=480 and x<540:
            if y<=400 and y>=340:
                self.__feld=8
            if y<340 and y>=280:
                self.__feld=18
            if y<280 and y>=220:
                self.__feld=28
            if y<220 and y>=160:
                self.__feld=38
            if y<160 and y>=100:
                self.__feld=48
            if y<100 and y>=40:
                self.__feld=58
            if y<40 and y>=-20:
                self.__feld=68
            if y<-20 and y>=-80:
                self.__feld=78
            if y<-80 and y>=-140:
                self.__feld=88
            if y<-140 and y>=-200:
                self.__feld=98

        #Spalte 10
        if x>=540 and x<600:
            if y<=400 and y>=340:
                self.__feld=9
            if y<340 and y>=280:
                self.__feld=19
            if y<280 and y>=220:
                self.__feld=29
            if y<220 and y>=160:
                self.__feld=39
            if y<160 and y>=100:
                self.__feld=49
            if y<100 and y>=40:
                self.__feld=59
            if y<40 and y>=-20:
                self.__feld=69
            if y<-20 and y>=-80:
                self.__feld=79
            if y<-80 and y>=-140:
                self.__feld=89
            if y<-140 and y>=-200:
                self.__feld=99
        return self.__feld

#------------------------------------------------------------------------------
    
    def eckkoord(self,feld,rechtesBrett):
        #Vor:   -feld- ist vom Typ Integer
        #       -brett- ist vom Typ boolean
        #Erg:   Die linken unteren Eckkoordinaten des Feldes sind geliefert.
        
        c=feld//10
        a=0
        if rechtesBrett:
            a=620
        return (-620+((feld-(c*10))*60)+a),(340-(c*60))
        
        
