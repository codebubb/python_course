items = [1, 94, 3, 54, 34, 65, 32, 87, 63, 6, 33, 12, 3, 34, 65, 43, 87, 17, 98, 90, 9, 21, 1, 92, 33, 4, 17, 71, 53, 23, 69, 92, 41, 39]
print(items)


def insertionSort(items):
    for index in range(1,len(items)):

        currentvalue = items[index]
        position = index

        while position>0 and items[position-1]>currentvalue:
            items[position]=items[position-1]
            position = position-1

        items[position]=currentvalue
insertionSort(items)
print(items)