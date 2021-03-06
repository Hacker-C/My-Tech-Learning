playersList = [
    ("王平", "男", 1, 1, 0, 0, 1, 1, 0),
    ("李丽", "女", 0, 1, 0, 1, 0, 1, 1),
    ("陈小梅", "女", 0, 0, 1, 0, 1, 0, 1),
    ("孙洪涛", "男", 0, 1, 1, 1, 0, 0, 1),
    ("方亮", "男", 1, 0, 1, 0, 0, 0, 1),
    ("范闲", "男", 0, 0, 0, 0, 1, 1, 1)
]

countsOverTwo = 0
female = []  # 存储女性选手的索引
ThreeKM = []  # 3000m选手索引
maleCount = femaleCount = 0  # 用于比较参加项目数量
maleMax = femaleMax = 0  # 存储参加项目最多的男女的索引


#  定义输出参加运动会情况的函数
def showDetails(it):
    print("{}参加了: ".format(it[0]), end='')
    if it[2]:
        print('100m', end=' ')
    if it[3]:
        print('3000m', end=' ')
    if it[4]:
        print('跳远', end=' ')
    if it[5]:
        print('跳高', end=' ')
    if it[6]:
        print('田径', end=' ')
    if it[7]:
        print('跨栏', end=' ')
    if it[8]:
        print('接力赛跑', end=' ')
    print()


#  遍历列表，筛选符合条件的信息
for tup in playersList:
    if sum(tup[2:]) >= 2:
        countsOverTwo += 1
    if tup[1] == '女':
        female.append(playersList.index(tup))
    if tup[3]:
        ThreeKM.append(playersList.index(tup))
    if tup[1] == '男' and tup.count(1) > maleCount:
        maleMax = playersList.index(tup)
        maleCount = tup.count(1)
    if tup[1] == '女' and tup.count(1) > femaleCount:
        femaleMax = playersList.index(tup)
        femaleCount = tup.count(1)

#  根据筛选得到的信息输出相关信息
print("1.报名项目超过两项（含两项）的学生人数：{}".format(countsOverTwo))
print('-' * 20)
print("2.女生的报名情况：")
print("共有{}位女生报名。".format(len(female)))
for i in female:
    showDetails(playersList[i])
print('-' * 20)
print("3.所有报名3000m的学生姓名和性别：")
for i in ThreeKM:
    print("{0}, {1}".format(playersList[i][0], playersList[i][1]))
print('-' * 20)
print("4.输出参加运动项目最多的男选手是：{}".format(playersList[maleMax][0]))
showDetails(playersList[maleMax])
print("输出参加运动项目最多的女选手是：{}".format(playersList[femaleMax][0]))
showDetails(playersList[femaleMax])
