###############################
#Hangman program av enkel type#
###############################

#Importerer random funksjonen og andre Python filer for senere bruk av tilhørende variabler
import random
import ASCII
import Ordliste

#Velger ut et tilfeldig ord fra ordlisten tilknyttet filen "Ordliste" ved hjelp av random funksjonen
random_ord = random.choice(Ordliste.word_list).lower()

#Kamuflerer ordet ved å legge til en _ for hver bokstav i ordet igjennom en for-loop
kamuflert_ord = []
lengde_ord = len(random_ord)
for bokstaver in range(lengde_ord):
    kamuflert_ord += "_" 

#Gir brukeren en velkomsthilsen og presenterer antall bokstaver som utgjør ordet
print(ASCII.velkomst_logo)
velkomsthilsen = print("\nVelkommen til Hangman! Du har syv forsøk på å gjette ordet riktig før du blir hengt!")
print(f"Ordet består av: {lengde_ord} bokstaver")
print(kamuflert_ord)

spill_over = False
#Setter antall forsøk spilleren får på å gjette (liv)
antall_liv = 7

#Lar spillet fortsette frem til spilleren eventuelt vinner, eller går tom for liv
while not spill_over and antall_liv > 0:

    #Variabel som lagrer brukers gjettede bokstav
    gjettet = input("\nGjett en bokstav: ")

    #Sjekker om den gjettede bokstaven allerede har blitt gjettet riktig tidligere
    if gjettet in kamuflert_ord:
        print(f"Du har allerede gjettet bokstaven: {gjettet} riktig. Prøv igjen :)")

    #Looper igjennom hver bokstav i det tilfeldige ordet og sjekker om den gjettede bokstaven finnes i ordet
    for index in range(lengde_ord):
        bokstav = random_ord[index]
        #Dersom bokstaven som er gjettet finnes i ordet, settes det inn på riktig posisjon i listen kamuflert_ord
        if bokstav == gjettet:
            kamuflert_ord[index] = bokstav
    
    #Dersom bokstaven som bruke gjetter ikke er en del av ordet, mister bruker ett liv og får feedback på dette
    if gjettet not in kamuflert_ord:
        antall_liv -= 1
        print(ASCII.nivåer[antall_liv])
        print(f"Du gjettet feil og mistet ett liv. Du har {antall_liv} igjen! ")
        #Dersom bruker går tom for liv, får bruker tilbakemelding om dette, samt info om hva som var løsningsordet
        if antall_liv == 0:
            print(f"\nBeklager, men du er død. Det riktige ordet var: {random_ord} ")
            #Spillet avsluttes
            spill_over = True
    
    #Presenterer bruker for gjenværende kamuflerte bokstaver som utgjør det tilfeldige ordet
    print(f"\n{kamuflert_ord}")

    #Dersom alle forekomster av "_" har blitt byttet ut i listen, har spilleren vunnet og får beskjed om det
    if "_" not in kamuflert_ord:
        spill_over = True
        print("\nGratulerer! Du har vunnet!")
    
