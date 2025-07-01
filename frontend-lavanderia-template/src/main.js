// src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/tailwind.css'

const app = createApp(App)
app.use(router)
app.mount('#app')


// ESTO FUNCIONA JUAN: 
//import { createApp } from 'vue'
//import App from './App.vue'
//import './assets/tailwind.css'

//createApp(App).mount('#app')