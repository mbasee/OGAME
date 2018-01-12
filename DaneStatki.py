class DaneStatkow:
    ''' Wczytanie danych wszystkich statkow(skrot, nazwa, punkty_strukturalne, oslona, atak)'''
    skrot = []
    nazwa = []
    punkty_str = []
    oslona = []
    atak = []
    szybkie_dziala = []

    def __init__(self):
        ''' Pobranie danych z pliku i wczytanie ich do poszczegolnych tablic.'''
        temp = False
        with open("dane_statkow.txt") as plik:
            self.linia = filter(None, (line.rstrip() for line in plik))

        for i in self.linia:
            if temp is True:
                self.skrot.append(i.split()[0])
                self.nazwa.append(i.split()[1])
                self.punkty_str.append(i.split()[2])
                self.oslona.append(i.split()[3])
                self.atak.append(i.split()[4])
            else:
                temp = True
        with open("szybkie_dziala.txt") as plik1:
            linia = filter(None, (linia.rstrip() for linia in plik1))
        for x in linia[1 :]:
            self.szybkie_dziala.append(x.split())

DS = DaneStatkow()
