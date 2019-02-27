#Use Python Turtle to draw the following shapes
#1/ A square

from turtle import *
speed(0)
color("green","yellow")
begin_fill()

for i in range(4):
    forward(200)
    left(90)

end_fill()

mainloop()