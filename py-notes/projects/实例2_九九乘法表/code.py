# 实例2：九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{1:d} x {0:d} = {2:d}'.format(i, j, i * j), end='\t')
    print()
