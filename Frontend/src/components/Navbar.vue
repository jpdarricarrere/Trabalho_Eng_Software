<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <ul class="navbar-nav">
      <a class="navbar-brand" href="#">
        <img src="../assets/logo-bike-nome.png" height="75" alt="Logo-rike" />
      </a>
    </ul>

    <!--<ul class="navbar-nav">
     <form class="text">
        <input
          class="form-control"
          type="text"
          placeholder="Pesquisar pelo nome ou modelo..."
          v-model="search" @keyup.enter="submit"
        />       
      </form>

    </ul>-->
    <ul class="navbar-nav">
      <li class="nav-item me-3">
        <router-link to="/home" active-class="active" class="nav-link" exact>
          <a class="nav-link text-primary fw-bolder" href="#">
            <b-icon-house-fill></b-icon-house-fill>
            <i>Home</i>
          </a>
        </router-link>
      </li>
    </ul>
  </nav>
</template>
<script>
export default {
  name: "Login",
  components: {},
  data() {
    return {
      search: "",
      cliente_id: localStorage.getItem("_bikesystem_cliente_id"),
      cliente_nome: localStorage.getItem("_bikesystem_cliente_nome"),
    };
  },
  methods: {
    submit: function () {
      this.$emit("inputData", this.tempMessage);
      this.tempMessage = "";
    },
  },
};
</script>
<style>
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
