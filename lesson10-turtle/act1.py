import turtle #Importing Library
turtle.Screen().bgcolor("orange")
turtle.Screen().setup()
polygon = turtle.Turtle() #Defined variable

num_sides = 6 #Variable
side_length = 10560
angle = 360.0 / num_sides

#iterate loop for total number of side
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    

turtle.done()