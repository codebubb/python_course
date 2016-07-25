age = int(input("Please enter your age: "))
if age < 18:
    print("As you are under 18 your bus fare is half price, £1.15 please!")
if age >= 65:
    print("As you are 65 or over your bus journey is free!")
else:
    print("no discount requirements are met, please pay the full fare of £2.30")