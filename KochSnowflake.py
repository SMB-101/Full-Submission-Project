import turtle

def koch_snowflake(t, order, length):
    if order == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, order - 1, length)
        t.left(60)
        koch_snowflake(t, order - 1, length)
        t.right(120)
        koch_snowflake(t, order - 1, length)
        t.left(60)
        koch_snowflake(t, order - 1, length)

def draw_snowflake(order, length):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    
    # Positioning the turtle
    t.penup()
    t.goto(-length/2, length/3)
    t.pendown()
    
    for _ in range(3):  # Draw three sides of the triangle
        koch_snowflake(t, order, length)
        t.right(120)
    
    screen.mainloop()

# Example usage
draw_snowflake(3, 300)  # Level 3 Koch Snowflake
