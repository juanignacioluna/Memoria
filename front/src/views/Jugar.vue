<template>
  <div class="jugar">

  	<h1>El juego de la memoria</h1>

  	<h3>Tiempo: <span id="contadorRegresivo"></span> segundos</h3>

  	<router-link :to="{ name: 'Tabla', params: { nombre: nombre }}">
  		<span id="tabla"></span>
  	</router-link>

  	<hr>

	<div class="container-fluid juego">

		<div class="row">

		    <div v-for="(back, index) in backs" class="col-sm-6 col-lg-3 col-md-4 col-6" align="center">

				<Carta :indexNro="index" :bus="bus" ref="form" :backIMG="back" />

		    </div>

		</div>

	</div>




  </div>
</template>

<style>

	div{
		margin-bottom: 10px;
	}

	h1{
		margin-bottom: 20px;
		margin-top: 10px;
	}

</style>

<script>

import Carta from '@/components/Carta.vue'
import Vue from 'vue'; 
import tingle from 'tingle.js'; 

export default {
  name: 'Jugar',
  data(){

    return{

    	nombre: "",

    	puntaje: 404,

    	gano: false,

    	contadorDeParejas: 0,

		tiempoTotal: 25,

    	primera: "",

    	segunda: "",

    	indxPrimera: 404,

    	bus: new Vue(),

    	contadorDeCartas: 0,

    	backs: [

    		{img: "tesla"},
    		{img: "boring"},
    		{img: "solar"},
    		{img: "spaceX02"},
    		{img: "tesla"},
    		{img: "boring"},
    		{img: "solar"},
    		{img: "spaceX02"},

    	],

    }
  },
  components: {
    Carta,
  },
  mounted: function () {

  	this.backs.sort( () => Math.random() - 0.5);

  	this.contadorRegresivo();

  	this.nombre = this.$route.params.nombre;

  },
   methods: {

		contadorRegresivo(){

			document.getElementById('contadorRegresivo').innerHTML = this.tiempoTotal;

			if(this.tiempoTotal==0){

				if(this.gano==false){


						let modalCargando = new tingle.modal({
							    closeMethods: ['']
						});

						modalCargando.setContent(`
							<div class="text-center">
								<div class="spinner-border text-success" role="status" style="width: 8rem; height: 8rem;">
									<span class="sr-only">Loading...</span>
								</div>
							</div>`);

						modalCargando.open();

						fetch('https://memoria-back.herokuapp.com/polls/final/',{
							method: 'POST',
							headers: new Headers({}),
							body: JSON.stringify({nombre: this.nombre, puntaje: 0}),
						})
						.then(response => response.text())
						.then((data) => {

							let modalPerdiste = new tingle.modal({
								footer: true,
								stickyFooter: false,
							    closeMethods: ['']
							});

							modalPerdiste.setContent("<h1 style='color:black;'>Upps...perdiste! :(</h1>");

							modalPerdiste.addFooterBtn('SIGUIENTE', 'tingle-btn tingle-btn--primary', function() {

								modalPerdiste.close();

								document.getElementById('tabla').click();

							});

							modalCargando.close();

							modalPerdiste.open();

							console.log(data);

						});

				}

			}else{

				this.tiempoTotal-=1;

	            let self = this;

	            setTimeout(function(){

	                self.contadorRegresivo();

	            }, 1000);

			}

		},

		sleep(ms) {
		  return new Promise(resolve => setTimeout(resolve, ms));
		},

		async clickCarta(indx, tipo){


		   if(this.contadorDeCartas==0){

		   		this.indxPrimera = indx;

		   		this.contadorDeCartas++;

		   		this.bus.$emit('primera'+indx);

		   		this.primera = tipo;

		   }else if(this.contadorDeCartas==1){

		   		this.contadorDeCartas++;

		   		this.bus.$emit('segunda'+indx);

		   		this.segunda = tipo;

		   		if(this.segunda==this.primera){

		   			this.contadorDeParejas++;

		   			this.primera="";

		   			this.segunda="";

		   			this.contadorDeCartas=0;

		   			if(this.contadorDeParejas==4){

		   				this.gano = true;

						this.puntaje = (this.tiempoTotal * 740);


						let modalCargando = new tingle.modal({
							    closeMethods: ['']
						});

						modalCargando.setContent(`
							<div class="text-center">
								<div class="spinner-border text-success" role="status" style="width: 8rem; height: 8rem;">
									<span class="sr-only">Loading...</span>
								</div>
							</div>`);

						modalCargando.open();

						fetch('https://memoria-back.herokuapp.com/polls/final/',{
							method: 'POST',
							headers: new Headers({}),
							body: JSON.stringify({nombre: this.nombre, puntaje: this.puntaje}),
						})
						.then(response2 => response2.text())
						.then((data2) => {

							let modalGanaste = new tingle.modal({
								footer: true,
								stickyFooter: false,
							    closeMethods: ['']
							});

							modalGanaste.setContent(`
								<h1 style='color:black;'>Felicitaciones! Has ganado :)</h1>
								<br><h2 style='color:black;'>Tu puntaje es: `+ this.puntaje + `</h2>`);

							modalGanaste.addFooterBtn('SIGUIENTE', 'tingle-btn tingle-btn--primary', function() {

								modalGanaste.close();

								document.getElementById('tabla').click();
								
							});

							modalCargando.close();

							modalGanaste.open();

							console.log(data2);

						});

		   			}


		   		}else{

		   			this.bus.$emit('primera2'+this.indxPrimera);

		   			this.bus.$emit('segunda2'+indx);

		   			await this.sleep(2000);

		   			this.primera="";

		   			this.segunda="";

		   			this.contadorDeCartas=0;

		   			this.indxPrimera=404;

		   		}



		   }






	   	


	   }

   }

}
</script>
