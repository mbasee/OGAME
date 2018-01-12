from Statek import Statek
from DaneStatki import DaneStatkow
import random

class Flota():
    '''Klasa flota obsluguje utworzenie floty i dzialanie wykonywane z walka.'''
    def __init__(self, dana):
        temp = False
        with open(dana) as plik:
            self.linia = filter(None, (line.rstrip() for line in plik))
        self.statki = []
        self.skr = []
        self.ilosc = []

        for i in self.linia[1:]:
            z = int(i.split()[1])
            if z >= 1:
                while z >= 1:
                    S1 = Statek(i.split()[0])
                    self.statki.append(S1)
                    self.skr.append(i.split()[0])
                    self.ilosc.append(1)
                    z -= 1
            else:
                S1 = Statek(i.split()[0])
                self.statki.append(S1)
                self.skr.append(i.split()[0])
                self.ilosc.append(z)

    def usun_zniszczony(self):
        ''' Metoda obslugujaca usuwanie zniszczonych statkow. '''
        _statki = self.statki[:]
        for k in xrange(len(_statki)):
            # print _statki[k].stan()
            if Statek.czy_zniszczony(_statki[k]) is True:
                self.ilosc[k] = 0


    def losowanie_przeciwnika(self, flota):
        ''' Metoda obslugujaca losowanie przeciwnika do oddania strzalu przez statek.'''
        if len(flota.statki) > 0:
            przeciwnik = random.randint(0, len(flota.statki)-1)
            if int(flota.ilosc[przeciwnik]) != 0:
                return flota.statki[przeciwnik]
            else:
                return self.losowanie_przeciwnika(flota)
        else:
            return False

    def losuj_cel(self, flota, przeciwnik = 0, x = 0):
        ''' Metoda obslugujaca bitwe pomiedzy statkami a przeciwnikami. '''
        while x < len(self.statki)-1:
            if self.ilosc[x] != 0:
                przeciwnik = self.losowanie_przeciwnika(flota)
                if przeciwnik == False:
                    return self.losuj_cel(flota, przeciwnik, x+1)
                strzal = self.statki[x].strzal(przeciwnik)
                if strzal is True:
                    temp = self.statki[0].szybkie_dzialaa(self.skr[x], flota.skr[flota.statki.index(przeciwnik)])
                    temp = 1 - (1/temp)
                    los = random.random()
                    if los < temp:
                        przeciwnik = self.losowanie_przeciwnika(flota)
                        x+=1
                        self.losuj_cel(flota, przeciwnik, x)
            x += 1
    def stan_floty(self):
        ''' Metoda zwracajaca aktualna ilosc floty. '''
        counter = 0
        for i in xrange(len(self.statki)):
            if self.ilosc[i] != 0:
                counter += 1
                # print self.statki[i], self.ilosc[i], self.skr[i]
        print counter, 'count'

# 1 runda
#F1 = Flota("flota_1.txt")
#F1.losuj_cel("flota_2.txt")
# print F1.stan_floty()
# print F1.usun_zniszczony()

# 2 runda
#F1 = Flota("flota_1.txt")
#F2 = Flota("flota_2.txt")
#F2.losuj_cel(F1)

#F1 = Flota("flota_1.txt")
#F2 = Flota("flota_2.txt")
#F1.losuj_cel(F2)




