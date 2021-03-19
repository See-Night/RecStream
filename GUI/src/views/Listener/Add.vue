<template>
  <div id="addListener">
    <div class="topBar">
      <el-page-header @back="goBack" :content="headerContent"></el-page-header>
    </div>
    <div class="content">
      <el-col :span="12">
        <el-form ref="form" :model="listener" label-width="6rem">
          <el-form-item label="监听器名称">
            <el-input v-model="listener.Name"></el-input>
          </el-form-item>
          <el-form-item label="监听地址">
            <el-input v-model="listener.LiveURL"></el-input>
          </el-form-item>
          <el-form-item label="默认启动">
            <el-switch v-model="listener.Status"></el-switch>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">确认新建</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </div>
  </div>
</template>

<script>
export default {
  name: "addListener",
  data() {
    return {
      headerContent: "新增",
      listener: {
        Name: "",
        LiveURL: "",
        Status: false,
      },
    };
  },
  methods: {
    goBack() {
      this.$store.state.navActive = "/";
      this.$router.push("/");
    },
    onSubmit() {
      let reg = /https?:\/\/([a-zA-Z0-9]+\.)?([a-zA-Z0-9]+)\..*/;
      this.listener.Platform = reg.exec(this.listener.LiveURL)[2];
      
      const API = this.$store.state.API;
      let v = this;
      v.$axios.post(API.listener.add, this.listener).then(res => {
        if (res.data.status) {
          this.$notify.success({
            title: '成功',
            message: '已将' + this.listener.LiveURL + '添加到监听器中'
          });
        }
        else {
          this.$notify.error({
            title: '错误',
            message: res.data.msg
          });
        }
      })
    },
  },
};
</script>

<style scoped>
.el-form-item {
  text-align: left;
}
</style>