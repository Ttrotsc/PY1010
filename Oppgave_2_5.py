# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:57:54 2025

Oppgave 2.5 innlevering i PY1010

Oppg 5) Lag et program med en funksjon som tar a og b som inn-argumenter og som så
regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en
halvsirkel, se figuren under. Med «ytre» omkrets menes samlet lengde av de sorte strekene.
Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende
tekst.



@author: turida


def hils(name):
    print("Hei", (name),"!")

# Kalle funksjonen
hils("Alice")
"""

import math
def figur(a,b):
    
 
    r= a/2
    areal_halv_sirk = math.pi*r*r/2
    omkrets_halv_sirk = math.pi*r
    areal_trekant = a*b/2
    hypotenus = math.sqrt(a**2 + b**2)
    omkrets_trekant_uten_grunnlinje = b+ hypotenus
    areal_figur = areal_trekant + areal_halv_sirk
    
    
    print("Arealet til en figur med diameter" ,(a), "cm og høyde", (b), "cm er ", round(areal_figur), "cm\u00B2, mens omkretsen er ", round(omkrets_trekant_uten_grunnlinje), "cm." )
   
figur(4,8)