import random
import turtle
import time

delay = 0.1

# Obstacle Count
obs_count = 0

# Score
score = 0
high_score = 0

# Set up the screen
window = turtle.Screen()
window.title("Snake Game by Weng Kin Lee")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0) # Turns off screen updates

# Obstacle
obstacles = []

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# Snake Body
segments = []

# Pen for writing score.
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Century Gothic", 24, "bold"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction  = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def generate_obs(obs_count):
    obs = turtle.Turtle()
    obs.speed(0)
    obs.shape("square")
    obs.color("blue")
    obs.penup()
    obs.goto(random.randint(-290, 290),random.randint(-290, 290))
    obs.direction = "stop"
    obstacles.append(obs)
    return len(obstacles)

# Keyboard bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# Main Game Loop
while True:
    window.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or \
    head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.5)
        head.goto(0,0)
        head.direction = "stop"

        # Hide Segments
        for segment in segments:
            segment.goto(1000,1000)

        # Hide obs
        for obs in obstacles:
            obs.goto(1000,1000)

        # Clear the segments list and obs
        segments.clear()
        obstacles.clear()

        # Resets Score
        score = 0
        pen.clear()
        pen.write("Score: {} Hight Score: {}".format(score,high_score),\
         align="center", font=("Century Gothic", 24, "bold"))

    # Check for collision with the food.
    if head.distance(food) < 20:
        # Move the food to a random spot.
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Generate new obstacle
        if(obs_count <= 10):
            obs_count = generate_obs(obs_count)

        # Increase the Score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} Hight Score: {}".format(score,high_score),\
         align="center", font=("Century Gothic", 24, "bold"))


    # Move the end segments first in reverse order
    for i in range(len(segments)-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with the body Segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction = "stop"

            # Hide Segments
            for segment in segments:
                segment.goto(1000,1000)

            # Hide obs
            for obs in obstacles:
                obs.goto(1000,1000)

            # Clear the segments list and obs
            segments.clear()
            obstacles.clear()

            # Resets Score
            score = 0
            pen.clear()
            pen.write("Score: {} Hight Score: {}".format(score,high_score),\
             align="center", font=("Century Gothic", 24, "bold"))

    # Check collision with obstacle
    for obs in obstacles:
        if obs.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction ="stop"

            # Hide Segments
            for segment in segments:
                segment.goto(1000,1000)

            # Hide obs
            for obs in obstacles:
                obs.goto(1000,1000)

            # Clear the segments list and obs
            segments.clear()
            obstacles.clear()

            # Resets Score and obs_Count
            score = 0
            obs_count = 0
            pen.clear()
            pen.write("Score: {} Hight Score: {}".format(score,high_score),\
             align="center", font=("Century Gothic", 24, "bold"))

    time.sleep(delay)

window.mainloop()
