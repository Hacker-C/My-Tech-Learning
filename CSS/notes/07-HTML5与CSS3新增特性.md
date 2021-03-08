# （七）HTML5与CSS3新增特性

## 1. HTML5新特性

### 1.1 HTML5新增语义化标签

- `<header>`：头部标签
- `<nav>`：导航标签
- `<article>`：内容标签
- `<section>`：定义文档某个区域
- `<asider>`：侧边栏标签
- `<footer>`：尾部标签

### 1.2 HTML5新增多媒体标签

#### 1. 视频 `<vedio>`

所有浏览器支持 mp4 格式。

- `autoplay="autoplay"` 
- `controls="controls"` 显示控件
- `width` 设置宽度
- `height` 设置高度
- `loop=loop` 设置循环播放
- `preload="auto/none"` 是否预加载
- `src=url` 视频地址 
- `poster=url` 封面图片
- `muted=muted` 静音播放

#### 2. 音频 `<audio>`

所有浏览器支持 mp3 格式。

- `controls`：显示控件
- `autoplay`：（谷歌禁用）
- `loop=loop` 设置循环播放

### 1.3 HTML5 新增 input 类型

- `type="email"`
- `type="url"`
- `type="date"`
- `type="time"`
- `type="month"`
- `type="week"`
- `type="number"`
- `type="tel"`
- `type="search"`
- `type="color"`

### 1.4 HTML5新增的表单属性

|属性 |值 |说明|
|-|-|-|
|required |required |表单拥有该属性表示其内容不能为空，必填|
|placeholder |提示文本| 表单的提示信息|
|autofocus |autofocus |自动聚焦属性，页面加载完成自动聚焦到指定表单|
|autocomplete| off/on|当用户在字段开始键入时，浏览器基于之前键入过的值，应该显示出在字段中填写的选项默认已经打开,如autocomplete="on",关闭autocomplete ="off" 需要放在表单内，同时加上name属性，同时成功提交|
|multiple|multiple| 可以多选文件|

可以通过以下设置方式修改placeholder里面的字体颜色：

```css
input::placeholder {
    color: pink;
}
```

## 2. CSS3 新特性

### 2.1 CSS3 新增选择器

CSS3给我们新增了选择器，可以更加便捷，更加自由的选择元素。

1. 属性选择器
2. 结构伪类选择器
3. 伪元素选择器

### 2.2 属性选择器

属性选择器可以根据元素特定属性的来选择元素。这样就可以不用借助于类或者id选择器。
|简介| 选择|
|-|-|
|`E[att]`|选择具有att属性的E元素|
|`E[att:val`|选择具有att属性且属性值等于val的E元素|
|`E[att^=val]`|匹配具有att属性且值以val开头的E元素|
|`E[att$=val]`|匹配具有att属性且值以val结尾的E元素|
|`E[att*=val]`|匹配具有att属性且值中含有val的E元素|

```css
input[type=text] {
    color: green;
}
```

```HTML
<input type="password">
<input type="text">
```

类选择器、属性选择器、伪类选择器的权重都为 10