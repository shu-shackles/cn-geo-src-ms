<template>
    <div id="chinaEcharts" ref="chinaEcharts" v-loading='loading2' class="leftEcharts" style="height:100%;width: 100%;"></div>
</template>

<script>
// import { Province_count } from '@/api/api.js';
import '../../../static/map/china.js'
import echarts from 'echarts'
export default {
    name: 'MasterMap',
    data() {
        return {
            loading2: true,
            myData: {
                ReturnCode: 200,
                rows: [
                    { "name": "南海诸岛", "value": 0 },
                    { "name": "北京", "value": 1 },
                    { "name": "天津", "value": 2 },
                    { "name": "上海", "value": 3 },
                    { "name": "重庆", "value": 4 },
                    { "name": "河北", "value": 5 },
                    { "name": "河南", "value": 6 },
                    { "name": "云南", "value": 7 },
                    { "name": "辽宁", "value": 8 },
                    { "name": "黑龙江省", "value": 9 },
                    { "name": "湖南", "value": 10 },
                    { "name": "安徽", "value": 11 },
                    { "name": "山东", "value": 12 },
                    { "name": "新疆", "value": 13 },
                    { "name": "江苏", "value": 14 },
                    { "name": "浙江", "value": 15 },
                    { "name": "江西", "value": 16 },
                    { "name": "湖北", "value": 17 },
                    { "name": "广西", "value": 18 },
                    { "name": "甘肃", "value": 19 },
                    { "name": "山西", "value": 20 },
                    { "name": "内蒙古自治区", "value": 21 },
                    { "name": "陕西", "value": 22 },
                    { "name": "吉林", "value": 23 },
                    { "name": "福建", "value": 24 },
                    { "name": "贵州", "value": 25 },
                    { "name": "广东", "value": 26 },
                    { "name": "青海", "value": 27 },
                    { "name": "西藏", "value": 28 },
                    { "name": "四川", "value": 29 },
                    { "name": "宁夏回族自治区", "value": 30 },
                    { "name": "海南", "value": 31 },
                    { "name": "台湾", "value": 32 },
                    { "name": "香港", "value": 33 },
                    { "name": "澳门", "value": 34 }
                ]
            }
        };
    },
    mounted() {
        // 热力图
        this.getProvince_count()
    },
    methods: {
        getProvince_count() {
            // Province_count().then(res => {
            //     const { ReturnCode, Data } = res
            if (this.myData.ReturnCode == 200) {
                let maxNum = this.myData.rows[0].value
                for (const i in this.myData.rows) {
                    if (this.myData.rows[i].name == '内蒙古自治区') {
                        this.myData.rows[i].name = '内蒙古'
                    } else if (this.myData.rows[i].name == '宁夏回族自治区') {
                        this.myData.rows[i].name = '宁夏'
                    } else if (this.myData.rows[i].name == '黑龙江省') {
                        this.myData.rows[i].name = '黑龙江'
                    } else {
                        this.myData.rows[i].name = (this.myData.rows[i].name).substring(0, 2)
                    }
                }
                // for (const j in province) {
                //     for (const m in this.myData.rows) {
                //         if (province[j].name == this.myData.rows[m].name) {
                //             province[j].value = this.myData.rows[m].value
                //         }
                //     }
                // }
                this.chinaEcharts(this.myData.rows, maxNum)
            }
            this.loading2 = false
            // })
        },

        // 热力图
        chinaEcharts(dataList, maxNum) {
            // let this_ = this;
            let myChart = echarts.init(document.getElementById('chinaEcharts'));
            let resizeTimer = null;
            let option = {
                // tooltip: {
                //     formatter: function (params, ticket, callback) {
                //         return params.seriesName + '<br />' + params.name + '：' + params.value
                //     }//数据格式化
                // },
                // visualMap: {
                //     min: 0,
                //     max: maxNum,
                //     left: 'left',
                //     top: 'bottom',
                //     text: ['高', '低'],//取值范围的文字
                //     inRange: {
                //         color: ['#e0ffff', '#006edd']//取值范围的颜色
                //     },
                //     show: true//图注
                // },
                // geo: {
                //     map: 'china',
                //     roam: false,//不开启缩放和平移
                //     zoom: 1.23,//视角缩放比例
                //     label: {
                //         normal: {
                //             show: true,
                //             fontSize: '10',
                //             color: 'rgba(0,0,0,0.7)'
                //         }
                //     },
                //     itemStyle: {
                //         normal: {
                //             borderColor: 'rgba(0, 0, 0, 0.2)'
                //         },
                //         emphasis: {
                //             areaColor: '#F3B329',//鼠标选择区域颜色
                //             shadowOffsetX: 0,
                //             shadowOffsetY: 0,
                //             shadowBlur: 20,
                //             borderWidth: 0,
                //             shadowColor: 'rgba(0, 0, 0, 0.5)'
                //         }
                //     }
                // },
                // series: [
                //     {
                //         name: '信息量',
                //         type: 'map',
                //         geoIndex: 0,
                //         data: dataList
                //     }
                // ]
                title: {
                    text: `全国{矿物}资源分布热力图`,
                    x: 'center',
                    textStyle: {
                        fontSize: 24
                    },
                },
                visualMap: {
                    left: 'left',
                    min: 0,
                    max: 300000,
                    inRange: {
                        color: ['#FFFFBF', '#CAEB44', '#7ED756', '#0EC00B']
                    },
                    text: ['High', 'Low'],
                    calculable: true
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
                        name: '矿物含量',
                        id: 'forest',
                        type: 'map',
                        roam: true,
                        map: 'china',
                        animationDurationUpdate: 1000,
                        universalTransition: true,
                        data: this.myData.rows,
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

