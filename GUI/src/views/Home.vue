<template>
  <el-container>
    <el-header>
      <span id="logo">
        <strong>RecStream</strong>
      </span>
    </el-header>
    <el-container>
      <el-aside width="15%">
        <sideNav></sideNav>
      </el-aside>
      <el-main>
        <section>
          <div style="height: 100%;">
            <router-view></router-view>
          </div>
        </section>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import sideNav from "../components/sideNav";
export default {
  name: "Home",
  data() {
    return {
      breadcrumbItems: []
    };
  },
  components: {
    sideNav,
  },
  methods: {
  },
  created() {
    this.$store.state.navActive = this.$route.path;
  }
};
</script>

<style>
body {
  margin: 0 !important;
  background-color: #e9eef3;
}
.el-header {
  background-color: #545c64;
  height: 6vh !important;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
.el-main {
  height: 94vh;
}
.el-main > section {
  background-color: #ffffff;
  height: calc(100% - 40px);
  padding: 1rem;
}

.topBar {
  padding: .5rem 0;
  border-bottom: 1px solid #DCDFE6;
}
.content {
  padding: 1rem;
}
</style>

<style scoped>
#logo {
  font-size: 1.5rem;
  color: #ffffff;
}
</style>
