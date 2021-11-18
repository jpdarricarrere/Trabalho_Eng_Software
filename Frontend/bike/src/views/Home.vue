<template>
<div>
  <Navbar @inputData="updateSearch(search)" />

  <ul >
     <form class="text">
        <input
          class="form-control"
          type="text"
          placeholder="Pesquisar pelo nome ou modelo..."
          v-model="search" @keyup.enter="submit"
        />       
      </form>

    </ul>
  
        <!-- img-src so pega imagens com url -->
  <div class="col d-flex justify-content-center ">
       
    <b-row>
    <b-card-group class="col-md-3" v-for="bike in filteredBikes" :key="bike.id">
        <b-card 
                :title= "bike.nome"
                :img-src= "bike.link_imagem"
                img-alt="Img"
                img-top>
            <p class="card-text">
                <ul><li>Tipo: {{bike.tipo}}</li>
                <li>Ano: {{bike.ano}}</li>
                <li>Aro: {{bike.aro}}</li> 
                <li>Marchas: {{bike.num_marchas}}</li></ul>
                </p>
            
            <div slot="footer">
                <b-btn :id="bike.id" type="button" :disabled="bike.alugada == true" variant="primary"  @click="selectBike(bike.id)">Alugue</b-btn>
            </div>
        </b-card>
    </b-card-group>
  </b-row>
  </div>
</div>


    
  
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import Navbar from "../components/Navbar.vue";
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
      teste:""
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
  
  methods:{
    updateSearch(variable){
      this.search = variable;
    },
    async selectBike(id){
      document.getElementById(id).disabled = true;
      await axios.get("http://127.0.0.1:8000/emprestimos/reserva/" + id,id)
            .then(response => (console.log(response)))
    }
  }
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

