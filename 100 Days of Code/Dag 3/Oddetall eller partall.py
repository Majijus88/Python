
#Programmet sjekker ut om tallet som gis som input er et oddetall eller et partall

tall_input = int(input("Skriv inn et tall og du får svar på om det er et partall eller oddetall "))

if tall_input % 2 > 0:
    print(f"Tallet: {tall_input} er et oddetall")
else:
    print(f"Tallet: {tall_input} er et partall")