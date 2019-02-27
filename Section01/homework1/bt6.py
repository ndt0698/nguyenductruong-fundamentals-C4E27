#Use Python Turtle to draw the following shapes
#2/ An equilateral triangle
from turtle import *
speed(0)
color("green","yellow")
begin_fill()
for i in range(3):
    forward(200)
    left(120)

end_fill()
mainloop()