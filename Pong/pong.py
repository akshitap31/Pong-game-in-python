import turtle
import winsound

#Window
win=turtle.Screen()
win.title("Classic Pong Game")
win.bgcolor("pink")
win.setup(width=800, height=600)
#Stops screen from refreshing, makes faster
win.tracer(0)

#Score
score_a=0
score_b=0

#Paddle A
paddle_a=turtle.Turtle()
#Speed for turtle module, makes the prog run fast, its not the paddle speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
#The default size is 2*2 pix, this will change the width to 10
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
#Turtle draws lina as it moves, we dont need a line and hence penup
paddle_a.penup()
#Position at which it starts, centre of screen is coordinates 0,0
paddle_a.goto(-350,0)

#Paddle B
paddle_b=turtle.Turtle()
#Speed for turtle module, makes the prog run fast, its not the paddle speed
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
#The default size is 2*2 pix, this will change the width to 10
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
#Turtle draws lina as it moves, we dont need a line and hence penup
paddle_b.penup()
#Position at which it starts, centre of screen is coordinates 0,0
paddle_b.goto(350,0)


#Ball

ball=turtle.Turtle()
#Speed for turtle module, makes the prog run fast, its not the paddle speed
ball.speed(0)
ball.shape("circle")
ball.color("white")
#Turtle draws lina as it moves, we dont need a line and hence penup
ball.penup()
#Position at which it starts, centre of screen is coordinates 0,0
ball.goto(0,0)

#Ball movement
ball.dx=0.2 #moves by 0.25 px
ball.dy=0.2

#Pen
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Function for Paddle movement
def paddle_a_up():
    y=paddle_a.ycor() #returns y cordinates of the paddle
    y += 20
    paddle_a.sety(y) #sets to new y
def paddle_a_down():
    y=paddle_a.ycor() #returns y cordinates of the paddle
    y -= 20
    paddle_a.sety(y) #sets to new y
def paddle_b_up():
    y=paddle_b.ycor() #returns y cordinates of the paddle
    y += 20
    paddle_b.sety(y) #sets to new y
def paddle_b_down():
    y=paddle_b.ycor() #returns y cordinates of the paddle
    y -= 20
    paddle_b.sety(y) #sets to new y
#Keyboard Binding
win.listen() #listens keyboard input
win.onkeypress(paddle_a_up, "w") #when key w is pressed, it will call the function and move up
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up") #when key w is pressed, it will call the function and move up
win.onkeypress(paddle_b_down, "Down")


while True:
    win.update()
    #Moves ball
    ball.setx(ball.xcor() +ball.dx) #loop to keep the ball moving
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290: #upper border
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("ClickOn-Sound.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290: #lower border
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("ClickOn-Sound.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        # ball.setx(390)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0) #moves ball to centre
        # ball.setx(-390)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    #paddle ball collisions
    if (ball.xcor()> 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("ClickOn-Sound.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("ClickOn-Sound.wav", winsound.SND_ASYNC)
