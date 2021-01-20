import jieba
import wordcloud
import jieba.posseg as psg
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

# 设置字体为楷体
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']


def getStopWords(file):
    """读取停用词表stopwords.txt"""
    try:
        stopWords = [line.strip() for line in open(file, 'r', encoding='utf-8').readlines()]
        return stopWords
    except:
        print("读取停用词表失败！")


def getText(file):
    """获取文件内容"""
    try:
        with open(file, 'r', encoding='utf-8') as fp:
            txt = fp.read()
        return txt
    except:
        print("读取水浒传内容失败！")


def analyzeWordFrequency(file, txt, topNum, y=False):
    """ 获取指定范围词频图"""
    if y:
        # y来标注是否进行人名筛选
        seg = psg.cut(txt)
        words = [x.word for x in seg if x.flag == 'nr']
        for i in words:
            if i == '玄德曰' or i == '孔明' or i == '孔明曰' or i == '魏兵':
                words.remove(i)
    else:
        words = jieba.lcut(txt.strip())
    counts = {}
    stopwords = getStopWords(file1)
    for word in words:
        if len(word) == 1:
            continue
        elif word not in stopwords:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    with open(file, 'w', encoding='utf-8') as fp:
        for i in range(topNum):
            word, count = items[i]
            fp.writelines("{}\t{}\n".format(word, count))


def makeWordCloudImage(file):
    """制作词云图"""
    with open(file, 'r', encoding='utf-8') as fp:
        txt = fp.read()
        wcCloud = wordcloud.WordCloud(
            font_path=r'C:\Windows\Fonts\simhei.ttf',
            background_color="white",
            width=1000,
            # max_words=20,
            height=1000,
            margin=2
        ).generate(txt)
    wcCloud.to_file(file[:-4] + '.png')


def getSocialRelationImage(names):
    """出场次数最多的20位人物社交关系网络图"""
    try:
        with open(file2, 'r', encoding='utf-8') as fp:
            s = fp.read()

        relations = {}
        lst_para = s.split('\n')
        for txt in lst_para:
            for name1 in names:
                if name1 in txt:
                    for name2 in names:
                        if name2 in txt and name1 != name2 and (name2, name1) not in relations:
                            relations[(name1, name2)] = relations.get((name1, name2), 0) + 1
        maxRelations = max([v for k, v in relations.items()])
        relations = {k: v / maxRelations for k, v in relations.items()}
        # 构建社交关系网络
        plt.figure(figsize=(15, 15))
        G = nx.Graph()
        for k, v in relations.items():
            G.add_edge(k[0], k[1], weight=v)
        elarge = [(u, v) for (u, v, d) in G.edges(data=True)
                  if d['weight'] > 0.6]
        emiddle = [(u, v) for (u, v, d) in G.edges(data=True)
                   if 0.3 < d['weight'] <= 0.6]
        esmall = [(u, v) for (u, v, d) in G.edges(data=True)
                  if d['weight'] <= 0.3]
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, alpha=0.8, node_size=800)
        nx.draw_networkx_edges(G, pos, edgelist=elarge, width=2.5,
                               alpha=0.9, edge_color='g')
        nx.draw_networkx_edges(G, pos, edgelist=emiddle, width=1.5,
                               alpha=0.6, edge_color='y')
        nx.draw_networkx_edges(G, pos, edgelist=esmall, width=1,
                               alpha=0.4, edge_color='b', style='dashed')
        nx.draw_networkx_labels(G, pos, font_size=12)
        plt.axis('off')
        plt.title('《三国演义》主要人物社交关系图')
        plt.show()
    except:
        print('生成关系图失败！')


# ! 各个文件
file1 = 'stopwords.txt'  # 停用词表
file2 = '三国演义.txt'  # 三国演义原文件内容
file3 = '三国演义词频top500.txt'  # 前 500词频
file4 = '三国演义词频人名字top20.txt'  # 前20名字词频

# !获取原文件内容
text = getText(file2)

# !制作三国演义高频词词云图
analyzeWordFrequency(file3, text, 500)  # 获取前500高频词文件
makeWordCloudImage(file3)  # 制作前500高频词云图

# ！制作并显示三国演义名字前20社交关系图
analyzeWordFrequency(file4, text, 20, True)  # 获取高频词人名前20
Names = ['曹操', '关公', '张飞', '吕布',
         '孙权', '赵云', '司马懿', '周瑜', '魏延',
         '袁绍', '马超', '姜维', '黄忠', '诸葛亮',
         '庞德', '刘表', '张辽', '董卓', '刘备', '曹兵']
getSocialRelationImage(Names)
