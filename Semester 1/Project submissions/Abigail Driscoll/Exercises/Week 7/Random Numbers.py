def randlist():
    import random
    n = int(input("Please enter the length of the list that you would like to produce: "))
    randomlist = random.sample(range(1, 100), n)
    print(randomlist)
randlist()