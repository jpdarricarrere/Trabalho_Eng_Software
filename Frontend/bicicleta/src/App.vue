<template>
  <div>
    <img alt="vue" src="./assets/logo-bike.png" />

 
    <input class="form-control" v-model="search" placeholder="Procure por nome ou modelo de bicicleta">
      <div>
        <!-- img-src so pega imagens com url -->
        
  <b-card
    title= "MTB Specialized"
    img-src="https://d2ul2exfru69gk.cloudfront.net/Custom/Content/Products/13/16/13163_bicicleta-nova-specialized-epic-ht-carbon-29-2020-37241_z4_637288976190418780.jpg"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
      Bicicleta Aro 29 boa para trilhas em terrenos dificeis 
    </b-card-text>

    <b-button href="javascript:;" variant="primary">Alugue</b-button>
  </b-card>
</div>


    <!--<HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'

export default {
  name: "App",
  components: {
    //  HelloWorld
  },
};
</script>

<style>

</style>
