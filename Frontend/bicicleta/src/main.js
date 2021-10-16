import Vue from 'vue'
import App from './App.vue'
import VueAxios from "axios"
import axios from "axios";
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import router from "./router"

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap-icons/font/bootstrap-icons';

Vue.config.productionTip = false
Vue.use(BootstrapVue)

Vue.use(router);
Vue.use(VueAxios, axios);
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
new Vue({
    render: h => h(App),
}).$mount('#app')