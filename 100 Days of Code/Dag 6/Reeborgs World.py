
#Basert på siden: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
#Funksjonen move() og turn_left() er ferdig definerte på siden

#Lager to egne funksjoner som styrer roboten turn_right() og hopp()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hopp():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#lopper igjennom 6 ganger da det er 6 hinder på banen
for hinder in range(6):
    hopp()

#Samme kode men ved bruk av while loop
antall_hinder = 6
while antall_hinder > 0:
    hopp()
    antall_hinder -= 1
    print(f"Antall hinder igjen til mål: {antall_hinder}")
