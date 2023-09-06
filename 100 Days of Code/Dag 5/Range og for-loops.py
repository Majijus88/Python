
#Dette programmet legger sammen alle partall mellom 1 til 100 og presenterer sluttsummen av disse for bruker

verdi = 0

for number in range(2, 101, 2):
    verdi += number

print(verdi)


#Alterntiv løsning

verdi_alt = 0

for number in range (1,101):
    if number % 2 == 0:
        verdi_alt += number

print(verdi_alt)
