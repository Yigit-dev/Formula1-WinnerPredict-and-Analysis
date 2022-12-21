<template>
    <footer>
        <p>Formula 1 Winner Predict & Analysis</p>
        <p>{{ new Date().getFullYear() }} — <strong>Yigit Cakmak - Berfin Tek</strong></p>
    </footer>
</template>

<script>
export default {
    name: 'Footer'
}
</script>
<style scoped>
footer{
    background: var(--c-formula1);
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

footer p{
    font-size: 1.5rem;
}
</style>