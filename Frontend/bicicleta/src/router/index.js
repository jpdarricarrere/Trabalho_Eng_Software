import VueRouter from 'vue-router'
const routes = [{
    path: "/home",
    name: "Home",
    component: () =>
        import ( /* webpackChunkName: "home" */ "../views/Home.vue"),
}, ];

export default new VueRouter({
    routes,
    mode: 'history'
})