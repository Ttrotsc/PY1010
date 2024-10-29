# -*- coding: utf-8 -*-
"""
Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne de årlige 
kostnadene ved elbil sammenliknet med bensinbil.

Lag et Python-program som beregner og presenterer (i konsollen) de årlige totalkostnadene for elbil og for bensinbil samt 
årlig kostnadsdifferanse basert på informasjonen gitt nedenfor. 
Du kan her for enkelhets skyld se bort fra kostnader som renter på billån og 
verditap (du har da egentlig antatt at slike kostnader er like for elbil og bensinbil).

Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, men ikke ifm. denne oppgaven :-)

Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
Lykke til!


"""
import locale
locale.setlocale(locale.LC_ALL, 'no_NO.UTF-8')  # Setter norsk lokalitet

KM_AAR = 10000 #ant kjørte kilometer
EL_FOR_AAR = 5000 #forsikring kr/år elbil
BEN_FOR_AAR = 7500 #forsikring kr/år bensinbil 
BIL_TFA_AAR = 8.38*365 #trafikkforsikringsavgift uansett type bil pr år
EL_KR_KWH_KM = 0.2*2 #drivstoffkostnader per km kjørt elbil
EL_KR_KWH_KM_AAR=EL_KR_KWH_KM*KM_AAR #drivstoffkostnader per år elbil
BEN_KR_KM = 1 #drivstoffkostnader per km kjørt bensinbil
BEN_KR_KM_AAR=BEN_KR_KM*KM_AAR #drivstoffkostnader per år bensinbil
EL_BOM_KM = 0.1 #bomkostnader per km elbil
BEN_BOM_KM = 0.3 #bomkostnader per km bensinbil
EL_BOM_KM_AAR=EL_BOM_KM*KM_AAR #bomkostnader per år elbil
BEN_BOM_KM_AAR= BEN_BOM_KM*KM_AAR #bokkostnader per år bensinbil
EL_TOTKOST_AAR = EL_FOR_AAR + BIL_TFA_AAR + (KM_AAR*EL_KR_KWH_KM)+(KM_AAR*EL_BOM_KM) #totale kostander for elbil per år gitt KMAAR km
BEN_TOTKOST_AAR =  BEN_FOR_AAR + BIL_TFA_AAR + (KM_AAR*BEN_KR_KM)+(KM_AAR*BEN_BOM_KM) #totale kostnader for bensingbil per år gitt KMAAR km.
EL_TOTKOST_AAR_AVRUND = int(EL_TOTKOST_AAR) # runder av til heltall
BEN_TOTKOST_AAR_AVRUND = int(BEN_TOTKOST_AAR) # runder av til heltall
EL_TOTKOST_AAR_TUSENST = locale.format_string('%d', EL_TOTKOST_AAR, grouping=True) #spesifiserer at det skal være heltakk og siden jeg har brukt norsk locale blir grupperingen tusenskilletegn med mellomrom
BEN_TOTKOST_AAR_TUSENST = locale.format_string ('%d', BEN_TOTKOST_AAR, grouping=True) # se over
DIFFERANSE_BE_EL=BEN_TOTKOST_AAR - EL_TOTKOST_AAR
DIFFERANSE_BE_EL_TUSENST=locale.format_string ('%d', DIFFERANSE_BE_EL, grouping= True) #se over
 

print('Trafikkforsikringsavgift per år:', BIL_TFA_AAR,',-')
print ('Forsikring for elbil per år:', EL_FOR_AAR,',-')
print ('Forsikring for bensinbil per år', BEN_FOR_AAR,',-')
print ('Drivstoffkostnader for elbil pr år:', EL_KR_KWH_KM*KM_AAR,',-')
print ('Drivstoffkostnader for bensinbil per år:', BEN_KR_KM_AAR,'-')
print ('Bomkostnader for elbil per år:', EL_BOM_KM_AAR,',-')
print ('Bomkostnader for bensinbil per år:', BEN_BOM_KM_AAR,',-')
print ('Totale kostnader for elbil per år:', EL_TOTKOST_AAR_TUSENST,'-')
print ('Totale kostnader for bensinbil per år:', BEN_TOTKOST_AAR_TUSENST,',-')
#print ('Forskjell i totale kostnader for bensinbil vs elbil per år:', int(BEN_TOTKOST_AAR - EL_TOTKOST_AAR),',-')
print('Forskjell i totale kostnader for bensinbil vs elbil per år:', DIFFERANSE_BE_EL_TUSENST,',-')

