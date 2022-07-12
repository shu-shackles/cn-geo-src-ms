<template>
    <el-table :data="TableData" stripe style="width: 95%;margin-left: 15px;"
        :header-cell-style="{ background: '#004d8c', color: '#FFFFFF', fontWeight: 'bold' }">
        <el-table-column :label="title" align="center">
            <el-table-column prop="rank" label="排名" width="100" align="center">
            </el-table-column>
            <el-table-column prop="province" label="省份" width="150" align="center">
            </el-table-column>
            <el-table-column prop="value" :label="unit" align="center">
            </el-table-column>
        </el-table-column>
    </el-table>
</template>

<script>
export default {
    name: "Rank",
    data() {
        return {
            MineralType: '煤炭',
            MineralUnit: '亿吨',
            MineralData: []
        }
    },
    props: ['MineralData'],
    computed: {
        title() {
            return `${this.MineralType}资源排名前十省份`
        },
        unit() {
            return `含量（${this.MineralUnit}）`
        },
        TableData() {
            let data = this.MineralData
            data = data.slice(0, 10)
            for (let i = 0; i < data.length; i++) {
                data[i].rank = i + 1
            }
            return data
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
}
</script>