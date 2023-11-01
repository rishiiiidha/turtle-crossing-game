from turtle import Turtle
FONT = ("Calibri", 24, "bold")
class Score:
  def __init__(self):
    self.score=Turtle()
    self.score.hideturtle()
    self.score.penup()
    self.level(0)
    self.score_board(0)
    
  def game_over(self):
    self.score.goto(0,0)
    self.score.write("GAME OVER 😕 ",move=False, align='center', font=FONT)
  def level(self,a):
    self.score.clear()
    self.message=f"Level🚀: {a}"
    self.score.goto(-280,245)
    self.score.write(self.message,move=False, align='left', font= ("Calibri", 17, "bold"))
  def score_board(self,a):
    self.board=f"Score🏆: {a}"
    self.score.goto(280,245)
    self.score.write(self.board,move=False, align='right', font= ("Calibri", 17, "bold"))