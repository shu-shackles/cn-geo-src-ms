<template>
    <div class="survey_content2 clearfix" style="overflow-x:hidden;">
        <headers :header="header" :name="name"></headers>
        <div class="contents clearfix">
            <div class="grahp">
                <div class="grahps">
                    <MineralChart />
                </div>
            </div>
            <div style="text-align:center;width:80%;margin-left:10%;">
                <el-table :data="tableData" border size="small"
                    :header-cell-style="{ background: '#58a0db', color: '#fff' }">
                    <el-table-column prop="name"
                        label="矿物名称（单位）" align="center" :resizable="false" width="150px">
                    </el-table-column>
                    <el-table-column v-for="(item, index) in tableHeader" :key="index" :prop="item.value"
                        :label="item.label" align="center" :resizable="false">
                    </el-table-column>
                </el-table>
            </div>

        </div>
    </div>
</template>

<script>
import * as consts from "../../common/const";
import * as Contents from "../../common/content";
import MineralChart from "../common/chart/MineralChart.vue";
import axios from 'axios';

export default {
    name:'MineralAnalysis',
    components: {
        MineralChart
    },
    data() {
        return {
            header: [],
            contens: {},
            one: {},
            tableData: [],
            test:[1,2,3,4,5,6,7,8,9,10],
            hashmap: undefined,
            tableHeader: [
                //{ id: 0, value: `name`, label: "矿物名称（计量单位）" },
                { id: 1, value: "2011", label: "2011年" },
                { id: 2, value: "2012", label: "2012年" },
                { id: 3, value: "2013", label: "2013年" },
                { id: 4, value: "2014", label: "2014年" },
                { id: 5, value: "2015", label: "2015年" },
                { id: 6, value: "2016", label: "2016年" },
                { id: 7, value: "2017", label: "2017年" },
                { id: 8, value: "2018", label: "2018年" },
                { id: 9, value: "2019", label: "2019年" },
            ],
            multipleSelection: [],
            search: "",
            currentPage: 1,
            name: "数据分析——矿产资源",
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
        this.hashmap = new Map([['bronze', '铜矿（万吨）'], ['coal', '煤炭（亿吨）'], ['FeS2', '硫铁矿（万吨）'],
        ['fossil_oil', '石油（亿吨）'], ['gas', '天然气（亿立方米）'], ['gold', '金矿（吨）'], ['iron', '铁矿（亿吨）'],
        ['lead', '铅矿（万吨）'], ['silver', '银矿（万吨）'], ['zinc', '锌矿（万吨）']])
        this.header = consts.getHeaderConfig("MineralAnalysis");
        this.page = consts.getPageConfig("two");
        // this.contens=Contents.getContent('table')
        // this.one=this.contens.one
        //this.getTableData();
        this.getPointsData();
                axios({
            method: 'get',
            url: 'http://localhost:8080/api/v1/mineralHistory',
        }).then(response => {
            this.tableData = response.data
            console.log(this.tableData)
            for(let i = 0; i < this.tableData.length; i++){
                this.tableData[i].name = this.hashmap.get(this.tableData[i].name)
            }
            this.$bus.$emit('MineralData',this.tableData)
        },
            error => {
                this.tableData = error.message
            });
    },
    mounted() {
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
                background-color: #fff;
            }
        }
    }
}
</style>

