from Flota import Flota


def gra_glowna():
    ''' Funkcja realizujaca wojne pomiedzy flotami. Wykonuje 6 rund. '''

    F1 = Flota("flota_1.txt")
    F2 = Flota("flota_2.txt")

    for i in xrange(6):
        if F2.ilosc.count(0) == len(F2.ilosc) or F1.ilosc.count(0) == len(F1.ilosc):
            break
        F2.stan_floty()
        F1.stan_floty()

        F2.losuj_cel(F1)  # 2 na 1
        F1.losuj_cel(F2)  # 1 na 2

        F1.usun_zniszczony()
        F2.usun_zniszczony()

    print "stan F2: "
    F2.stan_floty()
    print "stan F3: "
    F1.stan_floty()


gra_glowna()