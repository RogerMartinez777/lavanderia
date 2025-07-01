<template>
  <div class="min-h-screen flex bg-[#1e2235] text-gray-800">
    <!-- Sidebar -->
    <aside class="w-64 bg-white shadow-xl p-6 space-y-6 rounded-tr-3xl rounded-br-3xl">
      <div class="text-center">
        <h2 class="text-2xl font-bold text-purple-700">Lavandería Beatriz</h2>
        <p class="text-sm text-gray-500">Panel de Control</p>
      </div>
      <nav class="space-y-3">
        <router-link
          to="/dashboard"
          class="block px-4 py-2 rounded-lg bg-purple-100 text-purple-800 hover:bg-purple-200 transition"
        >
          📊 Dashboard
        </router-link>
        <router-link
          to="/clientes"
          class="block px-4 py-2 rounded-lg bg-purple-100 text-purple-800 hover:bg-purple-200 transition"
        >
          🧑‍🤝‍🧑 Clientes
        </router-link>
        <router-link
          to="/clientes/alta"
          class="block px-4 py-2 rounded-lg bg-purple-200 text-purple-900 font-semibold transition"
        >
          ➕ Alta de Clientes
        </router-link>
      </nav>
    </aside>

    <!-- Main content -->
    <main class="flex-1 p-10 text-white">
      <div class="flex justify-between items-center mb-6">
        <h1 class="text-3xl font-bold">🧑‍🤝‍🧑 Gestión de Clientes</h1>
      </div>
      <div class="bg-white p-6 rounded-xl shadow-lg text-gray-800 max-w-xl">
        <h2 class="text-xl font-semibold mb-4 text-indigo-700">Alta de Clientes</h2>
        <div class="mb-6"></div> <form @submit.prevent="crearCliente">
          <div class="mb-4">
            <label class="block text-purple-800 font-medium mb-2">Nombre</label>
            <input v-model="cliente.nombre" type="text" class="w-full px-4 py-2 border rounded-lg" required />
          </div>
          <div class="mb-4">
            <label class="block text-purple-800 font-medium mb-2">Apellido</label>
            <input v-model="cliente.apellido" type="text" class="w-full px-4 py-2 border rounded-lg" required />
          </div>
          <div class="mb-4">
            <label class="block text-purple-800 font-medium mb-2">Teléfono</label>
            <input v-model="cliente.telefono" type="text" class="w-full px-4 py-2 border rounded-lg" required />
          </div>
          <div class="mb-4">
            <label class="block text-purple-800 font-medium mb-2">Email</label>
            <input v-model="cliente.mail" type="email" class="w-full px-4 py-2 border rounded-lg" required />
          </div>
          <div class="mb-4">
            <label class="block text-purple-800 font-medium mb-2">Notas</label>
            <input v-model="cliente.nota" type="text" class="w-full px-4 py-2 border rounded-lg" required />
          </div>
          <button
            type="submit"
            class="bg-purple-700 text-white px-6 py-2 rounded-lg hover:bg-purple-800 transition"
          >
            Crear Cliente
          </button>
        </form>
        <p v-if="mensaje" class="mt-4 text-green-600 font-semibold">{{ mensaje }}</p>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()

const cliente = ref({
  nombre: '',
  apellido: '',
  telefono: '',
  mail: '',
  nota: ''
})

const mensaje = ref('')

const crearCliente = async () => {
  try {
    const response = await axios.post('http://192.168.100.132:8000/clientes', cliente.value)
    mensaje.value = 'Cliente creado exitosamente ✔️'
    setTimeout(() => {
      router.push('/clientes')
    }, 1500)
  } catch (error) {
    console.error('Error al crear cliente:', error)
    mensaje.value = 'Error al crear cliente ❌'
  }
}
</script>
