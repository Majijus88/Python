
#Programmet sjekker om et oppgitt årstall var et skuddår

input_aar = int(input("Skriv inn et årstall, så får du vite om det var et skuddår! "))

sjekk_1 = input_aar % 4
sjekk_2 = input_aar % 100
sjekk_3 = input_aar % 400


if sjekk_1 == 0:
    if sjekk_2 == 0:
        if sjekk_3 == 0:
            print(f"Året: {input_aar} er et skuddår")
        else:
            print(f"Året: {input_aar} var ikke et skuddår")
    else:
        print(f"Året: {input_aar} var ikke et skuddår")
else:
    print(f"Året: {input_aar} var ikke et skuddår")