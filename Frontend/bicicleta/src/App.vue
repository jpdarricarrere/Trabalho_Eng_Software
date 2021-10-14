<template>
  <div>
    <img alt="vue" src="./assets/logo-bike.png" />

 
    <input class="form-control" v-model="search" placeholder="Procure por nome ou modelo de bicicleta">
      <div>
  <b-card
    title="Card Title"
    img-src="/assets/bike-mtb.png"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
      Some quick example text to build on the card title and make up the bulk of the card's content.
    </b-card-text>

    <b-button href="javascript:;" variant="primary">Go somewhere</b-button>
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
