
items = [1, 94, 3, 54, 34, 65, 32, 87, 63, 6, 33, 12, 3, 34, 65, 43, 87, 17, 98, 90, 9, 21, 1, 92, 33, 4, 17, 71, 53, 23, 69, 92, 41, 39]
print(items)
end=len(items)-1
while (end!=-1):
    swapped=-1
    for i in range(0,end):
        if items [i]>items[i+1]:
            temp=items[i]
            items[i]=items[i+1]
            items[i+1]=temp
            swapped=i
    end=swapped
print(items)

print(set(items))


2 5 12 