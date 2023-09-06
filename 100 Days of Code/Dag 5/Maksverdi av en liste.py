
#Dette programmet finner ut hva som er den høyeste verdien i en liste

#Gir bruker mulighet til å skrive inn en rekke scores ved å benytte mellomrom mellom hvert tall. 
#Split funksjonen deler opp strings til ulike items i en liste 
verdier = input("Vennligst skriv inn score-verdi. For å legge til flere benytt SPACE mellom hver input: ").split()

#Lager en tom hjelpevariabel som får verdi fra for-loopen
maks_verdi = 0


for verdi in verdier:
    #Caster om fra string til int
    verdi = int(verdi)
    #Dersom verdien av verdi variabelen er høyere enn det som ligger lagret i maks_verdi, oppdateres maks_verdi
    if verdi > maks_verdi:
        maks_verdi = verdi
         
#Printer ut output til bruker
print(f"Den maksimale verdien i score-listen var: {maks_verdi}")
         