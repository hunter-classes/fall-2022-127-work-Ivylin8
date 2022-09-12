import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
def hexagon(t,x,y,w,color,sidelen):
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color("blue")
    t.pendown()


for i in range (6):
    alex.forward(100)
    alex.left(360/6)
    
for aColor in ["yellow", "red", "purple", "blue", "yellow", "blue"]:
    alex.color(aColor)
    alex.forward(100)
    alex.left(360/6)