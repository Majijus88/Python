
#Funksjonen type() gir mulighet til å finne ut av hva slags type klasse som utgjør innholdet i en variabel

#Her har jeg en string som eksempel
variabel_string = "1"
#type() funksjonen bekrefter at variabelen er en string
print(f"variabelen er av typen {type(variabel_string)}")

#Her har jeg en integer som eksempel
variabel_integer = 1
#type() funksjonen bekrefter at variabelen er en integer
print(f"variabelen er av typen {type(variabel_integer)}")

#Her har jeg en float som eksempel
variabel_float = 1.25
#type() funksjonen bekrefter at variabelen er en integer
print(f"variabelen er av typen {type(variabel_float)}")

#Her har jeg en liste som eksempel
variabel_liste = ["Marius", "Tine", "Melis", "Ellie", "Esther"]
#type() funksjonen bekrefter at variabelen er en integer
print(f"variabelen er av typen {type(variabel_liste)}")

#Her har jeg en dictionary som eksempel
variabel_dictionary = dict(By="Oslo", Kommune="Oslo", Bydel="Alna")
#type() funksjonen bekrefter at variabelen er en dictionary
print(f"variabelen er av typen {type(variabel_dictionary)}")

