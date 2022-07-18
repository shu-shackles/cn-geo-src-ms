<template>
    <div class="echart" id="mychart" :style="myChartStyle"></div>
</template>

<script>
import * as echarts from "echarts";

export default {
    name: 'ForestChart',
    data() {
        return {
            myChart: {},
            tableData: [],
            forestType: '森林覆盖面积',
            myChartStyle: { float: "left", width: "100%", height: "400px", padding: "20px" } //图表样式
        };
    },
    computed: {
        pieData() {
            let pieData = []
            for (let i = 0; i < this.tableData.length; i++) {
                pieData[i] = {
                    'name': this.tableData[i]["省市或公司"],
                    'value': this.tableData[i][this.forestType]
                }
            }
            return pieData
        },
        pieName() {
            let pieName = []
            for (let i = 0; i < this.tableData.length; i++) {
                pieName[i] = this.tableData[i]["省市或公司"];
            }
            return pieName
        }
    },
    mounted() {
        this.$bus.$on('ForestData', (data) => {
            this.tableData = data
            this.initEcharts();
        })
        this.$bus.$on('ForestType', (data) => {
            this.forestType = data.label
            this.initEcharts();
        })
    },
    beforeDestroy() {
        this.$bus.$off('ForestData')
        this.$bus.$off('ForestType')
    },
    methods: {
        // initData() {
        //     console.log(this.tableData)
        //     for (let i = 0; i < this.tableData.length; i++) {
        //         console.log(this.tableData[i]["province/company"])
        //         this.pieName[i] = this.tableData[i]["province/company"];
        //         this.pieData[i].name = this.tableData[i]["province/company"];
        //         this.pieData[i].value = this.tableData[i]["forest coverage"];
        //     }
        // },
        initEcharts() {
            // 饼图
            const option = {
                legend: {
                    // 图例
                    data: this.pieName,
                    right: "10%",
                    top: "30%",
                    type: 'scroll',
                    orient: "vertical"
                },
                title: {
                    // 设置饼图标题，位置设为顶部居中
                    text: "第九次全国森林资源清查统计饼图",
                    top: "0%",
                    left: "center"
                },
                series: [
                    {
                        name: `${this.forestType}（单位:万公顷）`,
                        type: "pie",
                        label: {
                            show: true,
                            formatter: "{b}" // b代表名称，c代表对应值，d代表百分比
                        },
                        data: this.pieData,
                        radius: '55%',
                        //center: ['40%', '50%'],
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ],
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                },
                color: ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc']
            };
            console.log(this.seriesData);
            this.myChart = echarts.init(document.getElementById("mychart"));
            this.myChart.setOption(option);
            //随着屏幕大小调节图表
            window.addEventListener("resize", () => {
                this.myChart.resize();
            });
        }
    }
};
</script>

