
#Program som lager en pizza med ingredienser basert på brukers input og legger til summen for hver ingrediens til sluttsummen

print("Velkommen til Pamparious Pizza - Vennligst svar på hvilke ingredienser du ønsker på din pizza ")

Regning = 0

Storrelse = input("Hvor stor pizza vil du ha? - Liten, Medium eller Stor? ")
if Storrelse == "Liten":
    Regning += 100
elif Storrelse == "Medium":
    Regning += 125
else:
    Regning += 150

Pepperoni = input("Ønsker du å legget til Pepperoni? - Ja eller Nei ")
if Pepperoni == "Ja":
    Regning += 25
else:
    Regning = Regning

Ekstra_ost = input("Ønsker du ekstra ost på pizzaen? - Ja eller Nei? ")
if Ekstra_ost == "Ja":
    Regning += 20
else:
    Regning = Regning

Oppsummering = print(f"Din valgte pizza kommer på {Regning} kroner :) ")

