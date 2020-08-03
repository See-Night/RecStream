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
$ sudo python3 manage.py runserver 0.0.0.0:<port> --insecure
```

#### Windows

```powershell
PS> python manage.py runserver 0.0.0.0:<port> --insecure
```

#### 参数

`--port` Web端口