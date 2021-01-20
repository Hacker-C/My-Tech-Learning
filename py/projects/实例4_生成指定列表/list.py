# 生成一个1-100的奇数列表l1
l1 = [x for x in range(100) if x % 2 != 0]

# 生成嵌套列表l2
l2 = []
for i in range(0, 16, 4):
    l_temp = list()
    for j in range(i, i+4):
        l_temp.append(i)
        i += 1
    l2.append(l_temp)

# 将嵌套列表平铺l3
l3 = [num for l1 in l2 for num in l1]

# 生成质数列表l4(1-100)
from math import sqrt
l4 = []
for i in range(2, 100):
    is_even = True
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            is_even = False
    if is_even:
        l4.append(i)

print('生成的奇数列表：{}'.format(l1))
print('生成的嵌套列表：{}'.format(l2))
print('平铺后的列表：{}'.format(l3))
print('生成的质数列表：{}'.format(l4))