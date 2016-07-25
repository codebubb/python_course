quick_list0 = range(10) # quickly creats a list ranging from 0-9 (which is 10 integers)

for lst in quick_list0: # print the list line by line using a for loop
    print lst


subjects = ["Chemistry", "Maths", "Physics", "Drama"]
for sub in subjects:
    print "-" * 10 # prints the "-" string 10 times
    print sub


print "-" * 10
# FOR LOOP AND RANGE USED TOGETHER #
# -------------------------------- #


for num in range(1, 13):
    print num, "x 7 = ", num * 7
