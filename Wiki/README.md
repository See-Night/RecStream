# 简介

BiliRec是一项基于Python的Bilibili自动录播器开源项目。

## 主要特性

BiliRec支持本地部署，并且兼容Windows和Linux系统，可部署在RespberryPi等ARM平台的操作系统上。

## 注意事项

- 本项目为开源项目，允许随意下载使用
- 在使用前请仔细阅读使用说明
- 如果您有更好的灵感欢迎您随时贡献代码
- 如果您在使用过程中遇到无法解决的问题，请在本仓库下直接提交Issue

- 本项目为开源项目，禁止任何人或团体使用该项目以任何形式进行盈利活动

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.css">

<script src="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.min.js"></script>

<div id="gitalk-container"></div>

<script>
    const gitalk = new Gitalk({
        clientID: "a9f7d3f091928b45e225",
        clientSecret: "af98a2e872ffd57b4443842cd200d5acf50d7f7d",
        repo: "BiliRec",
        owner: "Dreammer12138",
        admin: ['Dreammer12138'],
        id: location.pathname
    });
    gitalk.render('gitalk-container');
</script>