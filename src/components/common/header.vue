<template>
    <div class="title">
        <div :class="'nav_title clearfix left1'">
            <p class='survey'>{{ name }}</p>
            <div class='content'>
                <div class="float_left" v-if="headerShow[0]">
                    <span>类型：</span>
                    <el-select size="medium" v-model="queryData.tableType" @change="changeTableType">
                        <el-option v-for="item in TableTypeList" :key="item.value" :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>
                </div>
                <div class="float_left" v-if="headerShow[1]">
                    <el-autocomplete type="text" v-model="queryString" :fetch-suggestions="querySearch"
                        placeholder="请输入搜索内容" @select="handleSelect" @change="handleChange" clearable="true"
                        onkeypress="if(window.event.keyCode==13) this.blur()" ref="autocomplete"
                        @keyup.enter.native="handleChange" prefix-icon="el-icon-search"></el-autocomplete>
                </div>
                <div class="float_left" v-if="headerShow[2]">
                    <span>类型：</span>
                    <el-select size="medium" style="width:200px;" v-model="queryData.forestType" @change="changeForestType">
                        <el-option v-for="item in ForestTypeList" :key="item.value" :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import * as consts from '../../common/const'
import * as util from '../../common/util'

export default {
    props: {
        header: [Object],
        name: [String]
    },
    data() {
        return {
            query: {
                time: [],
                time_contrast: []
            },
            time: '',
            queryData: {
                projectId: 1,
                tableType: 0,
                forestType: 0,
                compareTableType: null
            },
            projectList: [],
            pointList: [],
            initPoint: [3, 30],
            TableTypeList: [],
            ForestTypeList:[],
            headerShow: [],
            switchStatus: false,
            contrastStatus: false,
            checkId: 1,
            options: [{
                value: 1,
                label: '时间'
            }, {
                value: 2,
                label: '类型'
            }, {
                value: 3,
                label: '监测点'
            }
            ],
            checked: [true, false, false, false, false],
            showPick: false,
            timeVal: '',
            queryString: '',
        }
    },
    computed: {
        pickerOptions() {
            return util.pickerdisabled
        },
        showMenu() {
            return this.$store.state.menu.showMenu
        },
    },
    created() {
        if (this.$route.params.projectId !== undefined) {
            this.queryData.projectId = this.$route.params.projectId
        }
        this.getProject()
        this.headerShow = this.header.headerShow
        this.contrastStatus = this.header.contrast
        this.changeStart()
    },
    watch: {
    },
    mounted() {
        this.$nextTick(() => {
            this.changeTableType();
        });
    },
    methods: {
        getProject() {
            this.projectList = consts.Project
            this.pointList = consts.Points
            this.TableTypeList = consts.TableType
            this.ForestTypeList = consts.ForestType
        },
        changeProject(v) {
            console.log(v);
        },
        // 改变表格类型
        changeTableType() {
            this.$bus.$emit('MineralType', this.TableTypeList[this.queryData.tableType])
        },
        changeForestType(){
            this.$bus.$emit('ForestType', this.ForestTypeList[this.queryData.forestType])
        },
        // 改变对比表格类型
        changeTable_other() { },
        changePoint() { },
        onContrast(val) {
            this.showPick = !val
        },
        updateCheck(index) {
            this.checkId = index
            this.checked = this.checked.map(() => false)
            this.checked.splice(index - 1, 1, true)
            this.showPick = false

        },
        changeEnd() {
            this.showPick = true
        },
        changeStart() {
            let a = new Date()

        },
        changeTime(v) {
            console.log(v, 8);
        },
        submitUpload() {
            this.$refs.upload.submit();
        },
        querySearch(queryString, cb) {
            var historyList = JSON.parse(sessionStorage.getItem('historyList'));
            var results = queryString ? historyList.filter(this.createFilter(queryString)) : historyList;
            // 调用 callback 返回建议列表的数据
            cb(results);
        },
        createFilter(queryString) {
            return (historyList) => {
                return (historyList.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
            };
        },
        handleSelect(item) {
            this.$bus.$emit('search', item.value)
            this.queryString = ''
        },
        handleChange() {
            var historyList = JSON.parse(sessionStorage.getItem('historyList'));
            let p = { value: this.queryString }
            historyList.push(p)
            historyList = historyList.reduce((cur, next) => {
                historyList[next.value] ? "" : historyList[next.value] = true && cur.push(next);
                return cur;
            }, [])
            sessionStorage.setItem('historyList', JSON.stringify(historyList))
            this.$bus.$emit('search', this.queryString)
            this.queryString = ''
            this.$refs.autocomplete.suggestions = []
        }
    }
}
</script>

<style lang="less" scoped>
@import '../../../static/css/clear';
@import '../../../static/css/common';

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

.title {
    height: 80px;
    width: 100%;
    background-color: #fff;
}

.left1 {
    left: 160px;
}

.left2 {
    left: 30px;
}

.nav_title {
    position: absolute;
    left:160px;
    width:85%;
    top: 0;
    right: 0;
    z-index: 99;
    background-color: #fff;

    .survey {
        text-align: left;
        padding: 10px 10px 18px;
        font-weight: 900;
        font-size: 14px;
    }

    .content {
        height: 30px;
        font-size: 12px;

        .upload {
            margin-right: 20px;
            position: fixed;
        }

        .el-select {
            width: 120px;
        }

        .float_left {
            float: left;
            padding-left: 15px;
            padding-bottom: 6px;

            .el-cascader {
                width: 166px;
            }
        }

        .float_right {
            float: right;
            right: 20px;
        }

        .el-date-editor--datetimerange.el-input,
        .el-date-editor--datetimerange.el-input__inner {
            width: 174px;
        }

        .padding-right-md {
            padding-right: 20px;
        }

        .slide-fade-enter-active {
            transition: all .3s ease;
        }

        .slide-fade-leave-active {
            transition: all .3s ease;
        }

        .slide-fade-enter,
        .slide-fade-leave-to {
            transform: translateX(20px);
            opacity: 0;
        }

    }
}
.el-upload-list {
    background-color: #fff;
}

.el-date-range-picker__time-header {
    display: none;
}

.el-picker-panel .el-date-range-picker .el-popper has-time {
    top: 65px;
}

.el-date-range-picker {
    width: 414px;
}

.el-input--small {
    font-size: 10px;
}

.el-date-range-picker__content {
    width: 50%;
    padding: 7px;
}

.el-date-range-picker__header {
    height: 20px;
}

.el-date-range-picker__header div {
    font-size: 12px;
}

.el-picker-panel__icon-btn {
    margin-top: 0px;
}

.el-date-table {
    font-size: 10px;
}

.el-date-table td,
.el-date-table td div {
    height: 20px;
}

.el-date-table td {
    padding: 2px 0;
}

.el-date-table td div {
    padding: 0px;
}

.el-date-table td span {
    width: 20px;
    height: 20px;
    line-height: 20px;
}

.el-picker-panel__footer {
    padding: 2px;
}

.el-date-range-picker .el-picker-panel__body {
    min-width: 0px;
}

.el-time-panel {
    width: 100px;
}

.el-time-spinner__item {
    font-size: 10px;
}

.el-select-dropdown__item {
    font-size: 12px;
}

.el-select-dropdown {
    min-width: 120px !important;
}

.el-cascader-panel {
    font-size: 12px;
}

.el-cascader-menu {
    min-width: 130px;
}

.el-cascader-node {
    height: 25px;
    line-height: 25px;
}

.el-cascader {
    width: 130px;
}

.el-range-editor--mini .el-range__close-icon,
.el-range-editor--mini .el-range__icon {
    display: none;
}

.el-date-editor .el-range-input {
    width: 44%;
}
</style>

