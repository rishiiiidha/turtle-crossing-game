from turtle import Screen,Turtle
from score import Score
import time
from cars import Car
MOVE=10
FINISH_LINE=280
level=0
marks=0
STARTING_POSITION=(0,-280)
def up():
  timmy.forward(MOVE)
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("pink")
screen.tracer(0)
timmy=Turtle(shape="turtle")
timmy.color("black")
timmy.shapesize(1.25,1.25)
timmy.penup()
timmy.goto(STARTING_POSITION)
timmy.setheading(90)
car=Car()
finish=Score()
screen.listen()
screen.onkey(up,"Up")
game=True
def go_start():
  timmy.goto(STARTING_POSITION)
def is_at_finishline():
  if(timmy.ycor()>FINISH_LINE):
    return True
  else:
    return False
while(game):
  time.sleep(0.1)
  screen.update()
  car.create_cars()
  car.move()
  #detech collision
  for cars in car.segments:
    if(timmy.distance(cars) < 20):
       finish.game_over()
       game=False
  #detect succesful crossing
  if is_at_finishline():
    go_start()
    level=level+1
    #each level 5 marks
    marks=marks+5
    finish.level(level)
    car.level_up()
    finish.score_board(marks)
    
    

screen.exitonclick()