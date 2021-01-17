<template>
  <div class="tabla container-fluid">


	<h1>Tabla de resultados</h1>

	<div class="row">

	    <div class="col-sm"></div>

	    <div class="col-sm-6">

	    	<router-link :to="{ name: 'Jugar', params: { nombre: nombre }}">
	    		<button type="button" class="btn btn-light again">JUGAR DE NUEVO</button>
	    	</router-link>

			<table class="table table-dark table-striped table-hover">
			  <thead>
			    <tr>
			      <th scope="col">Puesto</th>
			      <th scope="col">Nombre</th>
			      <th scope="col">Mejor puntaje</th>
			      <th scope="col">Último puntaje</th>
			    </tr>
			  </thead>
			  <tbody>


			    <tr v-for="(registro, index) in registros">
			      <th scope="row">{{ (index+1) }}</th>
			      <td>{{ registro.fields.nombre }}</td>
			      <td>{{ registro.fields.mejorPuntaje }}</td>
			      <td>{{ registro.fields.ultimoPuntaje }}</td>
			    </tr>


			  </tbody>
			</table>

			<div class="text-center" id="cargando">
				<div class="spinner-border text-success" style="width: 12rem; height: 12rem;" role="status">
				  <span class="sr-only">Loading...</span>
				</div>
			</div>

	    </div>

	    <div class="col-sm"></div>

	  </div>


  </div>
</template>

<style>

	.again{
		margin-bottom: 20px;
	}

</style>

<script>

export default {
  name: 'Tabla',
  data(){

    return{

    	nombre: "",

    	registros: [],

    }
  },
  components: {

  },
  mounted: function () {

  	this.nombre = this.$route.params.nombre;



	fetch('https://memoria-back.herokuapp.com/polls/getTabla/',{
		method: 'GET',
		headers: new Headers({})
	})
	.then(response2 => response2.json())
	.then((data2) => {

		console.log(data2['Resultados'])

		this.registros = data2['Resultados']

		document.getElementById("cargando").outerHTML = "";


	})



  },
  methods: {


  }

}
</script>
