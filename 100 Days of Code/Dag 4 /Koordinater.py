
#Program som lar brukeren legge inn en oransje boks på input basert på koordinater i et grid oppsett

import random

          #0    #1    #2
rad_1 = ["🟥", "🟥", "🟥"] #0
rad_2 = ["🟥", "🟥", "🟥"] #1
rad_3 = ["🟥", "🟥", "🟥"] #2

rader = [rad_1, rad_2, rad_3]
print(f"{rad_1}\n{rad_2}\n{rad_3}\n")

koordinat1 = int(input("Vennligst skriv inn første koordinat (0 - 2):"))
koordinat2 = int(input("Venligst skriv inn andre koordinat (0 - 2):"))

rader[koordinat1][koordinat2] = "🟧"
print(f"{rad_1}\n{rad_2}\n{rad_3}\n")


#Alternativ versjon ved hjelp av random funksjonen

              #0    #1    #2
rad_1_alt = ["🟥", "🟥", "🟥"] #0
rad_2_alt = ["🟥", "🟥", "🟥"] #1
rad_3_alt = ["🟥", "🟥", "🟥"] #2

rader_alt = [rad_1_alt, rad_2_alt, rad_3_alt]
print(f"{rad_1_alt}\n{rad_2_alt}\n{rad_3_alt}\n")

random_koordinat1 = random.randint(0,2)
random_koordinat2 = random.randint(0,2)

rader_alt[random_koordinat1][random_koordinat2] = "🟦"
print(f"{rad_1_alt}\n{rad_2_alt}\n{rad_3_alt}\n")