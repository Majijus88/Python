
regning = float(input("Hva er den totale summen på regningen? "))
prosent = int(input("Hvor mange prosent ønsker du å gi i driks? "))

sum = regning + (regning * prosent) / 100
print (sum)