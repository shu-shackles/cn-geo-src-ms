<template>
  <div class="x-bar text-center flex-center-center">
    <div></div>
  </div>
</template>

<script>
import HighCharts from "highcharts";

// import * as queryUtil from '../../../common/query'

export default {
  props: {
    options: Object
  },
  data() {
    return {
      chart: null
    };
  },
  computed: {},
  watch: {},
  mounted() {
    console.log(this.options);
    this.$nextTick(() => {
      this.init();
    });
  },
  methods: {
    setGlop() {
      HighCharts.setOptions({
        colors: [
          "#A39FFE",
          "#FF79C4",
          "#4ED9FF",
          "#FFDB7D",
          "#FF826F",
          "#58E49F",
          "#FFBD71",
          "#C5E778",
          "#7DC6FD",
          "#F1D69A",
          "#FCB9D8",
          "#E4DAA4"
        ],
        title: {
          text: ""
        },
        subtitle: {
          text: ""
        },
        credits: {
          enabled: false
        },
        lang: {
          noData: "暂无数据"
        },
        noData: {
          style: {
            fontWeight: "bold",
            fontSize: "14px",
            color: "#CCCCCC"
          }
        },
        tooltip: {
          crosshairs: true,
          shared: true,
          useHTML: true,
          style: {
            padding: 0,
            borderWidth: 0,
            backgroundColor: "#FFF"
          },
          footerFormat: "</table>",
          valueDecimals: 0
        },
        loading: {
          hideDuration: 0,
          showDuration: 0,
          labelStyle: {
            color: "#3B86FF",
            fontWeight: "bold",
            fontSize: "14px",
            width: "100%",
            height: "100%",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            top: "0"
          }
        }
      });
    },
    getChart() {
      return this.chart;
    },
    init() {
      const self = this;
      self.setGlop();
      let chartInstance = self.highCharts || HighCharts;
      self.chart = new chartInstance.Chart(self.$el, self.options, function(c) {
        // 饼图
        // c.series[0].data[4].push()
        // setTimeout(function () {
        // }, 1000)
        // console.log(c.series[0].data[4])
        // if (self.options.chart.type && self.options.chart.type === 'pie') {
        //   let centerY = c.series[0].center[1]
        //   let titleHeight = parseInt(c.title.styles.fontSize)
        //   // // 动态设置标题位置
        //   if (Number.parseInt(self.tag) === 1) {
        //     c.setTitle({
        //         y: centerY + titleHeight/2,
        //         x: -95
        //     })
        //   } else {
        //     c.setTitle({
        //         y:centerY + titleHeight/2,
        //         x: -55
        //     })
        //   }
        // }
      });
    },
    addMethod(name, ...arg) {
      if (!this.getChart()) {
        return;
      }
      return this.getChart()[name](...arg, false);
    },
    // lineCharts.addMethod('showLoading', '数据正在加载中...'),
    showLoading(txt) {
      // this.getChart().showLoading()
      // console.log(this.getChart()[showLoading])
    },
    hideLoading() {
      this.getChart().hideLoading();
    }
  },

  beforeDestroy() {
    if (this.getChart()) {
      this.getChart().destroy();
    }
  }
};
</script>

<style lang="less" scoped>
.x-bar {
  .font-theme {
    cursor: pointer;
    font-size: 16px;
  }
}
.className {
  width: 100%;
}
</style>