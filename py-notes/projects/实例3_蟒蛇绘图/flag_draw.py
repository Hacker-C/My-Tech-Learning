# 一面有旗杆的国旗

from turtle import *

# 初始化位置
setup(800, 500, 200, 100)
up()
setx(-200)
sety(180)
speed(5)
ht()

# 画外形
down()
fillcolor('red')
begin_fill()
fd(300)
rt(90)
fd(200)
rt(90)
fd(300)

# 画旗杆
up()
rt(90)
fd(200)
end_fill()
lt(180)
down()
pensize(10)
fd(400)

# 画五角星
lt(180)
fd(350)
up()
rt(90)
fd(20)  # 第一个五角星离旗杆的距离
down()
pensize(1)
i = 5
fillcolor('yellow')
pencolor('yellow')
begin_fill()
while i:
    fd(60)
    rt(180 - 36)
    i -= 1
end_fill()

#  调整2位置
up()
fd(100)
lt(90)
fd(25)
lt(30)

# 第二个五角星
down()
begin_fill()
n = 5
while n:
    fd(20)
    rt(180 - 36)
    n -= 1
end_fill()

#  调整3位置
rt(170)
up()
fd(25)
down()
lt(90)

# 第三个五角星
begin_fill()
n = 5
while n:
    fd(20)
    rt(180 - 36)
    n -= 1
end_fill()

# 调整4位置
up()
rt(130)
fd(30)
lt(90)

# 第4个五角星
down()
begin_fill()
n = 5
while n:
    fd(20)
    rt(180 - 36)
    n -= 1
end_fill()

#  调整5位置
up()
rt(120)
fd(35)
lt(90)

# 第5个五角星
down()
begin_fill()
n = 5
while n:
    fd(20)
    rt(180 - 36)
    n -= 1
end_fill()

#  结束
done()
