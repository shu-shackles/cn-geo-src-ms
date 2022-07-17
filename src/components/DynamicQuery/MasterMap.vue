<template>
    <div id="chinaEcharts" ref="chinaEcharts" v-loading='loading' class="leftEcharts" style="height:100%;width: 100%">
    </div>
</template>

<script>
import '../../../static/map/china.js'
import echarts from 'echarts'
export default {
    name: 'MasterMap',
    data() {
        return {
            MineralType: '煤炭',
            MineralUnit: '亿吨',
            loading: false,
        };
    },
    props: ['MineralData'],
    watch: {
        MineralData() {
            this.chinaEcharts(this.MineralData, this.MineralData[0].value)
        }
    },
    mounted() {
        this.$bus.$on('MineralType', (data) => {
            this.MineralType = data.label
            this.MineralUnit = data.unit
        })
    },
    beforeDestroy() {
        this.$bus.$off('MineralType')
    },
    methods: {
        // 生成热力图
        chinaEcharts(dataList, maxNum) {
            let that = this;
            let myChart = echarts.init(document.getElementById('chinaEcharts'));
            let resizeTimer = null;
            let option = {
                title: {
                    text: `全国${this.MineralType}资源分布热力图`,
                    x: 'center',
                    textStyle: {
                        fontSize: 24
                    },
                },
                visualMap: {
                    left: 'left',
                    min: 0,
                    max: maxNum,
                    inRange: {
                        color: ['#e0ffff', '#006edd']
                    },
                    text: ['高', '低'],
                    calculable: true,
                    show: false
                },
                tooltip: {
                    trigger: 'item',
                    formatter: function (params) {
                        let toolTiphtml = ''
                        if (isNaN(params.value)) {
                            toolTiphtml = params.seriesName + '<br />' + params.name + '：' + '暂无数据'
                        }
                        else {
                            toolTiphtml = params.seriesName + '<br />' + params.name + '：' + params.value + that.MineralUnit
                        }
                        return toolTiphtml
                    }
                },
                toolbox: {
                    feature: {
                        saveAsImage: {}
                    }
                },
                series: [
                    {
                        name: `${this.MineralType}含量`,
                        id: 'forest',
                        type: 'map',
                        roam: false,
                        map: 'china',
                        animationDurationUpdate: 1000,
                        universalTransition: true,
                        data: dataList,
                        layoutCenter: ['30%', '30%'],
                        zoom: 1
                    }
                ]
            };
            myChart.setOption(option);
            window.addEventListener('resize', function () {
                if (resizeTimer) clearTimeout(resizeTimer);
                resizeTimer = setTimeout(function () {
                    myChart.resize();
                }, 100)
            })
        },
    }
};
</script>


<style>
</style>

