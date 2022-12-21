<template>
<div>
  <Navigation />
  <video-background />
    <div class="container">
        <main class="pageAnimation">
            <slot />
        </main>
    </div>
  <Footer />
</div>
</template>

<script>
import VideoBackground from '../VideoBackground.vue';
import Footer from './Footer.vue';
import Navigation from './Navigation.vue';

export default {
    name: 'Layout',
    components: { Navigation, Footer, VideoBackground }
}
</script>

<style scoped>
  .container {
    position: relative;
    /* background: var(--theme-bg); */
    transition: background-color 0.5s;
    width: 100%;
    min-height: 100vh;
    padding: 4vw 10vw;
    overflow: hidden;
  }
  main{
    display: flex;
    justify-content: center;
    flex-direction: column;
  }
</style>