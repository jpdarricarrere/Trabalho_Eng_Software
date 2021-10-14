<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo-bike.png" />

    <h1>Alguel de Bicicletas</h1>
  </div>
  <!--
    
<div class="container px-4 px-lg-5">
    <div class="row">
      <div class="col">
        <div class="card-body " >
          <img src= />
        </div>
      </div>
    </div>
    -->
  <section class="py-5">
    <div
      class="
        row
        gx-4 gx-lg-5
        row-cols-2 row-cols-md-3 row-cols-xl-4
        justify-content-center
      "
    >
      <div class="col mb-5">
        <div class="card-body h-100">
          <!-- Product image-->
          <img class="card-img-top" src="../assets/bike-mtb.png" alt="..." />
          <!-- Product details-->
          <div class="card-body p-4">
            <div class="text-center">
              <!-- Product name-->
              <h5 class="fw-bolder">Fancy Product</h5>
              <!-- Product price-->
              $40.00 - $80.00
            </div>
          </div>
          <!-- Product actions-->
          <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
            <div class="text-center">
              <a class="btn btn-outline-dark mt-auto" href="#">View options</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  components: {},
};
</script>
<style scoped>
#bike {
  max-width: 100px;
  max-height: 100px;
}
</style>