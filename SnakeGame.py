#Made by ArhanCodes

#Create a Screen ie 800x600
import turtle
import time
import random


delay=0.1
body=[]       #creating an empty list

s=turtle.Screen()
s.title("Snake Game")
s.setup(800,600)
s.tracer(0)


#Draw a thick border
def drawborder():
    b=turtle.Turtle()
    b.ht()
    b.pu()
    b.goto(-390,290)
    b.pd()
    b.pensize(8)
    b.speed(0)
    for i in range(2):
        b.fd(775)
        b.rt(90)
        b.fd(575)
        b.rt(90)

drawborder()

#Draw Snake Food as circle in red color in 1st Quadrant(Top-right)
food=turtle.Turtle()
food.shape("circle")
food.color("red")
food.pu()
food.speed(0)
food.goto(50,100)



#Draw Snake head as square in black color
head=turtle.Turtle()
head.shape("square")
head.direction="stop"
head.up()


#move snake
#Keys Up arrow -- up,Down -- down, Left -- left, Right-- right

def move_up():
    head.direction="up"

def move_down():
    head.direction="down"

def move_left():
    head.direction="left"

def move_right():
    head.direction="right"


def move():
    if head.direction=="up":
        y=head.ycor()
        y=y+20
        head.sety(y)
    if head.direction=="down":
        y=head.ycor()
        y=y-20
        head.sety(y)
    if head.direction=="left":
        x=head.xcor()
        x=x-20
        head.setx(x)
    if head.direction=="right":
        x=head.xcor()
        x=x+20
        head.setx(x)
    

s.listen()
s.onkey(move_up,"w")
s.onkey(move_down,"s")
s.onkey(move_left,"a")
s.onkey(move_right,"d")

#Main Code
try:
    while True:
        s.update()

        #Detect collision of snake head with food
        #and move food to a new place

        if head.distance(food)<20:
            x=random.randint(-200,200)
            y=random.randint(-200,200)
            food.goto(x,y)

            #Snake Grows when it eats food
            bodyparts=turtle.Turtle()
            bodyparts.shape("square")
            bodyparts.color("gray")
            bodyparts.up()
            bodyparts.speed(0)
            body.append(bodyparts)

        #Attach bodyparts to snake
        for i in range(len(body)-1,0,-1):
            x=body[i-1].xcor()
            y=body[i-1].ycor()
            body[i].goto(x,y)

        if len(body)>0:
            x=head.xcor()
            y=head.ycor()
            body[0].goto(x,y)

            
            






        
        move()
        
        time.sleep(delay)

except:
    print("Game Over")















        
