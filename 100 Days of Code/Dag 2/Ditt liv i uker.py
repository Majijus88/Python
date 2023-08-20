
#Program som gir tilbakemelding på hvor mange dager / uker og måneder som gjenstår i livet ved oppgitt alder

alder = int(input("Hvor gammel er du? "))
gjennomsnittlig_levealder = 90

#Regner ut hvor mange dager et menneske opplever i snitt igjennom livet
dager_i_gjennomsnitt = 90 * 365

#Regner ut hvor mange uker et menneske opplever i snitt igjennom livet
uker_i_gjennomsnitt = 90 * 52

#Regner ut hvor mange måneder et menneske opplever i snitt igjennom livet
maaneder_i_gjennomsnitt = 90 * 12

#Regner ut hvor mange dager, uker og måneder som gjenstår basert på brukers input
dager_igjen = dager_i_gjennomsnitt - (alder * 365)
uker_igjen = uker_i_gjennomsnitt - (alder * 52)
maaneder_igjen = maaneder_i_gjennomsnitt - (alder * 12)

#Gir bruker tilbakemelding
utregning = print(f"Du har igjen: {dager_igjen} dager. {uker_igjen} uker eller {maaneder_igjen} måneder av livet ditt")