from turtle import *
pensize(10)

#leaves
pencolor("green")
penup()
goto(-50, 100)
pendown()
fillcolor("greenyellow")
begin_fill()
goto(50, 100)
goto(0, 50)
goto(-50, 100)
end_fill()

#stem
penup()
goto(0, 200)
pendown()
goto(0,0)
