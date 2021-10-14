<template>
  <div class="home">
    <img id="logo" alt="Vue logo" src="../assets/logo-bike.png">
    <h1>Aluguel de Bicicletas</h1>
    <div class="container">
        <img class="bike-pesquisa" alt ="bike_central" src="../assets/bike-mtb.png"/>
        <img class="bike-pesquisa" alt ="bike_central" src="../assets/bike-mtb.png"/>
        <img class="bike-pesquisa" alt ="bike_central" src="../assets/bike-mtb.png"/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'Home',
  components: {
    
  }
}
</script>
<style scoped>
#logo{
  max-width: 100px;
  max-height: 100px;
  width: 50%;
  height: 50%;
}


.container{
  display: flex;
  justify-content: center;
}

.bike-pesquisa{
max-width: 480px;
max-height: 270px;
padding: 5px;
width: 50%;
height: 50%;
}

</style>
