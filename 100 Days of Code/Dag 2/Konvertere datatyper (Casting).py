
#Det er mulig å konvertere datatyper igjennom å legge til en ekstra "brakket" foran.
#I eksemplet nedenfor er det nødvendig å konvertere variabelen til en string for å kunne concate sammen print-linjen

antall_tegn = (str(len(input("Hva heter du? "))))
print(("Navnet ditt utgjør totalt " + antall_tegn + " tegn"))
print()

#Eks: - Caste en string til en integer:

stringen_min = "88"
stringen_min_som_int = int(stringen_min)
print(type(stringen_min_som_int))
print()

#Eks: - Caste en string til en float:

stringen_min = "8.8"
stringen_min_som_float = float(stringen_min)
print(type(stringen_min_som_float))
print()
