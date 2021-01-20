# 数据结构概述与常见算法

### 一、数据结构概述

1.1 数据与数据之间的逻辑关系

​	   集合、一对一、一对多、多对多

1.2 数据的存储结构

+ 线性表：顺序表（比如数组）、链表、栈、队列

+ 树形结构：二叉树

+ 图形结构

### 二、数组中的常见算法

1.1 总纲

+ 数组元素的赋值（杨辉三角、回形数等）

+ 求数值型数组中元素的最大值、最小值、平均数、总和等

+ 数组的复制、反转、查找（线性查找、二分法查找）

+ 数组元素的排序算法 

1.2   数组元素的赋值

① 杨辉三角

```java
// 1.第一行有一个元素，第n行有n个元素
// 2.每一行的第一个元素和第二个元素都是1
// 3.yanghui[i][j] = yanghui[i-1][j-1] + yanghui[i-1][j];
```

② 回形数

```java
/*	当输入为2：
  	1 2
   	3 4
    输入为3：
  	1 2 3
    8 9 4
		7 6 5 
    以此类推.. 
*/
```

1.3 数值型数组随机不重复赋值并求最大（小）值、和值

```java
/*
要求：
1.定义一个有10个元素的int型数组
2. 随机赋值，元素不重复且均为2位数
3. 求最大值、最小值、和值
*/
```

1.4 数组间的复制、反转、查找

**① 复制**

*关于赋值*

```java
arr2 = arr1;
```

数组间的赋值，<font color=red>实质上是栈空间中的两个数组指向了堆空间中的唯一一个数组实体，地址值相同</font>。

对于arr1和arr2的关系，可以理解为文件夹1和快捷方式链接文件夹2的关系。

因此数组的赋值不是数组的复制，两个数组只要有一个发生改变，另外一个也会发生改变。

*真正的复制*

```java
int[] arr4 = new int[arr3.length]l;
for (int i = 0; i < arr1.length; i++){
		arr4[i] = arr3[i];
}
```

各自的改变不会影响对方。

对于arr3和arr4的关系，可以理解为文件夹1和复制所得文件夹2的关系。

**② 反转**

方法一

```java
String[] letters = new String[] { "AA", "BB", "CC", "DD", "EE" };
for (int i = 0; i < letters.length / 2; i++) {
    String temp = letters[i];
    letters[i] = letters[letters.length - i - 1];
    letters[letters.length - i - 1] = temp;
}
```

方法二

```java
String[] letters = new String[] { "AA", "BB", "CC", "DD", "EE" };
for (int i = 0, j = arr.length - 1; i < j; i++, j--){
  	temp = arr[i];
  	arr[i] = arr[j];
  	arr[j] = temp;
}
```

**③ 查找**（只涉及线性和二分法）

+ 线性查找

  定义：按照顺序依次查找目标元素。

  方法：遍历数组，直至找到目标元素。

  缺点：查找效率低。

+ 二分法查找

  定义：折半查找，判断在哪一半，继续折半查找。

  前提：<font color=red>所要查找的数组必须要有序。</font>

  方法：定义首索引`head`，尾索引`end`，中间索引`middle`，折半查找。

  优点：效率比线性查找高。

  代码：

  ```java
  int headIndex = 0;
  int endIndex = arr.lenghth - 1;
boolean isNotFinded = true;
  while (headIndex <= endIndex) {
    	int middleIndex = (headIndex + endIndex) / 2;
    	if (arr[middleIndex] == dest) {
        	System.out.println("Successfully finded!");
  	      isNotFinded = false;
        	break;
      } else if (arr[middleIndex] < dest) {
        	headIndex = middleIndex + 1;
      } else {
        	endIndex = middleIndex - 1;
      }
  }
  if (isNotFinded) {
    	System.out.println("未找到！");
  }
  ```
  
