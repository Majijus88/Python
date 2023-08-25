
#Program som spiller "Stein saks papir"

#      Regler 
#Stein vinner mot saks
#Saks vinner mot papir
#Papir vinner mot stein

stein = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papir = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

saks = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
game_images = [stein, papir, saks]

bruker_input = input("Hva velger du? stein, saks eller papir? ")
if bruker_input == "stein":
  print (f"\nDu valgte {bruker_input}")
  print(game_images[0])

elif bruker_input == "papir":
  print (f"\nDu valgte {bruker_input}")
  print(game_images[1])

elif bruker_input == "saks":
  print (f"\nDu valgte {bruker_input}")
  print(game_images[2])

else:
  print("Ugyldig input. Du tapte")

data_input = random.randint(0,2)
if data_input == 0 and bruker_input == "stein":   #stein vs stein
  print(game_images[0])
  data_input = "stein"
  print(f"Du valgte {bruker_input} og maskinen valgte {data_input}. Det blir uavgjort")

elif data_input == 0 and bruker_input == "papir":   #stein vs papir
  print(game_images[0])
  data_input = "stein"
  print(f"Du valgte {bruker_input} og maskinen valgte {data_input}. Du vant!")

elif data_input == 0 and bruker_input == "saks":   #stein vs saks
  print(game_images[0])
  data_input = "stein"
  print(f"Du valgte {bruker_input} og maskinen valgte {data_input}. Du tapte!")

elif data_input == 1 and bruker_input == "stein":   #stein vs papir
  print(game_images[1])
  data_input = "papir"
  print(f"Du valgte {bruker_input} og maskinen valgte {data_input}. Du tapte")

elif data_input == 1 and bruker_input == "papir":   # papir vs papir
  print(game_images[1])
  data_input = "papir"
  print(f"Du valgte {bruker_input} og maskinen valgte {data_input}. Det blir uavgjort")

elif data_input == 1 and bruker_input == "saks":   # papir vs saks
  print(game_images[1])
  data_input = "papir"
  print(f"Du valgte {bruker_input} og maskinen valgte {data_input}. Du vant!")

elif data_input == 2 and bruker_input == "stein":   #saks vs stein
  print(game_images[2])
  data_input = "saks"
  print(f"Du valgte {bruker_input} og maskinen valgte {data_input}. Du vant")

elif data_input == 2 and bruker_input == "papir":   # saks vs papir
  print(game_images[2])
  data_input = "saks"
  print(f"Du valgte {bruker_input} og maskinen valgte {data_input}. Du tapte!")

elif data_input == 2 and bruker_input == "saks":   # stein vs saks
  print(game_images[2])
  data_input = "saks"
  print(f"Du valgte {bruker_input} og maskinen valgte {data_input}. Det ble uavgjort!")