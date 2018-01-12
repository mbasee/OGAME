from DaneStatki import DaneStatkow
import random

class Statek():
    ''' Klasa Statek obsluguje zdarzenia wywolywane na danym statku.'''
    def __init__(self, param):
        self.skr = DaneStatkow.skrot.index(param)
        self.skrot = DaneStatkow.skrot[self.skr]
        self.atak = int(DaneStatkow.atak[self.skr])
        self.nazwa = DaneStatkow.nazwa[self.skr]
        self.oslona = int(DaneStatkow.oslona[self.skr])
        self.punkty_str = int(DaneStatkow.punkty_str[self.skr])

    def strzal(self,statek):
        ''' Metoda obslugujaca oddanie strzalu przez statek.'''
        if self.atak < 0.01 * statek.oslona:
            print 'nie trafilem'
            return False
        else:
            # print 'trafilem'
            self.trafiony(statek)
            return True

    def szybkie_dzialaa(self, skrot,skrot_przec):
        ''' Metoda zwracajaca szanse na oddanie kolejnego strzalu przez statek.'''
        for i in xrange(len(DaneStatkow.szybkie_dziala)):
            try:
                z = DaneStatkow.szybkie_dziala[i].index(skrot)  # nr miejsca
                t = i  # nr linii
            except Exception:
                pass
                # print "Nie znaleziono dziala"
            try:
                x = DaneStatkow.szybkie_dziala[i].index(skrot_przec)  # nr miejsca
                y = i
            except Exception:
                pass
                # print "Nie znaleziono dziala"
        # print t, y+1
        return  int(DaneStatkow.szybkie_dziala[t][y+1])


    def trafiony(self,statek):
        ''' Metoda obslugujaca trafienie, sprawdzenie wybuchu, odejmowanie punktow.
        True - wybuch
        False - zyje'''
        statek.punkty_str -= (self.atak - statek.oslona)
        # print statek.punkty_str,'statek trafiony', self.atak
        index = DaneStatkow.skrot.index(statek.skrot)
        if (statek.oslona - self.atak) < 0:
            statek.oslona = 0
        else:
            statek.oslona = statek.oslona - self.atak
        #print statek.oslona, 'oslona!'
        #print statek.punkty_str, 'pkt!'
        if statek.punkty_str < 0.7 * int(DaneStatkow.punkty_str[index]):
            wybuch = (1 - (float(statek.punkty_str)/ float(DaneStatkow.punkty_str[index])))
            los = random.random()
            if los < wybuch:
                statek.punkty_str = 0

    def czy_zniszczony(statek):
        ''' Metoda sprawdzajaca, czy statek zostal zniszczony.
         True - zniszczony
         False - niezniszczony '''
        if statek.punkty_str <= 0:
            return True
        else:
            return False
    def stan(self):
        ''' Metoda zwracajaca aktualny stan statku. '''

        return self.skrot, self.punkty_str, self.atak, self.oslona

# S = Statek('mt')
# print S.strzal('dt')
