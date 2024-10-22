import figures
import turtle

if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    figures.draw_square(window, pen, 100)
    pen.penup()
    pen.goto(-100, 100)  # Move to a different location
    pen.pendown()
    figures.draw_square(window, pen, 100)  # Draw again at the new location

    figures.draw_triangle(window, pen, 100)
    pen.penup()
    pen.goto(50, 87)  # Move to a different location
    pen.pendown()
    figures.draw_triangle(window, pen, 100)  # Draw again at the new location

    figures.draw_rectangle(window, pen, 150, 75)
    pen.penup()
    pen.goto(-115, 150)
    pen.pendown()
    figures.draw_rectangle(window, pen, 150, 75)

    pen.hideturtle()
    window.mainloop()
