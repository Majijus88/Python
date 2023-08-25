
#Program som ved hjelp av random funksjonen flipper en virtuell "mynt"

import random

peng = random.randint(0,1)

if peng > 0:
    print("Det ble mynt!")
else:
    print("Det ble kron!")



