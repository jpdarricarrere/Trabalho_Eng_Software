<template>
  <div >
   <router-link to="/home">Home</router-link> |
    <Navbar  />
    <input
          class="form-control"
          type="text"
          placeholder="Pesquisar pelo nome ou modelo..."
          v-model="search"
        /> 
  
        <!-- img-src so pega imagens com url -->
  <div class="col d-flex justify-content-center ">
       
    <b-row>
    <b-card-group class="col-md-3" v-for="bike in filteredBikes" v-bind:key="bike">
        <b-card 
                v-bind:title= "bike.nome"
                v-bind:img-src=  "bike.link_imagem"
                img-alt="Img"
                img-top>
            <p class="card-text">
                descrição da bike</p>
            
            <div slot="footer">
                <b-btn variant="primary" block>Alugue</b-btn>
            </div>
        </b-card>
    </b-card-group>
  </b-row>
  </div>
</div>


    
  
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import Navbar from "./components/Navbar.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    //  HelloWorld
    Navbar,
  },
  data() {
    return {
      search: "",
      bikes: [],
    };
  },
  async created() {
    await axios
      .get("http://127.0.0.1:8000/bikes")
      .then((response) => (this.bikes = response.data))
      .catch((error) => console.log(error));
  },
  computed: {
    filteredBikes: function () {
      return this.bikes.filter((bikes) => {
        return bikes.nome.match(this.search) !== null;
      });
    },
    formattedBikes() {
      return this.bikes.reduce((c, n, i) => {
        if (i % 4 === 0) c.push([]);
        c[c.length - 1].push(n);
        return c;
      }, []);
    },

    searchBikes() {
      return this.$refs.search.search_return();
    },
  },
};
</script>

<style>
#logo {
  max-width: 80px;
  max-height: 80px;
}

.input-search {
  height: 50%;
  width: 30%;
  margin-left: 30%;
}

.mb-2 {
  margin-left: 10px;
}
</style>
