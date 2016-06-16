my_list = ['Baxter', 'is', 'that', 'you?', 'Baxter!', 'Bark', 'twice', 'if', 'youre', 'in', 'Milwaukee']
y = len(my_list)
z =[]
for i in my_list:
    x = len(i)
    z.append(int(x))
print sum(z) / y
