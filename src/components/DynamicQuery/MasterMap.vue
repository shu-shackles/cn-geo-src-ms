<template>
    <div id="chinaEcharts" ref="chinaEcharts" v-loading='loading2' class="leftEcharts" style="height:100%;width: 100%">
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
            loading2: false,
        };
    },
    props: ['MineralData'],
    watch: {
        MineralType() {
            this.getProvince_count()
        }
    },
    mounted() {
        this.$bus.$on('MineralType', (data) => {
            this.MineralType = data
        })
        this.getProvince_count()
    },
    beforeDestroy() {
        this.$bus.$off('MineralType')
    },
    methods: {
        getProvince_count() {
            let maxNum = Math.max.apply(Math, this.MineralData.map(item => { return item.value }))
            this.chinaEcharts(this.MineralData, maxNum)
            this.loading2 = false
        },

        // 热力图
        chinaEcharts(dataList, maxNum) {
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
                },
                tooltip: {
                    trigger: 'item',
                    formatter: function (params) {
                        let toolTiphtml = ''
                        if (isNaN(params.value)) {
                            toolTiphtml = '暂无数据'
                        }
                        else {
                            toolTiphtml = params.seriesName + '<br />' + params.name + '：' + params.value
                            return toolTiphtml
                        }
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

