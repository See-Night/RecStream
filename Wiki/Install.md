# 安装

## Windows

```powershell
PS > git clone https://github.com/Dreammer12138/BiliRec.git
PS > cd BiliRec
PS > pip install -r requirements.txt
PS > python manage.py migrate
```

## Linux

```shell
$ git clone https://github.com/Dreammer12138/BiliRec.git
$ cd BiliRec
$ sudo pip3 install -r requirements.txt
$ sudo python3 manage.py migrate
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