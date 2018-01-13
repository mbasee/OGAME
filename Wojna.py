from Flota import Flota


def gra_glowna(flota_1, flota_2):
    ''' Funkcja realizujaca wojne pomiedzy flotami. Wykonuje 6 rund. '''

    F1 = Flota(flota_1)
    F2 = Flota(flota_2)

    for i in xrange(6):
        if F2.ilosc.count(0) == len(F2.ilosc) or F1.ilosc.count(0) == len(F1.ilosc):
            break

        F2.losuj_cel(F1)  # 2 na 1
        F1.losuj_cel(F2)  # 1 na 2

        F1.usun_zniszczony()
        F2.usun_zniszczony()

    stan_1 = F2.stan_floty()
    stan_2 = F1.stan_floty()
    if stan_2 > stan_1:
        return "Wygrala flota nr 2"
    elif stan_2 < stan_1:
        return "Wygrala flota nr 1"
    else:
        return "Walka zakonczona remisem"

# gra_glowna()