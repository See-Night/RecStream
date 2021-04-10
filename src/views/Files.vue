<template>
  <div id="files">
    <div class="topBar">
      <el-page-header @back="goBack" :content="headerContent"></el-page-header>
    </div>
    <div class="content">
      <div class="searchBar">
        <el-input
          v-model="search"
          placeholder="请输入内容"
          class="input-with-select"
        >
          <el-button slot="append" icon="el-icon-search"></el-button>
        </el-input>
      </div>
      <el-alert
        title="频繁转码会导致视频质量下降，请勿频繁转码"
        type="warning">
      </el-alert>
      <el-table :data="searchFile()" style="width: 100%" height="725">
        <el-table-column sortable prop="Title" label="标题" width="250">
          <template slot-scope="scope">
            <el-link :href="'/Movie/' + scope.row.FileName">{{ scope.row.Title }}</el-link>
          </template>
        </el-table-column>
        <el-table-column sortable prop="FileName" label="文件名" width="300">
        </el-table-column>
        <el-table-column sortable prop="Date" label="日期" width="150">
        </el-table-column>
        <el-table-column sortable prop="Time" label="时长"> </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-popover placement="right">
              <div style="text-align: right; margin: 0">
                <el-button
                  size="mini"
                  @click="recode(scope.row.FileName, 'mp4', scope.row.Title, scope.row.LiveURL)"
                >
                  MP4
                </el-button>
                <el-button
                  size="mini"
                  @click="recode(scope.row.FileName, 'flv', scope.row.Title, scope.row.LiveURL)"
                >
                  FLV
                </el-button>
                <el-button
                  size="mini"
                  @click="recode(scope.row.FileName, 'mov', scope.row.Title, scope.row.LiveURL)"
                >
                  MOV
                </el-button>
              </div>
              <el-button size="mini" slot="reference">转码</el-button>
            </el-popover>
            <el-button @click="deleteFile(scope.row.FileName)" size="mini" type="danger" style="margin: 0 0.5rem"
              >删除</el-button
            >
          </template>
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
      search: "",
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
      v.$axios.get(API.file.get).then((res) => {
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
    },
    recode(FileName, format, title, LiveURL) {
      const API = this.$store.state.API;
      let v = this;
      v.$axios.post(API.file.recode, { 
        FileName,
        format,
        title,
        LiveURL
      }).then(res => {
        if (res.data.status) {
          v.$notify.success({
            title: '正在转码',
            message: '请稍后刷新查看'
          })
        }
      });
    },
    deleteFile(FileName) {
      const API = this.$store.state.API;
      let v = this;
      v.$axios.post(API.file.delete, { FileName })
      .then(res => {
        if (res.data.status) {
          v.$notify.success({
            title: '成功'
          })
        }
        this.getFiles();
      });
    },
  },
  mounted() {
    this.getFiles();
  },
};
</script>

<style scoped>
.searchBar {
  width: 30%;
  margin-top: 15px;
  margin-bottom: 15px;
}
.el-dropdown {
  vertical-align: top;
}
.el-dropdown + .el-dropdown {
  margin-left: 15px;
}
.el-icon-arrow-down {
  font-size: 12px;
}
</style>