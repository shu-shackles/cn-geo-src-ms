<template>
    <div class="survey_content2 clearfix">
        <headers :header="header" :name="name"></headers>
        <div class="contents clearfix">
            <div class="grahp">
                <div class="grahps1">
                    <NewsList />
                </div>
                <div class="grahps2">
                    <div v-if="src!=''" style="height:100%;overflow-y:hidden;overflow-x:hidden">
                        <iframe class="iframeA" :src="src"
                            frameborder="0" scrolling="yes">
                        </iframe>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import * as consts from "../../common/const";
import * as Contents from "../../common/content";
import * as Points from "../monitor/points";
import NewsList from "./NewsList.vue"

export default {
    components: {
        NewsList
    },
    data() {
        return {
            header: [],
            contens: {},
            one: {},
            tableData: [],
            tableHeader: [{ id: 0, value: "value", label: "地下水位(m7)" }],
            multipleSelection: [],
            search: "",
            currentPage: 1,
            name: "动态查询——地质新闻",
            page: {},
            //loading: false,
            option: {},
            src: ''
        };
    },
    created() {
        this.header = consts.getHeaderConfig("geoNews");
        this.page = consts.getPageConfig("one");
        // this.contens=Contents.getContent('table')

        // this.one=this.contens.one
        this.getTableData();
        this.getPointsData();
    },
    mounted() {
        this.$bus.$on('openPage',(url)=>{
            this.src = url
        })
    },
    beforeDestroy() {
        this.$bus.$off('openPage')
    },
    methods: {
        // 获取表格列表
        getTableData() {
            this.tableData = Contents.pointsTable;
        },
        // 删除
        deleteRow(index, rows) {
            rows.splice(index, 1);
        },
        filterTag(value, row) {
            return row.format === value;
        },
        getPointsData() {
            this.option = Points.onePoints;
            // this.option=Points.one
        }
    }
};
</script>

<style lang="less" scoped>
@import "../../../static/css/clear";
@import "../../../static/css/common";

.clearfix {
    *zoom: 1;
}

.clearfix:after {
    content: "";
    display: block;
    visibility: hidden;
    clear: both;
    height: 0;
}

.survey_content2 {
    margin-left: 18px;
    width: auto;
    height: 100%;
    background-color: #fff;

    .contents {
        background-color: #fff;
        // background-color: rgb(198, 219, 212);
        //margin: 15px;
        padding: 15px;

        .grahp {
            height: 560px;
            background-color: red;
            margin: 20px 0;
            display: flex;

            .grahps1 {
                height: 100%;
                width: 100%;
                background-color: #fff;
            }

            .grahps2 {
                height: 100%;
                width: 100%;
                background-color: #fff;
            }
        }
    }
}

.iframeA {
    //position: absolute;
    transform: scale(.5, .5) translate(-50%, -50%);
    width: 200%;
    height: 200%;
    top: 0;
    left: 0
}
</style>
