
#Grov inndeling av conditional statements:

#   if condition:
#        gjør dette
#   else:
#        gjør dette

#Eks:

Antall_liter_vann = int(input("Hvor mange liter vann er i badekaret? "))

if Antall_liter_vann > 80:
    print("For mye vann! Sluket må åpnes!")
elif Antall_liter_vann == 50:
    print("Vann-nivået er optimalt")
else:
    print("Fyll mer vann!")



