#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Github Page 图片CDN加速
# 作者: zhengfan2014

Url = 'https://zhengfan2014.github.io'
User = 'zhengfan2014'
Repo = 'zhengfan2014.github.io'
CdnDir = ['/post-images/','/styles/','/images/','/favicon.ico']

import os
num = 0
for root, dirs, files in os.walk('/workdir/github-blog', topdown=False):
    for name in files:

        #遍历所有的html文件并开始改Url
        if name[-5:] == '.html':
            #读取
            with open(os.path.join(root, name)) as f:
                html = f.read()
                for i in range(len(CdnDir)):
                    html = html.replace(Url + CdnDir[i],'https://cdn.jsdelivr.net/gh/' + User + '/' + Repo + CdnDir[i])
                f.close()
            #写入
            with open(os.path.join(root, name),'w') as f:
                f.write(html)
                f.close()
            num += 1
print("[Cdn]替换完成: 共完成 " + str(num) + "处替换")