import turtle
import math

intial = turtle.Turtle()
intial.speed(1)
intial.up()
intial.color('blue')
intial.goto(0,0)
intial.down()
intial.right(60)
intial.goto(-50, -50)

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
  drawFlatLine(dart)
  toCos = -360
  result = whereDoesCosStart(toCos)
  print("If", toCos, "is the starting x-coordinate for the Cosine curve, then", result, "is the starting y-coordinate.")
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

def drawFlatLine(myturtle=None):
  myturtle = turtle.Turtle()
  myturtle.up()
  myturtle.goto(-360, 0.5)
  myturtle.down()
  for i in range(-360, 360):
    x = i + 1
    y = 0.5
    myturtle.goto(x, y)
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

def whereDoesCosStart(a):
  b = math.cos(math.radians(a))
  return b

  
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
    drawFlatLine(dart)
    wn.exitonclick()
main()
