import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/jugar/:nombre',
    name: 'Jugar',
    component: () => import('../views/Jugar.vue')
  },
  {
    path: '/tabla/:nombre',
    name: 'Tabla',
    component: () => import('../views/Tabla.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
