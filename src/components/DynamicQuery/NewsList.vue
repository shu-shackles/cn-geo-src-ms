<template>
    <div class="NewsList">
        <a-list item-layout="vertical" :pagination="pagination" :data-source="listData">
            <a-list-item slot="renderItem" key="item.title" slot-scope="item">
                <img slot="extra" width="272" alt="logo"
                    src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png" />
                <a-list-item-meta :description="item.description">
                    <a slot="title" :href="item.href">{{ item.title }}</a>
                </a-list-item-meta>
                {{ item.content }}
            </a-list-item>
        </a-list>
    </div>
</template>
<script>
const listData = [];
for (let i = 0; i < 23; i++) {
    listData.push({
        href: 'https://www.antdv.com/',
        title: `ant design vue part ${i}`,
        avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
        description:
            'Ant Design, a design language for background applications, is refined by Ant UED Team.',
        content:
            'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
    });
}

export default {
    data() {
        return {
            listData,
            pagination: {
                onChange: page => {
                    console.log(page);
                },
                pageSize: 3,
            },
            actions: [
                { type: 'star-o', text: '156' },
                { type: 'like-o', text: '156' },
                { type: 'message', text: '2' },
            ],
        };
    },
};
</script>
<style scoped>
.NewsList {
    width: auto;
    height: 100%;
    position: relative;
    text-align: left;
    margin-left:10px;
    margin-right: 10px;
}
</style>
