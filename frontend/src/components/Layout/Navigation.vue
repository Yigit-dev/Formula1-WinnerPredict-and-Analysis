<template>
    <nav>
        <IconF1 />
        <h1>Formula 1 Winner Predict & Analysis</h1>
    </nav>
</template>

<script>
import IconF1 from '../../icons/IconF1.vue';

export default{
    name: "Navigation",
    components: { IconF1 }
}
</script>

<style scoped>
nav{
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--c-formula1);
    padding: 12px 9vw;
}
@media screen and (max-width: 960px){
    nav h1{
        display: none;
    }
}
nav h1{
    color: #fff;
}
</style>