import { createApp } from 'vue'
import App from './App.vue'
import router from "./router"
import Vue from "vue";
import VueRouter from "vue-router";
Vue.use(VueRouter);
createApp(App).mount('#app')
createApp(App).use(router);