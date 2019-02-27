import tkinter as tk
import turtle
t = turtle.Pen()
t.speed(100)

            
def draw_left_spiral():
    for x in range (100):
        t.forward(x)
        t.left(91)
def draw_right_spiral():
    for x in range (100):
        t.forward(x)
        t.right(91)       
def draw_left_star():
    for x in range (100): 
        t.forward(x)
        t.left(150)
def draw_right_star():
    for x in range (100):
        t.forward(x)
        t.right(150)
def draw_left_box():
    for x in range (100):
        t.forward(x)
        t.left(90)
def draw_right_box():
    for x in range (100):
        t.forward(x)
        t.right(90)

def make_it_blue():
    t.pencolor("blue")
def make_it_red():
    t.pencolor("red")
def make_it_green():
    t.pencolor("green")
def make_it_black():
    t.pencolor("black")
def make_it_cyan():
    t.pencolor("cyan")
def make_it_purple():
    t.pencolor("purple")
    
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

###color buttons
blue_button = tk.Button(frame, 
                   text="Blue", 
                   fg="blue",
                   command=make_it_blue)
blue_button.pack(side=tk.LEFT)
blue_button.config(height = 3, width = 8)

red_button = tk.Button(frame, 
                   text="Red", 
                   fg="red",
                   command=make_it_red)
red_button.pack(side=tk.LEFT)
red_button.config(height = 3, width = 8)

green_button = tk.Button(frame, 
                   text="Green", 
                   fg="green",
                   command=make_it_green)
green_button.pack(side=tk.LEFT)
green_button.config(height = 3, width = 8)

cyan_button = tk.Button(frame, 
                   text="Cyan", 
                   fg="cyan",
                   command=make_it_cyan)
cyan_button.pack(side=tk.LEFT)
cyan_button.config(height = 3, width = 8)

purple_button = tk.Button(frame, 
                   text="Purple", 
                   fg="purple",
                   command=make_it_purple)
purple_button.pack(side=tk.LEFT)
purple_button.config(height = 3, width = 8)

black_button = tk.Button(frame,
                   text="Black", 
                   fg="black" ,
                   command=make_it_black)
black_button.pack(side=tk.LEFT)
black_button.config(height = 3, width = 8)

###shape buttons
left_spiral = tk.Button(frame, 
                   text="Left Spiral", 
                   fg="black",
                   command=draw_left_spiral)
left_spiral.pack(side=tk.LEFT)
left_spiral.config(height = 3, width = 8)
 
right_spiral = tk.Button(frame, 
                   text="Right Spiral", 
                   fg="black",
                   command=draw_right_spiral)
right_spiral.pack(side=tk.LEFT)
right_spiral.config(height = 3, width = 8)

left_star = tk.Button(frame, 
                   text="Left Star", 
                   fg="black",
                   command=draw_left_star)
left_star.pack(side=tk.LEFT)
left_star.config(height = 3, width = 8)

right_star = tk.Button(frame, 
                   text="Right Star", 
                   fg="black",
                   command=draw_right_star)
right_star.pack(side=tk.LEFT)
right_star.config(height = 3, width = 8)

left_box = tk.Button(frame, 
                   text="Left Box", 
                   fg="black",
                   command=draw_left_box)
left_box.pack(side=tk.LEFT)
left_box.config(height = 3, width = 8)

right_box = tk.Button(frame, 
                   text="Right Box", 
                   fg="black",
                   command=draw_right_box)
right_box.pack(side=tk.LEFT)
right_box.config(height = 3, width = 8)

quit_button = tk.Button(frame,
                   text="Quit",
                   command=quit)
quit_button.pack(side=tk.LEFT)
quit_button.config(height = 3, width = 8)

root.mainloop()
