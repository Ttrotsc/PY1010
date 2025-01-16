# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:43:56 2024

Oppgave 2.3 til innlevering i PY1010

Oppg 3) Lag et program med en funksjon som regner om fra grader til radianer.
Programmet skal starte med:
import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))
Radiantallet til vinkelen regnes så ut ved følgende formel: v_rad = v_grad*np.pi/180
Resultatet v_rad skrives til skjerm med passende tekst og verdi.
Merk: np.pi er en ferdiglaget funksjon som gir verdien 3.1415....

@author: turida
"""

import numpy as np
v_grad = int(float(input('Skriv inn gradtallet:' )))
v_rad =round((v_grad*np.pi/180), 3)
print(v_grad,'grader er', v_rad,'radianer')