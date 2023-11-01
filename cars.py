from turtle import Turtle
import random
MOVE_INCREMENT = 10
color=["coral","red","blue","purple","gray","orange"]
class Car:
  def __init__(self):
    self.segments=[]
    self.create_cars()
    self.distance=5
  def create_cars(self):
       random_chance=random.randint(1,6)
       if(random_chance==1):
         timmy=Turtle(shape="triangle")
         timmy.tilt(180)
         timmy.penup()
         timmy.color(random.choice(color))
         timmy.shapesize(1,2.5)
         timmy.goto(300,random.randint(-240,240))
         self.segments.append(timmy)
  def move(self):
    for i in range(len(self.segments)):
      self.segments[i].speed(1)
      self.segments[i].backward(self.distance)
  def level_up(self):
    self.distance+=MOVE_INCREMENT
    
    
    
         

    
    
    