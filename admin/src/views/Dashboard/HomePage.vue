<script setup lang="ts">
import { usePageInfoStore } from '@/stores/PageInfo';
import { ref, onMounted } from 'vue';
import * as echarts from 'echarts';
import { he } from 'element-plus/es/locales.mjs';
let pageInfoStore = usePageInfoStore();
pageInfoStore.pageNameHint = "首 页";

onMounted(() => {
    const chart = document.getElementById("chart");
    const myChart = echarts.init(chart);
    let option = {
        xAxis: {
            type: 'category',
            data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        },
        yAxis: {
            type: 'value',
        },
        textStyle: {
            fontFamily: "San Francisco Pro"
        },
        title: {
            text: "各项运动打卡情况"
        },
        legend: {
            x: 'center',
            y: 'top'
        },
        series: [
            {
                data: [820, 932, 901, 934, 1290, 1330, 1320],
                type: 'line',
                smooth: true,
                name: '引体向上',
                lineStyle: {
                    normal: {
                        type: "linear",
                        x: 0,
                        y: 0,
                        x2: 0,
                        y2: 1,
                        colorStop: [
                            {
                                offset: 0,
                                color: "#34A3E5",
                            },
                            {
                                offset: 1,
                                color: "#934CD5",
                            },
                        ],
                        global: false,
                    }
                }
            },
            {
                data: [220, 123, 564, 657, 1234, 1678, 1132],
                type: 'line',
                smooth: true,
                name: '实心球'
            },
            {
                data: [123, 432, 542, 666, 689, 890, 1022],
                type: 'line',
                smooth: true,
                name: '立定跳远'
            },
            {
                data: [103, 232, 142, 556, 789, 560, 652],
                type: 'line',
                smooth: true,
                name: '仰卧起坐'
            }
        ],
        grid: {
            show: true
        },
        areaStyle: {
            normal: {
                type: "linear",
                x: 0,
                y: 0,
                x2: 0,
                y2: 1,
                colorStop: [
                    {
                        offset: 0,
                        color: "#CAE7F8",
                    },
                    {
                        offset: 1,
                        color: "#E3D1F4",
                    },
                ],
                global: false,
            }
        }
    };
    option && myChart.setOption(option);

    window.onresize = myChart.resize;
})

</script>

<template>
    <el-container>
        <el-container class="container">
            <el-main class="homepage-main-content" style="overflow: hidden; height: 100%;">

                <el-row :gutter="20" type="flex">
                    <el-col :span="12">
                        <el-card style="width: 100%; box-shadow: none; height:100%">
                            <template #header>
                                <div class="card-header">
                                    <span>快捷访问</span>
                                </div>
                            </template>

                            <el-row :gutter="20" class="shortcut">

                                <el-col :span="6">
                                    <el-card shadow="hover" class="shorcut-icon-wrapper">
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"
                                            data-v-ea893728="" class="shortcut-icon">
                                            <path fill="currentColor"
                                                d="M512 128 128 447.936V896h255.936V640H640v256h255.936V447.936z">
                                            </path>
                                        </svg>
                                        <p class="shorcut-caption">首 页</p>
                                    </el-card>
                                </el-col>

                                <el-col :span="6">
                                    <el-card shadow="hover" class="shorcut-icon-wrapper">
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"
                                            data-v-ea893728="" class="shortcut-icon">
                                            <path fill="currentColor"
                                                d="M288 320a224 224 0 1 0 448 0 224 224 0 1 0-448 0m544 608H160a32 32 0 0 1-32-32v-96a160 160 0 0 1 160-160h448a160 160 0 0 1 160 160v96a32 32 0 0 1-32 32z">
                                            </path>
                                        </svg>
                                        <p class="shorcut-caption">账号设置</p>
                                    </el-card>
                                </el-col>

                                <el-col :span="6">
                                    <el-card shadow="hover" class="shorcut-icon-wrapper">
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"
                                            data-v-ea893728="" class="shortcut-icon">
                                            <path fill="currentColor"
                                                d="M416 896V128h192v768zm-288 0V448h192v448zm576 0V320h192v576z"></path>
                                        </svg>
                                        <p class="shorcut-caption">数据总览</p>
                                    </el-card>
                                </el-col>

                                <el-col :span="6">
                                    <el-card shadow="hover" class="shorcut-icon-wrapper">
                                        <svg t="1709862126288" class="shortcut-icon" viewBox="0 0 1024 1024"
                                            version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4353">
                                            <path
                                                d="M388.096 301.056a122.88 121.856 0 1 0 245.76 0 122.88 121.856 0 1 0-245.76 0Z"
                                                fill="#333333" p-id="4354"></path>
                                            <path
                                                d="M510.976 464.896c-77.824 0-141.312 63.488-141.312 141.312v239.616h282.624V606.208c0-77.824-63.488-141.312-141.312-141.312z"
                                                fill="#333333" p-id="4355"></path>
                                            <path
                                                d="M806.912 369.664m-95.232 0a95.232 95.232 0 1 0 190.464 0 95.232 95.232 0 1 0-190.464 0Z"
                                                fill="#333333" p-id="4356"></path>
                                            <path
                                                d="M806.912 502.784c-63.488 0-114.688 51.2-114.688 114.688v190.464H921.6V617.472c0-63.488-51.2-114.688-114.688-114.688z"
                                                fill="#333333" p-id="4357"></path>
                                            <path
                                                d="M217.088 369.664m-95.232 0a95.232 95.232 0 1 0 190.464 0 95.232 95.232 0 1 0-190.464 0Z"
                                                fill="#333333" p-id="4358"></path>
                                            <path
                                                d="M217.088 502.784c-63.488 0-114.688 51.2-114.688 114.688v190.464h228.352V617.472c0-63.488-51.2-114.688-113.664-114.688z"
                                                fill="#333333" p-id="4359"></path>
                                        </svg>
                                        <p class="shorcut-caption">学生管理</p>
                                    </el-card>
                                </el-col>
                            </el-row>

                            <el-row :gutter="20" class="shortcut">
                                <el-col :span="6">
                                    <el-card shadow="hover" class="shorcut-icon-wrapper">
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"
                                            data-v-ea893728="" class="shortcut-icon">
                                            <path fill="currentColor"
                                                d="M764.416 254.72a351.68 351.68 0 0 1 86.336 149.184H960v192.064H850.752a351.68 351.68 0 0 1-86.336 149.312l54.72 94.72-166.272 96-54.592-94.72a352.64 352.64 0 0 1-172.48 0L371.136 936l-166.272-96 54.72-94.72a351.68 351.68 0 0 1-86.336-149.312H64v-192h109.248a351.68 351.68 0 0 1 86.336-149.312L204.8 160l166.208-96h.192l54.656 94.592a352.64 352.64 0 0 1 172.48 0L652.8 64h.128L819.2 160l-54.72 94.72zM704 499.968a192 192 0 1 0-384 0 192 192 0 0 0 384 0">
                                            </path>
                                        </svg>
                                        <p class="shorcut-caption">系统设置</p>
                                    </el-card>
                                </el-col>
                                <el-col :span="6">
                                    <el-card shadow="hover" class="shorcut-icon-wrapper">
                                        <svg t="1709862315390" viewBox="0 0 1024 1024" version="1.1"
                                            xmlns="http://www.w3.org/2000/svg" p-id="7235" class="shortcut-icon">
                                            <path
                                                d="M871.616 64H152.384c-31.488 0-60.416 25.28-60.416 58.24v779.52c0 32.896 26.24 58.24 60.352 58.24h719.232c34.112 0 60.352-25.344 60.352-58.24V122.24c0.128-32.96-28.8-58.24-60.288-58.24zM286.272 512c-23.616 0-44.672-20.224-44.672-43.008 0-22.784 20.992-43.008 44.608-43.008 23.616 0 44.608 20.224 44.608 43.008A43.328 43.328 0 0 1 286.272 512z m0-202.496c-23.616 0-44.608-20.224-44.608-43.008 0-22.784 20.992-43.008 44.608-43.008 23.616 0 44.608 20.224 44.608 43.008a43.456 43.456 0 0 1-44.608 43.008zM737.728 512H435.904c-23.68 0-44.672-20.224-44.672-43.008 0-22.784 20.992-43.008 44.608-43.008h299.264c23.616 0 44.608 20.224 44.608 43.008a42.752 42.752 0 0 1-41.984 43.008z m0-202.496H435.904c-23.616 0-44.608-20.224-44.608-43.008 0-22.784 20.992-43.008 44.608-43.008h299.264c23.616 0 44.608 20.224 44.608 43.008a42.88 42.88 0 0 1-42.048 43.008z"
                                                p-id="7236"></path>
                                        </svg>
                                        <p class="shorcut-caption">系统日志</p>
                                    </el-card>
                                </el-col>
                                <el-col :span="6">
                                    <el-card shadow="hover" class="shorcut-icon-wrapper">
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"
                                            data-v-ea893728="" class="shortcut-icon">
                                            <path fill="currentColor"
                                                d="M640 832a128 128 0 0 1-256 0zm192-64H134.4a38.4 38.4 0 0 1 0-76.8H192V448c0-154.88 110.08-284.16 256.32-313.6a64 64 0 1 1 127.36 0A320.128 320.128 0 0 1 832 448v243.2h57.6a38.4 38.4 0 0 1 0 76.8z">
                                            </path>
                                        </svg>
                                        <p class="shorcut-caption">消息通知</p>
                                    </el-card>
                                </el-col>
                            </el-row>

                        </el-card>
                    </el-col>

                    <el-col :span="12">
                        <el-card style="width: 100%; box-shadow: none; height: 100%;" class="system-info">
                            <template #header>
                                <div class="card-header">
                                    <span>系统信息</span>
                                </div>
                            </template>
                            <el-row :gutter="20">
                                <el-col :span="12">
                                    <el-card shadow="never">
                                        <span class="system-info-item-caption">上次登录时间</span>
                                        <span class="system-info-display">4分钟前</span>
                                    </el-card>
                                </el-col>
                                <el-col :span="12">
                                    <el-card shadow="never">
                                        <span class="system-info-item-caption">学生总数</span>
                                        <span class="system-info-display">167</span>
                                    </el-card>
                                </el-col>
                            </el-row>
                            <el-row :gutter="20">
                                <el-col :span="12">
                                    <el-card shadow="never">
                                        <span class="system-info-item-caption">学生打卡总次数</span>
                                        <span class="system-info-display">721</span>
                                    </el-card>
                                </el-col>
                                <el-col :span="12">
                                    <el-card shadow="never">
                                        <span class="system-info-item-caption">体育锻炼总体情况</span>
                                        <span class="system-info-display">合格</span>
                                    </el-card>
                                </el-col>
                            </el-row>
                        </el-card>
                        <div style="clear: both"></div>
                    </el-col>

                </el-row>

                <el-row class="chart-row" type="flex">
                    <el-col class="chart-col">
                        <div ref="chart" class="chart-wrapper">
                            <div id="chart"></div>
                        </div>
                        <div style="clear: both;"></div>
                    </el-col>

                </el-row>

            </el-main>

            <el-aside width="350px" class="aside-dynamics">
                <el-card style="max-width: 480px" class="aside-content" shadow="never">
                    <template #header>
                        <div class="card-header">
                            <span>最新动态</span>
                        </div>
                    </template>
                    <div class="dynamics" v-for="i in 6">
                        <svg t="1709878671810" class="dynamics-icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="4428" width="128" height="128">
                            <path
                                d="M730.453333 426.666667l-46.08-77.653334-31.146666 122.453334 106.24 193.706666V938.666667H682.666667v-213.333334l-99.413334-132.693333-68.266666 192.426667-205.653334 89.6L264.533333 810.666667l178.773334-105.386667 107.52-420.693333-90.026667 28.16V469.333333H384V247.466667l231.253333-72.106667 21.333334-3.413333c26.453333 0 49.493333 14.506667 62.293333 35.84l85.333333 142.08H938.666667V426.666667h-208.213334M725.333333 162.133333c-42.666667 0-76.8-34.133333-76.8-76.8S682.666667 8.533333 725.333333 8.533333s76.8 34.133333 76.8 76.8S768 162.133333 725.333333 162.133333M298.666667 384v85.333333H170.666667a42.666667 42.666667 0 0 1-42.666667-42.666666 42.666667 42.666667 0 0 1 42.666667-42.666667h128m96 170.666667l-21.333334 85.333333H213.333333a42.666667 42.666667 0 0 1-42.666666-42.666667 42.666667 42.666667 0 0 1 42.666666-42.666666h181.333334M298.666667 213.333333v85.333334H128a42.666667 42.666667 0 0 1-42.666667-42.666667 42.666667 42.666667 0 0 1 42.666667-42.666667h170.666667z"
                                fill="#3f9785" p-id="4429"></path>
                        </svg>
                        <span class="dynamics-detail">xxx刚刚完成了一次引体向上打卡。</span>
                        <span class="dynamics-time">一分钟前</span>
                    </div>
                </el-card>
            </el-aside>

        </el-container>
    </el-container>
</template>

<style scoped>
.container {
    height: 100%;
}

.el-main {
    /* background-color: transparent; */
    border-radius: .3rem;
    height: 100%;
    /* background-image: url(@/assets/icon-transparent.png); */
    /* background-position: right -30% bottom -20%; */
    /* background-size: 50%; */
    /* background-repeat: no-repeat; */
}

.el-aside {
    border-radius: .3rem;
    padding: var(--el-main-padding);
    box-sizing: border-box;
}

.el-row {
    margin-bottom: 20px;
}

.el-row:last-child {
    margin-bottom: 0;
}

.el-col {
    border-radius: 4px;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}

.shortcut {
    display: flex;
}

.shortcut .el-card {
    background-color: #f8f8f8;
}

.aside-content {
    background-color: white;
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    border-radius: .3rem;
}

.shortcut-icon {
    width: 30px;
    height: 30px;
}

.shorcut-caption {
    font-size: .8rem;
    text-align: center;
    user-select: none;
    margin-top: 10px;
}

.system-info .el-card {
    background-color: #f8f8f8;
}

.system-info-item-caption {
    font-size: .8rem;
    text-align: center;
    display: block;
    color: #5e5e5e;
    user-select: none;
}

.system-info-display {
    color: #1dd165;
    font-size: 2rem;
    text-align: center;
    display: block;
}

.card-header {
    user-select: none;
}

#chart {
    background-color: white;
    padding: 20px;
    box-sizing: border-box;
    border-radius: .3rem;
    border: #e4e7ed 1px solid;
    height: 440px;
}

.aside-dynamics {
    height: 810px;
}

.dynamics {
    height: 80px;
    border-bottom: #e4e7ed 1px solid;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    user-select: none;
}

.dynamics-icon {
    width: 20px;
    height: 20px;
    margin-bottom: 10px;
}

.dynamics-detail {
    color: #060606;
    font-size: .8rem;
    margin-bottom: 10px;
}

.dynamics-time {
    color: #aeaeae;
    font-size: .8rem;
    margin-bottom: 10px;
}
</style>