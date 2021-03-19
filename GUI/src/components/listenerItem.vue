<template>
  <div class="listener-item">
    <el-col :span="16">
      <strong class="title">{{ listener.Name }}</strong>
      <br />
      <span class="liveurl">{{ listener.LiveURL }}</span>
    </el-col>
    <el-col :span="8" v-if="btnShow">
      <el-button-group>
        <el-button icon="el-icon-edit"></el-button>
        <el-button
          icon="el-icon-switch-button"
          @click="switchy"
          :class="listener.Status === 0 ? 'text-dinger' : 'text-success'"
        ></el-button>
        <el-button type="danger" icon="el-icon-delete" @click="deleteListener"></el-button>
      </el-button-group>
    </el-col>
  </div>
</template>

<script>
export default {
  name: "ListenerItem",
  props: {
    listener: Object,
    btnShow: Boolean
  },
  methods: {
    switchy() {
      const API = this.$store.state.API;
      let v = this;
      v.$axios.post(API.listener.switch, {
        LiveURL: v.listener.LiveURL,
        Status: v.listener.Status === 0 ? 1 : 0
      }).then((res) => {
        if (res.data.status) {
          v.listener.Status = v.listener.Status === 0 ? 1 : 0;
          this.$notify.success({
            title: "成功",
            message:
              "已将 " +
              v.listener.LiveURL +
              (v.listener.Status === 0 ? " 关闭" : " 启动"),
          });
          
        } else {
          this.$notify.error({
            title: "错误",
            message: res.data.msg,
          });
        }
      });
    },
    deleteListener() {
      const API = this.$store.state.API;
      let v = this;
      v.$axios.post(API.listener.delete, this.listener).then(res => {
        if (res.data.status) {
          this.$notify.success({
            title: '成功',
            message: '已将 ' + v.listener.LiveURL + ' 删除'
          });
          v.$emit('reloadListener');
        }
        else {
          this.$notify.error({
            title: '错误',
            message: res.data.msg
          });
        }
      });
    }
  },
};
</script>

<style scoped>
.listener-item {
  height: 6vh;
  border-top: 1px solid #dcdfe6;
  border-bottom: 1px solid #dcdfe6;
  border-right: 1px solid #dcdfe6;
  border-left: 10px solid #409eff;
  padding: 1rem;
  margin: 1rem 0;
}
.el-col {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  height: 100%;
}
.title {
  font-size: 1.5rem;
}
.liveurl {
  font-size: 0.8rem;
  color: #aaaaaa;
}
.text-dinger {
  color: #f56c6c;
}
.text-success {
  color: #67c23a;
}
.text-warning {
  color: #e6a23c;
}
</style>