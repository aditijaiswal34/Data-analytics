from turtle import *

#define a function
def hexagon():
    for i in range(6):
        fd(100)
        lt(360/6)


# call the function
hexagon()
goto(100,100)
hexagon()
goto(-100,100)
hexagon()
goto(-100,100)
hexagon()
hideturtle()
mainloop()