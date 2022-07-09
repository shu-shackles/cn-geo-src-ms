<template>
    <el-table :data="tableData" stripe style="width: 99%" :header-cell-style="{background:'#004d8c',color:'#FFFFFF',fontWeight:'bold'}">
        <el-table-column label="{矿物}资源排名前十省份" align="center">
            <el-table-column prop="date" label="排名" width="100" align="center">
            </el-table-column>
            <el-table-column prop="name" label="省份" width="100" align="center">
            </el-table-column>
            <el-table-column prop="address" label="含量" align="center">
            </el-table-column>
        </el-table-column>
    </el-table>
</template>

<script>
export default {
    name: "Rank",
    data() {
        return {
            tableData: [{
                date: '1',
                name: '上海市',
                address: '100000000'
            }, {
                date: '2',
                name: '上海市',
                address: '100000000'
            }, {
                date: '3',
                name: '上海市',
                address: '100000000'
            }, {
                date: '4',
                name: '上海市',
                address: '100000000'
            }, {
                date: '5',
                name: '上海市',
                address: '100000000'
            }, {
                date: '6',
                name: '上海市',
                address: '100000000'
            }, {
                date: '7',
                name: '上海市',
                address: '100000000'
            }, {
                date: '8',
                name: '上海市',
                address: '100000000'
            }, {
                date: '9',
                name: '上海市',
                address: '100000000'
            }, {
                date: '10',
                name: '上海市',
                address: '100000000'
            }]
        }
    }
}
</script>