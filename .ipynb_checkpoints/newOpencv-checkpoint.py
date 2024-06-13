import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#parametre du signal
f0=400
duree=2
Fe=2000
#creation du vecteur temps
t=np.linspace(0,duree,int(Fe*duree),endpoint=False)
#creation du signal sinusoidal
signal=np.sin(2*np.pi*f0*t)
#representation du signal
plt.plot(t,signal)
plt.title("signal sinusoidal")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()