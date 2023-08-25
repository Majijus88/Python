
#Program som avgjør hvem som tar regningen basert på random funksjonen

import random

Kandidater = ["Kåre", "Åge", "Jonas", "Pelle", "Hjalmar", "Bjarne", "Jeppe", "Kristian", "Tom", "Fredrik"]
antall_mulighter = len(Kandidater)
Taper = random.randint(0, (antall_mulighter - 1))
Person = Kandidater[Taper]
print(f"Den som betaler for dagens lunsj er: {Person}")


#Mer interaktiv versjon der man kan skrive inn navn selv og deretter legge navnene inn i en liste igjennom split() funksjonen
navn_streng = input("Skriv inn navnene til alle, separert med et komma ")
navn_som_liste = navn_streng.split(",")
antall_mulighter_alt = len(navn_som_liste)
Taper_alt = random.randint(0, (antall_mulighter_alt - 1))
Person_alt = navn_som_liste[Taper_alt]
print(f"Den som betaler for dagens lunsj er: {Person_alt}")


#Enklere versjon av den interaktive versjonen som tar i bruk choice() funksjonen
navn_streng = input("Skriv inn navnene til alle, separert med et komma ")
navn_som_liste_alt = navn_streng.split(",")
Betaler = random.choice(navn_som_liste_alt)
print(f"Den som betaler for dagens lunsj er: {Betaler}")

