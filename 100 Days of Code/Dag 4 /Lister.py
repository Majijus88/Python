
#Lister i Python gir mulighet til å samle data som hører sammen 
#EKS:

Bydeler_Oslo = ["Alna", "Grünerløkka", "Vestre Aker", "Ullern", "Bjerke", "Søndre Nordstrand", "Gæmle Oslo", "Stovner"]
print(Bydeler_Oslo)

#Endre innhold i en liste ved f.eks. korrigering av feil navn. I dette tilfellet Gæmle Oslo --> Gamle Oslo

#Her setter jeg index 6 da dette er plassen tilknyttet navnet som må korrigeres. Dette endrer Gæmle Oslo til Gamle Oslo
Bydeler_Oslo[6] = "Gamle Oslo"
print(Bydeler_Oslo)


#Legge til noe i slutten av en liste ved hjelp av append() funksjonen
Bydeler_Oslo.append("Nordre Aker")
print(Bydeler_Oslo)

#For å legge til flere ting på slutten av listen kan man også bruke extend() funksjonen
Bydeler_Oslo.extend(["Randombydel1", "Randombydel2", "Randombydel4"])
print(Bydeler_Oslo)

#Man kan fjerne noe spesifikt om man bruker remove() funksjonen
Bydeler_Oslo.remove("Randombydel1")
print(Bydeler_Oslo)

print(len(Bydeler_Oslo))
#Man kan legge til noe i en liste på et spesifisert punkt dersom man benytter insert() funksjonen og spesifiserer indeksen
Bydeler_Oslo.insert(10, "Randombydel 3")
print(Bydeler_Oslo) 
