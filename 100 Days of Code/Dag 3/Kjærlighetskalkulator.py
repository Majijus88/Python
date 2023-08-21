
#Program som gir bruker en "kjærlighetsscore" basert på hvor mange ganger bokstavene som utgjør "true love" 
#befinner seg i navnene som skrives inn av bruker.

print("Velkommen til kjærlighetskalkulatoren. Vennligst oppgi to navn for en tilbakemelding på hvor kompatible dere er sammen :)")

navn_1 = input("Hva er navnet på første personen ")
navn_2 = input("Hva er navnet på den andre personen? ")

kombinerte_navn = navn_1.lower() + navn_2.lower()

antall_t = kombinerte_navn.count("t")
antall_r = kombinerte_navn.count("r")
antall_u = kombinerte_navn.count("u")
antall_e = kombinerte_navn.count("e")
forste_tall = antall_t + antall_r + antall_u + antall_e

antall_l = kombinerte_navn.count("l")
antall_o = kombinerte_navn.count("o")
antall_v = kombinerte_navn.count("v")
antall_e = kombinerte_navn.count("e")
andre_tall = antall_l + antall_o + antall_v + antall_e

kombinerte_tall = str(forste_tall) + str(andre_tall)

kombinerte_tall_som_int = int(kombinerte_tall)

if(kombinerte_tall_som_int > 90 or kombinerte_tall_som_int < 10):
    print(f"Deres kombinerte score er {kombinerte_tall_som_int} - Dette medfører enten 10 eller 90 prosent sjans for at forholdet skal fungere. Tar dere sjansen?")
elif(kombinerte_tall_som_int > 40 and kombinerte_tall_som_int < 50):
    print(f"Deres kombinerte score er: {kombinerte_tall_som_int} - Dette er rimelig middelmådig, men gode 50/50 sjans for suksess :)")
else:
    print(f"Deres kombinerte score er: {kombinerte_tall_som_int} - Tja... ")