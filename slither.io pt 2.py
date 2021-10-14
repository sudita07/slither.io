import turtle
import time
import random
delay = 0.1
score = 0
high_score = 0
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)
# the head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"
# the food for the snake
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)
segments = []
# the score turtle
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0 High score:0", align = "center", font=("Courier", 24, "normal"))
def go_up():
    if head.direction != "down":
        head.direction = "up"
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
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
while True:
    wn.update()
    # for when the snake touches the border it should reset
    if head.xcor()>550 or head.xcor()<-550 or head.ycor()>450 or head.ycor()<-450:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write("Score: {} High score: {}".format(score, high_score),align="center", font=("Courier", 24, "normal"))
    # for when the head touches the food another segment/tail is created
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        # once food is eaten new food should come at a different x y position
        food.goto(x,y)
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        delay-=0.001
        score+=10
        # if the score is bigger than the highscore the new score should become the highscore
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {} High score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    # to identify the index value of each and every turtle getting added/tail
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    # the length of the tail or the amount of tails should be more than 0 in order to be shown on the screen
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()

    # for when the snake hits its body/self
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for segment in segments:
                # in case it never ends 1000 is the maximum value the tails can reach
                segment.goto(1000, 1000)
            segments.clear()
            score=0
            delay=0.1
            pen.clear()
            pen.write("Score: {} High score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))
    time.sleep(delay)
wn.mainloop()