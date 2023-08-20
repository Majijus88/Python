
#Program som regner ut hvor mye driks hver person skal betale basert på antall personer og prosentsats

#Printer ut en velkomsthilsen til bruker
velkomst = print("Velkommen til driks-kalkulatoren!")

#Spør etter hva den totale summen på regningen er og caster svaret som float
regning = float(input("Hva er den totale summen på regningen? "))

#Spør etter hvor mange prosent man ønsker å gi i driks
prosent = int(input("Hvor mange prosent ønsker du å gi i driks? "))

#Spør etter antall personer som skal splitte regningen
personer = int(input("Hvor mange personer skal dele regningen? "))

#Utregning som gir svaret på ny totalsum basert på prosenten man ønsket å gi i driks
regning_med_driks = regning + (regning * prosent) / 100

#Deler den nye totalsummen på antallet som skal splitte regningen
regning_delt_paa_antall = regning_med_driks / personer 

#Gir en tilbakemelding til bruker på hvor mye hver person skal betale 
tilbakemelding = print(f"Hver person skal betale: {round(regning_delt_paa_antall, 2)} kr")