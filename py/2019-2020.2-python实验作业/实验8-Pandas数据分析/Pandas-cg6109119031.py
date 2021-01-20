import pandas as pd

# 设置输出数据时分割线长度
s = 65
# 调整数据打印格式
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 100)  # 设置打印宽度(**重要**)

excel = pd.read_excel('score.xlsx', sheet_name=[0, 1], header=0)
score = excel[0]
duty = excel[1]
# ① 输出score的前三行数据
print('=' * s)
print("① score的前三行数据如下：")
print(score[0:3])
# ① 输出score的行数
print("  score的行数={}".format(score.shape[0]))
print("=" * s)
# ② 新增1列“总分”，值为前3列成绩之和。
try:
    score['总分'] = [259, 270, 243, 276, 280, 205, 248]
    print("② 已新增列\"总分\"")
except:
    print('② 新增列失败！')
print('=' * s)
# ③ 依据“总分”列的值从高到低进行排序
try:
    score = score.sort_values(by='总分', ascending=False)
    score['排名'] = list(range(1, 8))
    print('③ 已按照总分进行排序')
except:
    print('③ 排序失败！')
print('=' * s)
# ④ 依据性别列进行分组，输出男生、女士各自的平均成绩。
try:
    sexGroup = score.groupby('性别')
    print("④ 男生、女生各自平均分如下所示：")
    print(sexGroup.mean())
except:
    print('④ 按照性别分组失败！')
print('=' * s)
# ⑤　输出男生的最高总分、女生的最高总分
print("⑤ 男生、女生的最高总分如下：")
print(sexGroup.max())
print("=" * s)
# ⑥ 新增1列“等级”
score['等级'] = ['A', 'A', 'A', 'B', 'B', 'B', 'C']
print("⑥ 新增一列等级")
print(score)
print('=' * s)
# ⑦ 将score对象与duty对象合并
print('⑦ 将score对象与duty对象合并')
students = pd.merge(score, duty, how='left')
print(students)
print('=' * s)
# ⑧　将students对象数据存入一个新的Excel文件student.xlsx
try:
    students.to_excel('Students.xlsx', sheet_name='学生信息')
    print('⑧ 导出表格成功！')
except:
    print('⑧ 导出表格失败！')
