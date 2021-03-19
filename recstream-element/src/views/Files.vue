<template>
  <div id="files">
    <div class="topBar">
      <el-page-header @back="goBack" :content="headerContent"></el-page-header>
    </div>
    <div class="content">
      <div class="searchBar">
        <el-input v-model="search" placeholder="请输入内容" class="input-with-select">
          <el-button slot="append" icon="el-icon-search"></el-button>
        </el-input>
      </div>
      <el-table :data="searchFile()" style="width: 100%" height="725">
        <el-table-column sortable prop="Title" label="标题" width="250">
        </el-table-column>
        <el-table-column sortable prop="FileName" label="文件名" width="300">
        </el-table-column>
        <el-table-column sortable prop="Date" label="日期" width="150">
        </el-table-column>
        <el-table-column sortable prop="Time" label="时长">
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  name: "files",
  data() {
    return {
      headerContent: "文件",
      files: [],
      search: ''
    };
  },
  methods: {
    goBack() {
      this.$store.state.navActive = "/";
      this.$router.push("/");
    },
    getFiles() {
      const API = this.$store.state.API;
      let v = this;
      v.$axios.get(API.file.get).then(res => {
        v.files = res.data;
      });
    },
    searchFile() {
      let res = [];
      for (let file in this.files) {
        if (
          this.files[file].Title.indexOf(this.search) !== -1 ||
          this.files[file].FileName.indexOf(this.search) !== -1
        ) {
          res.push(this.files[file]);
        }
      }
      return res;
    }
  },
  mounted() {
    this.getFiles();
  }
};
</script>

<style scoped>
.searchBar {
  width: 30%;
  margin-top: 15px;
  margin-bottom: 15px;
}
</style>