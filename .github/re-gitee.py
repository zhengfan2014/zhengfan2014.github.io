#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Gridea Github.io -> Gitee.io Url替换
# 作者: zhengfan2014
GithubUrl = 'https://zhengfan2014.github.io'
GiteeUrl = 'https://zhengfan2014.gitee.io'

num = 0
import os
for root, dirs, files in os.walk('/workdir/gitee-blog', topdown=False):
    for name in files:

        #遍历所有的html和rss(xml)文件并开始改Url
        if name[-5:] == '.html' or name[-4:] == '.xml':
            #读取
            with open(os.path.join(root, name)) as f:
                html = f.read()
                html = html.replace(GithubUrl,GiteeUrl)
                f.close()
            #写入
            with open(os.path.join(root, name),'w') as f:
                f.write(html)
                f.close()
            num += 1

print("[Url]替换完成: 共完成 " + str(num) + "处替换")