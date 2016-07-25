shopping_list = ["Bananas", "Apples", "Grapes"]

print "-" * 5
print "\n"

print "Shopping list before stack: \n"

for x in shopping_list:
    print x

print "\n"
print "-" * 5
print "\n"

shopping_list.pop()
shopping_list.pop()
shopping_list.pop()
shopping_list.append("Grapes")
shopping_list.append("Apples")
shopping_list.append("Bananas")

print "Shopping list after stack: \n"

for x in shopping_list:
    print x


print "\n"
print "-" * 5
