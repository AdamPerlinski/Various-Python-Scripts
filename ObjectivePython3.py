import math
class Rownanie():
    def __init__(self):
        self.a = (int(input("A: "))) 
        self.b = (int(input("B: ")))
        self.c = (int(input("C: ")))
        if self.a == 0 and self.b != 0:
            print(("Rozwiazanie:",-self.c/self.b))
            raise SystemExit
        elif self.a == 0 and self.b == 0 and self.c == 0:
            print(("Rownanie tozszamosciowe"))
            raise SystemExit
        elif self.a == 0 and self.b == 0 and self.c != 0:
            print(("Rownanie sprzeczne"))
            raise SystemExit
    def oblicz_delte(self):
        self.delta = self.b * self.b - ( 4 * self.a * self.c)
    def formatuj_rownanie(self):
        if self.a == 1:
            print("xx",end='', sep='')
        elif self.a == -1:
            print("-xx", sep='')
        else:
            print (self.a,"xx",end='', sep='')
        if self.b == 0:
            pass
        elif self.b > 0:
            print("+",self.b,"x",end='', sep='')
        else:
            print(self.b,"x",end='', sep='')
        if self.c == 0:
            pass
        elif self.b > 0:
            print("+",self.c, sep='')
        else:
            print(self.c)
    def oblicz(self):
        if self.delta < 0:
            real = (-self.b/(2*self.a))
            imagin = math.sqrt(math.fabs(self.delta))/(2*self.a)
            self.urojona=complex(real,imagin)
            self.urojonadruga=complex(real,-imagin)
            self.flaga=0
        elif self.delta > 0:
            self.rozwiazanie = (-self.b - math.sqrt(self.delta))/(2*self.a)
            self.rozwiazaniedrugie = (-self.b - math.sqrt(self.delta))/(2*self.a)
            self.flaga=1
        else:
            self.rozwiazanie = (-self.b)/(2*self.a)
            self.flaga=2
    def ending(self):
        print("Rozwiazanie tego rownania: ")
        if self.flaga == 0:
            print(self.urojona)
            print(self.urojonadruga)
        elif self.flaga ==1:
            print(self.rozwiazanie)
            print(self.rozwiazaniedrugie)
        else:
            print(self.rozwiazanie)
            
        
        
            
B = Rownanie()
B.oblicz_delte()
B.formatuj_rownanie()
B.oblicz()
B.ending()



