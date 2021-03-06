#  实验三 字典与集合
#  三个已知初始数据
#  表1 小明舍友通信录数据
dictTXL = {
    "小新": [13912345678, 1819122001],
    "小亮": [13900001111, 1819122002],
    "小刚": [13900002222, 1819122003]
}
#  表2 隔壁宿舍舍长通信录数据
dictOther = {
    '大刘': [13912349876, 1819122004],
    '大张': [13911223344, 1819122005],
    '大王': [13988880911, 1819122006]
}
#  表3 部分微信号
dictWX = {
    '小新': 'xx007',
    '小刚': 'gang1001',
    '大王': 'jack_w',
    '大刘': 'liu666',
    '大张': '',
    '小亮': ''
}

#  按照小明的步骤创建通讯录 dictTXL
# 合并两个字典，也可以使用python3.9的字典联结运算符
#dictTXL |= dictOther
dictTXL.update(dictOther)

for k, v in dictTXL.items():
    #  创建微信号
    if dictWX[k]:
        v.append(dictWX[k])
        dictTXL[k] = v
    else:
        v.append(v[1])
        dictTXL[k] = v
    #  创建qq邮箱
    v.append(str(v[2]) + '@qq.com')
    dictTXL[k] = v

#  测试功能
#  1.将大王的手机号更改为13988889999
dictTXL['大王'][0] = 13988889999

#  打印通通讯录表
print("由代码生成的通信录：")
print("-" * 35 + "通信录" + "-" * 35)
print("{:<12}".format('\t姓名'), end='')
print("{:<12}".format('手机'), end='')
print("{:<12}".format('QQ'), end='')
print("{:<12}".format('微信号'), end='')
print("{:<12}".format('邮箱'), end='')
print()
for k, v in dictTXL.items():
    print("  {:<8}".format(k), end='')
    for info in v:
        print('{:<15}'.format(info), end='')
    print()
print("-" * 75)


def findInfo():
    #  2.输入姓名查找并输出对应同学的姓名、手机号、QQ号、Email、微信号
    name = input('请输入要查询的同学的姓名：')
    if name in dictTXL.keys():
        i = dictTXL[name]
        print('姓名:\t{0}\n手机号:\t{1}\nQQ号:\t{2}\nEmail:\t{3}\n微信号:\t{4}'
              .format(name, i[0], i[1], i[3], i[2]))
    else:
        print('抱歉！尚没有该同学的联系方式！')


findInfo()
