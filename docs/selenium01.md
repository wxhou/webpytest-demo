# selenium+pytest自动化测试框架—基础篇

## 前言

>  pytest框架结合selenium

* 使用python使用版本为python3.7.3

* 电脑操作系统为MacOS

**本章你需要**

- 一定的python基础

- 一定的selenium基础——不讲selenium，不会的自己去看[selenium中文翻译网](https://selenium-python-zh.readthedocs.io/)

## 浏览器驱动安装

> <font color=#FF0000 >注意：下载驱动时一定要注意浏览器版本和驱动版本匹配，否则会出问题</font>

- 火狐浏览器的驱动：https://github.com/mozilla/geckodriver/releases
- 谷歌浏览器的驱动：https://npm.taobao.org/mirrors/chromedriver
- IE浏览器的驱动：http://selenium-release.storage.googleapis.com/index.html
- Opera浏览器的驱动：https://github.com/operasoftware/operachromiumdriver/releases
- 根据浏览器版本下载完驱动后，放在环境变量目录。如`python的根目录`，或者你可以自定义

## selenium的安装

所有的软件对于学习的你而言都是从安装开始的。

不过我们这篇教程的安装不同于软件下载，而是安装python的selenium库。

#### 1.  新建python项目

​	新建一个python项目的目录`webpytest-demo`

#### 2. cd到该目录并执行创建虚拟环境的命令

```shell
cd webpytest-demo

python3 -m venv venv
```

> 这个创建虚拟环境的方法详见python官方文档

当我们的命令执行完成后，我们的文件夹中应该出现一个`venv`文件夹

#### 3. 进入这个虚拟环境中执行 

> window和MacOS进入方式不同

<font color=#FF0000 >注：此处是Mac的</font>

```shell
source venv/bin/activate
```

当终端中的前缀出现 `venv` 说明我们已经成功进入了python虚拟环境。

selenium项目和python虚拟环境已经设置成功了。

#### 4. 验证一下我们有没有在虚拟环境中

在命令行`shell`中输入：

```shell
pip list
```
![img](https://tva1.sinaimg.cn/large/006tNbRwly1gaxa8eewntj30g202jt8u.jpg)

 如图：`Package`只有两个基础包，是我们刚创建的的虚拟环境。

我们执行安装命令

```shell
pip install selenium
```

 出现如下提示代码安装成功：

<font color=#008000 >Successfully installed selenium-3.141.0 urllib3-1.25.3</font>



#### 5. 简单验证安装结果

在项目目录中新建文件`demo.py`，输入以下代码。

```python
#!/usr/bin/env python3
# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(3)
driver.quit()
```

点击查看运行详情：[视频详情](https://www.bilibili.com/video/av67177248/)

这样一个简单的`selenium+python`环境就搭建好了。



## 测试框架简介

- **测试框架有什么优点呢：**

   - 代码复用率高，如果不使用框架的话，代码会很冗余	
   - 可以组装日志、报告、邮件等一些高级功能
   - 提高元素等数据的可维护性，元素发生变化时，只需要更新一下配置文件
   - 使用更灵活的PageObject设计模式

- **测试框架的整体目录**

   目录   | 说明                                                         
   ------ | ------------------------------------------------------------ 
   common | 这个包中存放的是常见的通用的类，比如读取配置文件的或者读取json的类 
   logs|日志
   Page |对selenium的方放进行深度的封装，如查找元素，click，sendkeys等等
   PageElments|页面元素存放目录
   PageObject|页面对象POM设计模式，本人对这个的理解来自于[苦叶子](https://www.cnblogs.com/lym51/p/6646033.html)的博客
   screenshot|测试的产生的截图保存到这个目录
   TestCase|所有的测试用例集
   TestData|测试数据文件等
   utils|第三方的如日志邮件等等
   config.ini|配置文件
   conftest.py|pytest测试框架的胶水文件
   README.md|自述文件
   report.html| 输出的报告文件
   pytest.ini|pytest配置文件

　　

　　**这样一个简单的框架结构就清晰了。** 

 <table><tr><td bgcolor=#FAEBD7	>喜欢python自动化测试或正在学习自动化测试的同学<br>欢迎加入我的QQ群:<font color=#FF0000 >299524235</font>(python自动化测试学习)</td></tr></table>
