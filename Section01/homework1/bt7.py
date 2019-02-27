#Use Python Turtle to draw the following shapes
#3/ A circle
from turtle import *
speed(0)
color("green","yellow")
begin_fill()

for i in range(360):
    forward(1)
    left(1)

end_fill()
mainloop()