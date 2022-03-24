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
    <b-card-group class="col-md-3" v-for="servico in filteredServicos" :key="servico.id">
        <b-card 
                :title= "servico.nome"
                :img-src= "servico.link_imagem"
                img-alt="Img"
                img-top>
            <p class="card-text">
                <ul>
                  <!-- <li>Tipo: {{servico.tipo}}</li> -->
                  <!-- <li>Ano: {{servico.ano}}</li> -->
                  <!-- <li>Aro: {{servico.aro}}</li>  -->
                  <!-- <li>Marchas: {{servico.num_marchas}}</li> -->
                </ul>
            </p>
            
            <div slot="footer">
                <!-- <b-btn :id="servico.id" type="button" :disabled="servico.contratado == true" variant="primary"  @click="selectBike(bike.id)">Alugue</b-btn> -->
                <b-btn :id="servico.id" type="button" variant="primary">Alugue</b-btn>
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
  name: "Home",
  components: {
    Navbar,
  },
  data() {
    return {
      search: "",
      servicos: [],
      teste:""
    };
  },
  async created() {
    await axios
      .get("http://127.0.0.1:8000/servicos")
      .then((response) => (this.servicos = response.data))
      .catch((error) => console.log(error));
  },
  computed: {
    filteredServicos: function () {
      return this.servicos.filter((servicos) => {
        return servicos.nome.match(this.search) !== null;
      });
    },
    formattedServicos() {
      return this.servicos.reduce((c, n, i) => {
        if (i % 4 === 0) c.push([]);
        c[c.length - 1].push(n);
        return c;
      }, []);
    },

    searchServicos() {
      return this.$refs.search.search_return();
    },
    
  },
  
  methods:{
    updateSearch(variable){
      this.search = variable;
    },
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

