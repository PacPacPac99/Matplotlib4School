import numpy as np
import matplotlib.pyplot as plt 
import os
import time
import math
from tkinter import *
glavniScreen = Tk()

def Ocisti():
    poljeunosaA.delete(0,END)
    poljeunosaB.delete(0,END)
    poljeunosaC.delete(0,END) 

def Izracunaj():
    plt.grid(True)
    rasponNaX = 10
    #dohvati vrijednosti iz polja
    a = float(poljeunosaA.get())
    b = float(poljeunosaB.get())
    c = float(poljeunosaC.get())
    D = float(math.pow(b,2)-4*a*c)
    
    #TJEME PARABOLE
    x0 = (-1*b)/(2*a)
    y0 = (4*a*c-math.pow(b,2))/(4*a)

    #Definiramo polja koje sadrže koordinate točaka koje planiramo nacrtati
    tockeX = []
    tockeY = []
    #Ovisno o vrijednosti diskriminante nacrtaj graf s takvim osobinama
    if D > 0:
        x1 = float((-b+math.sqrt(D))/(2*a))
        x2 = float((-b-math.sqrt(D))/(2*a))
        #U niz točaka za crtanje dodaj rješenja kvadratne jednadžbe
        tockeX.append(x1)
        tockeX.append(x2)
        tockeY.append(0)
        tockeY.append(0)
        #U niz točaka za crtanje dodaj tjeme parabole
        tockeX.append(x0)
        tockeY.append(y0)
    elif D == 0:
        x1 = float((-1*b)/(2*a))
        tockeX.append(x1)
        tockeY.append(0)
        tockeX.append(x0)
        tockeY.append(y0)
    else:
        tockeX.append(x0)
        tockeY.append(y0)

    #PRIPREMI SVE ZA CRTANJE
    global xos
    xos = np.arange(float(x0-rasponNaX),float(x0+rasponNaX),0.01) #Odredi interval grafa
    global yos
    yos = (a*xos*xos+(b*xos)+c) #Definiramo krivulju
    
    
    #Određujemo raspon prikaza x-osi i y-osi
    if a < 0:
        plt.xlim(x0-rasponNaX,x0+rasponNaX)
        plt.ylim(x0-rasponNaX,x0+4)
    if a > 0:
        plt.xlim(x0-rasponNaX,x0+rasponNaX)
        plt.ylim(x0-4,x0+rasponNaX)
    

    #DODAJ SVOJSTVA CRTEŽU
    #plt.axis("equal") #izjednačava brojke na x i y osi
    plt.scatter(tockeX,tockeY, marker="o", c="y")
    plt.plot(xos,yos, "r-") #nacrtaj krivulju
    plt.vlines(x=0,ymin=-1000,ymax=1000, colors="b") #y os
    plt.hlines(y=0,xmin=-1000,xmax=1000, colors="b") #x os
    plt.ylabel("y-os")
    plt.xlabel("x-os")
    plt.title("Graf kvadratne funkcije")
    plt.legend()
    plt.show()

    #Obriši prethodno stvorene podatke
    del a,b,c,D,x1,x2,x0,y0
    #Isprazni sadržaj liste, ali ne briši listu kao varijablu
    tockeX.clear()
    tockeY.clear()







naslov = Label(glavniScreen, text = "Kalkulator kvadratne jednadzbe")
gumbIzracunaj = Button(glavniScreen, text = "Izracunaj", command=Izracunaj)
gumbOcisti = Button(glavniScreen, text = "Ocisti", command=Ocisti)

labelaA = Label(glavniScreen, text = "a = ")
labelaB = Label(glavniScreen, text = "b = ")
labelaC = Label(glavniScreen, text = "c = ")

poljeunosaA = Entry(glavniScreen, width = 40)
poljeunosaB = Entry(glavniScreen, width = 40)
poljeunosaC = Entry(glavniScreen, width = 40)

labelaRezultat = Label(glavniScreen, text = "")
#stvaranje naslova i texta
naslov.grid(row = 1, column = 0, columnspan = 2)
labelaA.grid(row = 2, column = 0)
labelaB.grid(row = 3, column = 0)
labelaC.grid(row = 4, column = 0)

#stvaranje unosa polja
poljeunosaA.grid(row = 2, column = 1)
poljeunosaB.grid(row = 3, column = 1)
poljeunosaC.grid(row = 4, column = 1)

#stvaranje gumbeka
gumbIzracunaj.grid(row = 5, column = 0, columnspan = 2)
gumbOcisti.grid(row = 6, column = 0, columnspan = 2)

#Započni program
glavniScreen.mainloop()