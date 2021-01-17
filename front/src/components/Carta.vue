<template>

  <div id="carta">


		<div class="cartaContenedor">


			<div class="cartaContenido" v-on:click="clickCarta">


				<div class="cartaFront">

					<img v-bind:class="front[random].img" :src="getImgUrl(front[random].img)">
							

				</div>


				<div class="cartaBack">

					<img v-bind:class="this.backIMG.img" :src="getImgUrl(this.backIMG.img)">

				</div>




			</div>
					

		</div>

    
  </div>

</template>

<script>
  
export default {
  name: 'Carta',
	props: {
	    backIMG: Object,
	    indexNro: Number,
	    bus: Object
	},
	data(){
    return{

    	front: [

    		{img: "elon"},
    		{img: "elon2"},

    	],

    	random: 0,

    	elemento: null,

    }
	},
	mounted: function () {

		this.random = Math.floor(Math.random() * 2);

		this.bus.$on('primera'+this.indexNro, this.primera)

		this.bus.$on('primera2'+this.indexNro, this.primera2)

		this.bus.$on('segunda'+this.indexNro, this.segunda)

		this.bus.$on('segunda2'+this.indexNro, this.segunda2)

	},
	methods: {

		getImgUrl(empresa) {

		    var images = require.context('../assets/', false, /\.png$/);

		    return images('./' + empresa + ".png");

		},

		sleep(ms) {
		  return new Promise(resolve => setTimeout(resolve, ms));
		},

		async primera2(){

			let elementoo = this.elemento;

			await this.sleep(2000);

			elementoo.style.transform = "rotateY(0deg)";

		},

		async segunda2(){

			let elementoo = this.elemento;

			await this.sleep(2000);

			elementoo.style.transform = "rotateY(0deg)";

		},

		segunda(){

			let elementoo = this.elemento;

			elementoo.style.transform = "rotateY(180deg)";

		},

		primera(){

			let elementoo = this.elemento;

			elementoo.style.transform = "rotateY(180deg)";

		},

	   	clickCarta(event){

	   				this.elemento = event.currentTarget;

				    let indx = this.indexNro;

				    let tipo = this.backIMG.img;

				    this.$parent.clickCarta(indx, tipo);
		

	   	},

	},


}
</script>


<style scoped>


	.tesla{
		width: 100%;
		margin-top: 15px;
	}

	.boring{
		width: 90%;
		margin-top: 45px;
	}

	.solar{
		width: 90%;
	}

	.solar{
		margin-top: 70px;
	}

	.spaceX02{
		width: 90%;
		margin-top: 70px;
		margin-left: 15px;
	}

	.elon{
		width: 100%;
		margin-top: 10px;
	}

	.elon2{
		width: 80%;
		margin-top: 10px;
	}


	.cartaContenedor {
		background-color: rgba(51,204,0,0.5);
		min-height: 200px;
		max-width: 175px;
		border: 2px solid rgba(51,204,0,0.5);
		border-radius: 10px;
		perspective: 1000px; 
	}

	.cartaContenido {
	  position: relative;
	  width: 100%;
	  height: 100%;
	  text-align: center;
	  transition: transform 0.8s;
	  transform-style: preserve-3d;
	}

	.cartaFront, .cartaBack {
	  position: absolute;
	  width: 100%;
	  height: 100%;
	  -webkit-backface-visibility: hidden;
	  backface-visibility: hidden;
	}

	.cartaFront {
	  background-color: rgba(51,204,0,0.5);
	}

	.cartaBack {
	  background-color: rgba(51,204,0,0.5);
	  transform: rotateY(180deg);
	}


</style>
