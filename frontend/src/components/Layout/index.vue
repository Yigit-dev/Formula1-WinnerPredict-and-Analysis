<template>
<div>
    <Navigation />
    <div class="container">
        <v-main class="pageAnimation">
            <slot />
        </v-main>
    </div>
    <Footer />
</div>
</template>

<script>
import Footer from './Footer.vue';
import Navigation from './Navigation.vue';

export default {
    name: 'Layout',
    components: { Navigation, Footer }
}
</script>

<style scoped>
  .container {
    position: relative;
    /* background: var(--theme-bg); */
    transition: background-color 0.5s;
    width: 100%;
    min-height: 100vh;
    padding: 4vw;
    overflow: hidden;
  }
  main{
    display: flex;
    justify-content: center;
    flex-direction: column;
  }
</style>