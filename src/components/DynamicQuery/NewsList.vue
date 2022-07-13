<template>
    <div class="NewsList">
        <a-spin v-if="loading"></a-spin>
        <template v-else>
            <a-list item-layout="vertical" :pagination="pagination" :data-source="listData">
                <a-list-item slot="renderItem" key="item.title" slot-scope="item">
                    <img slot="extra" width="240" alt="logo"
                        src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png" />
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
// const listData = [];
// for (let i = 0; i < 23; i++) {
//     listData.push({
//         href: 'https://www.antdv.com/',
//         title: `ant design vue part ${i}`,
//         avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
//         description:
//             'Ant Design, a design language for background applications, is refined by Ant UED Team.',
//         content:
//             'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
//     });
// }

export default {
    data() {
        return {
            listData: [],
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
        this.update()
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
                url: 'http://localhost:8080/api/v1/news/geological_survey',
                params: { key: this.queryString, nums: 5, pages: 1 }
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
