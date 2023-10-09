
import ACSII_bilde
#Kombinert funksjon som både kan kryptere og dekryptere
def caesar(tekst, forskyvning, rettning):
    ord = ""
    for tegn in tekst:
        if tegn in alfabetet:
            posisjon = alfabetet.index(tegn)
            if rettning == "+":
                ny_posisjon = posisjon + forskyvning
            elif rettning == "-":
                ny_posisjon = posisjon - forskyvning
            ny_bokstav = alfabetet[ny_posisjon]
            ord += ny_bokstav
        #Dersom tegnet ikke finnes i listen over alfabetet, så settes det inn uendret. F.eks. et mellomrom.
        else:
            ord += tegn
    print(f"Ditt resultat er: {ord}")

#Ordliste med alfabetet
alfabetet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']

#Enkel test av funksjonen med direkte input av argumenter til parametere
caesar("Hiv og hoi!", 5, "+")
caesar("Hnæ tl mtn!", 5, "-")

#Printer et velkomstbilde
print(ACSII_bilde.logo)

#Loop som kjører programmet frem til bruker velger å avslutte
fortsette_program = True
while fortsette_program:

    #Spør bruker om det skal krypteres eller dekrypteres
    valg = input("Velkommen! Ønsker du å kryptere eller dekryptere? ").lower()

    #Kjøres dersom bruker skriver "kryptere"
    if valg == "kryptere":
        bruker_input_krypter = input("Vennligst skriv inn ordet du ønsker å kryptere: ").lower()
        bruker_forskyving_krypter = int(input("Vennligst velg ønsket forskyvning "))
        bruker_forskyving_krypter = bruker_forskyving_krypter % 28
        caesar(tekst=bruker_input_krypter, forskyvning=bruker_forskyving_krypter, rettning="+")

    #Kjøres dersom bruker skriver "dekryptere"
    elif valg == "dekryptere":
        bruker_input_dekrypter = input("Vennligst skriv inn ordet du ønsker å kryptere: ").lower()
        bruker_forskyving_dekrypter = int(input("Vennligst velg ønsket forskyvning "))
        bruker_forskyving_dekrypter = bruker_forskyving_dekrypter % 28
        caesar(tekst=bruker_input_dekrypter, forskyvning=bruker_forskyving_dekrypter, rettning="-")

    #Etter kjøring blir bruker spurt om hen ønsker å gjenta prosessen. Om bruker skriver "nei" så avsluttes programmet
    fortsette = input("Ønsker du å prøve igjen? Skriv ja, eller nei ").lower()
    if fortsette == "nei":
        print("Takk for nå :)")
        fortsette_program = False


