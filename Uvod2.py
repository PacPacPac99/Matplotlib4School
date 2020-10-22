import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
import matplotlib as mpl
import numpy as np
import pylab

mplstyle.use("fast")
mplstyle.use(["dark_background", "fast"])

x = np.linspace(0,2,100)

povrsina, graf = plt.subplots() #stvori površinu i graf
graf.plot(x,x,label="linear") #dodaj nove podatke
graf.plot(x,x**2,label="quadratic") #dodaj nove podatke
graf.plot(x,x**3,label="cubic") #dodaj nove podatke
graf.set_xlabel("x-os") #dodaj opis pokraj x-osi
graf.set_ylabel("y-os") #dodaj opis pokraj y osi
graf.set_title("Jednostavan graf") #dodaj naziv grafu
graf.legend() #dodaj legendu grafa
plt.show() #prikaži graf u novom prozoru