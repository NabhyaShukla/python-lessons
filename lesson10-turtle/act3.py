import turtle 
my_wn = turtle.Screen()
my_wn.bgcolor("lightblue") #screen background color
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 0 
while True: #iterate loo;
    for i in range(2):
        my_pen.fd(size + 1)
        my_pen.left(40)
        size = size - 1
    size = size + 1
