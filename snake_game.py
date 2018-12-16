import random
import turtle

# Set up the screen
window = turtle.Screen()
window.title("Snake Game by Weng Kin Lee")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0) # Turns off screen updates


# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Main Game Loop
while True:
    window.update()

window.mainloop()
