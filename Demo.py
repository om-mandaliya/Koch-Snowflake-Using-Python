import turtle

def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)
        t.right(120)
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-150, 150)
t.pendown()

t.color("blue")
for i in range(3):
    koch_snowflake(t, 300, 3)
    t.right(120)

turtle.done()
