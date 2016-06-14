import hello

name = raw_input("What is your name?")

hello.p(name)

def q():
    question = raw_input("Would you like to know how to count to 10? ").lower()
    if question == "yes":
        hello.g()
    elif question == "no":
        "Goodbye!"
        exit()
    else:
        "Please enter yes or no."
        q()
q()
