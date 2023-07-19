from turtle import *

speed('fastest')
colors=['pink','blue','yellow','purple']
pensize(2)
for i in range(100):
     print(i%4,colors[i%4])
     pencolor(colors[i%4])
     fd(i*2)
     lt(90)
     circle(i*2,60)
mainloop()     