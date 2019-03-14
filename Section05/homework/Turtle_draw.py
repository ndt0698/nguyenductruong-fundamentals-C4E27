# #1. Write a function that prints out “Hello world” 3 times (note no arguments, no return)
from turtle import*
# def print_hello():
#    for a in range(3):
#         print("Hello world")
# print_hello()


#2.Write a function that takes 2 numbers as arguments and print out sum of them (note: has arguments, no return)

# def add_2_number(a, b):
#    print('tong hai so la:', a + b)
# sum = "a" + "b"
# add_2_number(5, 6)

#3. Write a Python function that draws a square, named draw_square, takes 2 arguments: length and color, where length is the length of its side and color is the color of its bound (line color)

# def draw_square(length, line_color_):
#     color(line_color_)
#     for a in range(4):
#         forward(length)
#         left(90)
# draw_square(100,"blue")

# for i in range(30):
#     draw_square(i*5,"red")
#     left(17)
#     penup()
#     forward(i * 2)
#     pendown()

# mainloop()

#4. Write a Python function that draws a star, named draw_star, take 3 parameters: x, y, and length. Where x, y are the location of the star, length is the length of its side


def draw_star(x,y,length):
    penup()
    setx(x)
    sety(y)
    pendown()
    for i in range(5):	
    	right(144)	
    	forward(length)

draw_star(200,250,200)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

draw_star(0,200,200)

mainloop()