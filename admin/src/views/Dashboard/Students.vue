<script setup lang="ts">
import { usePageInfoStore } from '@/stores/PageInfo';
const handleClick = () => {
    console.log('click')
}
const tableData = [
    {
        class: "1 班",
        number: "1",
        name: "彭家豪",
        sex: "男",
        account: "学生1",
        latest: '2024年3月1日14点52分',
    },
    {
        class: "1 班",
        number: "2",
        name: "王敏怡",
        sex: "女",
        account: "学生2",
        latest: '2024年2月29日12点02分',
    },
    {
        class: "1 班",
        number: "3",
        name: "张铎",
        sex: "男",
        account: "学生3",
        latest: '2024年2月28日11点08分',
    },
    {
        class: "1 班",
        number: "4",
        name: "许俊杰",
        sex: "男",
        account: "学生4",
        latest: '2024年2月29日15点12分',
    },
    {
        class: "1 班",
        number: "5",
        name: "李婧",
        sex: "女",
        account: "学生5",
        latest: '2024年3月1日14点52分',
    },
    {
        class: "1 班",
        number: "6",
        name: "刘紫怡",
        sex: "女",
        account: "学生6",
        latest: '2024年2月29日12点02分',
    },
    {
        class: "1 班",
        number: "7",
        name: "钟舒晴",
        sex: "女",
        account: "学生7",
        latest: '2024年2月28日11点08分',
    },
    {
        class: "1 班",
        number: "8",
        name: "张松",
        sex: "男",
        account: "学生8",
        latest: '2024年2月29日15点12分',
    },
    {
        class: "1 班",
        number: "9",
        name: "王敏怡",
        sex: "女",
        account: "学生9",
        latest: '2024年3月1日14点52分',
    },
    {
        class: "1 班",
        number: "10",
        name: "邹典苡",
        sex: "男",
        account: "学生10",
        latest: '2024年2月29日12点02分',
    },
    {
        class: "1 班",
        number: "11",
        name: "张晖",
        sex: "女",
        account: "学生11",
        latest: '2024年2月28日11点08分',
    },
    {
        class: "1 班",
        number: "12",
        name: "钱毓婷",
        sex: "女",
        account: "学生12",
        latest: '2024年2月29日15点12分',
    },
    {
        class: "1 班",
        number: "13",
        name: "李鸣涛",
        sex: "男",
        account: "学生13",
        latest: '2024年3月1日14点52分',
    },
    {
        class: "1 班",
        number: "14",
        name: "牛佳佳",
        sex: "男",
        account: "学生14",
        latest: '2024年2月29日12点02分',
    },
    {
        class: "1 班",
        number: "15",
        name: "瞿鑫亮",
        sex: "男",
        account: "学生15",
        latest: '2024年2月28日11点08分',
    }
]
let pageInfoStore = usePageInfoStore();
pageInfoStore.pageNameHint = "管 理 / 学生信息";
</script>

<template>
    <el-container>
        <el-main>
            <el-row>
                <el-col :span="24" class="toolBar">
                    <section class="title">
                        <span>学生信息</span>
                    </section>
                    <section class="tools">
                        <el-tooltip placement="top" transition="none" effect="light">
                            <template #content><span style="font-size: .9rem;">刷新</span></template>
                            <el-icon class="refreshBtn">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-ea893728="">
                                    <path fill="currentColor"
                                        d="M771.776 794.88A384 384 0 0 1 128 512h64a320 320 0 0 0 555.712 216.448H654.72a32 32 0 1 1 0-64h149.056a32 32 0 0 1 32 32v148.928a32 32 0 1 1-64 0v-50.56zM276.288 295.616h92.992a32 32 0 0 1 0 64H220.16a32 32 0 0 1-32-32V178.56a32 32 0 0 1 64 0v50.56A384 384 0 0 1 896.128 512h-64a320 320 0 0 0-555.776-216.384z">
                                    </path>
                                </svg>
                            </el-icon>
                        </el-tooltip>
                        <el-tooltip placement="bottom" transition="none" effect="light">
                            <template #content><span style="font-size: .9rem;">排序</span></template>
                            <el-icon class="refreshBtn">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-ea893728="">
                                    <path fill="currentColor"
                                        d="M384 96a32 32 0 0 1 64 0v786.752a32 32 0 0 1-54.592 22.656L95.936 608a32 32 0 0 1 0-45.312h.128a32 32 0 0 1 45.184 0L384 805.632zm192 45.248a32 32 0 0 1 54.592-22.592L928.064 416a32 32 0 0 1 0 45.312h-.128a32 32 0 0 1-45.184 0L640 218.496V928a32 32 0 1 1-64 0V141.248z">
                                    </path>
                                </svg>
                            </el-icon>
                        </el-tooltip>
                        <el-tooltip placement="top" effect="light" transition="none">
                            <template #content><span style="font-size: .9rem;">搜索</span></template>
                            <el-icon class="searchBtn">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-ea893728=""
                                    alt="sads">
                                    <path fill="currentColor"
                                        d="m795.904 750.72 124.992 124.928a32 32 0 0 1-45.248 45.248L750.656 795.904a416 416 0 1 1 45.248-45.248zM480 832a352 352 0 1 0 0-704 352 352 0 0 0 0 704">
                                    </path>
                                </svg>
                            </el-icon>
                        </el-tooltip>
                    </section>
                </el-col>
            </el-row>

            <el-row>
                <el-col>
                    <el-table :data="tableData" style="width: 100%">
                        <el-table-column prop="number" label="学号" width="120" />
                        <el-table-column prop="class" label="班级" width="250" />
                        <el-table-column prop="name" label="姓名" width="220" />
                        <el-table-column prop="sex" label="性别" width="220" />
                        <el-table-column prop="account" label="用户名" width="210" />
                        <el-table-column prop="latest" label="最后登录时间" width="260" />
                        <el-table-column fixed="right" label="操作" width="200">
                            <template #default>
                                <el-button link type="primary" size="small" @click="handleClick">更 多</el-button>
                                <el-button link type="primary" size="small">编 辑</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </el-col>
            </el-row>

            <el-row>
                <el-col :span="24">
                    <el-pagination background layout="prev, pager, next" :total="1000" />
                </el-col>
            </el-row>
        </el-main>
    </el-container>
</template>

<style scoped>
.el-col {
    margin-bottom: 20px;
}

.el-table {
    border-radius: 3px;
}

.el-pagination {
    display: flex;
    justify-content: center;
}

.toolBar {
    background-color: #ffffff;
    height: 60px;
    border-radius: 3px;
    padding: 15px;
    color: #909399;
    user-select: none;
    display: flex;
    justify-content: space-between;
}

section.title,
section.tools {
    display: flex;
    align-items: center;
    align-content: center;
    height: 100%;
}

.toolBar .el-icon {
    margin-left: 15px;
    transform: scale(1.5);
    color: rgb(148, 148, 148);
    margin-right: 15px;
    cursor: pointer;
}

.el-tooltip {
    font-size: 2px !important;
}</style>