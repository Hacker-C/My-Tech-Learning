# python 小蛇
from turtle import *
setup(800, 600, 200, 80)
pensize(35)
pencolor('purple')
up()
left(180)
fd(300)
left(180)
down()
r = 50
rt(60)
for i in range(6):
    circle(r, 120)
    r = -r
lt(60)
fd(30)
dot(10, 'black')
done()