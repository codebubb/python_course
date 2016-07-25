'''
towers.py
---------
Towers of hanoi puzzle
'''
from __future__ import print_function

# Game state to decide whether to keep playing
all_discs_moved = False

# Have four discs each with a different size
discs = []
discs.append("   -   ")
discs.append("  ---  ")
discs.append(" ----- ")
discs.append("-------")

# Have three stacks
rod_height = len(discs)
rod_names = ["A","B","C"]
rods = [    ["","","",""], ["","","",""], ["","","",""]]


# Fill one stack with discs
rods[0] = discs

# Loop
while not all_discs_moved:
    
    # Display all stacks with discs
    print("\n", " "*10, rod_names[0], " "*18, rod_names[1], " "*18, rod_names[2], "\n")
    for n in range(rod_height):
        for r in rods:
            if r[n] == "":
                print("        ","   |   ", "    ", end="")
            else:
                print("        ",r[n], "    ", end="")
        print()
    print("      ", "="*53)
    
    # Give the user the option to 'pop' from one of the stacks to another
    while True:
        move_from = raw_input("Which stack would you like to move from?").upper()
        if move_from in rod_names:
            move_from = rod_names.index(move_from)
            break
        else:
            print ("Please enter A, B or C")
    while True:
        move_to = raw_input("Which stack would you like to move to?").upper()
        if move_to in rod_names:
            move_to = rod_names.index(move_to)
            break
        else:
            print ("Please enter A,B or C")
    print ("Move from", move_from, "to",move_to)

    # Get top of the from stack
    top_of_from = 0
    while True:
        if "-" in rods[move_from][top_of_from] or top_of_from == rod_height -1:
            break
        top_of_from +=1

    # Get top of the to stack
    top_of_to = rod_height -1 
    while True:
        if "-" not in rods[move_to][top_of_to] or top_of_to == 0:
            break
        top_of_to -=1

    # Check that the discs is allowed to move to that stack
    if top_of_to == rod_height - 1 or len(rods[move_from][top_of_from].strip()) < len(rods[move_to][top_of_to+1].strip()):
        # Yes? Update that stack making sure it is removed from the previous one
        rods[move_to][top_of_to] = rods[move_from][top_of_from]
        rods[move_from][top_of_from] = ""
    else:
        print("You can't put a larger discs on top of a smaller one!")
        
    # Check if all the discs have been moved to another stack
    for r in range(1,len(rods)): # Don't check the first stack as that's where we started!
        if rods[r] == discs:
            all_discs_moved = True
            print("Well done, you moved all of the discs!")

# Final print of stacks
print("\n", " "*10, rod_names[0], " "*18, rod_names[1], " "*18, rod_names[2], "\n")
for n in range(rod_height):
    for r in rods:
        if r[n] =="":
            print("        ","   |   ", "    ", end="")
        else:
            print("        ",r[n], "    ", end="")
    print()
print("      ", "="*53)
