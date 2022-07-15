<template>
    <div class="a" id='allmap' style="overflow: hidden" >
        <sider></sider>
        <baidu-map style="margin-left:160px;" :class="'hello flex10'" :zoom="zoom" @ready="handler" center="延安"
            :scroll-wheel-zoom="true">
            <TagForm/>
            <div class="float_left">
                <el-select size="mini" style="position:absolute;left:200px;top:20px;" v-model="searchName"
                    @change="changeType" placeholder="请选择标记类型">
                    <el-option v-for="item in type" :key="item.value" :label="item.label" :value="item.value">
                    </el-option>
                </el-select>
            </div>
            <bm-geolocation anchor="BMAP_ANCHOR_TOP_LEFT" :showAddressBar="true" :autoLocation="true"></bm-geolocation>
            <bm-map-type :map-types="['BMAP_NORMAL_MAP', 'BMAP_HYBRID_MAP']" anchor="BMAP_ANCHOR_BOTTOM_RIGHT">
            </bm-map-type>
            <div v-for="item in projects" :key='item.id'>
                <bm-marker :position="{ lng: item.lng, lat: item.lat }" @click="infoWindowOpen(item.id)"
                    :icon="{ url: item.url, size: { width: 32, height: 32 } }">
                    <bm-label :content="item.title" :labelStyle="{ color: 'red', fontSize: '12px' }"
                        :offset="{ width: 0, height: 32 }" />
                    <bm-info-window :show="item.show" style="width:150px;" @open="infoWindowOpen(item.id)"
                        @close="infoWindowClose(item.id)">
                        <el-descriptions :title="item.title" :column="1" size="mini" style="width:150%;">
                            <el-descriptions-item label="类型">{{ item.enentype }}</el-descriptions-item>
                            <el-descriptions-item label="时间">{{ item.time }}</el-descriptions-item>
                            <el-descriptions-item label="描述">{{ item.tag_sesc }}
                            </el-descriptions-item>
                            <el-descriptions-item label="图片"><img src="../../assets/images/25771966_214139380083_2.jpg"
                                    style="width:175px;height:100px;" alt="" /></el-descriptions-item>
                        </el-descriptions>
                    </bm-info-window>
                </bm-marker>
            </div>
        </baidu-map>
        <div class="jwd">
            经度：{{ lng }} ， 纬度：{{ lat }}
        </div>
    </div>
</template>
<script>
import TagForm from './TagForm.vue'
import axios from 'axios'
export default {
    name: "index",
    data() {
        return {
            map: null,
            lng: '',
            lat: '',
            zoom: 5.5,
            searchName: "全部",
            type: [{ value: '全部', label: '全部' },
            { value: '动物', label: '动物' },
            { value: '植物', label: '植物' },
            { value: '景观', label: '景观' },
            { value: '矿物', label: '矿物' },
            { value: '事件', label: '事件' },
            { value: '其他', label: '其他' }],
            projectPoints: [],
            projects: [],
        };
    },
    created() {

    },
    mounted() {
        window.sessionStorage.setItem('historyList', JSON.stringify([]))
        var that = this
        var projectPoints = []
        axios.post('http://localhost:8080/api/v1/areatags/全部')
            .then(function (response) {
                projectPoints = response.data
                for (let i = 0; i < projectPoints.length; i++) {
                    projectPoints[i].show = false
                    projectPoints[i].id = i
                    projectPoints[i].time = projectPoints[i].time.replace('T', ' ')
                    if(projectPoints[i].enentype==='动物'){
                        projectPoints[i].url = require('@/assets/images/ico1.png')
                    } else if(projectPoints[i].enentype==='植物'){
                        projectPoints[i].url = require('@/assets/images/ico2.png')
                    } else if(projectPoints[i].enentype==='景观'){
                        projectPoints[i].url = require('@/assets/images/ico3.png')
                    } else if(projectPoints[i].enentype==='矿物'){
                        projectPoints[i].url = require('@/assets/images/ico4.png')
                    } else if(projectPoints[i].enentype==='事件'){
                        projectPoints[i].url = require('@/assets/images/ico5.png')
                    } else if(projectPoints[i].enentype==='其他'){
                        projectPoints[i].url = require('@/assets/images/ico6.png')
                    }
                }
                that.projectPoints = projectPoints;
                that.projects = projectPoints;
            })
            .catch(function (error) {
                that.projectPoints = error.message
                that.projects = error.message
            });
    },
    watch: {},
    methods: {
        changeType() {
            this.projects = []
            for (let i = 0; i < this.projectPoints.length; i++) {
                this.projectPoints[i].show = false
                if (this.projectPoints[i].enentype === this.searchName || this.searchName === '全部') {
                    this.projects.push(this.projectPoints[i])
                }
            }
        },
        infoWindowOpen(id) {
            for (let i = 0; i < this.projects.length; i++) {
                if (this.projects[i].id === id) {
                    this.projects[i].show = true
                    return
                }
            }
        },
        infoWindowClose(id) {
            for (let i = 0; i < this.projects.length; i++) {
                if (this.projects[i].id === id) {
                    this.projects[i].show = false
                    return
                }
            }
        },
        handler({ map }) {
            this.map = map;
            map.addEventListener("mousemove", (e) => {
                this.lng = e.point.lng.toFixed(2) + "°";
                this.lat = e.point.lat.toFixed(2) + "°";
            });
        },
    },
    components: { TagForm }
}
</script>
<style scoped lang="less">
@import '../../../static/css/clear';
@import '../../../static/css/common';

.float_left {
    float: left;
    padding-left: 15px;
    padding-bottom: 6px;
}

.a {
    position: relative;
    margin: 0;
    height: 100%;
    width: 100%;
    display: flex;

    .hello {
        // position: absolute;
        height: 100%;
        // width: 90%;
        right: 0;
        // flex: 0.9;
        // float: right;
        // width: 100%;
    }

    .search {
        position: absolute;
        top: 10px;
        right: 10px;
        width: 350px;
    }

    .searchResult {
        position: absolute;
        top: 60px;
        right: 10px;
        width: 350px;

        .texts {
            overflow: hidden;
            height: 300px;
            text-overflow: ellipsis;
            text-indent: 25px;
            text-align: left;
            padding: 0 10px;
        }

        .more {
            color: #71a8e0;
            float: right;
            margin-right: 10px;
        }

        .words {
            text-align: left;
            height: 300px;
            overflow: auto;

            .wordsUl {
                height: 15px;
                padding: 0 30px;

                a {
                    color: #606266;
                }
            }
        }

        .imgs {
            float: left;
            list-style: none;
            height: 200px;

            .imgUl {
                list-style: none;
                float: left;
                padding: 0 8px;

                img {
                    width: 100px;
                    height: 50px;
                }
            }
        }


    }

    .jwd {
        position: absolute;
        right: 150px;
        bottom: 10px;
    }

}

.el-collapse-item__header {
    color: #71a8e0;
    font-size: 14px;
    padding: 0 10px;
}
</style>

