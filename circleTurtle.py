import turtle
import math

def drawCircle(t, center_x, center_y, radius):
    # Move the turtle to the starting position
    t.penup()
    t.goto(center_x + radius, center_y)
    t.pendown()
    
    # Calculate the step size for the circle approximation
    step_size = (2.0 * math.pi * radius) / 120.0
    
    # Draw the circle by making 120 small movements
    for _ in range(120):
        t.forward(step_size)
        t.right(3)

# Example usage
if __name__ == "__main__":
    screen = turtle.Screen()
    t = turtle.Turtle()
    drawCircle(t, 0, 0, 100)
    screen.mainloop()
