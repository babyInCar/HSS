HSS(House Storage System)

基于Python3.11和Fastapi0.11.0实现

## 主要功能：
<hr/>
1.实现家庭商品的分类
2.实现家庭空间的管理
3.实现家里物品的添加以及分类，查找等功能
4.实现家里物品的借阅维护
5.实现家庭物品的维修状态管理

## 安装
<hr/>
mysql客户端使用了pymysql，具体请参考 pypi 查看安装前的准备。

使用pip安装所需Python库： pip install -Ur requirements.txt

如果你没有pip，使用如下方式安装：

OS X / Linux 电脑，终端下执行:

curl http://peak.telecommunity.com/dist/ez_setup.py | python
curl https://bootstrap.pypa.io/get-pip.py | python

Windows电脑
下载 http://peak.telecommunity.com/dist/ez_setup.py 和 https://raw.github.com/pypa/pip/master/contrib/get-pip.py 这两个文件，双击运行。

## 运行
<hr/>
修改settigs.py中的数据库配置信息，如下所示
"connections": {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': '127.0.0.1',
                'port': '3306',
                'user': 'root',
                'password': 'Test1234',
                'database': 'fastapi',
                'minsize': 1,
                'maxsize': 5,
                'charset': 'utf8mb4',
                'echo': True
            }
        }
        }

 ## 创建数据库
 Mysql中执行
 CREATA database `fastapi` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;

然后终端下执行(在执行之前确保已经安装了aerich)：
aerich init -t settings.TORTOISE_ORM
aerich init-db

## 开始运行
执行 uvicorn main:app --reload
在浏览器中输入:http://127.0.0.1:8081/docs 即可看到效果。

## Q&A
有任何问题欢迎提Issue,或者将问题描述发送至我邮箱 gaoshuang916@gmail.com.我会尽快解答.推荐提交Issue方式.

<hr/>


 
