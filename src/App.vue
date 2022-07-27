<template>
    <div id="app">
        <router-view v-if="isRouterAlive"/>
    </div>
</template>

<script>
export default {
    name: "App",
    components: {
    },
    provide () {    
        //父组件通过provide来提供变量，在子组件中通过inject来注入变量                                       
            return {
                reload: this.reload                                              
            }
        },
        data() {
            return{
                isRouterAlive: true  //控制视图是否显示
            }
        },
        methods: {
            reload () {
                this.isRouterAlive = false;
                this.$nextTick(function () {
                    this.isRouterAlive = true;
                }) 
            }
        },
};
</script>

<style lang="less">
@import "../static/css/clear";
@import "../static/css/common";

#app {
    text-align: center;
    color: #2c3e50;
    height: 100%;
}

.clearfix:after {
    visibility: hidden;
    display: block;
    font-size: 0;
    content: " ";
    clear: both;
    height: 0;
}

// .clearfix{*zoom:1;}
// .clearfix:after {
//   content: "";
//   display: block;
//   visibility: hidden;
//   clear: both;
//   height: 0;
// }
.clearfix {
    zoom: 1;
    /* 为了照顾ie6浏览器*/
}
</style>
