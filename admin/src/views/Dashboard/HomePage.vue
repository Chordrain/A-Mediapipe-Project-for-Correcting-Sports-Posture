<script setup lang="ts">

</script>

<template>
    <el-container>
        <el-main>
            <el-row>
                <el-col :span="24" class="carousel-row">
                    <el-carousel trigger="click" height="170px">
                        <el-carousel-item v-for="item in 4" :key="item">
                        </el-carousel-item>
                    </el-carousel>
                </el-col>
            </el-row>

            <el-row>
                
            </el-row>
        </el-main>
    </el-container>
</template>

<style scoped>
.el-carousel {
    border-radius: 3px;
}

.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    margin: 0;
    text-align: center;
}

.el-carousel__item {
    background-image: url("../../assets/football.png");
    background-position: 50% 60%;
}

.el-container {
    height: 100%;
    background-image: url("../../assets/sports.svg");
    background-size: 40%;
    background-repeat: no-repeat;
    background-position: right bottom;
    /* background-attachment: fixed; */
}
</style>