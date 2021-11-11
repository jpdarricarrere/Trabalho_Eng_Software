<template>
  <div class="home">
    <Navbar />
    <img alt="Vue logo" src="../assets/logo.png">
   
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'
import Navbar from "../components/Navbar.vue";
export default {
  name: 'Home',
  components: {
    Navbar
  }
}
</script>
