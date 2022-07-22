import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        uid   : sessionStorage.getItem('uid'),
        name  : sessionStorage.getItem('name'),
        password: sessionStorage.getItem('password'),
        type  : sessionStorage.getItem('type'),
        area  : sessionStorage.getItem('area'),
        IDName: sessionStorage.getItem('IDName'),
        ID    : sessionStorage.getItem('ID'),
        token : sessionStorage.getItem('userToken'),
        data  : sessionStorage.getItem('data')
    },
    mutations:{

    },
    actions:{

    }
})