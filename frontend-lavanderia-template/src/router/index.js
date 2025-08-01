// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import DashboardView from '../views/DashboardView.vue'
import ClientesView from '../views/ClientesView.vue'
import ClientesAltaView from '../views/ClientesAltaView.vue'

const routes = [
  { path: '/', name: 'Login', component: LoginView },
  { path: '/dashboard', name: 'Dashboard', component: DashboardView },
  { path: '/clientes', name: 'Clientes', component: ClientesView },
  { path: '/clientes/alta', name: 'AltaClientes', component: ClientesAltaView},
  { path: '/', redirect: '/login'}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
