# My First Turtle Program (02/02/16)

import turtle #imports the turtle library

gra_screen = turtle.Screen() #creates the graphics screen
mike = turtle.Turtle() #creates the turtle named mike
gra_screen.bgcolor("lightgreen") #changed the background colour
mike.color("blue") #changes the turtle colour blue
mike.pensize(3) #changes the turtle size

# draws "A"
mike.back(300)
mike.left(90)
mike.forward(120)
mike.right(90)
mike.forward(50)
mike.right(90)
mike.forward(100)
mike.back(60)
mike.right(90)
mike.forward(50)

# draws "N"
mike.back(70)
mike.left(90)
mike.forward(60)
mike.right(180)
mike.forward(60)
mike.right(140)
mike.forward(75)
mike.left(140)
mike.forward(60)

# draws "D"
mike.right(90)
