
#Program som genererer et tilfeldig vanskelig passord for brukeren

import random

bokstaver = ["a","b","c","d","e","f","g","h","i","j","k","l","m","o","p","q""r","s","t", 
             "u", "v", "d", "x", "y", "z", "æ", "ø", "å","A","B","C","D","E","F","G","H","I",
             "J","K","L","M","N","O","P","Q","R","S", "T", "U", "V", "W", "X", "Y", "Z", "Æ", "Ø", "Å"]

tallrekke = [1, 2, 3, 4, 5, 6, 7, 8, 9]

tegn = ["@", "!", "$", "#", "=", "?", "&"]

bruker_input_bokstaver = int(input("Hvor mange bokstaver ønsker du?: "))
bruker_input_tall = int(input("Hvor mange tall vil du ha?: "))
bruker_input_tegn = int(input("Hvor mange tegn vil du ha?: "))

lengde_bokstaver = len(bokstaver)
liste_bokstaver = []

for bokstav in range(1, bruker_input_bokstaver + 1):
      random_tall = random.randint(1, lengde_bokstaver)
      random_bokstav = bokstaver[random_tall]
      liste_bokstaver.append(random_bokstav)
     
tilfeldige_bokstaver = "".join(liste_bokstaver)

lengde_tall = len(tallrekke)
liste_tall = []
for tall in range(1, bruker_input_tall + 1):
      random_nummer = random.randint(1, lengde_tall)
      random_tall = tallrekke[random_nummer]
      random_tall = str(random_tall)
      liste_tall.append(random_tall)

tilfeldige_tall = "".join(liste_tall)

lengde_tegn = len(tegn)
liste_tegn = []
for symbol in range(1, bruker_input_tegn + 1):
     random_tegn = random.randint(1, lengde_tegn)
     random_symbol = tegn[random_tegn]
     liste_tegn.append(random_symbol)

tilfeldige_symboler = "".join(liste_tegn)

combo = tilfeldige_bokstaver + tilfeldige_tall + tilfeldige_symboler

print (f"Ditt genererte passord er: {combo}")