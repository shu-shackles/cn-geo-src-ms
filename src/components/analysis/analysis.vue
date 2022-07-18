<template>
    <div class="survey_content2 clearfix" style="overflow-x:hidden;">
        <headers :header="header" :name="name"></headers>
        <div class="contents clearfix">
            <div class="grahp">
                <div class="grahps">
                    <ForestChart/>
                </div>
            </div>
            <div style="text-align:center;width:80%;margin-left:10%;">
                <el-table :data="tableData" border size="small"
                    :header-cell-style="{ background: '#58a0db', color: '#fff' }">
                    <el-table-column sortable v-for="(item, index) in tableHeader" :key="index" :prop="item.value"
                        :label="item.label" align="center"  :resizable="false">
                    </el-table-column>
                </el-table>
            </div>

        </div>
    </div>
</template>

<script>
import * as consts from "../../common/const";
import * as Contents from "../../common/content";
import ForestChart from "../common/chart/ForestChart.vue";
import * as Points from "./points";
import axios from 'axios';

export default {
    components: {
        ForestChart
    },
    data() {
        return {
            header: [],
            contens: {},
            one: {},
            tableData: [],
            tableHeader: [
                { id: 0, value: "省市或公司", label: "统计单位" },
                { id: 1, value: "森林覆盖面积", label: "森林覆盖面积（万公顷）" },
                { id: 2, value: "森林覆盖率", label: "森林覆盖率（%）" },
                { id: 3, value: "自然林面积", label: "自然林面积（万公顷）" },
                { id: 4, value: "人工林面积", label: "人工林面积（万公顷）" },
            ],
            multipleSelection: [],
            search: "",
            currentPage: 1,
            name: "数据分析——森林资源",
            page: {},
            loading: {
                indexLoading: false,
                pieLoading: false,
                pieLoading1: false,
                chartLoading: false,
                chartLoading1: false,
                tableLoading: false,
                pieLoading2: false,
                pieLoading3: false
            },
            option: {}
        };
    },
    created() {
        this.header = consts.getHeaderConfig("analysis");
        this.page = consts.getPageConfig("two");
        // this.contens=Contents.getContent('table')
        // this.one=this.contens.one
        //this.getTableData();
        this.getPointsData();
    },
    mounted() {
        axios({
            method: 'get',
            url: 'http://localhost:8080/api/v1/forestAll',
        }).then(response => {
            this.tableData = response.data
            this.$bus.$emit('ForestData',this.tableData)
        },
            error => {
                this.tableData = error.message
            });
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

    .contents {
        background-color: #fff;
        // background-color: rgb(198, 219, 212);
        margin-top: -1px;
        padding-bottom: 20px;

        .grahp {
            // height: 300px;
            background-color: red;
            margin: 20px 0;

            .grahps {
                height: auto;
                background-color: green;
            }
        }
    }
}
</style>

