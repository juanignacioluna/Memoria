<template>
  <div class="home">

<!--     <Navbar /> -->

    <div class="container-fluid contenedor">

      <div class="row">

        <div class="col-sm"></div>

        <div class="col-sm">



          <h1>Bienvenido al juego de la memoria</h1>


          <br> <br>


          <div class="card text-white bg-dark mb-3">
            <div class="card-header">
              <h4>¿Cuál es tu nombre?</h4>
            </div>
            <div class="card-body">

              <div class="form-group">
                <input v-model="nombre" id="nombre" type="text" class="form-control">
              </div>

              <router-link :to="{ name: 'Jugar', params: { nombre: nombre }}">
                <button type="button" class="btn btn-success">JUGAR!</button>
              </router-link>

            </div>
          </div>



        </div>

        <div class="col-sm"></div>

      </div>



    </div>


  </div>
</template>

<style>

  .contenedor{

    margin-top: 20px;

  }

</style>

<script>

export default {
  name: 'Home',
  data(){

    return{

      nombre: "",

    }
  },
}
</script>
