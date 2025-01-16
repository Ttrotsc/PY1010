# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:23:09 2025

Oppg 6) Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10].
Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet
[-10,10].


@author: turida
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
   return  -2*x - 5

x = np.linspace(-10,10,20)
y = f(x)

plt.plot (x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=-2x-5")


