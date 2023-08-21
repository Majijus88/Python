print('\n')
print("Skattejakten\n")                                            #Linjen er kun for å huske hvilken oppgave som besvares i terminalen
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Velkommen til skattejakt! - Oppdraget ditt er å finne skatten, men pass opp for farer underveis!")
      
forste_input = input("Du står ved et veiskille, vil du gå til høyre eller venstre? ").lower()
if forste_input == "høyre":
    print("You snublet ned i et hull og brakk benet ditt. Spillet er slutt! ")
else:
    second_input = input("Du ankommer en innsjø og du ser en øy langt ute. Vil du svømme, eller ta båten som ligger ved stranden? \n").lower()
    if second_input == "svømme":
        print("Du ble angrepet av en hissig gjedde og druknet. Spillet er slutt!")
    else: 
        third_input = input("Du kommer uskadet over til øyen i innsjøen, og får øye på et hus med tre dører. En rød, en blå og en grønn. Hvilken dør velger du? \n").lower()
        if third_input == "rød":
            print("Auda, rommet sto i full brann og du smeltet. Spillet er slutt!")
        elif third_input == "blå":
            print("Ouch, rommet var fullt av sultne og ville dyr som river deg i filler. Spillet er slutt!")
        elif third_input == "grønn":
            print("Innerst i rommet ser du skatten! Gratulerer du vant spillet! :)")
        else:
            print("Du valgte en dør som ikke finnes, og klarer åpenbart ikke forholde deg til instruksjoner. Du har dermed havnet i limbo :( Spillet er slutt")