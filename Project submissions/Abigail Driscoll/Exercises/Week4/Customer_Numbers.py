numbers = {
    "Ronnie Sullivan": '01234 567890',
    "Marilyn Tucker": '01987 654321',
    "Brad Bennett": '01897 65320',
    "Rodney White": '020 765 6655',
    "Brian Burton": '01382 763999',
}
name = input("Please enter the name of the person you wish to contact: ")
if name in numbers.keys():
    print(numbers[name])
else:
    response = input("Sorry that name does not exist, do you wish to create a new record? ")

    if response.lower() == 'yes':
        newname = input("Please enter the name of the customer: ")
        newnumber = input("Please enter the customer number: ")
        numbers.update({newname: newnumber})
        print(numbers)
