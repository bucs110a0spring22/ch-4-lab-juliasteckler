import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def drawSineCurve(dart):
  wn = turtle.Screen()
  dart = turtle.Turtle()
  setupWindow(wn)
  setupAxis(myturtle=None)
  dart.goto(-360, 0)
  dart.down()
  for i in range(-360, 360):
    x = i + 1
    y = math.sin(math.radians(x))
    dart.goto(x, y)
  dart.up()
  drawCosineCurve(dart)
  drawTangentCurve(dart)
  wn.exitonclick()

def setupWindow(mywindow=None):
  wn = turtle.Screen()
  wn.bgcolor("lightgreen")
  turtle.setworldcoordinates(-360, -1, 360, 1)

def setupAxis(myturtle=None):
  myturtle = turtle.Turtle()
  myturtle.goto(0, -1)
  myturtle.down()
  myturtle.goto(0, 1)
  myturtle.up()
  myturtle.goto(360, 0)
  myturtle.down()
  myturtle.goto(-360, 0)
  myturtle.up()

def drawCosineCurve(myturtle=None):
  myturtle = turtle.Turtle()
  myturtle.up()
  myturtle.goto(-360, 1)
  myturtle.down()
  for i in range(-360, 360):
    x = i + 1
    y = math.cos(math.radians(x))
    myturtle.goto(x, y)
  myturtle.up()

def drawTangentCurve(myturtle=None):
  myturtle = turtle.Turtle()
  myturtle.up()
  myturtle.goto(-360, 3.380140414)
  myturtle.down()
  for i in range(-360, 360):
    x = i + 1
    y = math.tan(math.radians(x))
    myturtle.goto(x, y)
  myturtle.up()



##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)
    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
