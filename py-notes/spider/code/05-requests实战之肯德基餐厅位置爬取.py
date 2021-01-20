import requests
import json
import ast

null = ''


def bb():
    global null


if __name__ == '__main__':
    bb()
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    keyword = input('请输入要查询的餐厅位置关键词：')
    # param = {
    #     'op': keyword
    # }
    data = {
        'cname': '',
        'pid': '',
        'keyword': keyword,
        'pageIndex': '1',
        'pageSize': '100'
    }
    response = requests.post(url=post_url, headers=headers, data=data)
    dict_obj = response.text
    fileName = keyword + 'KFC地址.json'
    with open(fileName, 'w', encoding='utf-8') as fp:
        dic = json.loads(dict_obj)
        json.dump(dic, fp, ensure_ascii=False)
    print("爬取成功！")
