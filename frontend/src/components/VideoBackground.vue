<template>
    <div class="bg-video-wrap">
        <video src="../assets/video.mp4" loop muted autoplay></video>
        <div class="overlay"></div>
    </div>
</template>
<script>
export default {
    
}
</script>
<style scoped>
.bg-video-wrap {
  position: relative;
  overflow: hidden;
  width: 100%;
  height: 50vh;
}
video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 1;
}
.overlay {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background: #000;
  z-index: 2;
  opacity: 0.4;
}
</style>