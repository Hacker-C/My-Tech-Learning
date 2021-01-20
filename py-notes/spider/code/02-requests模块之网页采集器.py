import requests

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/86.0.4240.111 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数：封装到字典中
    keywords = input('请输入所搜关键字：')
    param = {
        'query': keywords
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    fileName = keywords + '.html'
    with open(fileName, 'w', encoding='utf-8') as f_project:
        f_project.write(page_text)
    print(fileName + ' 保存成功！')
