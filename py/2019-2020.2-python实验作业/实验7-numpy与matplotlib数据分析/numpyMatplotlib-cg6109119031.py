import numpy as np
import matplotlib.pyplot as plt

# 设置水平轴的坐标范围为[-10,10]
x = np.arange(-10, 10, 0.1)
# f(x)
y1 = x ** 5 + 2 * x ** 3 + 1
# f(x)的一阶导数
y2 = 5 * x ** 4 + 6 * x ** 2
# f(x)的二阶导数
y3 = 20 * x ** 3 + 12 * x

# 将绘图区域分为三个子区域，当前绘制区域在第一个区域
plt.subplot(3, 1, 1)
plt.title('Polynominal')
plt.plot(x, y1, "r-")
# 将绘图区域分为三个子区域，当前绘制区域在第二个区域
plt.subplot(3, 1, 2)
plt.title('First Derivative')
plt.plot(x, y2, "b:")
# 将绘图区域分为三个子区域，当前绘制区域在第三个区域
plt.subplot(3, 1, 3)
plt.title('Second Devivative')
plt.plot(x, y3, "g.")
# 显示
plt.show()
