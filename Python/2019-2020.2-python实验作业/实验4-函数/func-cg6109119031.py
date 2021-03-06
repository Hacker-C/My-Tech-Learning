import random as rd
import math
import time

# 1.函数一：蒙特卡洛模拟计算圆周率
def MonteCarloPI(N):
    M = 0
    for i in range(N):
        randX = rd.uniform(-1, 1)
        randY = rd.uniform(-1, 1)
        distance = math.sqrt(randX ** 2 + randY ** 2)
        if distance < 1:
            M += 1
    return 4 * M / N


# 2.函数二：蒙特卡洛计算机积分值 f(x)=x^2
def FunctionIntegrals(N, a, b):
    M = 0
    for i in range(N):
        randX = rd.uniform(a, b)
        # 设置函数
        randY = rd.uniform(0, pow(b, 2))
        Y = pow(randX, 2)
        if randY <= Y:
            M += 1
    return M / N * (b - a) * pow(b, 2)


#  3.函数三：计算函数极值，可避免陷入局部极值
def FunctionMaxValuePoint(N):
    maxX = -2
    maxY = math.sin(-2) * pow(math.e, -0.05 * -2)
    for i in range(N):
        rangX = rd.uniform(-2, 2)
        y = math.sin(rangX) * pow(math.e, -0.05 * rangX)
        if y > maxY:
            maxY = y
            maxX = rangX
    return maxX, maxY


# 测试
# 测试数据
data = (1e2, 1e3, 1e4, 1e5, 1e6, 1e7)
t1 = time.time()
# 1. 测试圆周率
print("1. 圆周率模拟计算及结果精度测试比较")
print("{0:<8}{1:<8}{2:<8}".format("测试样本N", "计算所得PI", "精度差"))
for i in data:
    i = int(i)
    print("{0:<11}{1:<11}{2:<11.1e}".format(i, MonteCarloPI(i), abs(MonteCarloPI(i) - math.pi)))
print("-"*30)

# 2. 测试积分计算
print("2. 函数定积分模拟计算以及精度测试比较结果")
print("{0:<8}{1:<8}{2:<8}".format("测试样本N", "模拟计算结果", "精度差"))
for i in data:
    i = int(i)
    re = FunctionIntegrals(i, 0, 1)
    x = abs(re - 1 / 3)
    print("{0:<11}{1:<12}{2:<11.1e}".format(i, re, x))
print("-"*30)

# 3. 测试极大值计算
print("3. 函数极大值模拟计算结果以及精度比较结果")
print("{0:<8}{1:<10}{2:<10}{3:<10}".format("测试样本N", "极大值点x", "极大值y", "精度差"))
for i in data:
    i = int(i)
    tup = FunctionMaxValuePoint(i)
    x1 = tup[0]
    x2 = tup[1] * 200
    x3 = abs(tup[0] - 1.5144491499169481)
    print("{0:<11}{1:<12.6f}{2:<13.6f}{3:<12.1e}".format(i, x1, x2, x3))

t2 = time.time()
print("运行结束，共耗时{:.2f}s".format(t2-t1))
