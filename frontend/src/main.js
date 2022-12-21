import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "./assets/main.css"
import VideoBackground from 'vue-responsive-video-background-player'
import { Plugin } from 'vue-responsive-video-background-player'


createApp(App)
  .use(router)
  .use(VideoBackground)
  .use(Plugin)
  .mount('#app')