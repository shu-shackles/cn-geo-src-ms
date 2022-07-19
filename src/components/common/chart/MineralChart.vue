<template>
    <div class="proCharts" ref='charts'>
    </div>
</template>
 
<script>
import echarts from 'echarts'
export default {
    data() {
        return {
            hashmap: undefined,
            showType: '煤炭',
            showData: [20, 20, 30, 50, 50, 60, 70, 80, 90],
            mineralData: []
        }
    },
    computed: {
        option() {
            return {
                animationDuration: 3000,
                color: ['#5470c6'],
                title: {
                    // 设置饼图标题，位置设为顶部居中
                    text: `2011-2019年全国${this.showType}资源探明储量折线图`,
                    top: "0%",
                    left: "center"
                },
                tooltip: { //提示框
                    trigger: 'axis',
                },
                grid: {
                    left: '10%',
                    right: '10%',
                    bottom: '3%',
                    top: '17%',
                    containLabel: true //grid区域是否包含坐标轴的刻度标签
                },
                xAxis: {
                    type: 'category', //坐标轴类型。
                    boundaryGap: true, //坐标轴两边留白策略
                    data: ['2011年', '2012年', '2013年', '2014年', '2015年', '2016年', '2017年', '2018年', '2019年'],
                    axisLabel: {//坐标轴刻度标签的相关设置
                        interval: 0,
                        textStyle: {
                            color: '#000',
                            fontSize: 10
                        },
                    },
                    axisLine: {//坐标轴轴线相关设置
                        show: true,
                        lineStyle: {
                            color: 'rgb(0,47,167)',
                            width: 2
                        }
                    },
                    axisTick: { //坐标轴刻度相关设置。
                        show: false,
                    }
                },
                yAxis: {
                    name: this.hashmap.get(this.showType),
                    type: 'value',
                    axisLabel: { //x轴的坐标文字
                        show: true,
                        textStyle: {
                            color: '#000' //文字的颜色
                        },

                    },
                    min: this.lowNum(this.showData[0]),
                    max: this.upNum(this.showData[this.showData.length - 1]),
                    axisLine: {//坐标轴轴线相关设置
                        show: true,
                        lineStyle: {
                            color: 'rgb(0,47,167)',
                            width: 2
                        }
                    },
                    axisTick: { //坐标轴刻度相关设置。
                        show: false,
                    },
                    splitLine: {  //坐标在grid区域的分割线
                        lineStyle: { //设置分割线的样式(图表横线颜色)
                            color: ['gray']
                        }
                    }
                },
                series: [
                    {
                        name: this.showType,
                        type: 'line',
                        data: this.showData,
                        lineStyle: {
                            color: '#5470c6'  //线的颜色
                        }
                    },
                ]
            }
        }
    },
    created() {
        this.hashmap = new Map([['铜矿', '万吨'], ['煤炭', '亿吨'], ['硫铁矿', '万吨'],
        ['石油', '亿吨'], ['天然气', '亿立方米'], ['金矿', '吨'], ['铁矿', '亿吨'],
        ['铅矿', '万吨'], ['银矿', '万吨'], ['锌矿', '万吨']])
    },
    mounted() {
        this.$bus.$on('MineralData', (data) => {
            this.mineralData = data
            this.getData()
            this.mycharts()
        })
        this.$bus.$on('MineralType', (data) => {
            this.showType = data.label
            this.getData()
            this.mycharts()
        })
    },
    beforeDestroy() {
        this.$bus.$off('MineralData')
        this.$bus.$off('MineralType')
    },
    methods: {
        mycharts() {
            let myChart = echarts.init(this.$refs.charts, "macarons");
            myChart.setOption(this.option)
            //图表自适应
            window.addEventListener("resize", function () {
                myChart.resize()  // myChart 是实例对象
            })
        },
        upNum(num) {
            num = parseInt(num)
            const bite = Math.pow(10, String(num).length - 1 || 1)
            return Math.ceil(num / bite) * bite
        },
        lowNum(num) {
            num = parseInt(num)
            const bite = Math.pow(10, String(num).length - 1 || 1)
            return Math.ceil(num / bite - 1) * bite
        },
        getData() {
            let showData = []
            for (let i = 0; i < this.mineralData.length; i++) {
                if (this.mineralData[i].name.indexOf(this.showType) != -1) {
                    showData.push(this.mineralData[i]['2011'])
                    showData.push(this.mineralData[i]['2012'])
                    showData.push(this.mineralData[i]['2013'])
                    showData.push(this.mineralData[i]['2014'])
                    showData.push(this.mineralData[i]['2015'])
                    showData.push(this.mineralData[i]['2016'])
                    showData.push(this.mineralData[i]['2017'])
                    showData.push(this.mineralData[i]['2018'])
                    showData.push(this.mineralData[i]['2019'])
                    break
                }
            }
            this.showData = showData;
        }
    }
}
</script>
 
<style scoped>
.proCharts {
    width: 100%;
    height: 400px;
    background: '#fff';
}
</style>