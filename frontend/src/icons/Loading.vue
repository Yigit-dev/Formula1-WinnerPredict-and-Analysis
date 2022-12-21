<template lang="">
    <div class="loading">
        <img src="../assets/loading.gif" alt="">
        <small>loading table...</small>
    </div>
</template>
<script>
export default {
    name: "Loading"
}
</script>
<style scoped>
    .loading{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
    }
    .loading img{
        width: 48px;
        height: 48px;
    }
</style>