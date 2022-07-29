import Vue from "vue";
import Router from "vue-router";
import store from "../store/store.js";
import axios from "axios";
import { WindowsBalloon } from "node-notifier";
Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: "/",
      name: "login",
      component: resolve =>
        require(["@/components/common/Login.vue"], resolve),
    },
    {
      path: "/register",
      name: "register",
      component: resolve =>
        require(["@/components/common/register.vue"], resolve)
    },
    {
      path: "/index",
      name: "index",
      component: resolve => require(["@/components/common/index.vue"], resolve),
      beforeEnter: (to, from, next) => {
        store.commit("SET_SHOWMENU", false);
        next();
      }
    },
    {
      path: "/survey",
      component: resolve => require(["@/components/home.vue"], resolve),
      children: [
        {
          // 矿物数据
          path: "/query/mineral",
          name: "query_mineral",
          component: resolve =>
            require(["@/components/DynamicQuery/MineralData.vue"], resolve)
        },
        {
          // 地质新闻
          path: "/query/news",
          name: "query_news",
          component: resolve =>
            require(["@/components/DynamicQuery/GeoNews.vue"], resolve)
        },
        {
          // 森林资源
          path: "/analysis/forest",
          name: "analysis_forest",
          component: resolve =>
            require(["@/components/analysis/ForestAnalysis.vue"], resolve)
        },
        {
          // 矿产资源
          path: "/analysis/mineral",
          name: "analysis_mineral",
          component: resolve =>
            require(["@/components/analysis/MineralAnalysis.vue"], resolve)
        },
        {
          // 用户设置
          path: "/setting/user",
          name: "setting_user",
          component: resolve =>
            require(["@/components/setting/user.vue"], resolve)
        },
        {
          // 数据审核
          path: "/setting/audit",
          name: "data_audit",
          component: resolve =>
            require(["@/components/setting/DataAudit.vue"], resolve)
        }
      ]
    }
  ]
});
const whiteRouter = ["/","/register"];

router.beforeEach(async(to, from, next) => {
    let token = store.state.token;
    if(whiteRouter.indexOf(to.path) === -1 && !token){
        alert("请先登录！")
        next({name:'login'})
    } else {  
    // if(whiteRouter.indexOf(to.path) !== -1 && token){
    //     next('/index')
    // }
    //else{
        next()
    //    }
    }
})

export default router;