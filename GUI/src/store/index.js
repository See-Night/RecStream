import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    navActive: '/',
    API: {
      listener: {
        get: '/api/listener/get',
        add: '/api/listener/add',
        switch: '/api/listener/switch',
        update: '/api/listener/update',
        delete: '/api/listener/delete'
      },
      file: {
        get: '/api/file/get'
      },
      setting: {
        get: '/api/setting/get',
        update: '/api/setting/update'
      }
    }
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
