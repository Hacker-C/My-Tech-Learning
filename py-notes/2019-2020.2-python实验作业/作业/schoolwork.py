import jieba
import csv

# 读取原始文件
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

# 整合词频信息，存储到字典
newInfo = []
for elem in wordsCountInfo:
    if elem[0] not in stopwords:
        newInfo.append(elem)
# 取出前20
newInfo = newInfo[:20]
newInfo = dict(newInfo)


# 将结果存入D盘下的JaneEyre.csv
def saveToCsv():
    try:
        csvFile = open("D:\\JaneEyre.csv", "w", newline="")
        writer = csv.writer(csvFile)
        for k in newInfo:
            writer.writerow([k, newInfo[k]])
        csvFile.close()
    except:
        print("存入CSV文件失败！")
    else:
        print("存入JaneEyre.csv成功！")


saveToCsv()
