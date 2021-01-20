# json库

> 标准库
>
> JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。
>
> json库用来编码和解码 JSON 对象。

## 1. json.dumps

` json.dumps()` 将python对象格式化成json字符。

## 2. json.loads

`json.loads()` 将json字符串解码成python对象。

## 3. json.dump

`json.dump()` 主要用来将python对象写入json文件。

```python
json.load(source_data, json_file, ensure_ascii=False)
```

## 4. json.load

`json.load()` 加载json格式文件，返回python对象。