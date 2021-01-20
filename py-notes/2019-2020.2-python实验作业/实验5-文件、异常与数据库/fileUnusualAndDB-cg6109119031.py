import jieba
import json
import sqlite3

with open('Jane Eyre.txt', 'r') as fp:
    lines = fp.readlines()


def f(x):
    # 去除标点符号
    useless = [',', '.', '"', ",", '[', ']', ':', ';', '?', '!', '(', ')', '/', '_', '#', '*', '\\']
    if x not in useless:
        return x


allWords = []  # 存放所有单词（含重复）
for i in lines:
    if i.strip():
        s = ''.join(list(filter(f, i.strip())))  # 去除非英文字符
        ls1 = jieba.lcut(s)
        for j in ls1:
            if j != ' ':
                allWords.append(j)

wordsCountInfo = dict()
for i in allWords:
    if i not in wordsCountInfo:
        wordsCountInfo[i] = 1
    else:
        wordsCountInfo[i] += 1
# 按值排序
wordsCountInfo = sorted(wordsCountInfo.items(), key=lambda x: x[1], reverse=True)
# 使用停用词表去除虚词
try:
    with open('stopwords.txt', 'r') as fp:
        stopwords = fp.readlines()
        for i in range(len(stopwords)):
            stopwords[i] = stopwords[i].strip()
except FileNotFoundError:
    print("读取失败！")
else:
    print("停用词表读取成功！")

newInfo = []
for elem in wordsCountInfo:
    if elem[0] not in stopwords:
        newInfo.append(elem)
# 取出前20
newInfo = newInfo[:20]
newInfo = dict(newInfo)


# 1.存储到文件（Top20Words.json）中
def saveToFile():
    try:
        with open('Top20Words.json', 'w') as fp:
            json.dump(newInfo, fp=fp, ensure_ascii=False)
    except:
        print('存储到json文件中失败！')
    else:
        print("存储到json文件中成功！")


saveToFile()

# 2. 存储到数据库中
db_file = 'Top20Words.db'


def insertScoreData():
    try:
        # 1.获取连接
        conn = sqlite3.connect(db_file)
        # 2. 打开游标
        cur = conn.cursor()
        # 3.插入sql语句
        # insert into + 表名(列1，列2，...) values(?,?,...)
        sql = 'insert into Top20Word (word, count) values(?,?)'
        for k, v in newInfo.items():
            data = (k, v)
            cur.execute(sql, data)
        # 执行插入时需要进行显示提交数据，否则无法同步到数据库中
        conn.commit()
        # 4. 关闭数据库
        cur.close()
        conn.close()
    except:
        print("存储到数据库文件中失败！")
    else:
        print('存储到数据库文件中成功！')


insertScoreData()
