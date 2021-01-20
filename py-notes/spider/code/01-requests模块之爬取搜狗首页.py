import requests

if __name__ == '__main__':
    # 1.指定url
    url = 'https://www.sogou.com'
    # 2.发起请求
    # get方法会返回一个响应对象
    response = requests.get(url=url)
    # 3.获取响应数据，返回字符串类型的响应数据
    page_text = response.text
    print(page_text)
    # 4.持久化存储
    with open('./sougou.html', 'w', encoding='utf-8') as f_project:
        f_project.write(page_text)
    print('爬取数据结束.')
