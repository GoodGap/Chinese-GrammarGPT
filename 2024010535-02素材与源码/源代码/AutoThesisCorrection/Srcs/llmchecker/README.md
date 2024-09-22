# Web Cheker Demo

#### 项目分为七个文件夹：

```Flask_template_FeiYing```、```Quill Editor```、```Tiptap Editor v0.0```、```Tiptap Editor v1.0```、```Simple Demo```、```Simple Flask Backend```、```README_IMGs```

#### 文件夹介绍

1. ```Quill Editor```

   可以查看网页：[BeyondGrammar 插件](https://prowritingaid.com/en/App/BeyondGrammar)

   ProWritingAid官方开源插件，集成到了Quill富文本编辑器，支持对于英文等语言的拼写纠错、语法纠错、风格转换，唯独不支持中文。UI同网站版本，修改官方API为本地Pycorrector后端API即可得到中文纠错版本。

   目前因为后端功能不完善（无法提示错误类型【语法、拼写】、没有错误提示等），部分API返回值固定为了默认值。修改API后前端对于中文的纠错使用体验和官方版本一致，但是因为核心js文件是打包后的js文件（猜测源文件是ts代码，使用Webpack等工具打包之后可读性下降，且代码量超20000行），无法进行定制化修改，需要阅读或重构js代码。该核心js文件是文件夹中的``CORE_Feature_bundle.js``，该文件经过IDE重新格式化后得到较为可读的```CORE_Feature.js```，再经过[boompack](https://gitee.com/vvjiang/boompack)整理后得到更为可读的js文件```CORE_Feature_more_readable.js```(但仍然无法恢复源文件)，可供之后进一步分析。

2. ```Tiptap Editor v0.0```

   该项目是代码完全开源的Tiptap富文本编辑器插件，Tiptap是一个兼容性十分友好的无头富文本编辑器，至今仍在维护，而quiil已经停止维护。原项目接口使用 languagetool 的纠错API，经过修改后使得前端可以使用本地Pycorrector后端API，得到中文纠错版本。

   这个项目实现了标注错误、修正错误以及忽略错误等核心功能（代码1000行左右）且都能追溯到相应实现。但是这只是一个极其雏形的版本——界面不美观，而且实际使用体验确实不如Quill Editor的插件。具体体现在：

   1）只能一次性返回所有文本***（纠正：代码会按 500 个字符一个文本块对文本进行分割）***，如果用户一次性输入大量文本需要等待大量时间

   2）不能本地缓存之前处理过的相同文本

   3）忽略功能有Bug（v1.0版本已修复）

   4）修正错误功能有很大延时，可能计算逻辑比较落后，导致计算量很大。实际查看HTML元素结构可以发现，这个项目在进行DOM元素替换的时候要明显慢于第一个项目，两个项目分别的实现原理以及效率差异的原因暂时未知。

   前端的标注以及纠错涉及到DOM编程，这个项目揭示了一定的核心原理，可供进一步研究。同时可以和第一个项目进行对比学习，研究第二个使用体验不如第一个的原因，对我们的实际开发会有很大启发。

3. ```Simple Demo```

   该项目是一个使用 ```Vue3 ```编写的简单的只有输入输出文本框的简单Demo

4. ```Simple Flask Backend```

   1、2、3三个前端项目的后端，包括四个py文件，使用```Flask```后端 + ```Pycorrector```实现，只有一个检查语法错误的接口，用来测试前端功能。

   py文件的后缀表明是哪个项目的后端，只要使用```Python```命令运行对应的文件即可。四个后端文件实现方式完全相同，只是在解析请求数据和生成返回数据以及控制台打印内容方面有差异。另外，如py文件后缀所示，```flask_pycorrector_quill_log.py```文件在控制台打印引入了```logoru```作为日志打印工具，```flask_pycorrector_quill_process.py```文件引入了```rich```的Process Bar来可视化后端运作。

   此后端最多可以同时执行两次API请求，大型项目可能需要考虑多线程、多进程、高并发编程。

5. ```README_IMGs```

   存储```README.md```中的图片

6. ```Flask_template_FeiYing```

   复现飞鹰校正系统的后端渲染功能（仍需完善，只实现部分功能）

7. ```Tiptap Editor v1.0```

   在```Tiptap Editor v0.0```的基础上，修复忽略功能，美化界面。

8. ```Flask API Demo```

   采用Flask框架编写的后端API，目前没有前端，只能采用API测试软件发送模拟请求来使用。目前已实现的功能包括：登录、注册、查询成员信息、修改成员信息、删除成员

   Todo：文件的上传以及下载API

   

#### 安装运行说明

1. ```Quill Editor```

   在该文件夹目录运行```cnpm install```安装项目依赖，需要注意的是```node-sass```极难安装，可能需要安装Windows编译工具，如果报错参考网上教程。

   运行```npm run start```启动项目

2. ```Tiptap Editor v0.0```

   在该文件夹目录运行```cnpm install```安装项目依赖，本项目也需要安装```node-sass```,可能报错。同时尤其重要的一点是```node-sass```对版本的兼容性很敏感，需要保持```node```、```node-sass```和```sass-loader```的版本互相兼容。可以检查```package.json```文件中上述依赖的版本与电脑安装的```node```版本是否兼容

   运行```npm run start``` 或 ```npm run serve```启动项目

3. ```Simple Demo```

   在该文件夹目录运行```npm install```即可安装依赖

   运行```npm run serve```启动项目

4. ```Simple Flask Backend```

   前三个项目需要分别开启对应的后端才可以运行（使用```python```命令运行）

   下述安装为python环境的安装配置：

   需要安装```pycorrector```，参考```pycorrector```官网的配置安装

   需要安装```flask```以及```flask_cors```

   需要安装```loguru```(```pycorrector```已安装好)以及```rich```

5. ```Flask_template_FeiYing```

   查看```/Flask_template_FeiYing```文件夹中具体说明

6. ```Tiptap Editor v1.0```

   运行前端部分：

   ​	需要安装```node```版本```v16.20.0```

   ​	需要安装```cnpm```

   ​	在该文件夹目录运行```cnpm install```安装项目依赖

   ​	运行```npm run start``` 或 ```npm run serve```启动项目

   运行后端部分：

   ​	查看第4条```Simple Flask Backend```的安装运行说明

7. ```Flask API Demo```

   运行```pip install -r requirements.txt``` 安装 python 依赖

   安装 ```Mysql```、```Redis``` 数据库，并修改 setting.py 的配置信息

   运行 app.py

   

#### ```Quill Editor```插件的特性 以及 通过阅读源码需要学习和解决的技术问题

1. Quill只是一个承载文本和方便编辑的富文本编辑器，实质只是一个文本容器，要想实现对错误的高亮或者标注，必须要改变该容器内的HTML元素（添加新的元素或者修改样式），涉及HTML DOM（文档对象模型）编程知识。其中一个技术难点是如何拆分原HTML元素（无错误的句子）并将其组合成新的HTML元素（需要区分有错误的和无错误的文本，为不同的HTML元素）。

2. 调用纠错接口的时候会分割文本，分批次调用纠错接口，分割的方式还没有弄清楚。这对于实际的生产部署是有意义的，可以减少一次性调用的成本，而且在用户端方面不会有太大延时（陆续纠错而不是一次性返回全部结果）。

3. 可以实现检测修改，无需按下纠错按钮，可以实现实时纠错。没有修改的时候是不会调用纠错接口的，出现修改只会提交更改的文本，而不是全部的文本，即纠错是局部的，而不是全局的。

4. 对于错误存在缓存功能，即重复的错误文本不会引发接口调用，这样可以节约接口资源。

5. 该插件定义并实现了一个HTML元素模板```<pwa></pwa>```，所有的错误文本都是使用该元素标签包起来的。它的工作原理是

   1. 检测到文本修改

   2. 调用纠错接口，上传修改的文本

   3. 纠错接口返回所有错误的信息，最主要的信息是错误的类型以及错误文本的开始位置以及结束位置

   4. 根据返回信息进行标注，标注的过程就是替换Quill文本容器HTML元素的过程。对错误文本使用```<pwa></pwa>```标签进行包裹

      例如：

      ![image-20221221154434488.png](http://123.60.168.132:8888/Susancutie/web-cheker-demo/-/raw/main/README_IMGs/image-20221221154434488.png)

   5. 例如原文本是```<p>鹏友你好</p>```，”鹏“字错误，应该为“朋“，那么它会将这段HTML代码替换为```<p><pwa>鹏</pwa>友你好</p>```

      被```<pwa></pwa>```标签括起来的文本即可以实现标注效果，按照错误类型不同会显示不同的颜色（由```<pwa></pwa>```标签的css样式决定。

   6. 鼠标悬浮在```<pwa></pwa>```元素上，即标注的错误文本上，可以出现对于该标注的错误提示以及修改按钮等，该方式的实现原理应该是会检测鼠标的行为，当停留在```<pwa>```元素上时，会显示原先隐藏的一个容器，该容器会根据```<pwa>```元素的id或者其他一些唯一标识符加载对应的错误信息（全部是该pwa标签的属性值），从而将该错误的提示信息显示在该容器内。

   7. 当点击替换按钮时，会将```<p><pwa>鹏</pwa>友你好</p>```变成```<p>朋友你好</p>```，从而实现更正。还有Ignore操作，该操作会使得该HTML代码变为```<p>鹏友你好</p>```，即保留错字消除标记，之后不会对鹏字做任何操作，Ignore实现的原理还没有搞清楚。

6. 现在最重要的是搞清楚```<pwa></pwa>```标签的具体实现，以及利用HTML DOM替换原文本容器内容的方式。进行文本标注本质上是对HTML元素进行修改，需要分割原HTML元素，生成新的HTML元素，新的HTML元素样式不同于原来的元素，从而实现标注，这个是主要原理。

7. 因为没有深入阅读```CORE_Feature.js```，目前只发现了这些特性，还有更多的技术细节需要学习。

#### ```Tiptap```插件源码阅读

1. 基本技术路线

   1）Tiptap提供了自定义插件的接口，因此可以利用Tiptap富文本编辑器作为用户文本输入框。

   2）主要使用```ProseMirror```富文本编辑器框架来进行DOM操作，ProseMirror 是一个基于 contentEditable 的行为良好的丰富语义内容编辑器，支持协作编辑和自定义文档模式。

   3）“忽略”功能使用了```Dexie.js```来构建云端数据库，存储选择不再进行纠错的文本，这些文本后续不再进行标注。

2. 技术细节

   1）对错误的标注使用了```ProseMirror```中的```Decoration```功能，可以将错误文本转换为```<span></span>```标签，并使用下划线进行标注。

   2）标注接口需要每个错误的from（开始）、to（结束）等信息，这些信息都是后端纠错接口返回的。

   3）对每个```<span></span>```标签进行了鼠标事件监听函数的绑定，检测到鼠标行为后，即鼠标指针移到某个错误上，会读取该```<span>```标签的属性值（错误类型、修正建议等内容是以属性值的形式保存在每个```<span>```标签内），并弹出一个文本框来展示这些内容。

   4）文本内容超过500个字符会进行分块，分别调用纠错接口。代码会记录每个块的起始位置偏移量，以进行块的定位。

   5）在多处加入了优化函数——防抖函数 debounce( )，防抖函数 debounce 指的是某个函数在某段时间内，无论触发了多少次回调，都只执行最后一次。

   6）会通过```changedNodeWithPos```检测node是否发生变化，其实就是用户是否进行了新的修改，如果检测到新的修改会重新调用纠错接口。

   7）“忽略”功能实现的原理是将忽略的错误文本利用```Dexie.js```存入云端数据库，然后进行标注的时候会查询数据库，如果有相同文本就不进行标注，如果没有查询到相同文本就正常标注。

3. 还没有理解的部分

   1）DOM操作需要涉及节点关系的判断，例如```descendants```为求一个节点的所有后代元素，关于这些涉及节点关系的部分还没有理解。

   2）代码涉及大量关于文本偏移量、节点位置的记录，用来定位具体的文本块、标注的位置，以及判断用户是否进行了文本修改，这部分的判断逻辑还需要进一步研究。

4. 需要进一步研究的地方

   1）调研富文本编辑器框架```ProseMirror```、```Slate```和```Lexical```，这些框架一般包装了DOM操作的接口。

   2）对比```Quill Editor```插件的实现原理，探究不同的实现方案以及效率的差异。

#### 系统部署流程

##### 克隆项目

##### 安装MySQL

[参考](https://www.cnblogs.com/chenkx6/p/13366638.html)

首先下载 MySQL Linux通用版本[链接](https://dev.mysql.com/downloads/mysql/)。

```shell
curl -sSLO https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.34-linux-glibc2.17-x86_64.tar.gz
```

然后配置环境变量。配置好后使用下面的命令连接MySQL

```sh
mysql -u root -p -S /home/grammar/mysql/mysql.sock # 因为没有权限访问系统级目录，所以要为.sock文件指定在用户目录下
```

然后为了允许远程连接，首先要为远程ip创建用户，然后再给予权限。

```mysql
CREATE USER root@'%' IDENTIFIED BY '123456'; -- % 是通配符
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456';	-- 允许其他主机访问
flush privileges;
```

##### 安装redis

[Install Redis from Source | Redis](https://redis.io/docs/getting-started/installation/install-redis-from-source/)

中途遇到了找不到命令 `CC`。原因是没有 C 语言编译器。需要下载编译器并配置环境变量或是给 `make` 添加参数

```sh
sudo yum install gcc # 安装 gcc 编译器
make CC=gcc
```

之后使用 `make install` 安装。如果没有权限可以选择手动添加环境变量的方式。

```sh
vim ~/.bashrc
```

添加下边这行，根据具体路径更改

```sh
export PATH="/path/to/redis/src:$PATH"
```

服务程序启动后使用`redis-cli`连接redis，并输入下面的命令配置密码验证。

```
CONFIG set requirepass flask
```

之后连接需要输入密码验证，用下面的方法

```
AUTH flask
```

##### 配置python环境

下载miniconda并添加环境变量，之后安装python3.8版本。

切换到项目目录下的 `Flask API Demo` 目录。

```sh
pip install -r requirements.txt
```

##### 配置node环境

安装 [nvm](https://github.com/nvm-sh/nvm)

安装 node16.20.1

在 `Vue Material Kit` 目录下

```sh
npm install
npm run build
```

如果出现问题就使用中国镜像的cnpm

```sh
npm install cnpm -g --registry=https://registry.npmmirror.com
cnpm install
npm run build
```

##### 修改配置文件

根据实际情况修改下面文件中的配置

```
/path/to/Flask API Demo/config/setting.py
```

```
/path/to/Vue Material Kit/src/server/config.ts
```

##### 启动项目

启动数据库

```sh
# 启动mysql
/home/grammar/mysql/bin/mysqld_safe --defaults-file=/home/grammar/mysql/my.cnf --user=grammar &
# 登录mysql
# mysql -u root -p -S /home/grammar/mysql/mysql.sock

# 启动redis
/home/grammar/redis/src/redis-server &
# 登录并配置密码
/home/grammar/redis/src/redis-cli
CONFIG set requirepass <password>
```

启动后端

```sh
cd /path/to/Flask API Demo
python app.py
```

启动前端

```sh
cd /path/to/Vue Material Kit
python app.py
```

