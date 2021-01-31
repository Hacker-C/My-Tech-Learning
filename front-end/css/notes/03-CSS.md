# （三）CSS

## 1. 盒子模型

### 1.1 看透网页本质

网页布局过程：

1. 准备网页元素，网页元素基本都是盒子 box
2. ==利用 CSS 设置好盒子样式，然后摆放到相应位置。==
3. 往盒子里放东西。

本质：利用 CSS 摆盒子。

### 1.2 盒子模型（Box Model）组成

CSS 盒子模型本质上是一个盒子，封装周围的 HTML 元素，包括：边框、外边距、内边距和实际内容。

![box-model](https://s3.ax1x.com/2021/01/29/yilgJO.gif)

### 1.3 边框（border）

border 可以设置元素边框。边框有三个组成：`border-width`、`border-style`、`border-color`

语法

```css
/*属性可连写*/
border: border-width || border-style || border-color;
```

| 属性         | 作用                  |
| ------------ | --------------------- |
| border-width | 定义边框粗细，单位 px |
| border-style | 边框样式              |
| border-color | 边框颜色              |

**边框属性简写**

```css
/*习惯顺序*/
border: 5px solid pink;
```

**边框属性分写**

```css
/*注意层叠性*/
border-top: 1px solid red;
```

### 1.4 表格的细线边框

`border-collapse` 属性控制浏览器绘制表格边框的方式。它控制相邻单元格的边框。

语法

```css
border-collapse: collapse;
```

- collapse 是合并的意思
- `border-collapse:collapse;` 表示将相邻边框合并在一起

### 1.5 边框会影响盒子实际大小

边框会额外增加盒子的实际大小，因此有两种方案解决。

1. 测量盒子大小的时候，不测边框。
2. 若测量的时候包含了边框，则需要 width/height-边框宽度。

### 1.6 内边距 padding

`padding` 属性设置内边距，即边框与内容之间的距离。

- `padding-left`: 左内边距
- `padding-right`: 右内边距
- `padding-top`: 上内边距
- `padding-bottotm`: 下内边距

**padding 属性简写**

`padding` 的值的个数：

- 1 个值：上下左右
- 2 个值：上下，左右
- 3 个值：上，左右，下
- 4 个值：上，右，下，左，顺时针

**padding 会影响盒子实际大小**

当给盒子指定了 `padding` 值以后，发生了两件事情：

1. 内容和边框有了距离，增加内边距
2. padding 值影响了盒子实际大小

也就是说，当盒子已经有了宽度和高度，再指定内边距，会撑大盒子。

要保证盒子和效果图一样大，则让 `width/height`-多出来的内边距大小即可。

### 1.7 box-sizing 属性解决方案

CSS 中的 `box-sizing` 属性定义了 `user agent` 应该如何计算一个元素的总宽度和总高度。

在设置了一个盒子的 `width/height` 后，再设置其 `border/padding` 会影响盒子实际大小。当进行响应式布局时，这个尤其烦人。

box-sizing 属性可以被用来调整这些表现。

- `content-box` 是默认值。如果你设置一个元素的宽为`100px`，那么这个元素的内容区会有 `100px` 宽，并且任何边框和内边距的宽度都会被增加到最后绘制出来的元素宽度中。
  ```css
  box-sizing: content-box;
  ```
- `border-box` 告诉浏览器：你想要设置的边框和内边距的值是包含在 `width` 内的。也就是说，如果你将一个元素的 `width` 设为 `100px`，那么这 100px 会包含它的 `border` 和 `padding`，内容区的实际宽度是 `width` 减去 `(border + padding)` 的值。大多数情况下，这使得我们更容易地设定一个元素的宽高。
  ```css
  box-sizing: border-box;
  ```
  尺寸计算公式：
  `width = border + padding + 内容的宽度`
  `height = border + padding + 内容的高度`

若盒子没有指定 `width/height` 属性，则此时 `padding` 不会撑开盒子大小。
