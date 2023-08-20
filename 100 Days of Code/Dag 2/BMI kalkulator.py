
#BMI kalkulator:

#Formel for BMI = Vekt/Høyde*Høyde - Eks: 80kg / 1.75m * 1.75m = 26.122

#Konverterer input til integer
vekten = (int(input("Hva veier du? ")))

#Konverterer input til float
høyde = (float(input("Hvor høy er du? ")))

#Setter opp parantes rundt høyde*høyde for at dette skal prioriteres ved utregning
bmi = (vekten / (høyde * høyde))

#Alternativ måte å utregne på ved hjelp av potenser
bmi_alternativ = vekten / høyde ** 2

#Printer ut resultatet til bruker ved hjelp av en f-streng
print(f"Din utregnede BMI er: {bmi}")
print(f"Din utregnede BMI er: {bmi_alternativ}")

#Det er videre mulig å kutte ned antall desimaler ved å benytte round() funksjonen og spesifisere antall desimaler bak et komma.
#Eks:
print(f"Din utregnede BMI er: {round(bmi, 2)}")
