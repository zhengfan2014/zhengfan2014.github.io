<div style="text-align:center">
<img src="https://zhengfan2014.gitee.io/lotterysimulator/img/error.png">
<h1>Gridea action 推送助手</h1>
<p>一键修改Gridea站点Url&启用JsDelivr CDN&同步到Gitee</p>
</div>

![通过](https://img.shields.io/github/workflow/status/zhengfan2014/zhengfan2014.github.io/%E6%8E%A8%E9%80%81%E5%88%B0Gitee&Github%E5%90%AF%E7%94%A8Cdn?label=GithubAction%E8%BF%90%E8%A1%8C)
[![酷安粉丝][coolapk]](http://www.coolapk.com/u/2864549) [![b站粉丝][bilibili]](https://space.bilibili.com/25818910)
[![爱发电本月收入][mon]](https://afdian.net/@zhengfan2014)
[![爱发电发电人数][once]](https://afdian.net/@zhengfan2014)

## 功能
 - 基于Github Action
 - 自动白嫖JsDelivr CDN(仅限Github Page)
 - 自动同步到Gitee并拉动Page

## 演示
github action 执行
![屏幕截图 2021-02-24 163048.jpg](https://i.loli.net/2021/02/24/DIcqvMP8NUghd4E.jpg)
github 仓库效果
![屏幕截图 2021-02-24 163118.jpg](https://i.loli.net/2021/02/24/gInmQNe54UlfFcY.jpg)
gitee 仓库效果
![屏幕截图 2021-02-24 163138.jpg](https://i.loli.net/2021/02/24/WyuROm7CpIbBDfE.jpg)
## 安装

1. 复制本仓库`.github`整个文件夹到你Gridea的`static`文件夹里面，并确保`static`文件夹里面有一个`.nojekyll` 的空文件

2. 修改文件夹里`bulid.yml`里的env
```yml
  ################## github 设置 ###################################################
  # 注意替换为你的 Github 用户名
  GITHUB_USERNAME: zhengfan2014
  # 注意替换为你的 Github 仓库
  GITHUB_REPO: zhengfan2014.github.io
  # 注意替换为你的 Github 仓库的分支(也就是Gridea设置的分支)
  GITHUB_BRANCH: master
  # 注意替换为你的 Github 仓库Url
  GITHUB_URL: https://github.com/zhengfan2014/zhengfan2014.github.io
  ################## gitee 设置 ####################################################
  # 注意替换为你的 Gitee 用户名
  GITEE_USERNAME: zhengfan2014
  # 注意替换为你的 Gitee 绑定的邮箱
  GITEE_USER_EMAIL: zhengfan2014@outlook.com
  # 注意替换为你的 Gitee 仓库，仓库名严格区分大小写，请准确填写，否则会出错
  GITEE_REPO: zhengfan2014
  # 要部署的分支，默认是 master，若是其他分支，则需要指定（指定的分支必须存在）
  GITEE_BRANCH: master
  # 注意在 Settings->Secrets 配置 GITEE_PASSWORD
```
3. 增加机密
 - `GITEE_PASSWORD` : 你gitee账号的密码(用来自动刷新gitee page)
 - `GITEE_PRIVATE_KEY` : 你gitee仓库的私钥，用来免验证推送到gitee
 - `KNOWN_HOSTS` ： 第一次登录ssh后生成的，用来信任gitee的服务器

4. 开始享受  
![](https://zhengfan2014.gitee.io/lotterysimulator/img/error.png)
## FAQ
Q: action 跑到 Gitee 推送处卡住很久很久  
A: 美丽坚push到国内时网络卡了。无解，建议 ~~我们重新开始战斗(推送) 吧~~  

Q: Gridea预览成功，推送到Github成功，但是Github网页没有收到推送  
A: Gridea打开开发者模式 - console，点击推送到github，观察报错信息。如果出现了  

```python
refs/heads/master refusing to allow a Personal Access Token to create or update workflow '.github/workflows/bulid.yml' without 'workflow' scope
```  
错误，则是你的Gridea没有推送权限，请到 [https://github.com/settings/tokens](https://github.com/settings/tokens) 处更新你的token权限，增加workflow权限

## 恰饭
 - [爱发电](https://afdian.net/@zhengfan2014)

![fe198bb1523528c2b852d28626379a2a.png](https://i.loli.net/2021/02/24/krVdGptwEQ6C28g.png)

[coolapk]:https://img.shields.io/badge/dynamic/json?labelColor=11ab60&color=282c34&label=%E9%85%B7%E5%AE%89%20紫碧君&suffix=%20粉丝&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dcoolapk%26queryKey%3D2864549&logo=data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik0xMjcuODkzIDQyNi42NjdjMjkuOTItNjYuOTg3IDk0LjUwNy0xMTYuNjk0IDE2Ni40LTEzMC4zNDcgNTUuNzg3LTkuNiAxMTIuOTYgNS4wNjcgMTYxLjkyIDMxLjk0N0M0OTcuNzYgMzQ5LjQ0IDUzNC40IDM3OC44OCA1NjcuOTQ3IDQxMS4wNGMtMTYuMTYgMTguNC0zOS4wOTQgMjguODUzLTU3LjQ5NCA0NC43NDctNDYuMTMzLTM4Ljg4LTk2LjY0LTc3LjcwNy0xNTcuOTczLTg3LjA5NC03OC45MzMtMTMuMTczLTE1OC41NiA0OS4yMjctMTcwLjUwNyAxMjcuMTQ3LTguNjkzIDQ1LjkyIDEwLjEzNCA5NC42NjcgNDUuMTc0IDEyNC45MDcgMzkuNjggMzQuOTg2IDk3LjIyNiA0NC41ODYgMTQ3LjYyNiAzMS4yNTMgNTcuNi0xMy45MiAxMDEuOTc0LTU3LjA2NyAxMzYuODU0LTEwMi43NzMgNTQuMDgtNzIuMTA3IDk5LjItMTUwLjQgMTQ3Ljg0LTIyNi4xMzQgMTMuOTItMTkuMTQ2IDQ3LjQxMy0xNy4yMjYgNTguNzIgMy44NCA2My42MjYgMTA5LjAxNCAxMjYuMDggMjE4LjcyIDE4OS42IDMyNy43ODcgNy41NzMgMTUuMDkzIDQuNDI2IDM1Ljc4Ny05LjYgNDYuMTMzLTEzLjA2NyAxMC42MTQtMzMuMzM0IDEwLjI0LTQ2LjEzNC0uNjkzYTk3MDY2LjU1OCA5NzA2Ni41NTggMCAwMS0yMjYuMTg2LTE2Mi43MmMxOC44OC0xNS4wNCAzOC40LTI5LjMzMyA1Ny45NzMtNDMuNDY3IDIzLjczMyAxMi45MDcgNDMuNzg3IDMzLjE3NCA2OS42IDQxLjY1NC0yMC4zNzMtMzkuNTc0LTQzLjYyNy03Ny43MDctNjYuMzQ3LTExNS45NDctNDIuNjY2IDU5LjE0Ny03Ny4wNjYgMTI0LjIxMy0xMjMuMTQ2IDE4MS4wNjdDNTE2IDY2My40NjcgNDQ4LjggNzE2Ljk2IDM2OC42NCA3MjguNDhjLTM4Ljg4IDMuNDEzLTc5LjMwNyA0LjIxMy0xMTYuMzczLTkuOTczLTUzLjQ5NC0xOS4xNDctMTAwLjMyLTU4LjcyLTEyNC41ODctMTEwLjU2LTI4LjIxMy01Ni4xMDctMjYuNzczLTEyNS4wMTQuMjEzLTE4MS4yOHoiIGZpbGw9IiNmZmYiLz48L3N2Zz4=&longCache=true

[bilibili]:https://img.shields.io/badge/dynamic/json?labelColor=FE7398&label=bilibili%20紫碧君&suffix=%20粉丝&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dbilibili%26queryKey%3D25818910&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAD7ElEQVR4nO2dW9WrMBCFK6ESkFAJSKiESqgEHCABCZWAhEpAAhL2ecik5dDc/pXLBDLfWnlqy0xmJ5BMQnq5CIIgCIIgCIIgCIIgCEIBAHQAemYfrgCunD6wAKAHsEKxALgx+bCQD8/S9tmgVqeDr1lLigDgZvDhXso+K9TyTBQRwRJ8AHjntl0Flh5QRAQK/mKxPeayWx2OXpBNBKiHvi34b7T2MC4pAvW6twR/RwkRKPizBN8CgEcuESj4Lwm+BwBjahEk+H8EwJRKhOaCDzW8e1JLfkUUH1NgmR3XmHffHR1l+72BSs8d7w8U+JDAnZERQMcV+CtUi7dNqFqibB4J7vtrq7xKCuAasbTMXCL4T+5aVk6+2xHUrWdhruAR6HIJcOeu2UHI8zyAe2ytWfEdWz9PVvQ8YAmIQ5dDAB9LFsMVAv8oMO2zAGrC5WNIarRiAuKR9jYEd9pY08aa6uUzIHGRdkgKd8pY0yc1WjEBAqypDYoAG0QAZkQAZkQAZkQAZk4vANQenjsSzS3I/wcSbXU5jQBUkRtdf4Rar90v8kSv3+I3ffCCSpk8I/w+lgDkdI/v2rEp2CaiWm1AsDQLlDAD+dlFXLMeAaCSeLZdaSFE5VUQNot38cKuEeBgAsSuG0flVZBmEanbXfNQAsS0fgBYIn2fIu3/BBMHEyBmDXlFfA8IzeHb+Ems4WAChKykrVA9ZfsQTL57jXzRg4A5wC/A8N4ADiZAZwm2XjW75Qh2KOTfA0p4kygPw28OJcCVgn3nDnYo2EwEYRgGH0qAMyICMCMCMCMCMCMCMCMCMCMCfP3qwHDOQ4AAUekTk8FaBRihJnZdYbvtCGC7LvmkM63GjVDINPFrQgCq5ETXfmMzI90FXzPvfqt7x4rEu/ZaEcCUxFvgz2zO+BUn6UkoaEEAsptiMSX5e8FoRYCN7cVgb4Vq7U/H50Pq4JNP7Qiw8UFnJwcK+tXy+Wj6PLEvPgHSHv5UgwA1IQIwwyFAyLJin9RoxYgAzAQIkPwNmf26busC+OIx5TDqo5nDT+F/SS/9CYzwb+No49zNy2evkYv0LywGGAXUvp6eSneycqOic0w20k7CNgKE7jJunSGLACTCxF27ylmQc98T5MQUH49swd+I0HPXslLKnT0N+wnkrTKi9JZL/L9i1SorMmdeQ4TQQ7OFMxIMzGD45w8nUL1im7efENZLJpgPSw0pfz0cdt4U3230Td/Tvx2R6d2FrHhEWLkq5PELOMsRPHCPnAZGv1xJteL7jbJiaW3sB2nDvPC/osSYvjRQz4cJ6n7KO3rYQL7M+L6nVtfDVRAEQRAEQRAEQRAEIZ5/SAXmdfXaoQsAAAAASUVORK5CYII=&color=282c34&longCache=true

[mon]:https://img.shields.io/badge/dynamic/json?label=本月收入&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3DafdianIncome%26queryKey%3Dzhengfan2014&prefix=%EF%BF%A5%20&suffix=%20%E6%AF%8F%E6%9C%88&labelColor=946ce6&color=282c34&longCache=true

[once]:https://img.shields.io/badge/dynamic/json?label=%E7%88%B1%E5%8F%91%E7%94%B5&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3DafdianFans%26queryKey%3Dzhengfan2014&suffix=%20%E5%8F%91%E7%94%B5%E4%BA%BA%E6%AC%A1%20%2F%20%E6%9C%88&labelColor=946ce6&color=282c34&longCache=true