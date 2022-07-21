import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        user: sessionStorage.getItem('user'),
        token : sessionStorage.getItem('userToken')
    },
    mutations:{

    },
    actions:{

    }
})