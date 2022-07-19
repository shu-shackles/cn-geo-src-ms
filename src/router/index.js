/*
 * @Description:
 * @Autor: Sia
 * @Date: 2019-07-20 10:19:32
 * @LastEditors: huacong
 * @LastEditTime: 2020-06-20 10:40:41
 */
import Vue from "vue";
import Router from "vue-router";
import store from "../store/index";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "login",
      component: resolve => require(["@/components/common/Login.vue"], resolve)
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
        // {
        //   // 项目简介
        //   path: "/project/survey",
        //   name: "project_survey",
        //   component: resolve =>
        //     require(["@/components/project/survey.vue"], resolve)
        // },
        // {
        //   // 项目文档
        //   path: "/project/word",
        //   name: "project_word",
        //   component: resolve =>
        //     require(["@/components/project/word.vue"], resolve)
        // },
        // {
        //   // 项目表格
        //   path: '/project/table',
        //   name: 'project_table',
        //   component: resolve => require(['@/components/project/table.vue'], resolve),
        // },
        // {
        //   // 项目矢量数据
        //   path: "/project/graph",
        //   name: "project_graph",
        //   component: resolve =>
        //     require(["@/components/project/graph.vue"], resolve)
        // },
        // {
        //   // 项目影像
        //   path: "/project/img",
        //   name: "project_img",
        //   component: resolve =>
        //     require(["@/components/project/img.vue"], resolve)
        // },
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
