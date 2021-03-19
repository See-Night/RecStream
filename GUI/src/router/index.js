import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import HomePage from '../views/HomePage.vue';
import About from '../views/About.vue';

// listener
import Add from '../views/Listener/Add.vue';
import All from '../views/Listener/All.vue';

// file
import Files from '../views/Files.vue';

// settings
import Settings from '../views/Settings.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    children: [
      {
        name: '',
        path: '/',
        component: HomePage
      },
      {
        name: 'addListener',
        path: '/listener/add',
        component: Add
      },
      {
        name: 'allListener',
        path: '/listener/all',
        component: All
      },
      {
        path: '/files',
        name: 'files',
        component: Files
      },
      {
        path: '/settings',
        name: 'settings',
        component: Settings
      },
      {
        path: 'about',
        name: 'about',
        component: About
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
