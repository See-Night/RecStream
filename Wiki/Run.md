# 运行

## Windows

```powershell
PS > python start.py -r <roomid> -u <uid> -p <port> -o <outpath>
```

## Linux

```shell
$ sudo python3 -r <roomid> -u <uid> -p <port> -o <outpath>
```

## 参数

`-r` / `--room` 房间号

`-u` / `--uid` 主播UID

`-p` / `--port` 端口

`-o` / `--outpath` 输出路径

## Web端监控

启动脚本以后打开浏览器，访问`http://localhost:<port>`



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