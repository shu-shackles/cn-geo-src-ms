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
            pieData: [
                {
                    value: 463,
                    name: "江苏"
                },
                {
                    value: 395,
                    name: "浙江"
                },
                {
                    value: 157,
                    name: "山东"
                },
                {
                    value: 149,
                    name: "广东"
                },
                {
                    value: 147,
                    name: "湖南"
                }
            ],
            pieName: [],
            myChartStyle: { float:"left", width: "100%", height: "400px", } //图表样式
        };
    },
    mounted() {
        this.initDate(); //数据初始化
        this.initEcharts();
    },
    methods: {
        initDate() {
            for (let i = 0; i < this.pieData.length; i++) {
                this.pieName[i] = this.pieData[i].name;
            }
        },
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
                    text: "全国森林资源分布饼图",
                    top: "5%",
                    left: "center"
                },
                series: [
                    {
                        name: '森林面积',
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

