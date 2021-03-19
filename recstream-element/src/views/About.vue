<template>
  <div class="about">
    <el-tabs tab-position="right" style="height: 100%">
      <el-tab-pane label="使用说明">
        <h1>使用说明</h1>
        <div style="text-align: left; padding: 1rem">
          <el-collapse>
            <el-collapse-item>
              <template slot="title">
                <p style="font-size: 1rem">新建监听器</p>
              </template>
              <div>
                从侧边栏打开“监听器 >
                新增”，填写监听地址和监听器名称，点击“确认新增”按钮。
              </div>
              <el-alert
                title="默认启动开关如果打开，新建好监听器后会自动开始监听；否则需要自行启动监听器。"
                type="warning"
                :closable="false"
              >
              </el-alert>
            </el-collapse-item>
            <el-collapse-item>
              <template slot="title">
                <p style="font-size: 1rem">启动/关闭监听器</p>
              </template>
              <div>
                从侧边栏打开“监听器 > 全部”，找到需要启动/关闭的监听器。点击
                <i class="el-icon-switch-button"></i> 按钮。
              </div>
              <el-alert
                title="页面最上端的搜索框支持根据监听器名称和监听器地址查找。"
                type="success"
                :closable="false"
              >
              </el-alert>
            </el-collapse-item>
            <el-collapse-item>
              <template slot="title">
                <p style="font-size: 1rem">删除监听器</p>
              </template>
              <div>
                从侧边栏打开“监听器 > 全部”，找到需要删除的监听器。点击
                <i class="el-icon-delete"></i> 按钮。
              </div>
              <el-alert
                title="页面最上端的搜索框支持根据监听器名称和监听器地址查找。"
                type="success"
                :closable="false"
              >
              </el-alert>
            </el-collapse-item>
            <el-collapse-item>
              <template slot="title">
                <p style="font-size: 1rem">查看已录制的文件</p>
              </template>
              <div>
                从侧边栏打开“文件”，可以根据日期、时长、文件名进行排序。
              </div>
              <el-alert
                title="页面最上端的搜索框支持根据文件名称和录播标题查找。"
                type="success"
                :closable="false"
              >
              </el-alert>
            </el-collapse-item>
            <el-collapse-item>
              <template slot="title">
                <p style="font-size: 1rem">开启网络代理</p>
              </template>
              <div>
                从侧边栏打开“设置”，打开网络代理的开关，并填写“代理地址”等相关信息。
              </div>
              <el-alert
                title="目前代理仅支持http/https代理，socks/ftp等代理模式暂不支持。"
                type="error"
                :closable="false"
              >
              </el-alert>
            </el-collapse-item>
          </el-collapse>
        </div>
      </el-tab-pane>
      <el-tab-pane label="项目说明">
        <h1>项目说明</h1>
        <div style="text-align: left; padding: 1rem">
          <p>本项目旨在通过更为简单的方法提供直播的录制服务。</p>
          <p>项目优点：</p>
          <ul>
            <li>占用资源少</li>
            <li>支持x86、arm等多平台，Windows、Linux、MacOS等多操作系统</li>
            <li>支持Docker容器部署</li>
            <li>支持分布式部署</li>
            <li>本项目遵守MIT开源协议</li>
          </ul>
          <p>
            部署说明书：
            <el-link type="info" href="https://1145141919810.wang/RecStream">
              https://1145141919810.wang/RecStream
            </el-link>
          </p>
          <p>
            Docker镜像：
            <el-link
              type="info"
              href="https://hub.docker.com/seenight/rec-stream"
            >
              https://hub.docker.com/seenight/rec-stream
            </el-link>
          </p>
          <p>
            项目地址：
            <el-link
              type="info"
              href="https://github.com/Dreammer12138/RecStream"
            >
              https://github.com/Dreammer12138/RecStream
            </el-link>
          </p>
          <p>
            作者：
            <el-link type="info" href="https://github.com/Dreammer12138">
              <i class="iconfont">&#xe689;</i>
              Dreammer12138
            </el-link>
          </p>
        </div>
      </el-tab-pane>
      <el-tab-pane label="MIT LICENSE">
        <h1>MIT LICENSE</h1>
        <div style="display: flex; justify-content: center">
          <p
            style="
              text-align: left;
              width: 75%;
              background-color: rgb(233, 233, 235);
              padding: 1rem;
              border-radius: 0.5rem;
            "
          >
            MIT License<br /><br />

            Copyright (c) 2021 Dreammer12138<br /><br />

            Permission is hereby granted, free of charge, to any person
            obtaining a copy of this software and associated documentation files
            (the "Software"), to deal in the Software without restriction,
            including without limitation the rights to use, copy, modify, merge,
            publish, distribute, sublicense, and/or sell copies of the Software,
            and to permit persons to whom the Software is furnished to do so,
            subject to the following conditions:<br /><br />

            The above copyright notice and this permission notice shall be
            included in all copies or substantial portions of the Software.<br /><br />

            THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
            EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
            MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
            NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
            BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
            ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
            CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
            SOFTWARE.<br /><br />
          </p>
        </div>
      </el-tab-pane>
      <el-tab-pane label="反馈">
        <h1>反馈</h1>
        <iframe
          style="height: 100%; width: 100%"
          src="https://kaguramea.net/RecStreamIssues"
          frameborder="0"
        ></iframe>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
export default {
  name: "about",
};
</script>

<style scoped>
.about {
  height: 100%;
}

h1 {
  font-size: 2.5rem;
  margin: 1rem;
}
@font-face {
  font-family: "iconfont"; /* project id 2323334 */
  src: url("//at.alicdn.com/t/font_2323334_0ghszlhid5hg.eot");
  src: url("//at.alicdn.com/t/font_2323334_0ghszlhid5hg.eot?#iefix")
      format("embedded-opentype"),
    url("//at.alicdn.com/t/font_2323334_0ghszlhid5hg.woff2") format("woff2"),
    url("//at.alicdn.com/t/font_2323334_0ghszlhid5hg.woff") format("woff"),
    url("//at.alicdn.com/t/font_2323334_0ghszlhid5hg.ttf") format("truetype"),
    url("//at.alicdn.com/t/font_2323334_0ghszlhid5hg.svg#iconfont")
      format("svg");
}
.iconfont {
  font-family: "iconfont" !important;
  font-size: 16px;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -webkit-text-stroke-width: 0.2px;
  -moz-osx-font-smoothing: grayscale;
}
</style>

<style>
.el-tabs__content {
  height: 100%;
}
.el-tab-pane {
  height: 100%;
}
</style>

