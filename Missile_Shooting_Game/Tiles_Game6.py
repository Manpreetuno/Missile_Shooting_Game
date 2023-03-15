import turtle
import time

turtle.register_shape("Background1.gif")
turtle.register_shape("Tile1.gif")
BG=turtle.Turtle()
obj1=turtle.Turtle()
obj2=turtle.Turtle()
obj3=turtle.Turtle()
obj4=turtle.Turtle()
BG.shape("Background1.gif")
Score=turtle.Turtle()
Score.color("white")
Score.hideturtle()
over=turtle.Turtle()
over.hideturtle()
Missile=turtle.Turtle()
Missile.setheading(90)
Missile.shape("turtle")
Missile.color("orange")
Missile.penup()
Missile.setpos(0,-160)
Missile.shapesize(1,3)
TURTLE=turtle.Turtle()
TURTLE.color("white")
TURTLE.shape("square")
TURTLE.shapesize(2,2)
screen=turtle.Screen()
TURTLE.setheading(90)
TURTLE.penup()
TURTLE.setpos(0,-160)
global E1,E2,E3,E4
E1=E2=E3=E4=0
OBJ=[obj1,obj2,obj3,obj4]
Y=170
t1=0
def Add_Tiles():
  X=-170
  for i in range(0,4):
    OBJ[i].penup()
    OBJ[i].shape("Tile1.gif")
    OBJ[i].shapesize(2,4)
    OBJ[i].setpos(X,Y)
    X=X+100
angle1=90
def left():
  global angle1
  if(angle1<181):
    angle1=angle1+1
  if(angle1==180):
    angle1=180
  TURTLE.setheading(angle1)
  

def right():
  global angle1
  if(angle1>0):
    angle1=angle1-1
  if(angle1==0):
    angle1=0
  TURTLE.setheading(angle1)

def Up():
  Missile.setheading(angle1)
  global E1,E2,E3,E4
  for num in range(0,85):
    Missile.forward(4)
    if(Missile.distance(obj1) < 20):
      obj1.hideturtle()
      E1=1
    if(Missile.distance(obj2) < 20):
      obj2.hideturtle()
      E2=1
    if(Missile.distance(obj3) < 20):
      obj3.hideturtle()
      E3=1
    if(Missile.distance(obj4) < 20):
      obj4.hideturtle()
      E4=1
  Missile.hideturtle()
  Missile.setpos(0,-160)
  Missile.showturtle()
  
screen.listen()

screen.onkey(left,"Left")
screen.onkey(right,"Right")
screen.onkey(Up,"Up")
Add_Tiles()
T=1
sec=0
score=0
while(True):
  screen.update()
  if((E1==1)and(E2==1)and(E3==1)and(E4==1)):
    score=score+1
    obj1.showturtle()
    obj2.showturtle()
    obj3.showturtle()
    obj4.showturtle()
    Y=170
    Add_Tiles()
    E1=E2=E3=E4=0
    Score.clear()
  if(((E1!=0)or(E2!=0)or(E3!=0)or(E4!=0))and(Y<=-180)):
    #over.clear()
    over.color("white")
    over.setpos(0,0)
    over.write("Game Over",font=("Calibri",15,"bold"))
  turtle.color("white")
  turtle.hideturtle()  
  turtle.clear()
  turtle.setpos(0,200)
  turtle.write("Timer="+str(sec),font=("Calibri",15,"bold"))
  Score.penup()
  Score.setpos(-170,200)
  Score.write("Score="+str(score),font=("Calibri",15,"bold"))
 
  if(T==1):
    a=time.time()
    T=0
  if(time.time()-a>1):
    sec=1
  if(time.time()-a>2):
    sec=2
  if(time.time()-a>3):
    sec=3
  if(time.time()-a>4):
    sec=4
  if(time.time()-a>5):
    sec=5
  if(time.time()-a>6):
    Y=Y-50
    Add_Tiles()
    T=1
  
  
screen.mainloop()






