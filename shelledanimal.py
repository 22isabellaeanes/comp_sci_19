import turtle
turtle.speed(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

def left_spiral():
    for x in range (shape2):
        turtle.pencolor(colors)
        turtle.forward(x)
        turtle.left(91)
        turtle.width(sizes)
def right_spiral():
    for x in range (shape2):
        turtle.pencolor(colors)
        turtle.forward(x)
        turtle.right(91)
        turtle.width(sizes)       
def left_star():
    for x in range (shape2):
        turtle.pencolor(colors)
        turtle.forward(x)
        turtle.left(150)
        turtle.width(sizes)
def right_star():
    for x in range (shape2):
        turtle.pencolor(colors)
        turtle.forward(x)
        turtle.right(150)
        turtle.width(sizes)
def left_box():
    for x in range (shape2):
        turtle.pencolor(colors)
        turtle.forward(x)
        turtle.left(90)
        turtle.width(sizes)
def right_box():
    for x in range (shape2):
        turtle.pencolor(colors)
        turtle.forward(x)
        turtle.right(90)
        turtle.width(sizes)
        
while True:
    colors = input("""What color would you like to use?
""")
    shapes = input("""What size would you like to use? (S, M, or L)?
""")
    if shapes == "S":
        shape2 = (100)
    if shapes == "M":
        shape2 = (200)
    if shapes == "L":
        shape2 = (300)
        
    sizes = input("""How wide would you like the shape (1-5 is best)?
""")
    instruction = input("""What do you want to draw?
1: left spiral,
2: right spiral,
3: left star
4: right star
5: left box
6: right box
""")
    if instruction == "1":
        left_spiral()
    if instruction == "2":
        right_spiral()
    if instruction == "3":
        left_star()
    if instruction == "4":
        right_star()
    if instruction == "5":
        left_box()
    if instruction == "6":
        right_box()

    moveshape = input("""Would you like the shape to return to the center
""")
    if moveshape == "yes":
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
