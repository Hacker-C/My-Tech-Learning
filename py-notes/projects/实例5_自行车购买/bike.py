# Bike Store

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# 展示剩余单车函数 left()
def left():
    print('-' * 20 + 'Bikes-Store' + '-' * 20 + '\nLeft:')
    n = 0
    print('0.quit')
    for i in range(len(bicycles)):
        print('{0}.{1}'.format(i + 1, bicycles[i]))

left()

while True:
    love = int(input('-' * 51  + '\nPlease choose your love(input numbers of bike): '))
    if love == 0:
        left()
        break
    elif 1 <= love <= 4:
        print('My Fisrt bike is {}.'.format(bicycles[love - 1].title()))
        # 弹出已被购买的商品并存储
        bought  = bicycles.pop(love - 1)
        print('You had bought {} successfully!'.format(bought.title()))
        left()
    else:
        print('Please input the right number(0-4): ')