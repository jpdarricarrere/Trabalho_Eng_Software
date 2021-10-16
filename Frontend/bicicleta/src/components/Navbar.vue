<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <ul class="navbar-nav">
      <a class="navbar-brand" href="#">
        <img src="../assets/logo-bike-nome.png" height="75" alt="Logo-rike" />
      </a>
    </ul>
<!-- 
    <ul class="navbar-nav">
     <form class="text">
        <input
          class="form-control"
          type="text"
          placeholder="Pesquisar pelo nome ou modelo..."
          v-model="search"
        />       
      </form>

    </ul>
-->
    <ul class="navbar-nav">
       <li class="nav-item me-3">
           <router-link to="/login" active-class="active" class="nav-link" exact>
           <a class="nav-link text-primary fw-bolder" href="#">
               <b-icon-person-fill></b-icon-person-fill>
               <i>Login</i>
           </a>
           </router-link>
        </li> 
    </ul>
    <ul class="navbar-nav">
       <li class="nav-item me-3">
           
           <a class="nav-link text-primary fw-bolder" href="#" @click="logout">
               <b-icon-door-open-fill></b-icon-door-open-fill>
               <i>Logout</i>
           </a>
           
        </li> 
    </ul>
  </nav>
</template>
<script>
import axios from "axios";
export default {
  name: "Login",
  components: {},
  data() {
    return {
        search:""
    };
  },
  methods: {
    async logout() {
      /* Faz a partde de deslogar com o autenticador*/
      await axios.delete(/*caminho do back */);
      this.$router.push("/login");
    },
    search_return(){
      console.log(this.search);
      return this.search;
      
    },
  },
};
</script>
<style >
.navbar-nav .nav-link.active {
  border-bottom: 0.125rem solid $primary;
}

@include media-breakpoint-down(lg) {
  .navbar-nav .nav-link {
    padding-left: 0.625rem !important;
  }
  .navbar-nav .nav-link.active {
    padding-left: 0.5rem !important;
    border-left: 0.125rem solid $primary;
    border-bottom: none;
  }
}
.text {
  width: 1450px;
}
</style>
