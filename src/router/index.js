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

// 用了一些奇技淫巧解决了一些问题，不值得学习
var flag = true;
var n = 1;
//全局前置路由守卫：初始化的时候被调用、在每一次路由切换之前被调用
router.beforeEach((to, from, next) => {
  if (whiteRouter.indexOf(to.path) !== -1) {
    next();
    n = 1;
  } else {
    getToken();
    console.log(flag);
    if (flag) {
      next();
    } else {
      router.replace({ name: 'login' })
      //location.reload();
      alert("请先登录！");
    }
  }
});

function getToken() {
  if (n > 0) {
    var config = {
      method: "post",
      url: "http://localhost:8080/api/v1/login_get_user",
      headers: {
        Authorization: "Bearer " + store.state.token
      }
    };
    axios(config)
      .then(response => {
        flag = true;
        n = 1;
      })
      .catch(error => {
        flag = false;
        n = 0;
      });
  }
}

export default router;
