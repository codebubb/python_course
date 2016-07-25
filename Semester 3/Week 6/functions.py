
def add(n1,n2):
    # This function should return the sum of the parameters provided
    return n1 + n2

#Function 2
def count(str):
    # Count the number of words in the provided string
    return len(str.split(' '))

#Function 3
def login(user, passwd):
    # Return true or false depending if the user details match
    return user == "admin" and passwd == "letmein"

#Function 4
def average(*nums):
    # Takes any number of parameters and returns the average
    return float(sum(nums)) / len(nums)

#Function 5
def inlist(item, alist):
    # Returns a tuple containing True or False depending on whether the item is in the list, the type of the item and also the position in the list
    return (item in alist, type(item), alist.index(item))
