# （一）数据库和SQL概述

## 1.1 数据库的好处

+ 实现数据持久化
+ 使用完整的管理系统统一管理，便于查询

## 1.2 数据库的概念

+ DB

  数据库（database），存储数据的仓库，保存了一系列 **有组织** 的数据。

+ DBMS

  数据库管理系统（Database Management System）。数据库是通过 DBMS 创建和操作的容器。

  常见的数据库管理系统：MySql、Oracle、DB2、SqlServer

+ SQL

  结构化查询语言（Structure Query Language），专门用来 **与数据库通信** 的语言。

  SQL的优点

  1. 是一门通用的语言，几乎所有DBMS都支持SQL。
  2. 简单易学。
  3. ==灵活使用，可进行非常复杂而又高级的数据库操作。==

## 1.3 数据库结构特点

1. 将数据放在表中，表再放到库中。

2. 一个数据库中可以有多个表，每个表有一个名字，用来标识自己。

   ==表名具有唯一性。==

3. 表具有一些特性，这些特性定义了数据在表中如何存储，类似 java 中 “类” 的设计。

4. 表由 **列** 组成，也称为 **字段**。所有表都是由一个或多个列组成的，每一列类似 java 中的 “对象”。

# （二）MySQL的安装与使用

## 2.1 MySQL 产品特点

> 属于 MySQLAB 公司，后被 oracle 公司收购。

优点：

+ 成本低：开源且免费使用
+ 性能高：执行快
+ 简单：易安装使用

## 2.2 DBMS分类

分为两类

+ 基于共享文件系统的DBMS（Access）
+ 基于客户机——服务器的DBMS（MySQL，Oracle、SqlServer）

## 2.3 MySQL版本

+ 社区版（免费）
+ 企业版（收费）

## 2.4 安装

1. 安装包
2. 免安装

## 2.5 MySQL的使用

### 1. MySQL服务的启动和停止

+ Windows10：<kbd>Ctrl+Shift+Esc</kbd> -> 查看服务->点击，启动和停止服务

+ 通过命令行CMD（**管理员权限**）

  ```
  # 启动
  net stop [mysql服务名]
  # 停止
  net start [mysql服务名]
  ```

### 2. MySQL 的服务的登录和退出

+ 方式一：通过 mysql 自带客户端，只限于 root 用户 

  （MySQL 5.5 Command Line Client）

+ 方式二：通过 windows 自带的客户端

  ```
  # 登录
  mysql [-h 主机名 -P 端口号] -u 用户名 -p密码
  # 退出
  exit 或 ctrl+C
  ```

  举例

  ```
  # 本地登录
  mysql -h localhost -p 3306 -U root -p
  # root用户快捷登录
  mysql -u root -p密码
  ```

### 3.MySQL的常用命令

```sql
# 1.查看当前所有的数据库
show databases;
# 2.打开指定的数据库
use 库名;
# 3.查看当前所在的库
select database();
# 4.查看当前库的所有表
show tables;
# 5.查看其他库的所有表
show tables from 库名;
# 6.查看表中的所有数据
select * from 表名;
# 7.创建表
create table 表名(
		列名 列类型,
  	列名 列类型,
  	...
);
# 8.查看表结构
desc 表名;
# 9.查看服务器版本
# 方式一: 登录到 mysql 服务端
select version();
# 方式二：未登录到 mysql 服务端
mysql --version
mysql -V
```

### 4. MySQL 语法规范

1. 不区分大小写，但是由规范，建议关键字大小写，表名、列名小写
2. 每条命令用分号 `;` 结尾
3. 每条命令根据需要，可以进行缩进或换行
4. 注释
   + 单行注释：`#注释文字`
   + 单行注释：`-- 注释文字`
   + 多行注释：`/* 注释文字 */`