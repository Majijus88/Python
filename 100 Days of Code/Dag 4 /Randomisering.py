
#Importerer random modulen til filen
import random

#Printer et random  tall mellom definert startverdi og sluttverdi. I dette tilfellet mellom 1 og 99
random_int = random.randint(1,99)
print(random_int)

#Dersom man importerer inn en annen fil får man mulighet til å benytte seg av data tilknyttet denne filen som f.eks. varia
import Testfil
print(Testfil.pi)
print(Testfil.array)

#Genererer et random float nummer mellom 0,111111111 og 0,99999999999+++)
random_float = random.random()
print(random_float)

#For å utvide tallrekken videre til f.eks. alt mellom 0 - 5 så kan man gange variablen med det høyeste tallet. I dette tilfellet 5
storre_random_float = random_float * 5
print(storre_random_float)

