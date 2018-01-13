from appJar import gui
from Wojna import gra_glowna


def press(button):
    skroty = ["mt", "dt", "lm", "cm", "kr", "ow", "sk", "re", "ss", "b", "n", "gs", "p"]
    if button == "EXIT":
        app.stop()
    else:
        z = app.getAllEntries()
        flota_1 = open("flota.1.txt", "w")
        flota_2 = open("flota.2.txt", "w")

        flota_2.write('skrot ilosc')
        flota_2.write("\n")

        flota_1.write('skrot ilosc')
        flota_1.write("\n")
        pom = 0
        for i in xrange(1, len(z)+1, 2):
            flota_1.write(skroty[pom])
            flota_1.write(" ")
            a = int(z["" + str(i) + ""])
            flota_1.write(str(a))
            flota_1.write("\n")
            pom += 1

        pom = 0
        for x in xrange(2, len(z)+1, 2):
            flota_2.write(skroty[pom])
            flota_2.write(" ")
            a = int(z["" + str(x) + ""])
            flota_2.write(str(a))
            flota_2.write("\n")
            pom += 1
        flota_1.close()
        flota_2.close()
        print "zapisano"
        gra = gra_glowna("flota.2.txt", "flota.1.txt")
        app.infoBox("info", gra)



app = gui("OGAME", "777x600")
app.setBg("grey")
app.setFont(18)
app.addLabel("title_1", "FLOTA #1: ", 0)

app.addLabel("title_2", "FLOTA #2: ", 0, 2)
app.setLabelBg("title_1", "blue")
app.setLabelBg("title_2", "blue")
app.addLabel("mt_1", "mt", 1)
app.addLabel("mt_2", "mt", 1, 2)
app.addLabel("dt_1", "dt", 2)
app.addLabel("dt_2", "dt", 2, 2)
app.addLabel("lm_1", "lm", 3)
app.addLabel("lm_2", "lm", 3, 2)
app.addLabel("cm_1", "cm", 4)
app.addLabel("cm_2", "cm", 4, 2)
app.addLabel("kr_1", "kr", 5)
app.addLabel("kr_2", "kr", 5, 2)
app.addLabel("ow_1", "ow", 6)
app.addLabel("ow_2", "ow", 6, 2)
app.addLabel("sk_1", "sk", 7)
app.addLabel("sk_2", "sk", 7, 2)
app.addLabel("re_1", "re", 8)
app.addLabel("re_2", "re", 8, 2)
app.addLabel("ss_1", "ss", 9)
app.addLabel("ss_2", "ss", 9, 2)
app.addLabel("b_1", "b", 10)
app.addLabel("b_2", "b", 10, 2)
app.addLabel("n_1", "n", 11)
app.addLabel("n_2", "n", 11, 2)
app.addLabel("gs_1", "gs", 12)
app.addLabel("gs_2", "gs", 12, 2)
app.addLabel("p_1", "p", 13)
app.addLabel("p_2", "p", 13, 2)

app.addNumericEntry("1", 1, 1)
app.addNumericEntry("2", 1, 3, 0)
app.addNumericEntry("3", 2, 1)
app.addNumericEntry("4", 2, 3, 0)
app.addNumericEntry("5", 3, 1)
app.addNumericEntry("6", 3, 3, 0)
app.addNumericEntry("7", 4, 1)
app.addNumericEntry("8", 4, 3, 0)
app.addNumericEntry("9", 5, 1)
app.addNumericEntry("10", 5, 3, 0)
app.addNumericEntry("11", 6, 1)
app.addNumericEntry("12", 6, 3, 0)
app.addNumericEntry("13", 7, 1)
app.addNumericEntry("14", 7, 3, 0)
app.addNumericEntry("15", 8, 1)
app.addNumericEntry("16", 8, 3, 0)
app.addNumericEntry("17", 9, 1)
app.addNumericEntry("18", 9, 3, 0)
app.addNumericEntry("19", 10, 1)
app.addNumericEntry("20", 10, 3, 0)
app.addNumericEntry("21", 11, 1)
app.addNumericEntry("22", 11, 3, 0)
app.addNumericEntry("23", 12, 1)
app.addNumericEntry("24", 12, 3, 0)
app.addNumericEntry("25", 13, 1)
app.addNumericEntry("26", 13, 3, 0)


app.addButtons(["RUN"], press, 14)
app.addButtons(["EXIT"], press, 14, 3)

app.go()
