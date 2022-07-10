<template>
    <div class="survey_content2 clearfix">
        <headers :header="header" :name="name"></headers>
        <div class="contents clearfix">
            <div class="grahp">
                <div class="grahps1">
                    <MasterMap />
                </div>
                <div class="grahps2">
                    <Rank />
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import * as consts from "../../common/const";
import * as Contents from "../../common/content";
import * as Points from "./points";
import MasterMap from "../DynamicQuery/MasterMap.vue"
import Rank from "../DynamicQuery/Rank.vue"


export default {
    components: {
        MasterMap,
        Rank
    },
    data() {
        return {
            header: [],
            //   contens: {},
            //   one: {},
            //   tableData: [],
            //   tableHeader: [{ id: 0, value: "value", label: "地下水位(m7)" }],
            //   multipleSelection: [],
            //   search: "",
            //   currentPage: 1,
            name: "动态查询",
            page: {},
            //   loading: {
            //     indexLoading: false,
            //     pieLoading: false,
            //     pieLoading1: false,
            //     chartLoading: false,
            //     chartLoading1: false,
            //     tableLoading: false,
            //     pieLoading2: false,
            //     pieLoading3: false
            //   },
            //   option: {}
        };
    },
    created() {
        this.header = consts.getHeaderConfig("history");
        this.page = consts.getPageConfig("one");
        // this.contens=Contents.getContent('table')

        // this.one=this.contens.one
        this.getTableData();
        this.getPointsData();
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
    width: 100%;
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
                width: 200%;
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
</style>

