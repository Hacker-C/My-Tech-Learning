"""
姓名：陈桂
学号：6109119031
专业班级：计算机191班
程序目前实现的功能：
1. 通过设置U-A伪装，爬取到了豆瓣Top250榜单的前100，获取其对应html，并存入html文件中
2. 从html代码中过滤出标签的内容和图片的src属性，从而获取有用信息
    目前获取的信息有：电影名，排名，导演名/演员名/电影类型，电影海报信息
3. 实现了在python解释器中的简单交互模式，可通过【电影排名】来搜索获取电影相关信息（以上）
4. 实现了将数据存入Excel文件中
版本信息：
python: 3.8.5
requests: 2.24.0
BeautifulSoup4(bs4): 4.9.3
pandas: 1.2.0
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings

# 暂时忽略所有的警告信息
warnings.simplefilter('ignore')


def spiderOfTop250():
    """爬取豆瓣250榜单前100HTML文件"""
    url = 'https://movie.douban.com/top250'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/86.0.4240.111 Safari/537.36'
    }
    # 循环爬取四次，每次25部电影，共爬取到豆瓣Top250得前100部电影
    L = ['0', '25', '50', '75']
    for start in L:
        # 处理url携带的参数：封装到字典中
        params = {
            'start': start
        }
        try:
            # get方法返回一个响应对象
            response = requests.get(url=url, headers=headers, params=params)
            # 获取响应数据 .text返回的是字符串形式的响应对象
            page_text = response.text
            # 将爬取的HTML代码都存入html文件中
            filename = '豆瓣榜单' + start + '.html'
            with open(filename, 'w', encoding='utf-8') as fp:
                fp.write(page_text)
        except:
            print('爬取豆瓣Top' + str(int(start) + 25) + '失败！')
        else:
            print('爬取豆瓣Top' + str(int(start) + 25) + '成功！O(∩_∩)O\n......')


def getFilmName():
    """获取电影名"""
    re = []
    # 循环四次获取电影名，一次25部，共100部
    for i in ['0', '25', '50', '75']:
        filename = '豆瓣榜单' + i + '.html'
        bsObj = BeautifulSoup(open(filename, 'r', encoding='utf-8'))  # 用本地 HTML 文件来创建对象
        nameTagList = bsObj.findAll("span", {"class": "title"})
        nameTextList = []
        for item in nameTagList:
            nameTextList.append(item.get_text())
        # 去除重复电影名
        for item in nameTextList:
            if '/' not in item:
                re.append(item)
    return re


def getFilmScore():
    """获取电影评分"""
    scoreList = []
    # 循环获取
    for i in ['0', '25', '50', '75']:
        filename = '豆瓣榜单' + i + '.html'
        bsObj = BeautifulSoup(open(filename, 'r', encoding='utf-8'))
        scoreTagList = bsObj.findAll("span", {"class": "rating_num"})
        for item in scoreTagList:
            scoreList.append(item.get_text())
    return scoreList


def getDirectorNames():
    """获取导演和演员名字"""
    re = []
    def g(x):
        # 判断中文字符，配合filter函数去除非中文字符
        if '\u4e00' <= x <= '\u9fa5':
            return x
    # 循环获取
    for i in ['0', '25', '50', '75']:
        filename = '豆瓣榜单' + i + '.html'
        bsObj = BeautifulSoup(open(filename, 'r', encoding='utf-8'))
        L = bsObj.findAll("p", {"class": ""})
        for item in L:
            s = (item.get_text()).strip()
            s = ''.join(list(filter(g, s)))
            re.append(s)
    return re


def getPosters():
    """获取海报链接"""
    re = []
    # 循环获取
    for i in ['0', '25', '50', '75']:
        filename = '豆瓣榜单' + i + '.html'
        bsObj = BeautifulSoup(open(filename, 'r', encoding='utf-8'))
        # 过滤出所有的图片链接
        imgs = bsObj.find_all('img')
        for item in imgs:
            re.append(item.get('src'))
    return re


def saveToExcel(export):
    """存入Excel文件"""
    try:
        # 将字典列表转换为DataFrame
        pf = pd.DataFrame(list(export))
        # 指定字段顺序
        order = ['电影名', '排名', '电影评分', '导演演员及电影类型名', '电影海报链接']
        pf = pf[order]
        # 将列名替换为中文
        columns_map = {
            '电影名': '电影名',
            '排名': '排名',
            '电影评分': '电影评分',
            '导演演员及电影类型名': '导演演员及电影类型名',
            '电影海报链接': '电影海报链接'
        }
        pf.rename(columns=columns_map, inplace=True)
        # 指定生成的Excel表格名称
        file_path = pd.ExcelWriter('豆瓣Top250榜单前100.xlsx')
        # 替换空单元格
        pf.fillna(' ', inplace=True)
        # 输出
        pf.to_excel(file_path, encoding='utf-8', index=False)
        # 保存表格
        file_path.save()
    except:
        print("存入Excel文件失败！")
    else:
        print("存入Excel成功！O(∩_∩)O\n")


def searchFilmInfo(FilmList):
    """电影信息查询"""
    while 1:
        print("--->>>请输入电影排名以查询(1-100)，输入q退出：", end=' ')
        try:
            s = input()
            # q退出
            if s == 'q' or s == 'Q':
                print("再见！")
                break
            else:
                rankNum = int(s)
        except:
            print("请输入数字！")
        else:
            if 1 <= rankNum <= 100:
                print("=" * 50)
                # 输出查询电影信息
                for k, v in FilmList[rankNum - 1].items():
                    print("{0}：{1}".format(k, v))
                print("=" * 50)
            else:
                print("请输入1-100的数字")


# 开始爬取
spiderOfTop250()
# 获取前100电影名
names = getFilmName()
# 获取电影评分
scores = getFilmScore()
# 获取导演演员名字以及电影类型
directors = getDirectorNames()
# 获取电影海报图片链接
images = getPosters()
# 将爬取并过滤的数据存入Excel文件
FilmsList = []
for i in range(100):
    FilmsList.append({
        "电影名": names[i],
        "排名": i + 1,
        "电影评分": scores[i],
        "导演演员及电影类型名": directors[i],
        "电影海报链接": images[i]
    })
saveToExcel(FilmsList)
# 查询函数
searchFilmInfo(FilmsList)
