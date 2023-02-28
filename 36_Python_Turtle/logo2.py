import turtle
import random
myPen = turtle.Turtle()
myPen.shape("turtle")
myPen.speed(10)

window = turtle.Screen()
window.bgcolor("#B475B8")

def corner(turtle):
  for x in range(0, 6):
    turtle.left(15)
    turtle.forward(2)

def cornered_box(turtle, x1, y1, x2, y2, letter):
  turtle.penup()
  turtle.goto(x1, y1)
  turtle.pendown()
  turtle.color("#580870")
  turtle.fillcolor("#580870")
  turtle.begin_fill()
  for x in range(0, 4):
    turtle.forward(40)
    corner(turtle)
  turtle.end_fill()
  turtle.penup()
  turtle.goto(x2, y2)
  turtle.color("white")
  turtle.write(letter, None, None, "28pt bold")

cornered_box(myPen, -60, 20, -49, 35, "1")
cornered_box(myPen, 5, 20, 14, 35, "0")
cornered_box(myPen, 70, 20, 79, 35, "1")

myPen.color("#000000")
myPen.goto(-62, -30)
myPen.write("Computing", None, None, "24pt bold")
myPen.color("white")
myPen.goto(-102, -90)
myPen.write("Learn How To Code", None, None, "24pt bold")
myPen.left(90)

myPen.goto(-96,-120)
myPen.pendown()
myPen.goto(156,-120)
myPen.penup()

myPen.goto(-70, -150)
myPen.write("www.101computing.net", None, None, "16pt bold")


myPen.goto(26, 105)

for x in range(0, 100):
  myPen.color("#%06x" % random.randint(0, 2**24 - 1))
myPen.color("white")