# -*- coding: utf-8 -*-
"""
Oppgave 2.1 til innlevering i PY1010

Oppg 1) Du skal her lage et program som skal starter med
alder = int(input('Hvilket år er du født? ') )
Programmet skal så regne ut hvor gammel personen blir nå i løpet av år 2024 og skrive
svaret til skjerm med passende tekst.


Turid Trötscher
29 okt 24 
"""

alder = int(input('Hvilket år er du født?'))
alderidag = 2024 - alder
print('I løpet av 2024 blir du', alderidag, 'år')