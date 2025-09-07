<<<<<<< HEAD
import turtle

screen = turtle.Screen()
screen.title("Trident Drawing")
screen.bgcolor("red")

trident = turtle.Turtle()
trident.color("black")
trident.pensize(3)
trident.speed(5)

def draw_trident():
    trident.penup()
    trident.goto(0, -100)
    trident.pendown()
    trident.goto(0, 100)
    
    trident.penup()
    trident.goto(0, 50)
    trident.pendown()
    trident.goto(-50, 100)
    trident.goto(-50, 50)
    trident.goto(0, 50)
    
    trident.penup()
    trident.goto(0, 50)
    trident.pendown()
    trident.goto(50, 100)
    trident.goto(50, 50)
    trident.goto(0, 50)
    
    trident.penup()
    trident.goto(0, -100)
    trident.pendown()
    trident.goto(0, -200)

draw_trident()

trident.hideturtle()
screen.mainloop()
=======
import turtle

screen = turtle.Screen()
screen.title("Trident Drawing")
screen.bgcolor("red")

trident = turtle.Turtle()
trident.color("black")
trident.pensize(3)
trident.speed(5)

def draw_trident():
    trident.penup()
    trident.goto(0, -100)
    trident.pendown()
    trident.goto(0, 100)
    
    trident.penup()
    trident.goto(0, 50)
    trident.pendown()
    trident.goto(-50, 100)
    trident.goto(-50, 50)
    trident.goto(0, 50)
    
    trident.penup()
    trident.goto(0, 50)
    trident.pendown()
    trident.goto(50, 100)
    trident.goto(50, 50)
    trident.goto(0, 50)
    
    trident.penup()
    trident.goto(0, -100)
    trident.pendown()
    trident.goto(0, -200)

draw_trident()

trident.hideturtle()
screen.mainloop()
>>>>>>> 397691e3bddc1c2468c0790a7ae5dcc8aba4e6c3
