<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { RouterView } from 'vue-router';
import { usePageInfoStore } from '@/stores/PageInfo';

let side_bar_title = ref('易体后台管理系统')

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
</script>

<template>
    <div class="common-layout">
        <el-container>
            <el-aside>
                <div class="logo">
                    <img src="@/assets/logo.svg" alt="" id="logo-svg">
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

                    <el-sub-menu index="2">
                        <template #title>
                            <el-icon>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-ea893728="">
                                    <path fill="currentColor"
                                        d="M128 384v448h768V384zm-32-64h832a32 32 0 0 1 32 32v512a32 32 0 0 1-32 32H96a32 32 0 0 1-32-32V352a32 32 0 0 1 32-32m64-128h704v64H160zm96-128h512v64H256z">
                                    </path>
                                </svg>
                            </el-icon>
                            <span>管 理</span>
                        </template>
                        <RouterLink to="/dashboard/students">
                            <el-menu-item index="1-1">
                                学生管理
                            </el-menu-item>
                        </RouterLink>
                        <RouterLink to="/dashboard/classes">
                            <el-menu-item index="1-2">
                                班级管理
                            </el-menu-item>
                        </RouterLink>
                    </el-sub-menu>

                    <RouterLink to="/dashboard/homepage">
                        <el-menu-item index="3">
                            <el-icon><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-ea893728="">
                                    <path fill="currentColor"
                                        d="M416 896V128h192v768zm-288 0V448h192v448zm576 0V320h192v576z"></path>
                                </svg></el-icon>
                            <template #title>数 据</template>
                        </el-menu-item>
                    </RouterLink>

                    <RouterLink to="/dashboard/homepage">
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

                    <RouterLink to="/dashboard/homepage">
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
                        <span class="pageNameHint">{{ pageInfoStore.pageNameHint }}</span>
                    </div>
                    <div class="right">

                    </div>
                </el-header>
                <el-main>
                    <RouterView></RouterView>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<style scoped>
.el-aside {
    background-color: #545c64;
    box-sizing: border-box;
    border-right: 2px #dcdfe6 solid;
    user-select: none;
    width: 64px;
    transition: all .3s ease-in-out;
    overflow-x: hidden;
}

.el-main {
    background-color: #f0f2f5;
}

.main-content {
    min-width: 1497px;
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
    height: 56px;
}

/* logo */
#logo-svg {
    height: 30px;
    width: 30px;
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
</style>