import turtle

def draw_square(window, pen, side_length):
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)

  
def draw_triangle(window, pen, length):
    for i in range(2):
        pen.forward(length)
        pen.left(120)
    pen.forward(length)


def draw_rectangle(window, pen, length_a, length_b):
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)