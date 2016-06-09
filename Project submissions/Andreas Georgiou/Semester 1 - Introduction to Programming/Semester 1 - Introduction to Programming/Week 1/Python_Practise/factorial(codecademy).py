x = 4
total = 0

def factorial():
    a = x * x - 1
    total = total + a
    x = x - 1
    factorial()

    print total

factorial()
