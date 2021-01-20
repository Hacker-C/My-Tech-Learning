import requests
import json
if __name__ == "__main__":
    get_url = "https://movie.douban.com/j/chart/top_list"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    limit = input("请输入要爬取的榜单电影的数量：")
    param = {
        "type": "17",
        "interval_id": "100:90",
        "start": "0",
        "limit": limit,
        "action": ""
    }
    response = requests.get(url=get_url, params=param, headers=headers)
    # json对象
    list_data = response.json()
    with open("豆瓣科幻.json", "w", encoding="utf-8") as fp:
        json.dump(list_data, fp, ensure_ascii=False)
    print("爬取成功！")
