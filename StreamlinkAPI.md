# API 参考

<small>这是Streamlink中所有可用的API方法的引用。</small>

## Streamlink

### `streamlink.streams(url, params)`

尝试查找插件并从URL中提取流。

参数被传递给 `Plugin.streams()`。

如果未找到插件，则引发 `NoPluginError` 。

## Session

### `class streamlink.Streamlink(options = None)`

Streamlink会话用于跟踪插件、选项和日志设置。

#### `get_option(key)`

返回指定选项的当前值。

参数： 

- key -- 选项的键名

详细选项即参数值请参考 `Option`

#### `get_plugin_option(plugin, key)`

返回插件特定选项的当前值。

参数：

- Plugin -- 插件的名称
- Key -- 选项的键

#### `get_plugins()`

返回会话的加载插件。

#### `load_plugins(path)`

尝试从指定路径加载插件。

参数：

- path -- 查找插件的目录的完整路径

#### `logger`

向后兼容记录器属性：返回：记录器实例

#### `resolve_url(url, follow_redirect = True)`

尝试查找可以使用此URL的插件。

如果未指定，则默认协议(Http)将作为URL的前缀。

失败时引发 `NoPluginError`。

参数：

- url -- 与加载的插件匹配的URL
- follow_redirect -- 跟随重定向

#### `resolve_url_no_redirect(url)`

尝试查找可以使用此URL的插件。

如果未指定，则默认协议(Http)将作为URL的前缀。

失败时引发 `NoPluginError`。

参数：

- url -- 与加载的插件匹配的URL

#### `set_loglevel(level)`

设置此会话使用的日志级别。

有效级别为：`none`，`error`，`warning`，`info`，`debug`。

参数：

- level -- 输出的日志记录级别

#### `set_logoutput(output)`

设置此会话使用的日志输出。

参数：

- output -- 具有Write方法的文件类型对象

#### `set_option(key, value)`

设置源自此会话对象的插件和流使用的常规选项。

参数：

- key -- 选项的键
- value -- 要设置的值

详细选项即参数值请参考 `Option`

#### `set_plugin_option(plugin, key, value)`

设置源自此会话对象的插件使用的插件特定选项。

参数：

- plugin -- 插件的名称
- key -- 选项的键
- value -- 选项的值

#### `streams(url, params)`

尝试查找插件并从URL提取流。

参数被传递给 `Plugin.Streams()`。

如果未找到插件，则引发 `NoPluginError`。

#### Option

| key                      | 类型               | 值                                                         | 默认值             |
| ------------------------ | ------------------ | ---------------------------------------------------------- | ------------------ |
| hds-live-edge            | float              | 指定实时HDS流从流边缘开始的时间                            | 10.0               |
| hds-segment-attempts     | int                | 下载每个HDS段应该尝试多少次                                | 3                  |
| hds-segment-threads      | int                | 用于下载段的线程池大小                                     | 1                  |
| hds-segment-timeout      | float              | HDS段连接和读取超时                                        | 10.0               |
| hds-timeout              | float              | 从HDS流读取数据超时                                        | 60.0               |
| hls-live-edge            | int                | 从末尾开始多少段开始直播                                   | 3                  |
| hls-segment-attempts     | int                | 下载每个HLS段需要尝试多少次                                | 3                  |
| hls-segment-threads      | int                | 用于下载段的线程池大小                                     | 1                  |
| hls-segment-stream-data  | bool               | Stream HLS 段下载                                          | False              |
| hls-segment-timeout      | float              | HLS段连接和读取超时                                        | 10.0               |
| hls-timeout              | float              | 从HLS流读取数据超时                                        | 60.0               |
| http-proxy               | str                | 指定用于所有HTTP请求的HTTP代理                             |                    |
| https-proxy              | str                | 指定用于所有HTTPS请求的HTTPS代理                           |                    |
| http-cookies             | dict/str           | 要添加到每个HTTP请求的cookies                              |                    |
| http-headers             | dict/str           | 要添加到每个HTTP请求的headers                              |                    |
| http-query-params        | ditc/str           | 要添加到每个HTTP请求的参数                                 |                    |
| http-trust-env           | bool               | 信任环境中设置的HTTP设置，例如环境变量等                   |                    |
| http-ssl-verify          | bool               | 验证SSL证书                                                | True               |
| http-ssl-cert            | str/tuple          | 要使用的SSL证书，可以是`.pem`文件或`.crt/.key`对           |                    |
| http-timeout             | float              | 除其他选项覆盖的HTTP请求外，所有HTTP请求使用的常规超时     | 20.0               |
| http-stream-timeout      | float              | 从HTTP流读取数据超时                                       | 60.0               |
| subprocess-errorlog      | bool               | 将子进程中的错误记录到临时目录的文件                       |                    |
| subprocess-errorlog-path | str                | 将子进程中的错误记录道特定文件的路径                       |                    |
| ringbuffer-size          | int                | 大多数流类型使用的内部环境缓冲区大小                       | 16777216（16MB）   |
| rtmp-proxy               | str                | 指定rtmp流使用的代理（Socks）                              |                    |
| rtmp-rtmpdump            | str                | 指定rtmp流使用的rtmpdump可执行文件的位置                   |                    |
| rtmp-timeout             | float              | rtmp流读取数据超时                                         | 60.0               |
| ffmpeg-ffmpeg            | str                | 指定复用流使用的ffmpeg可执行文件的位置                     |                    |
| ffmpeg-verbose           | bool               | 将标准错误从ffmpeg记录到控制台                             |                    |
| ffmpeg-verbose-path      | str                | 指定ffmpeg stderr日志文件的位置                            |                    |
| ffmpeg-video-transcode   | str                | 在使用ffmpeg进行多路复用时对视频进行代码转换时使用的编码器 |                    |
| ffmpeg-audio-transcode   | str                | 在使用ffmpeg进行多路复用时转码音频时使用的编解码器         |                    |
| stream-segment-attempts  | int                | 下载每个段应该尝试多少次                                   | 3                  |
| stream-segment-threads   | int                | 用于下载分段的线程池大小                                   | 1                  |
| stream-segment-timeout   | float              | 段连接和读取超时                                           | 10.0               |
| stream-timeout           | float              | 从流中读取数据超时                                         | 60.0               |
| locale                   | str                | 区域设置，采用RFC 1766格式                                 | 系统区域设置       |
| user-input-requester     | UserInputRequester | 在运行时从用户收集输入的UserInputRequester实例             | UserInputRequester |

## Plugins

### `class streamlink.plugin.Plugin(url)`

插件可以从指定的URL检索流信息。

参数：

- url -- 插件将在其上运行的URL

#### `clear_cookies(cookie_filter = None)`

删除此插件的所有保存的Cookie。要过滤已删除的cookie，请指定 `COOKIE_FILTER` 参数*(请参见`save_cookies()`)*。

参数：

- cookie_filter -- 过滤Cookie的函数

返回值：

- 删除的Cookie名称列表

#### `load_cookies()`

加载该插件的所有存储的Cookie，该Cookie尚未过期。

返回值：

- 还原的Cookie名称列表

#### `classmethod piority(url)`

返回给定URL的插件优先级，默认情况下返回普通优先级。

返回值：

- 优先级

#### `save_cookies(cookie_filter = None, default_expires = 604800)`

将来自http的cookie存储在插件缓存中，直到它们过期。可以通过提供Filter方法来过滤Cookie。例如：Lambda c：c.name中的“auth”。如果Cookie中没有给出到期日期，则将使用DEFAULT_EXPILES值。

参数：

- cookie_filter -- 过滤cookie的函数
- default_expires -- 没有过期的cookie过期之前的时间（单位：秒）

返回值：

- 保存的cookie名称列表

#### `streams(stream_types = None, sorting_excludes = None)`

尝试提取可用流。

返回包含流的dict，其中键是流的名称，最常见的是质量，值是Stream对象。

结果可以包含同义词Best和Worst，它们分别指向可能具有最高和最低质量的流。

如果找到多个同名的流，则STREAM_TYPE中指定的流的顺序将确定保留该名称的流，而其余流将重命名为 `<name>_<stream type>`。

可以使用SORTING_EXCLUDE参数对同义词进行微调。这可以是以下两种类型之一：

1. 格式为[运算符]<值>的筛选器表达式列表。例如，过滤器“>480p”将从同义词排名中使用的列表中排除排名高于“480p”的流。有效运算符为>、>=、<和<=。如果未指定运算符，则将测试相等性。
2. 以流名称列表作为输入传递给filter()的函数。

参数：

- stream_type -- 要返回的流类型列表
- sorting_excludes -- 指定要从最佳/最差同义词中排除的流

### `class streamlink.options.Argumens(*args)`

提供参数列表的封装。例如：

```python
class PluginExample(Plugin):
    arguments = PluginArguments(
        PluginArgument(
            "username",
            help = "The username for your accont",
            metavar = "EMAIL",
            requires = ["password"]
        ),
        PluginArgument(
            "password",
            sensitive = True,
            help = "The password for your account",
            metavar = "PASSWORD"
        )
    )
```

这将向CLI添加 `--plugin-username` 和 `--plugin-password` 参数(假设插件模块为plugin)。

#### `requires(name)`

按名称查找所需的所有参数。

参数：

-  name -- 查找依赖项的参数名称

返回值：

- 从属参数列表

### `class streamlink.options.Argument(name, required = False, requires = None, prompt = None, sensitive = False, argument_name = None, dest = None, **options)`

参数接受大多数与 `ArgumentParser.add_argument()` 相同的参数，除了 `Requires` 是一个特例，因为在本例中，它仅在插件正在使用时强制执行。此外，`name` 参数是相对于插件的名称，例如。用户名、密码等。

> `__init__(name, requied = False, prompt = None, sensitive = False, argument_name = None, dest = None, **options)`

参数：

- name -- 参数的名称，不带 `--` 或插件名称前缀。例如：`password` `mu-subtitles` 等
- required -- 插件是否需要参数
- requires -- 此参数需要的参数列表。例如 `['password']`
- prompt -- 如果参数是必须的，但是没有给出，则此提示将在运行时显示
- sensitive -- 参数是否敏感（密码等）并且应该在日志中屏蔽
- argument_name -- 参数名称
- option_name -- 选项名称
- options -- 传递给ArgumentParser.add_Argument()的参数

## Streams

所有流都继承自Stream类。

### `open()`

尝试打开与流的连接。返回可用于读取流数据的类似文件的对象。

在失败时引发 `StreamError`。

### Stream 子类

您可以检查每个流使用的参数，不同的流类型提供不同的属性。

#### `class streamlink.stream.AkamaiHDStream(session, url, swf = None, seek = None)`

实施AkamaiHD自适应流协议。

参数：

- url -- 流的URL
- swf -- 握手协议使用的swf
- seek -- 查找打开流时要查找的位置

#### `class streamlink.stream.HDSStream(session, baseurl, url, bootstrap, metadata = None, timeout = 60, request_params)`

实现Adobe HTTP动态流协议。

参数：

- baseurl -- 基本URL
- url -- url基路径， 在获取片段时与基RUL连接
- 



