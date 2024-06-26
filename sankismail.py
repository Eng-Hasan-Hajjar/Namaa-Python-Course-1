import turtle
import time
import random
 
game_speed=0.1
score=0
high_score=0

window=turtle.Screen()
window.title("pyton snake game")
window.bgcolor("blue")
window.setup(width=700,height=700)
window.cv._rootwindow.resizable(False,False)
window.tracer(0)

head=turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.speed(0)
head.goto(0, 0)
head.direction="stop"

food=turtle.Turtle()
colors = random.choice(["white","red","black"])
shapes = random.choice(["square","circle"])
food.shape(shapes)
food.color(colors)
food.penup()
food.speed(0)
food.goto(0,100)

pen=turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.speed(0)
pen.goto(0,250)
pen.hideturtle()
pen.write("score= 0  high score=0",align="center",font=("arial",20, "bold"))

def goup():
    if head.direction!= "down":
        head.direction= "up"

def godown():
    if head.direction!= "up":
        head.direction= "down"

def goleft():
    if head.direction!="right":
        head.direction= "left"

def goright():
    if head.direction!="left":
        head.direction= "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

window.listen()
window.onkeypress(goup,"w")
window.onkeypress(godown,"s")
window.onkeypress(goleft,"a")
window.onkeypress(goright,"d")

segments = []
 
while True:
    window.update()
    
    if(
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction="stop"
        colors= random.choice(["white","red","black"])
        shapes= random.choice(["square","circle"])
        food.shape(shapes)
        food.color(colors)
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score=0
        game_speed=0.1
        pen.clear()
        pen.write(
            "score:{} high score:{}".format(score,high_score),
            align="center",
            font=("arial",20,"bold"),
        )

    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("orange")  
        new_segment.speed(0)
        new_segment.penup()
        segments.append(new_segment)
        game_speed -=0.001
        score +=10
        if score > high_score:
            high_score=score
        pen.clear()
        pen.write("score:{} high score:{}".format(score,high_score),
             align="center",
             font=("arial",20,"bold"), )
        
    for index in range(len(segments) - 1, 0, -1):
         x = segments[index - 1].xcor()
         y = segments[index - 1].ycor()
         segments[index].goto(x, y)
    if len(segments) > 0:
         x = head.xcor()
         y = head.ycor()
         segments[0].goto(x, y)
    move()


    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(["red", "green", "black"])
            shapes = random.choice(["square", "circle"])
            food.shape(shapes)
            food.color(colors)
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            game_speed = 0.1
            pen.clear()
            pen.write(
                "Score: {}   High Score: {} ".format(score, high_score),
                align="center",
                font=("Arial", 20, "bold"),
            )
    time.sleep(game_speed)
