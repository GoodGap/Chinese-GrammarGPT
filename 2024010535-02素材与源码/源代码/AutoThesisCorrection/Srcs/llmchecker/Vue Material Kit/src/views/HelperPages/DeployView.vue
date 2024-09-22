<script setup lang="ts">
import { onMounted } from "vue";

// Sections components
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";

// nav-pills
import setNavPills from "@/assets/js/nav-pills";

import hljs from 'highlight.js';
import 'highlight.js/styles/github-dark-dimmed.css';
import HighlightJs from "./HighlightJs.vue";

const code1 = `curl -sSLO https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.34-linux-glibc2.17-x86_64.tar.gz`;
const code2 = `mysql -u root -p -S /home/grammar/mysql/mysql.sock # 因为没有权限访问系统级目录，所以要为.sock文件指定在用户目录下`;
const code3 = `CREATE USER root@'%' IDENTIFIED BY '123456'; -- % 是通配符
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456';	-- 允许其他主机访问
flush privileges;`;
const code4 = `sudo yum install gcc # 安装 gcc 编译器
make CC=gcc`;
const code5 = `vim ~/.bashrc`;
const code6 = `export PATH="/path/to/redis/src:$PATH"`;
const code7 = `CONFIG set requirepass flask`;
const code8 = `AUTH flask`;
const code9 = `pip install -r requirements.txt`;
const code10 = `npm install
npm run build`;
const code11 = `npm install cnpm -g --registry=https://registry.npmmirror.com
cnpm install
npm run build`;
const code12 = `/path/to/Flask API Demo/config/setting.py
/path/to/Vue Material Kit/src/server/config.ts`;

const code13 = `# 启动mysql
/home/grammar/mysql/bin/mysqld_safe --defaults-file=/home/grammar/mysql/my.cnf --user=grammar &
# 登录mysql
# mysql -u root -p -S /home/grammar/mysql/mysql.sock

# 启动redis
/home/grammar/redis/src/redis-server &
# 登录并配置密码
/home/grammar/redis/src/redis-cli
CONFIG set requirepass <password>`;
const code14 = `cd /path/to/Flask API Demo
python app.py`;
const code15 = `cd /path/to/Vue Material Kit
python app.py`;

onMounted(() => {
  setNavPills();
});
</script>
<template>
  <BaseLayout title="部署流程" :breadcrumb="[{ label: '帮助文档', route: '#' }, { label: '部署流程' }]">
    <h5 id="克隆项目">克隆项目</h5>
    <h5 id="安装mysql">安装MySQL</h5>
    <p><a href="https://www.cnblogs.com/chenkx6/p/13366638.html">参考</a></p>
    <p>首先下载 MySQL Linux通用版本<a href="https://dev.mysql.com/downloads/mysql/">链接</a>。</p>
    <HighlightJs :code="code1" language="bash" />
    <p>然后配置环境变量。配置好后使用下面的命令连接MySQL</p>
    <HighlightJs :code="code2" language="bash" />
    <p>然后为了允许远程连接，首先要为远程ip创建用户，然后再给予权限。</p>
    <HighlightJs :code="code3" language="sql" />
    <h5 id="安装redis">安装redis</h5>
    <p><a href="https://redis.io/docs/getting-started/installation/install-redis-from-source/">Install Redis from
        Source
        | Redis</a></p>
    <p>中途遇到了找不到命令 <code>CC</code>。原因是没有 C 语言编译器。需要下载编译器并配置环境变量或是给 <code>make</code> 添加参数</p>
    <HighlightJs :code="code4" language="bash" />
    <p>之后使用 <code>make install</code> 安装。如果没有权限可以选择手动添加环境变量的方式。</p>
    <HighlightJs :code="code5" language="bash" />
    <p>添加下边这行，根据具体路径更改</p>
    <HighlightJs :code="code6" language="bash" />
    <p>服务程序启动后使用<code>redis-cli</code>连接redis，并输入下面的命令配置密码验证。</p>
    <HighlightJs :code="code7" language="bash" />
    <p>之后连接需要输入密码验证，用下面的方法</p>
    <HighlightJs :code="code8" language="bash" />
    <h5 id="配置python环境">配置python环境</h5>
    <p>下载miniconda并添加环境变量，之后安装python3.8版本。</p>
    <p>切换到项目目录下的 <code>Flask API Demo</code> 目录。</p>
    <HighlightJs :code="code9" language="bash" />
    <h5 id="配置node环境">配置node环境</h5>
    <p>安装 <a href="https://github.com/nvm-sh/nvm">nvm</a></p>
    <p>安装 node16.20.1</p>
    <p>在 <code>Vue Material Kit</code> 目录下</p>
    <HighlightJs :code="code10" language="bash" />
    <p>如果出现问题就使用中国镜像的cnpm</p>
    <HighlightJs :code="code11" language="bash" />
    <h5 id="修改配置文件">修改配置文件</h5>
    <p>根据实际情况修改下面文件中的配置</p>
    <HighlightJs :code="code12" language="bash" />
    <h5 id="启动项目">启动项目</h5>
    <p>启动数据库</p>
    <HighlightJs :code="code13" language="bash" />
    <p>启动后端</p>
    <HighlightJs :code="code14" language="bash" />
    <p>启动前端</p>
    <HighlightJs :code="code15" language="bash" />
  </BaseLayout>
</template>

<style scoped lang="scss">
p {
  color: black;
  font-weight: normal;
}

ol {
  color: black;
  font-weight: bold;
}

a {
  color: #00bcd4;

  &:hover {
    text-decoration: underline;
  }
}
</style>
