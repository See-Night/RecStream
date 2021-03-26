<template>
  <div id="home">
    <el-col id="info">
      <el-card class="box-card text-align-left" id="listeners">
        <div slot="header" class="clearfix">
          <span>监听器</span>
          <el-button
            @click="moreListener"
            style="float: right; padding: 3px 0"
            type="text"
            >查看更多</el-button
          >
        </div>
        <div v-for="listener in 2" :key="listener">
          <ListenerItem
            :listener="listeners[listener]"
            :btnShow="false"
          ></ListenerItem>
        </div>
      </el-card>
      <el-card class="box-card text-align-left" id="files">
        <div slot="header" class="clearfix">
          <span>文件</span>
          <el-button
            @click="moreFiles"
            style="float: right; padding: 3px 0"
            type="text"
            >查看更多</el-button
          >
        </div>
        <div>
          <el-table :data="files" style="width: 100%">
            <el-table-column sortable prop="FileName" label="标题">
            </el-table-column>
            <el-table-column sortable prop="Date" label="日期" width="200">
            </el-table-column>
          </el-table>
        </div>
      </el-card>
    </el-col>
    <el-col id="echarts">
      
    </el-col>
  </div>
</template>

<script>
import ListenerItem from "../components/listenerItem";
export default {
  name: "home",
  data() {
    return {
      listeners: [],
      files: [],
      connection: {
        Controller: "",
        Database: "",
      },
    };
  },
  components: {
    ListenerItem,
  },
  methods: {
    getListener() {
      const API = this.$store.state.API;
      let v = this;
      v.$axios.get(API.listener.get).then((res) => {
        v.listeners = res.data;
      });
    },
    getFiles() {
      const API = this.$store.state.API;
      let v = this;
      v.$axios.get(API.file.get).then(res => {
        for (let i = 0; i < 4 || res.data[i] ; i++) {
          v.files.push(res.data[i]);
        }
      });
    },
    moreListener() {
      this.$router.push("/listener/all");
    },
    moreFiles() {
      this.$router.push("/files");
    },
  },
  mounted() {
    this.getListener();
    this.getFiles();
  },
};
</script>

<style scoped>
#home {
  height: 100%;
}

#title {
  font-size: 4rem;
  margin: 1rem;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.item {
  display: flex;
  justify-content: center;
  align-items: center;
}
.item span {
  font-size: 2rem;
}

#infoList {
  background-color: #f4f4f5;
  padding: 1rem;
  border-radius: 0.5rem;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: left;
}

#listeners {
  width: 49%;
}
#listeners > * {
  height: 100%;
}
#files {
  width: 49%;
}
#files > * {
  height: 100%;
}

#info {
  display: flex;
  justify-content: space-between;
}

.info {
  padding: 0.5rem !important;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

#contentTop {
  height: 25vh;
}

.text-align-center {
  text-align: center;
}
.text-align-left {
  text-align: left;
}
</style>

<style>
</style>