<template>
  <div id="settings">
    <div class="topBar">
      <el-page-header @back="goBack" :content="headerContent"></el-page-header>
    </div>
    <div class="content">
      <el-col :span="12">
        <el-form ref="form" :model="settings" label-width="6rem">
          <el-form-item label="存储路径">
            <el-input v-model="settings.savePath"></el-input>
          </el-form-item>
          <el-form-item label="监听间隔">
            <el-slider v-model="settings.listenInterval" :min="1000" :max="10000" :step="1000"> </el-slider>
          </el-form-item>
          <el-form-item label="存储格式">
            <el-select v-model="settings.format" placeholder="请选择存储格式">
              <el-option label="MP4" value="MP4"></el-option>
              <el-option label="FLV" value="FLV"></el-option>
              <el-option label="AVI" value="AVI"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="网络代理">
            <el-switch v-model="settings.proxyOn"></el-switch>
          </el-form-item>
          <el-form-item label="代理地址">
            <el-input v-model="settings.proxyHttp"></el-input>
          </el-form-item>
          <el-form-item label="代理用户名">
            <el-input v-model="settings.proxyUser"></el-input>
          </el-form-item>
          <el-form-item label="代理密码">
            <el-input v-model="settings.proxyPassword"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">保存</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </div>
  </div>
</template>

<script>
export default {
  name: "files",
  data() {
    return {
      headerContent: "设置",
      settings: {
        savePath: "",
        format: "",
        listenInterval: 2000,
        proxyOn: false,
        proxyHttp: "",
        proxyUser: "",
        proxyPassword: "",
      },
    };
  },
  methods: {
    goBack() {
      this.$store.state.navActive = "/";
      this.$router.push("/");
    },
    onSubmit() {
      const API = this.$store.state.API;
      let v = this;
      v.$axios.post(API.setting.update, v.settings).then(res => {
        if (res.data.status) {
          this.$notify.success({
            title: '成功',
            message: '配置已修改'
          });
        }
        else {
          this.$notify.error({
            title: '错误',
            message: res.data.msg
          });
        }
      });
    },
    getSettings() {
      const API = this.$store.state.API;
      let v = this;
      v.$axios.get(API.setting.get).then(res => {
        for (let setting in res.data) {
          v.settings[res.data[setting].key] = res.data[setting].value;
        }
      })
    }
  },
  mounted() {
    this.getSettings();
  }
};
</script>

<style scoped>
.el-form-item {
  text-align: left;
}
</style>