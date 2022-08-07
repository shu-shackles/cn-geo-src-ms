<template>
    <div class="NewsList">
        <a-spin v-if="loading"></a-spin>
        <template v-else>
            <a-list item-layout="vertical" :pagination="pagination" :data-source="listData">
                <a-list-item slot="renderItem" key="item.title" slot-scope="item">
                    <!-- <img slot="extra" width="240" alt="logo"
                        src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png" /> -->
                    <a-list-item-meta :description="item.date">
                        <a @click.prevent="openPage(item.url)" slot="title" :href="item.url">{{ item.title }}</a>
                    </a-list-item-meta>
                    {{ item['first paragraph'] }}
                </a-list-item>
            </a-list>
        </template>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    data() {
        return {
            listData: this.$store.state.news,
            pagination: {
                onChange: page => {
                    console.log(page);
                },
                pageSize: 3,
            },
            loading: true,
            queryString: '',
        };
    },
    mounted() {
        console.log(this.$store.state.news)
        if(!this.$store.state.news){
            this.update()
        }else{
            this.loading = false
        }
        this.$bus.$on('search', (data) => {
            this.queryString = data
            this.update()
        })
    },
    beforeDestroy() {
        this.$bus.$off('search')
    },
    methods: {
        openPage(url) {
            this.$bus.$emit('openPage', url)
        },
        update() {
            this.loading = true
            this.$bus.$emit('openPage', '')
            axios({
                method: 'get',
                url: 'http://localhost:8080/api/v1/news/title',
                params: { key: this.queryString, nums: 10 }
            }).then(response => {
                console.log(response.data)
                this.listData = response.data
                this.loading = false
            },
                error => {
                    this.listData = error.message
                });
        }
    }
};
</script>
<style scoped>
.NewsList {
    width: auto;
    height: 100%;
    position: relative;
    text-align: left;
    margin-left: 10px;
    margin-right: 10px;
}
</style>
