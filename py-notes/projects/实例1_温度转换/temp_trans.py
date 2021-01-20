# 温度转换
temp_str = input('请输入温度（以C或F结尾）：')
if temp_str[-1] in ['f', 'F']:
    C = (eval(temp_str[0:-1]) - 32 ) / 1.8
    print('转换后的温度是：{:.2f}C'.format(C))
elif temp_str[-1] in ['c', 'C']:
    F = (eval(temp_str[0:-1]) * 1.8 + 32)
    print('转换后的温度是：{:.2f}F'.format(F))
else:
    print('请输入正确格式！')

print('{:.2f}'.format(123.4567))
