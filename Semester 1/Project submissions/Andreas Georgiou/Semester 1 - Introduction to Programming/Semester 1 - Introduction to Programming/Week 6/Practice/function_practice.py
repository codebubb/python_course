def test(a1, a2):
    print a1 + a2
    return test

test(8, 8)




def add(n1, n2):
    return n1 + n2

print add(3,6)





def test(a1, a2):
    print a1 + a2
    return test

test(8, 8)



def hi(name):
    print "Hello master", name

hi(raw_input("Enter your name: ").title())



def hi(name = "Boss"):
    print "Hello master", name

hi()







def add_list(*num_list):
    total = 0
    for i in num_list:
        total += i
    return total

print add_list(7,8,7,9,1,4,5,4,52,4,5,4)
