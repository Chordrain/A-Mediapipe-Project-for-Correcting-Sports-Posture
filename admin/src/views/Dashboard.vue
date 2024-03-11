<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { RouterView } from 'vue-router';
import { usePageInfoStore } from '@/stores/PageInfo';
import { RefreshRight } from '@element-plus/icons-vue';

let side_bar_title = ref('易体后台管理系统');

const isCollapse = ref(true)
const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
function menuCollapseToggle() {
    if (isCollapse.value) {
        let open = document.getElementById('open');
        open?.click();
        let aside = document.getElementsByClassName('el-aside')[0] as HTMLElement;
        aside.style.width = '160px'
    } else {
        let close = document.getElementById('close');
        close?.click();
        let aside = document.getElementsByClassName('el-aside')[0] as HTMLElement;
        aside.style.width = '64px'
    }
}
let pageInfoStore = usePageInfoStore();
pageInfoStore.pageNameHint = "首 页";

function refresh() {
    location.reload();
}
</script>

<template>
    <el-container style="height: 100%">
        <!-- 侧栏 -->
        <el-aside>
            <div class="logo">
                <svg id="logo-svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                    data-v-0dd9719b="" version="1.0" width="32" height="32" viewBox="0 0 340.000000 250.000000"
                    preserveAspectRatio="xMidYMid meet" color-interpolation-filters="sRGB" style="margin: auto;">
                    <g data-v-0dd9719b="" fill="#1dd165" class="icon-text-wrapper icon-svg-group iconsvg"
                        transform="translate(117.77499771118164,56.87810516357422)">
                        <g class="iconsvg-imagesvg" transform="translate(22.22500228881836,0)">
                            <g>
                                <rect fill="#1dd165" fill-opacity="0" stroke-width="2" x="0" y="0" width="60"
                                    height="63.80128027902426" class="image-rect" /> <svg x="0" y="0" width="60"
                                    height="63.80128027902426" filtersec="colorsb9549903386"
                                    class="image-svg-svg primary" style="overflow: visible;"><svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        viewBox="-0.005511641502380371 -0.0011513382196426392 112.60130310058594 119.73571014404297">
                                        <title>资源 3</title>
                                        <g>
                                            <g>
                                                <path
                                                    d="M60.49 98.87c12.23.24 22.34-4.28 30-14.15 3.23-4.16 7.73-5.34 12.15-3.67a10.47 10.47 0 0 1 6.58 10.09 11 11 0 0 1-2.65 6.43c-16.13 20-37.32 25.93-61.39 19.94C20.73 111.42 5.64 95 1 70.09-5.19 36.84 17.89 5.32 51.23.58A56.83 56.83 0 0 1 59.67 0 10.18 10.18 0 0 1 70 10.43a10.15 10.15 0 0 1-10.31 10.19c-18.3-.15-35.62 13.43-38.77 33.63S32.6 95.16 52.74 98.32a36.64 36.64 0 0 0 7.75.55z"
                                                    fill="#1dd165" />
                                                <path
                                                    d="M65.69 55.72l26.16-26c2.54-2.53 5.3-4.31 9.08-4.32a10.74 10.74 0 0 1 10.31 6.33c2.08 4.12 1.85 8.51-1.27 11.75-11.17 11.63-22.48 23.1-34.2 34.16-.54-.79-.14-1.57.07-2.34 1.16-4.4.32-8.12-3.19-11.31a45.94 45.94 0 0 1-7.3-7.64.47.47 0 0 1 .34-.63z"
                                                    fill="#9971fe" />
                                                <path
                                                    d="M65.69 55.72a1.21 1.21 0 0 0 0 .38c-.77 2.06-2.66 3.17-4 4.71-1.21 1.35-2.54 2.58-3.72 4-2.75 3.19-3.21 6.79-2.2 10.71.2.79.61 1.55.1 2.35-6.63-6.57-13.35-12.98-19.75-19.69-3.94-4.13-3.25-11.42 1-15.33a11.29 11.29 0 0 1 15.58 0c4.35 4.26 8.65 8.59 12.99 12.87z"
                                                    fill="#feb228" />
                                                <path
                                                    d="M55.83 77.83c-2.65-6-1.5-11.1 3.41-15.46 2.23-2 4.3-4.17 6.45-6.27 2.9 2.85 5.94 5.58 8.67 8.59 3.55 3.89 3.24 8.38 1.41 13-4.77 7.16-14.48 7.73-19.94.14z"
                                                    fill="#0078fb" />
                                            </g>
                                        </g>
                                    </svg></svg> <!---->
                            </g>
                        </g>
                    </g>
                    <defs />
                </svg>
            </div>
            <el-radio-group v-model="isCollapse" style="margin-bottom: 20px; display: none;">
                <el-radio-button id="open" :label="false">expand</el-radio-button>
                <el-radio-button id="close" :label="true">collapse</el-radio-button>
            </el-radio-group>
            <el-menu default-active="1" text-color="#fff" background-color="#545c64" class="el-menu-vertical-demo"
                :collapse="isCollapse" @open="handleOpen" @close="handleClose">

                <RouterLink to="/dashboard/homepage">
                    <el-menu-item index="1">
                        <el-icon>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-ea893728="">
                                <path fill="currentColor"
                                    d="M192 413.952V896h640V413.952L512 147.328zM139.52 374.4l352-293.312a32 32 0 0 1 40.96 0l352 293.312A32 32 0 0 1 896 398.976V928a32 32 0 0 1-32 32H160a32 32 0 0 1-32-32V398.976a32 32 0 0 1 11.52-24.576">
                                </path>
                            </svg>
                        </el-icon>
                        <template #title>
                            首 页
                        </template>
                    </el-menu-item>
                </RouterLink>

                <RouterLink to="/dashboard/students">
                    <el-menu-item index="2">

                        <el-icon>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-ea893728="">
                                <path fill="currentColor"
                                    d="M128 384v448h768V384zm-32-64h832a32 32 0 0 1 32 32v512a32 32 0 0 1-32 32H96a32 32 0 0 1-32-32V352a32 32 0 0 1 32-32m64-128h704v64H160zm96-128h512v64H256z">
                                </path>
                            </svg>
                        </el-icon>
                        <template #title>
                            管 理
                        </template>
                    </el-menu-item>
                </RouterLink>

                <RouterLink to="/dashboard/dataview">
                    <el-menu-item index="3">
                        <el-icon><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-ea893728="">
                                <path fill="currentColor"
                                    d="M416 896V128h192v768zm-288 0V448h192v448zm576 0V320h192v576z"></path>
                            </svg></el-icon>

                        <template #title>数 据</template>
                    </el-menu-item>
                </RouterLink>

                <RouterLink to="/dashboard/notification">
                    <el-menu-item index="4">
                        <el-icon><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-ea893728="">
                                <path fill="currentColor" d="M512 64a64 64 0 0 1 64 64v64H448v-64a64 64 0 0 1 64-64">
                                </path>
                                <path fill="currentColor"
                                    d="M256 768h512V448a256 256 0 1 0-512 0zm256-640a320 320 0 0 1 320 320v384H192V448a320 320 0 0 1 320-320">
                                </path>
                                <path fill="currentColor"
                                    d="M96 768h832q32 0 32 32t-32 32H96q-32 0-32-32t32-32m352 128h128a64 64 0 0 1-128 0">
                                </path>
                            </svg></el-icon>

                        <template #title>通 知</template>
                    </el-menu-item>
                </RouterLink>

                <RouterLink to="/dashboard/setting">
                    <el-menu-item index="5">
                        <el-icon>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-ea893728="">
                                <path fill="currentColor"
                                    d="M600.704 64a32 32 0 0 1 30.464 22.208l35.2 109.376c14.784 7.232 28.928 15.36 42.432 24.512l112.384-24.192a32 32 0 0 1 34.432 15.36L944.32 364.8a32 32 0 0 1-4.032 37.504l-77.12 85.12a357.12 357.12 0 0 1 0 49.024l77.12 85.248a32 32 0 0 1 4.032 37.504l-88.704 153.6a32 32 0 0 1-34.432 15.296L708.8 803.904c-13.44 9.088-27.648 17.28-42.368 24.512l-35.264 109.376A32 32 0 0 1 600.704 960H423.296a32 32 0 0 1-30.464-22.208L357.696 828.48a351.616 351.616 0 0 1-42.56-24.64l-112.32 24.256a32 32 0 0 1-34.432-15.36L79.68 659.2a32 32 0 0 1 4.032-37.504l77.12-85.248a357.12 357.12 0 0 1 0-48.896l-77.12-85.248A32 32 0 0 1 79.68 364.8l88.704-153.6a32 32 0 0 1 34.432-15.296l112.32 24.256c13.568-9.152 27.776-17.408 42.56-24.64l35.2-109.312A32 32 0 0 1 423.232 64H600.64zm-23.424 64H446.72l-36.352 113.088-24.512 11.968a294.113 294.113 0 0 0-34.816 20.096l-22.656 15.36-116.224-25.088-65.28 113.152 79.68 88.192-1.92 27.136a293.12 293.12 0 0 0 0 40.192l1.92 27.136-79.808 88.192 65.344 113.152 116.224-25.024 22.656 15.296a294.113 294.113 0 0 0 34.816 20.096l24.512 11.968L446.72 896h130.688l36.48-113.152 24.448-11.904a288.282 288.282 0 0 0 34.752-20.096l22.592-15.296 116.288 25.024 65.28-113.152-79.744-88.192 1.92-27.136a293.12 293.12 0 0 0 0-40.256l-1.92-27.136 79.808-88.128-65.344-113.152-116.288 24.96-22.592-15.232a287.616 287.616 0 0 0-34.752-20.096l-24.448-11.904L577.344 128zM512 320a192 192 0 1 1 0 384 192 192 0 0 1 0-384m0 64a128 128 0 1 0 0 256 128 128 0 0 0 0-256">
                                </path>
                            </svg>
                        </el-icon>

                        <template #title>设 置</template>
                    </el-menu-item>
                </RouterLink>
            </el-menu>
        </el-aside>


        <el-container class="main-content">
            <!-- 顶栏 -->
            <el-header>
                <div class="left">
                    <el-icon @click="menuCollapseToggle" class="collapseIcon" v-show="!isCollapse">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-ea893728="">
                            <path fill="currentColor"
                                d="M896 192H128v128h768zm0 256H384v128h512zm0 256H128v128h768zM320 384 128 512l192 128z">
                            </path>
                        </svg>
                    </el-icon>
                    <el-icon @click="menuCollapseToggle" class="collapseIcon" v-show="isCollapse">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-ea893728="">
                            <path fill="currentColor"
                                d="M128 192h768v128H128zm0 256h512v128H128zm0 256h768v128H128zm576-352 192 160-192 128z">
                            </path>
                        </svg>
                    </el-icon>

                    <!-- 刷新按钮 -->
                    <el-tooltip class="box-item" effect="dark" placement="right">
                        <template #content><span style="font-size: .8rem;">刷 新</span></template>
                        <el-icon style="transform: scale(1.6); cursor: pointer; margin-left: 10px;" @click="refresh">
                            <RefreshRight />
                        </el-icon>
                    </el-tooltip>

                </div>
                <div class="right">
                    <el-container class="user-avatar">
                        <svg t="1709816488170" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="5643" width="32" height="32" id="avatar">
                            <path
                                d="M908.126 621.376c-45.5-38.25-54.376-126.75-63.688-220.56-9.25-92.718-18.876-188.59-62.5-265.59C730.566 44.602 642.258 0.384 511.93 0.008c-130.216 0.376-218.496 44.594-269.902 135.216-43.624 77-53.218 172.872-62.436 265.59-9.374 93.748-18.186 182.31-63.686 220.56l-18.5 15.562 17.718 16.438c2.376 2.188 24.812 21.938 85.216 40.934 78.5 24.688 183.374 37.25 311.652 37.25 128.266 0 233.136-12.562 311.634-37.25 60.376-18.996 82.876-38.746 85.25-40.934l17.75-16.438-18.5-15.56z"
                                fill="#343A42" p-id="5644"></path>
                            <path
                                d="M877.752 772.746l-3.624-1.062c-52.938-14.188-70.812-27.876-94.438-36.812-83.558-31.876-105.308-54.808-110.872-65.684-0.188-0.376-0.376-0.75-0.562-1.188l-0.688-97.062-155.576-2.312-155.59 2.312-0.688 97.062c-0.188 0.438-0.312 0.812-0.532 1.188-5.562 10.876-27.342 33.808-110.904 65.684-23.562 8.938-41.468 22.624-94.436 36.812l-3.624 1.062c-48.186 15.938-80.592 60.624-80.592 111.062v140.184h892.75v-140.184c0-50.436-32.436-95.124-80.624-111.062z"
                                fill="#DA4453" p-id="5645"></path>
                            <path
                                d="M633.882 634.188l-251.528-6.594-4.452 142.59 79.106 29.344 76.328 5.312 83.672-11.594 24-81.75z"
                                fill="#DBAFA5" p-id="5646"></path>
                            <path
                                d="M511.554 768.746c-62.842 0-98.294-21.312-98.294-21.312l77.42 276.558h42.656l77.422-276.558s-36.376 21.312-99.204 21.312z"
                                fill="#FFCE54" p-id="5647"></path>
                            <path
                                d="M753.126 726.09l-85.058-83.278-48.248 14.844-86.484 366.336 156.702-169.808-24.908-41.876zM270.872 726.09l85.014-83.308 48.312 14.874 86.482 366.336-156.7-169.808 24.89-41.876z"
                                fill="#ED5564" p-id="5648"></path>
                            <path
                                d="M787.126 382.128c0 178.748-170.432 343.244-275.134 343.244-104.686 0-275.088-164.496-275.088-343.244 0-178.81 123.186-296.714 275.088-296.714 151.952 0 275.134 117.904 275.134 296.714z"
                                fill="#EAC6BB" p-id="5649"></path>
                            <path
                                d="M564.008 161.32c0.376 0.312 34.312 30.5 87.31 60.874 43.312 24.842 107.808 54.498 178.872 62.216-9-53.218-22.876-104.404-48.25-149.184C730.566 44.602 642.258 0.384 511.93 0.008c-130.216 0.376 52.078 161.312 52.078 161.312z"
                                fill="#434A54" p-id="5650"></path>
                            <path
                                d="M236.904 382.128c0 8 0.36 16 1.016 23.968h548.176c0.656-7.968 1.032-15.968 1.032-23.968 0-6.312-0.188-12.562-0.5-18.686H237.372a387.45 387.45 0 0 0-0.468 18.686z"
                                fill="#656D78" p-id="5651"></path>
                            <path
                                d="M500.508 384.752c0 41.248-5.218 74.686-106.668 74.686-101.452 0-106.67-33.438-106.67-74.686 0-41.25 15.672-74.656 106.67-74.656 90.982 0.002 106.668 33.408 106.668 74.656zM736.066 384.752c0 41.248-5.188 74.686-106.652 74.686-101.438 0-106.656-33.438-106.656-74.686 0-41.25 15.672-74.656 106.656-74.656 90.998 0.002 106.652 33.408 106.652 74.656z"
                                fill="#5D9CEC" p-id="5652"></path>
                            <path
                                d="M377.808 363.066c63.092-31.968 126.216-76.438 187.7-132.092 75.562-68.436 129.31-136.154 154.186-169.684C668.444 20.416 599.758 0.228 511.93 0.008c-130.216 0.376-218.496 44.594-269.902 135.216-43.624 77-53.218 172.872-62.436 265.59-0.75 7.25-1.468 14.436-2.186 21.56 65.998-5.434 133.278-25.308 200.402-59.308z"
                                fill="#656D78" p-id="5653"></path>
                        </svg>
                        <el-text class="mx-1">Admin</el-text>
                    </el-container>
                    <!-- 更多 -->
                    <el-tooltip class="box-item" effect="dark" placement="top">
                        <template #content><span style="font-size: .8rem;">更 多</span></template>
                        <el-icon class="more" :size="20">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-ea893728="">
                                <path fill="currentColor"
                                    d="M176 416a112 112 0 1 0 0 224 112 112 0 0 0 0-224m0 64a48 48 0 1 1 0 96 48 48 0 0 1 0-96m336-64a112 112 0 1 1 0 224 112 112 0 0 1 0-224m0 64a48 48 0 1 0 0 96 48 48 0 0 0 0-96m336-64a112 112 0 1 1 0 224 112 112 0 0 1 0-224m0 64a48 48 0 1 0 0 96 48 48 0 0 0 0-96">
                                </path>
                            </svg>
                        </el-icon>
                    </el-tooltip>
                </div>
            </el-header>
            <!-- 面包屑 -->
            <section class="crumb-bar">
                <div class="green-spot"></div>
                <span class="pageNameHint">{{ pageInfoStore.pageNameHint }}</span>
            </section>
            <el-main class="homepage-wrapper">
                <RouterView></RouterView>
            </el-main>
        </el-container>
    </el-container>
</template>

<style scoped>
.el-aside {
    background-color: #545c64;
    box-sizing: border-box;
    border-right: 2px #dcdfe6 solid;
    user-select: none;
    width: 64px;
    transition: all .3s ease-in-out;
    overflow: hidden;
}

.el-main {
    background-color: #f0f2f5;
}

.homepage-wrapper {
    height: 100%;
}

.main-content {
    min-width: 1497px;
    height: 100%;
}

.el-menu {
    border: none;
}

.el-menu * {
    font-size: 1rem;
}

.el-sub-menu .el-menu-item {
    font-size: .88rem;
}

.el-header {
    min-height: 56px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
    z-index: 1;
}

.el-header .left,
.el-header .right {
    display: flex;
    align-items: center;
}

div.logo {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
    color: rgb(70, 70, 70);
    height: 60px;
}

/* logo */
#logo-svg {
    position: relative;
    top: 15px;
    transform: scale(5);
}

h1.h1-title {
    font-size: 1rem;
    margin-top: 5px;
    font-weight: 400;
}

.common-layout,
.common-layout>* {
    height: 100%;
}

.el-menu-item span {
    font-size: .9rem;
}

/* 折叠按钮 */
.collapseIcon {
    transform: scale(1.7);
    margin-right: 16px;
}

/* 面包屑 */
.pageNameHint {
    color: #545c64;
    font-size: .9rem;
    user-select: none;
}

.right .el-container .el-text {
    margin-left: 15px;
    user-select: none;
}

.more {
    margin-left: 30px;
    cursor: pointer;
    transform: rotate(90deg);
}

div.green-spot {
    background-color: #36b269;
    height: 10px;
    width: 10px;
    margin-right: 10px;
    border-radius: 50%;
}

.crumb-bar {
    height: 40px;
    display: flex;
    align-items: center;
    padding-left: 20px;
    padding-right: 20px;
    box-sizing: border-box;
}
</style>