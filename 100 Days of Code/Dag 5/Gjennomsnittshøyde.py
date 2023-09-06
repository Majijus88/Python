
#Program som tar inn x-antall høyder på personer og deretter regner ut et gjennomsnitt av disse

#Split deler opp hvert ord til en string og putter hver av disse i en liste
bruker_input = (input("Vennligst skriv inn høyden på personen. For flere personer, bruk SPACE som mellomrom: ")).split()

#Lager to tomme hjelpevariabler som får tilført verdier fra for-loopen lenger ned
antall_brukere = 0
total_sum = 0

for bruker in bruker_input:
    #Legger til verdien av loopens bruker variabel inn i variabelen "total sum" utenfor loopen
    total_sum += int(bruker)
    #Legger til +1 for hver gang loopen går igjennom for å telle antall brukere man har fått vite høyden
    antall_brukere += 1

#Regner ut gjennomsnittet med å ta totalsummen / antall personer
gjennomsnitt = total_sum / antall_brukere
print(f"Gjennomsnittet av de oppgitte høydene er: {gjennomsnitt}")

