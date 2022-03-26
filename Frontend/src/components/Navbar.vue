<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="collapse navbar-collapse">
    <ul class="navbar-nav mr-auto">
      <li class="navbar-brand">
        <img src="../assets/logo-social-sq.png" alt="Logo do site" height="60"/>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" style="padding-top: 25px">Home</a>
      </li>
      <li class="nav-item text-right">
        <form class="form-inline my-2 my-lg-0" style="padding-top: 20px">
          <input class="form-control mr-sm-2" type="search" placeholder="Pesquisar por serviço" v-model="search" @keyup.enter="submit">
        </form>
    </li>
    </ul>
  </div>
</nav>
</template>
<script>
export default {
  name: "Login",
  components: {},
  data() {
    return {
      search: "",
      // cliente_id: localStorage.getItem("_bikesystem_cliente_id"),
      // cliente_nome: localStorage.getItem("_bikesystem_cliente_nome"),
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
