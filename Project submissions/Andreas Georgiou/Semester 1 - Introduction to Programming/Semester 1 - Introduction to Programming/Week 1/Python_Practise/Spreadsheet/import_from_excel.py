typing = raw_input("Type your name and contact details: ")

with open("test.txt", "w") as sample:
    sample.write(typing)


with open("test.txt", "r") as sample:
    print sample.read()
