# 依赖

BiliRec依赖于以下内容/项目：

- Python 3 及以上（3.5 / 3.6 / 3.7 / 3.8）
- Streamlink
- FFMPEG

**请在安装BiliRec前保证已经安装以上内容**

## 安装Python3

### Windows

访问[Python官网](https://python.org)自行下载安装包进行安装

### Linux

<small>以Ubuntu为例</small>

```shell
$ sudo apt update
$ sudo apt install python3 python3-pip
```

## 安装Streamlink

### Windows

```powershell
PS > pip install streamlink
```

### Linux

```shell
$ sudo pip3 install streamlink
```

## 安装FFMPEG

### Windows

从[FFMPEG官网](https://ffmpeg.org/download.html)下载FFMPEG

![FFMPEG](./images/FFMPEG.png)

解压压缩包

配置环境变量

![FFMPEG](./images/FFMPEG_PATH.png)

### Linux

```shell
$ sudo apt install ffmpeg
$ sudo ln -s /usr/local/ffmpeg2/ffprobe /usr/local/bin/ffprobe
$ sudo ln -s /usr/local/ffmpeg2/ffmpeg /usr/local/bin/ffmpeg
```

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