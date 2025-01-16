# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:30:48 2024

Oppgave 2.2 til innlevering i PY1010

Oppg 2) Det skal arrangeres en klassefest og man antar at hver elev 
spiser 1/4 pizza. Lag et program som tar inn antall elever fra konsollen ved
antall_elever = int(input('Skriv inn antall elever:' ))
Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive
svaret til skjerm. Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe
5).
Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?
Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. Hvordan kan
sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)?

@author: turida
"""
import math #importerer pakken math for å bruke mattematiske funksjoner
antall_elever = int(input('Skriv inn antall elever i klassen:')) #input
pizza = 1
elevpizza = pizza/4
pizzabehov = antall_elever*elevpizza #pizzabehovet er gitt av antall elever multiplisert med elevpizza behovet.
hele_pizzabehov = math.ceil(pizzabehov) #runder av svaret til nærmeste hele oppover for ikke å få ,4 pizza til å bli for lite
print ('Basert på antall elever du har oppgitt (',antall_elever,') må det kjøpes inn: ', hele_pizzabehov, 'pizzaer til festen') #printer svaret
