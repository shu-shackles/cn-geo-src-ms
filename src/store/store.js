import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        news: undefined,
        uid   : sessionStorage.getItem('uid'),
        name  : sessionStorage.getItem('name'),
        password: sessionStorage.getItem('password'),
        type  : sessionStorage.getItem('type'),
        area  : sessionStorage.getItem('area'),
        IDName: sessionStorage.getItem('IDName'),
        ID    : sessionStorage.getItem('ID'),
        token : sessionStorage.getItem('userToken'),
        valid : sessionStorage.getItem('valid'),
        data  : JSON.parse(sessionStorage.getItem('data'))
    },
    mutations:{
        SET_Token(state, data) {
            state.token = data
            sessionStorage.setItem("userToken", data)
        },
        SET_Data(state, data) {
            state.data = data
            sessionStorage.setItem("data", data)
        },
        SET_Valid(state,data)
        {
            state.valid = data
            sessionStorage.setItem("valid", data)
        }
    },
    actions:{

    }
})