# BiliRec

## Bilibili自动录播站

> **需要python3+ffmpeg的支持**

> 录播脚本来源于之前写的一个[项目](https://github.com/dreammer12138/DDMonitor)

**详细说明书请访问[Wiki](https://1145141919810.wang/BiliRec)**

### 简介

BiliRec是一个基于Python的Bilibili自动录播器。

支持本地部署，兼容Windows和Linux系统，可在树莓派、香橙派等arm平台运行。

### 安装

#### Linux

```shell
# 安装python依赖
$ sudo pip3 install -r requirements.txt

$ sudo python3 manage.py migrate
```

#### Windows

```powershell
PS> pip install -r requirements.txt
PS> python manage.py migrate
```

### 运行

#### Linux

```shell
$ sudo python3 start.py -r <room_id> -o <out_path> -p <port> -u <uid>
```

#### Windows

```powershell
PS> python start.py -r <room_id> -o <out_path> -p <port> -u <uid>
```

#### 参数

`-r/--room` 房间ID

`-o/--outpath` 保存路径

`-p/--port` Web端口

`-u/--uid` 主播UID