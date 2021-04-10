<template>
  <el-col :span="24" id="sideNav">
    <el-menu
      unique-opened
      router
      :default-active="$store.state.navActive"
      :collapse="innerWidth < 768"
    >
      <el-menu-item index="/">
        <i class="el-icon-house"></i>
        <span slot="title">首页</span>
      </el-menu-item>
      <el-submenu index="/listener">
        <template slot="title">
          <i class="el-icon-headset"></i>
          <span>监听器</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="/listener/all">
            <i class="el-icon-files"></i>
            全部
          </el-menu-item>
          <el-menu-item index="/listener/add">
            <i class="el-icon-plus"></i>
            新增
          </el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-menu-item index="/files">
        <i class="el-icon-folder"></i>
        <span slot="title">文件</span>
      </el-menu-item>
      <el-menu-item index="/settings">
        <i class="el-icon-setting"></i>
        <span slot="title">设置</span>
      </el-menu-item>
      <el-menu-item index="/about">
        <i class="el-icon-warning-outline"></i>
        <span slot="title">关于</span>
      </el-menu-item>
    </el-menu>
  </el-col>
</template>

<script>
export default {
  name: "sideNav",
  data() {
    return {
      innerWidth: window.innerWidth
    }
  }
};
</script>

<style scoped>
#sideNav {
  position: absolute;
  left: 0;
  height: 94vh;
  width: 15vw;
}
#sideNav > .el-menu {
  height: 100%;
}

.el-submenu {
  width: 100%;
  text-align: left;
}
.el-submenu * {
  text-align: left;
}
.el-menu-item {
  width: 100%;
  text-align: left;
}
</style>