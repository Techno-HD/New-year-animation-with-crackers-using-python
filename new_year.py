import turtle
from turtle import color
import random

def pen(col):
	turtle.color(col)

def fireworks(size):
	for i in range(30):
		turtle.forward(size)
		turtle.rt(180-360/30)

def star(size):
	pen('yellow')
	move()
	turtle.fillcolor('yellow')
	turtle.begin_fill()
	for i in range(5):
		turtle.forward(size)
		turtle.rt(180-36)
	turtle.end_fill()



def move():
	turtle.penup()
	x=random.randint(-500,500)
	y=random.randint(-300,300)
	turtle.goto(x,y)
	turtle.pendown()


turtle.bgcolor('black')
turtle.speed(0)


colors=['purple','blue','green','red']


for i in range(50):
	star(random.randint(5,15))

for i in range(30):
	pen(random.choice(colors))
	move()
	fireworks(random.randint(25,75))

pen('white')
turtle.penup()
turtle.goto(-200,0)
turtle.speed(10)
turtle.pendown()
turtle.write('Happy New Year',font=("Verdana", 45, "normal"))
turtle.done()

