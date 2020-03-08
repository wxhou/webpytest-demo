## 前言

> 通篇使用的python版本是3.7.3

上一篇介绍了简单的搭建环境，示例代码以及整体的框架目录。

本篇作为一个进阶篇，我将分解这些框架的具体模块，逐一讲解。

## 元素定位

 在日常的工作中，我见过很多在浏览器中直接在浏览器中右键`Copy Xpath`复制元素的同学。这样获得的元素表达式放在 webdriver 中去运行往往是不够稳定的，像前端的一些微小改动，都会引起元素无法定位的<font color=#FF0000 >`NoSuchElementException`</font>报错。

 所以在实际工作和学习中我们应该加强自己的元素定位能力，尽可能的采用`xpath`和`CSS selector` 这种相对稳定的定位语法。由于`CSS selector`的语法生硬难懂，对新手很不友好，而且相比`xpath`缺少一些定位语法。所以我们选择`xpath`进行我们进阶篇的元素定位语法。

#### xpath

##### 语法规则

>  [菜鸟教程](https://www.runoob.com/xpath/xpath-intro.html)中对于 xpath 的介绍是一门在 XML 文档中查找信息的语言。

表达式|介绍|备注    
----|----|----
/|根节点|<font color=#FF0000 >绝对路径</font>
//|当前节点的所有子节点|<font color=#FF0000 >相对路径</font>
*|所有节点元素的|
@|属性名的前缀| <font color=#FF0000 >@class   @id</font>      
*[1]|[]  下标运算符|
[]|[ ]谓词表达式|<font color=#FF0000 >//input[@id='kw']</font>
Following-sibling|当前节点之后的同级|
preceding-sibling|当前节点之前的同级|
parent|当前节点的父级节点|

##### 定位工具

* chropath
  * 优点：这是一个Chrome浏览器的测试定位插件，类似于firepath，本人试用了一下整体感觉非常好。对小白的友好度很好。
  * 缺点：安装这个插件需要<font color=#FF0000 >科学上网</font>。
* 自己写——本人推荐这种
  * 优点：本人推荐的方式，因为当熟练到一定程度的时候，写出来的会更直观简洁，并且在运行自动化测试中出现问题时，能快速定位。
  * 缺点：需要一定`xpath`和`CSS selector`语法积累，不太容易上手。

## 设置文件

> 项目中都应该有一个文件对整体的目录进行管理，我也在这个python项目中设置了此文件。

在项目根目录创建`settings.py`文件，所有的目录相关的文件在这个里面。

```python
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File : settings.py
@Time : 2020-01-16 10:32:56
@Author : wxhou 
@Version : 1.0
@Contact : 1084502012@qq.com
'''
import sys
sys.path.append('.')
import os

# 项目目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 配置文件
CONFIG_PATH = os.path.join(BASE_DIR, 'config.ini')

# 页面元素目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'PageElements')

# SQLite数据库
SQLITE_PATH = os.path.join(BASE_DIR, 'TestData', 'sqlite3.sqlite')

# 截图目录
SCREENSHOT_PATH = os.path.join(BASE_DIR, 'screenshot')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')


if __name__ == '__main__':
    print(BASE_DIR)
```

在这个文件中我模仿了Django风格的settings.py文件。

在这个文件中我们可以设置自己的各个目录，也可以查看自己当前的目录。

遵循了约定：不变的常量名全部大写，变量名称小写的规范。看起来整体美观。

## 配置文件

> 所谓的配置文件就将固定不变的信息集中在一个文件中

在项目根目录新建一个`config.ini`文件，里面暂时先放入我们的需要测试的URL

```ini
[HOST]
HOST = https://www.baidu.com
```

配置文件创建好了，接下来我们需要读取这个配置文件以使用里面的信息。

我们在`common`目录中新建一个`readconfig.py`文件

```python
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File : readconfig.py
@Time : 2020-01-16 13:47:47
@Author : wxhou 
@Version : 1.0
@Contact : 1084502012@qq.com
'''
import sys
sys.path.append('.')
import os
import settings
import configparser

HOST = 'HOST'


class Config:
    """配置文件"""
    def __init__(self):
        self.config_path = settings.CONFIG_PATH
        if not os.path.exists(self.config_path):
            raise FileNotFoundError("配置文件%s不存在！" % self.config_path)
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(self.config_path, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(self.config_path, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)

    @url.setter
    def url(self, value):
        self._set(HOST, HOST, value)


conf = Config()

if __name__ == '__main__':
    print(conf.url)
```

可以看到我们用python内置的configparser模块对config.ini文件进行了读写。

对于url值的提取，我使用了高阶语法@property属性值，读取和重新赋值更简单。

### POM模型

> 由于下面要讲元素相关的，所以首先理解一下POM模型

