import requests
import json
if __name__ == '__main__':
    # 1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.post请求参数处理（同get请求）
    kw = input('请输入要翻译的单词（英翻中）:')
    data = {
        'kw': kw
    }
    # 3.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/86.0.4240.111 Safari/537.36'
    }
    # 4.请求成功则返回一个响应对象
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5.获取响应数据: json方法返回的是一个对象（需要确认响应数据类型是json类型才能使用）
    dict_obj = response.json()
    # 6.进行持久化存储
    fileName = kw + '.json'
    with open(fileName, 'w', encoding='utf-8') as fp:
        json.dump(dict_obj, fp, ensure_ascii=False)
    print('数据爬取结束！')


