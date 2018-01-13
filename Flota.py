from Statek import Statek
from DaneStatki import DaneStatkow
import random

class Flota():
    '''Klasa flota obsluguje utworzenie floty oraz dzialania wykonywane z walka.'''
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
        return self.ilosc.count(1)




