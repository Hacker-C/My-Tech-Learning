# 猜单词游戏
# 引入random和sqlite3库
from random import choice, shuffle
import sqlite3

# 数据库部分
# 数据库文件
db_file = 'WORDS.db'
# 连接数据库
conn = sqlite3.connect(db_file)
# 数据库操作
sql = 'select * from WORDS'
# 执行数据库操作
cur = conn.cursor()
cur.execute(sql)
# 从数据库读取单词

WORDS = cur.fetchall()[0][0].split(',')
# 关闭数据库
conn.close()

# 游戏逻辑部分
print('''      欢迎参加猜单词游戏
请把下列各字母组合成一个正确的单词.
''')

isContinue = 'Y'
while isContinue == 'Y' or isContinue == 'y':
    word = choice(WORDS)
    # true 存放正确顺序的单词
    correct = word
    # 打乱词序
    ls = list(word)
    shuffle(ls)
    next = ''.join(ls)
    print('乱序后单词：{}'.format(next))
    # 猜单词部分
    userInput = input('请你猜:')
    if userInput != correct and userInput != '':
        print('对不起，不正确.')
        while True:
            userInput = input('继续猜：')
            if userInput == correct:
                print('真棒，你猜对了！')
                break
            else:
                print('要继续猜吗？（Y/N）: ')
                if input() == 'n':
                    break
    else:
        print('真棒，猜对了！')
    isContinue = input('是否继续（Y/N）：')
