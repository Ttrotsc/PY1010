# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:51:31 2024

Oppgave 2.4 til innlevering i PY1010

Oppg 4)
a) Opprett en dictionary som gitt under. Dictionaryen har ulike land som nøkkel (Keys)
og gir info om hovedstaden i landet og antall innbyggere i mill. i hovedstaden.
b) Lag et program som ber brukeren skrive inn et land (eksempelvis England).
Programmet skal på bakgrunn av dette skrive ut følgende setning:
London er hovedstaden i England og det er 8.982 mill. innbyggere i London
c) Lag et program som ber brukeren skrive inn info om et nytt land (altså et land som
ikke allerede finnes i dictionaryen data). Videre skal brukeren oppgi hovedstad og
antall innbyggere for det «nye» landet. Programmet skal så utvide/oppdatere
dictionaryen med den nye informasjonen. Dictionaryen data skrives så til skjerm.


@author: turida
"""


land_dict = {
        "Norge": {"hovedstad": "Oslo", "innbyggere": "0.77"},
        "Sverige": {"hovedstad": "Stockholm", "innbyggere": "0.98"},
        "Danmark": {"hovedstad": "København", "innbyggere": "0.64"},
      }
land = input("Skriv inn et land i Skandinavia: ")
frabruker = land_dict[land]
print (frabruker["hovedstad"], "er hovedstaden i ", land," og det er ", frabruker["innbyggere"], " mill. innbyggere i ", frabruker["hovedstad"])

land_ny= (input("Skriv inn et valgfritt land: "))
hovedstad_ny = input ("Skriv inn hovedstaden i dette landet: ")
innbygger_ny = input ("Skriv inn antall innbyggere i hovedstaden i millioner: ")
land_dict [land_ny] = {"hovedstad": hovedstad_ny, "innbyggere": innbygger_ny}
print(land_dict)