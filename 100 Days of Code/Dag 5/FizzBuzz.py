
#Program som printer ut alle numre mellom 1 - 100 med noen unntak:
#Tall som kan deles på 3 printer: "Fizz" - Tall som kan deles med 5 som printer "Buzz"
#Kan tallet deles på både 3 og 5 printes "FizzBuzz"

for number in range (1,100):
    
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    
    elif number % 3 == 0:
        print("Fizz")
    
    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)