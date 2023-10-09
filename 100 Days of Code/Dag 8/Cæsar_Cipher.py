
import ACSII_bilde
def krypter(ren_tekst, forskyving):
    kryptert = ""
    for bokstav in ren_tekst:
        posisjon = alfabetet.index(bokstav)
        ny_posisjon = posisjon + forskyving
        ny_bokstav = alfabetet[ny_posisjon]
        kryptert += ny_bokstav
    print(f"Ditt krypterte ord er: {kryptert}")

def dekrypter(kryptert_tekst, forskyving):
    dekryptert = ""
    for bokstav in kryptert_tekst:
        posisjon = alfabetet.index(bokstav)
        ny_posisjon = posisjon - forskyving
        ny_bokstav = alfabetet[ny_posisjon]
        dekryptert += ny_bokstav
    print(f"Ditt dekrypterte ord er: {dekryptert}")

alfabetet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']

print(ACSII_bilde.logo)

fortsette_program = True
while fortsette_program:

    valg = input("Velkommen! Ønsker du å kryptere eller dekryptere? ").lower()

    if valg == "kryptere":
        bruker_input_krypter = input("Vennligst skriv inn ordet du ønsker å kryptere: ").lower()
        bruker_forskyving_krypter = input("Vennligst velg ønsket forskyvning ")
        bruker_forskyving_krypter = bruker_forskyving_krypter % 28
        krypter(ren_tekst=bruker_input_krypter, forskyving=bruker_forskyving_krypter)
    
    elif valg == "dekryptere":
        bruker_input_dekrypter = input("Vennligst skriv inn ordet du ønsker å kryptere: ").lower()
        bruker_forskyving_dekrypter = input("Vennligst velg ønsket forskyvning ")
        bruker_forskyving_dekrypter = bruker_forskyving_dekrypter % 28
        dekrypter(kryptert_tekst=bruker_input_dekrypter, forskyving=bruker_forskyving_dekrypter)

    fortsette = input("Ønsker du å prøve igjen? Skriv ja, eller nei ").lower()
    if fortsette == "nei":
        print("Takk for nå :)")
        fortsette_program = False
