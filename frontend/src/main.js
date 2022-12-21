import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "./assets/main.css"
import VideoBackground from 'vue-responsive-video-background-player'
import { Plugin } from 'vue-responsive-video-background-player'
import { appAxios } from './utils/appAxios'


const app = createApp(App)

app.config.globalProperties.$appAxios = appAxios
app.use(router)
app.use(VideoBackground)
app.use(Plugin)


app.mount('#app')