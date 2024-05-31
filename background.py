import turtle
import time 
import random

delay=0.1

#score
Score = 0
High_score =0


#screen setup
wn= turtle.Screen()
wn.title("snake")
wn.bgcolor("#454545")
wn.setup(width=600,height=600)
wn.tracer(0)

#snake head 
head= turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()  #so that it dos'nt raw anything 
head.goto(0,0)
head.direction ="stop"

#snake food
food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.shapesize(0.8)
food.penup()  #so that it dos'nt draw anything 
food.goto(0,100)

# pen
pen= turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0   High Score :0 ",align="center",font=("courier", 26,"normal"))

# move 
def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        y=head.xcor()
        head.setx(y-20)

    if head.direction == "right":
        y=head.xcor()
        head.setx(y+20)

    
#functions

def go_up ():
    if head.direction != "down":
        head.direction= "up"
def go_down ():
    if head.direction != "up":
        head.direction= "down"
def go_lefft ():
    if head.direction != "rght":
        head.direction= "left"
def go_right ():
    if head.direction != "left":
        head.direction= "right"

# keyboards binding
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_lefft,"a")
wn.onkeypress(go_right,"d")


segment= []



# as we stop the screen at 9 line
while True:
    wn.update()

    #check for the collision with the border
    if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()< -280 :
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # hide the segments
        for k in segment:
            k.goto(1000,1000)
        # clear list
        segment.clear()

        # reset the score
        Score=0
        pen.clear()
        pen.write("Score: {} High score :{}" .format(Score,High_score), align="center")

    if head.distance(food) < 20 :
        #move the food to random spot in the screen
        x= random.randint(-280,290)
        y= random.randint(-280,290)
        food.goto(x,y)

    #add new segments or body 
        new_segment = turtle.Turtle()
        new_segment .speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)

    #increasing the score
        Score +=10
        if Score > High_score :
            High_score = Score
        pen.clear()
        pen.write("Score: {} High score :{}" .format(Score,High_score), align="center")
    
    # move the end segments first in reverse order
    for index in range(len(segment)-1,0,-1):
        x=segment[index-1].xcor()
        y=segment[index-1].ycor()
        segment[index].goto(x,y)
    
    #move segment 0 to where the head is 
    if len(segment) > 0 :
        x= head.xcor()
        y= head.ycor()
        segment[0].goto(x,y)


   


    move()

     #check for the head collision with the body segments
    for k in segment:
        if k.distance(head) < 20 :
            time.sleep(0.7)
            head.goto(0,0)
            head.direction="stop"
            # hide the segments
            for k in segment:
                k.goto(1000,1000)
            # clear list
            segment.clear()

    time.sleep(delay)
wn.mainloop()