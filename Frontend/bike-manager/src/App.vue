<template>
  <img alt="Vue logo" src="./assets/logo-bike.png">
  <!--<HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <a class="text-center" href="/home">bikes</a>
  <router-link to="/home" active-class="active" exact></router-link>
  <router-view class="container-xxl mt-3" />
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'


export default {
  name: 'Home',
  components: {
    //HelloWorld,
    
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
