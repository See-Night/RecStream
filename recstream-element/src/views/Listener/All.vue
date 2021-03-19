<template>
  <div id="allListener">
    <div class="topBar">
      <el-page-header @back="goBack" :content="headerContent"></el-page-header>
    </div>
    <div class="content">
      <div class="searchBar">
        <el-input
          placeholder="请输入内容"
          class="input-with-select"
          v-model="search"
        >
          <el-button slot="append" icon="el-icon-search"></el-button>
        </el-input>
      </div>
      <div v-for="listener in searchListener()" :key="listener.LiveURL">
        <ListenerItem
          :listener="listener"
          @reloadListener="getListeners"
          :btnShow="true"
        ></ListenerItem>
      </div>
    </div>
  </div>
</template>

<script>
import ListenerItem from "../../components/listenerItem";

export default {
  name: "allListener",
  data() {
    return {
      headerContent: "全部",
      listeners: [],
      search: "",
    };
  },
  components: {
    ListenerItem,
  },
  methods: {
    goBack() {
      this.$store.state.navActive = "/";
      this.$router.push("/");
    },
    getListeners() {
      const API = this.$store.state.API;
      let v = this;
      v.$axios.get(API.listener.get).then((res) => {
        v.listeners = res.data;
      });
    },
    searchListener() {
      let res = [];
      for (let listener in this.listeners) {
        if (
          this.listeners[listener].LiveURL.indexOf(this.search) !== -1 ||
          this.listeners[listener].Name.indexOf(this.search) !== -1
        ) {
          res.push(this.listeners[listener]);
        }
      }
      return res;
    },
  },
  mounted() {
    this.getListeners();
  },
};
</script>

<style scoped>
.el-select .el-input {
  width: 130px;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}

.searchBar {
  width: 30%;
  margin-top: 15px;
  margin-bottom: 15px;
}
</style>