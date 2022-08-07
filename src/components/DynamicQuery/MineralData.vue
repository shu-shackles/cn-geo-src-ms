<template>
    <div class="survey_content2 clearfix">
        <headers :header="header" :name="name"></headers>
        <div class="contents clearfix">
            <div class="grahp">
                <div class="grahps1">
                    <MasterMap :MineralData="MineralData" />
                </div>
                <div class="grahps2">
                    <Rank :MineralData="MineralData" />
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import * as consts from "../../common/const";
import * as Contents from "../../common/content";
import MasterMap from "./MasterMap.vue"
import Rank from "./Rank.vue"
import axios from 'axios'

export default {
    components: {
        MasterMap,
        Rank
    },
    data() {
        return {
            header: [],
            name: "动态查询——矿物数据",
            page: {},
            query: 'coal(100M tons)',
            MineralData: []
        }
    },
    mounted() {
        this.$bus.$on('MineralType', (data) => {
            this.query = data.query
            axios({
                method: 'get',
                url: `http://localhost:8080/api/v1/mineralType`,
                params: { type: this.query }
            }).then(response => {
                console.log(response.data)
                this.MineralData = response.data
                for (let i = 0; i < this.MineralData.length; i++) {
                    this.MineralData[i].name = this.MineralData[i].province
                }
            },
                error => {
                    this.MineralData = error.message
                });
        })
    },
    created() {
        this.header = consts.getHeaderConfig("mineralData");
        this.page = consts.getPageConfig("one");
        this.getTableData();
        this.getPointsData();
    },
    beforeDestroy() {
        this.$bus.$off('MineralType')
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

