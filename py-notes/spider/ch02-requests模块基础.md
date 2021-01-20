#  requests模 块

- urllib模块（复杂）
- <font color=red>requests模块</font>（简洁，高效）

## requests模块

python中原生的一款基于网络请求的模块，功能非常强大，简单便捷，效率极高。
作用：<font color=red>模拟浏览器发请求。</font>

语法：

```python

```

## 如何使用：（requests模块的编码流程）

1. 指定url
   + UA伪装
   + 参数的处理

2. 发起请求

3. 获取响应数据

4. 持久化存储

## 环境安装：

```bash
pip install requests
```

## 实战编码：

1. 需求：爬取搜狗首页的页面数据

2. 需求：爬取搜狗指定词条对应的搜索结果页面（简易网页采集器）

   + UA：User-Agent（请求载体的身份标识）

   + UA检测

     <font color=red>门户网站的服务器会检测对应请求的载体身份标识，如果检测到的身份标识为某一款浏览器，说明该请求是一个正常的请求。但是如果检测到的请求载体不是基于某一种浏览器的，则表示该请求为不正常的请求（爬虫），则服务器端就很可能拒绝该次请求。</font>

   + UA伪装

     <font color=green>让爬虫对应的请求载体身份标识伪装成某一款浏览器</font>

     ```python
     headers = {
         User-Agent: 'Mozila/...'
     }
     ```

3. 需求：破解百度翻译
   + <font color=red>post请求（携带了参数）</font>
   + 响应数据是一组json数据

4. 需求：爬取豆瓣电影分类排行榜 https://movie.douban.com/中的电影详情数据

5. 作业：爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点的餐厅数据

6. 需求：爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据
     http://scxk.nmpa.gov.cn:81/xk/

     + <font color=red>动态加载数据</font>

     + <font color=red>首页中对应的企业信息数据是通过ajax动态请求到的。</font>

       ```
       http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList
       ```
       
     + 通过对详情页url的观察发现：

        - 所有的url的域名都是一样的，只有携带的参数（id）不一样

        - 如果我们可以批量获取多家企业的id后，就可以将id和url形成一个完整的详情页对应数据的ajax请求的url

        - id值可以从首页对应的ajax请求到的json串中获取

        - 域名和id值拼接处一个完整的企业对应的详情页的url

        - <font color=red>详情页的企业详情数据也是动态加载出来的</font>

          ```
          http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
          ```

     + 观察后发现
       + 所有的post请求的url都是一样的，只有参数id值是不同。
       + 如果我们可以批量获取多家企业的id后，就可以将id和url形成一个完整的详情页对应详情数据的ajax请求的url

> 下一章：
>
> 数据解析：
>
> + 聚焦爬虫
> + 正则
> + bs4
> + xpath