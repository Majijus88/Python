
#BMI kalkulator 2.0:

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
if bmi < 18.5:
    print(f"Din utregnede BMI er: {round(bmi, 2)} - Du regnes som undervektig")
elif bmi > 18.5 and bmi < 25:
    print(f"Din utregnede BMI er: {round(bmi, 2)} - Du regnes som normalvektig")
elif bmi > 25 and bmi < 30:
    print(f"Din utregnede BMI er: {round(bmi, 2)} - Du regnes som overvektig")       
elif bmi > 30 and bmi < 35:
    print(f"Din utregnede BMI er: {round(bmi, 2)} - Du har fedme ")
else: 
    print(f"Din utregnede BMI er: {round(bmi, 2)} - Du regnes som sykelig overvektig")


