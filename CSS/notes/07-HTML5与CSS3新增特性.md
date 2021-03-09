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

### 2.3 结构伪类选择器

结构伪类选择器主要根据文档结构来选择器元素，常用于根据父级选择器里面的子元素。

| 选择符              | 简介             |
|------------------|----------------|
| `E: first-child`    | 匹配父元素中的第一个子元素E |
| `E: last-child`     | 匹配父元素中最后一个E元素  |
| `E: nth-child(n)`   | 匹配父元素中的第n个子元素E |
| `E: first-of-type`  | 指定类型E的第一个      |
| `E: last-of-type`   | 指定类型E的最后一个     |
| `E: nth-of-type(n)` | 指定类型E的第n个      |

```css
ul li:first-child {
    background-color: pink;
}
ul li:last-child {
    background-color: pink;
}
ul li:nth-child(5) {
    background-color: skyblue;
}
```

重点：`E: nth-child(key)`

- `key` 可以是整数、关键字（`even/odd`）、公式（`n/2n/2n+1`）

|公式|取值|
|-|-|
|2n|偶数|
|2n-1|奇数|
|5n|5 10 15 ...|
|n+|5 6 7 8 ...|
|-n+5|前五个|

关于 `nth-of-type` 与 `nth-of-child`

1. `div: nth-child` 会把所有的盒子都排列序号 
    执行的时候首先看  `:nth-child(1)` 之后回去看 前面 `div`
2.  `div: nth-of-type` 会把指定元素的盒子排列序号
    执行的时候首先看  div指定的元素  之后回去看 `:nth-of-type(1)` 第几个孩子 

区别：
1. nth—child对父元素里面所有孩子排序选择（序号是固定的）先找到第n个孩子，然后看看是否和E匹配
2. nth—of—type对父元素里面指定子元素进行排序选择。先去匹配E ，然后再根据E找第n个孩子

### 2.4 伪元素选择器

==伪元素选择器可以帮助我们利用CSS创建新标签元素，而不需要HTML标签，从而简化HTML结构。==

|选择符 |简介|
|-|-|
|`::before` |在元素内部的前面插入内容|
|`::after`|在元素内部的后面插入内容|

注意：
- before 和 after 创建一个元素，但是属于行内元素
- 新创建的这个元素在文档树中是找不到的，所以我们称为伪元素
- 语法：`element：before{}`
- before 和 after 必须有 content 属性
- before 在父元素内容的前面创建元素， after 在父元素内容的后面插入元素
- 伪元素选择器和标签选择器一样，权重为 1

#### 案例一：伪元素字体图标

```css
 div::after {
    position: absolute;
    top: 10px;
    right: 10px;
    font-family: 'icomoon';
    content: '\e91b';
    color: red;
    font-size: 18px;
}
```

#### 案例二：伪元素遮罩层

```css
.tudou::before {
    content: '';
    display: none;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, .3) url(images/arr.png) no-repeat center;
}
```

#### 案例三：伪元素清除浮动


```css
.clearfix::after {
    content: '';
    display: block; 
    height: 0;
    clear: both;
    visibility: hidden;
}
```

双伪元素清除浮动

```css
.clearfix::before,
.clearfix::after {
    content: '';
    display: block;
}
.clearfix::after {
    clear: both;
}
```

### 2.5 CSS3盒子模型

CSS3中可以通过 box-sizing 来指定盒模型，有2个值：即可指定为 content-box，border-box ，这样我们计算盒子大小的方式就发生了改变。

可以分成两种情况：

1. ==box-sizing：content-box== 盒子大小为 width + padding + border （以前默认的）
2. ==box-sizing: border-box== 盒子大小为width
如果盒子模型我们改为了 box-sizing： border-box ，那padding 和 border就不会撑大盒子了（前提 padding 和 border 不会超过 width 宽度）

### 2.6 CSS3 的其他特性

#### 1. CSS3 滤镜 filter

filter CSS属性将模糊或颜色偏移等图形效果应用于元素。

```css
filter: 函数();
```
例如： `filter： blur(5px);` blur 模糊处理数值越大越模糊

#### 2. CSS3 calc函数

此 CSS 函数让你在声明CSS属性值时执行一些计算。

```css
width: calc(100%-30px);
/* 子盒子永远比父盒子小30px */
```
括号里面可以使用 `+ - * /` 来进行计算。

#### 3. CSS3 还有一些 2D、3D效果。。。

### 2.7 CSS3过渡（重点）

过渡（transition）是CSS3中具有颠覆性的特征之一，我们可以在不使用Flash动画或JavaScript的情况下，当元素从一种样式变换为另一种样式时为元素添加效果。

过渡动画：是从一个状态渐渐的过渡到另外一个状态
可以让我们页面更好看，更动感十足，虽然低版本浏览器不支持（ie9以下版本）但是不会影响页面布局。

==我们现在经常和 :hover 一起搭配使用。==

#### transition 的使用

```css
transition: 要过渡的属性 花费时间 运动曲线 何时开始;
```

1. 属性：想要变化的css属性，宽度高度背景颜色内外边距都可以。如果想要所有的属性都变化过渡，写一个all就可以。
2. 花费时间：单位是秒（==必须写单位==）比如 0.5s
3. 运动曲线：默认是ease （可以省略）
4. 何时开始：单位是秒（==必须写单位==）可以设置延迟触发时间默认是Os （可以省略）

```css
 div {
    width: 200px;
    height: 100px;
    background-color: pink;
    /* transition: width .5s, height .5s; */
    transition: all .5s;
}
div:hover {
    width: 400px;
    height: 200px;
    background-color: skyblue;
}
```
