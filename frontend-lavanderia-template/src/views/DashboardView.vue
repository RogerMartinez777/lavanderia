<template>
  <!-- Contenedor principal del dashboard con el fondo degradado -->
  <div class="min-h-screen flex text-gray-800" style="background: linear-gradient(135deg, #4b5a6c, #a7b7c5);">
    
    <!-- Sidebar de navegación -->
    <aside class="w-64 bg-gray-100 shadow-xl p-6 space-y-6 rounded-tr-3xl rounded-br-3xl">
      <div class="text-center">
        <h2 class="text-2xl font-bold text-gray-800">Lavandería Beatriz</h2>
        <p class="text-sm text-gray-500">Panel de Control</p>
      </div>
      <nav class="space-y-3">
        <router-link
          to="/clientes"
          class="block w-full text-left px-4 py-2 rounded-lg bg-purple-100 text-purple-800 hover:bg-purple-200 transition">
          🧑‍🤝‍🧑 Clientes
        </router-link>
        <router-link
          to="/acolchados"
          class="block w-full text-left px-4 py-2 rounded-lg bg-purple-100 text-purple-800 hover:bg-purple-200 transition">
          🛏️ Acolchados
        </router-link>
        <button class="w-full text-left px-4 py-2 rounded-lg bg-purple-100 text-purple-800 hover:bg-purple-200 transition">
          🧺 Lavados
        </button>
        <button class="w-full text-left px-4 py-2 rounded-lg bg-purple-100 text-purple-800 hover:bg-purple-200 transition">
          💳 Cobros
        </button>
        <button class="w-full text-left px-4 py-2 rounded-lg bg-purple-100 text-purple-800 hover:bg-purple-200 transition">
          🧺 Lavarropas
        </button>
        <button class="w-full text-left px-4 py-2 rounded-lg bg-purple-100 text-purple-800 hover:bg-purple-200 transition">
          🧴 Insumos
        </button>

        <!-- Botón para abrir el modal de Gestión de Servicios y Precios -->
        <button
          @click="showServiceConfigModal = true"
          class="w-full text-left px-4 py-2 rounded-lg bg-green-100 text-green-800 hover:bg-green-200 transition mt-6">
          ⚙️ Gestión Servicios y Precios
        </button>

        <!-- Botón de Cerrar Sesión con la nueva función -->
        <button @click="logout" class="w-full text-left px-4 py-2 rounded-lg bg-red-100 text-red-800 hover:bg-red-200 transition mt-6">
          🚪 Cerrar Sesión
        </button>
      </nav>
    </aside>

    <!-- Contenido principal (donde está el clima, etc.) -->
    <main class="flex-1 p-6">
      
      <!-- Panel blanco para el encabezado y logo -->
      <div class="mb-6 p-6 bg-white rounded-xl shadow-lg">
        <!-- Encabezado con logo y título -->
        <div class="text-center mb-8">
          <!-- El logo de la lavandería con el nuevo ícono de la remera -->
          <div class="inline-flex items-center justify-center rounded-full p-3 mb-2" style="background-color: #5b21b6;">
            <img src="/shirt-icon.svg" alt="Ícono de remera de Lavandería" class="h-10 w-10 text-white" />
          </div>
          <h1 class="text-4xl font-bold text-gray-800" style="color: #5b21b6;">Lavandería Beatriz</h1>
          <p class="text-lg text-gray-500">Sistema de Gestión de Clientes</p>
        </div>

        <!-- Contenedor para las tarjetas de estadísticas -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          
          <!-- Panel de Total Clientes -->
          <div class="p-6 rounded-2xl shadow-xl flex flex-col justify-between" style="background: linear-gradient(to right, #4c28bc, #7b58e7);">
            <div>
              <div class="flex items-center text-white mb-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h-4v-2a4 4 0 00-4-4H7a4 4 0 00-4 4v2h4" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 12a4 4 0 100-8 4 4 0 000 8zM5 20h14" />
                </svg>
                <h3 class="text-xl font-semibold">Total Clientes</h3>
              </div>
              <p class="text-sm text-gray-200">Clientes registrados</p>
            </div>
            <div class="mt-4 flex justify-between items-center text-white">
              <span class="text-4xl font-bold">128</span> <!-- Dato simulado -->
              <span class="flex items-center text-gray-200">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Activos
              </span>
            </div>
          </div>

          <!-- Panel de Clientes Premium -->
          <div class="p-6 rounded-2xl shadow-xl flex flex-col justify-between" style="background: linear-gradient(to right, #f59e0b, #fcd34d);">
            <div>
              <div class="flex items-center text-white mb-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7 4 7-4v-4l-7-4-7 4v4z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l-7-4v-4l7-4 7 4v4l-7 4z" />
                </svg>
                <h3 class="text-xl font-semibold">Clientes Premium</h3>
              </div>
              <p class="text-sm text-gray-800">Membresía Premium</p>
            </div>
            <div class="mt-4 flex justify-between items-center text-white">
              <span class="text-4xl font-bold">15</span> <!-- Dato simulado -->
              <span class="flex items-center text-gray-800">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.503 4.631a1 1 0 00.95.69h4.873c.969 0 1.371 1.24.588 1.81l-3.945 2.873a1 1 0 00-.364 1.118l1.503 4.631c.3.921-.755 1.688-1.54 1.118l-3.945-2.873a1 1 0 00-1.176 0l-3.945 2.873c-.785.57-1.84-.197-1.54-1.118l1.503-4.631a1 1 0 00-.364-1.118L2.52 9.558c-.783-.57-.381-1.81.588-1.81h4.873a1 1 0 00.95-.69l1.503-4.63z" />
                </svg>
                VIP
              </span>
            </div>
          </div>

          <!-- Panel de Clientes Corporativos -->
          <div class="p-6 rounded-2xl shadow-xl flex flex-col justify-between" style="background: linear-gradient(to right, #10b981, #34d399);">
            <div>
              <div class="flex items-center text-white mb-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 21.75c-2.485 0-4.5-2.015-4.5-4.5s2.015-4.5 4.5-4.5 4.5 2.015 4.5 4.5-2.015 4.5-4.5 4.5zm0-16.5c-2.485 0-4.5-2.015-4.5-4.5s2.015-4.5 4.5-4.5 4.5 2.015 4.5 4.5-2.015 4.5-4.5 4.5z" />
                </svg>
                <h3 class="text-xl font-semibold">Clientes Corporativos</h3>
              </div>
              <p class="text-sm text-gray-200">Empresas y organizaciones</p>
            </div>
            <div class="mt-4 flex justify-between items-center text-white">
              <span class="text-4xl font-bold">5</span> <!-- Dato simulado -->
              <span class="flex items-center text-gray-200">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21h-2a2 2 0 01-2-2v-4a2 2 0 012-2h2a2 2 0 012 2v4a2 2 0 01-2 2z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 11V9a2 2 0 00-2-2H9a2 2 0 00-2 2v2" />
                </svg>
                Empresas
              </span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Contenedor del clima -->
      <div class="bg-blue-100 p-6 rounded-xl shadow-md flex flex-col items-center text-center max-w-sm mx-auto mb-6 relative">
        <h2 class="text-2xl font-bold text-purple-700">Clima en la ciudad de Cordoba</h2>
        <img
          :src="`https://openweathermap.org/img/wn/${clima?.icon}@4x.png`"
          :alt="clima?.descripcion"
          class="w-32 h-32 mb-4"
        />

        <div v-if="mostrarNieve" class="absolute inset-0 pointer-events-none z-20 overflow-hidden">
          <div v-for="n in 20" :key="n"
            class="snowflake"
            :style="{
              left: `${Math.random() * 100}%`,
              animationDuration: `${Math.random() * 5 + 3}s`,
              animationDelay: `${Math.random() * 5}s`
            }">
            ❄️
          </div>
        </div>
        
        <svg v-if="mostrarSol" id="sun-animation" width="100" height="100" viewBox="0 0 100 100" class="absolute right-0 top-0 z-10 opacity-80">
          <circle cx="50" cy="50" r="20" fill="yellow"></circle>
        </svg>

        <svg v-if="mostrarNubes" id="cloud-animation"
          width="200" height="100" viewBox="0 0 150 80"
          class="absolute top-1/4 z-10 opacity-70"> <path fill="#ffffff" d="M140 50 A30 30 0 0 0 110 20 A20 20 0 0 0 90 0 A30 30 0 0 0 60 30 A30 30 0 0 0 30 0 A20 20 0 0 0 10 20 A30 30 0 0 0 0 50 C0 65 15 80 30 80 H140 C125 80 140 65 140 50 Z"/>
        </svg>

        <h2 class="text-4xl font-bold text-blue-800">{{ clima?.temperatura }}°C</h2>
        <p class="text-lg text-gray-700 capitalize">{{ clima?.descripcion }}</p>
        <p class="text-sm text-gray-500 mt-1">🌡️ Sensación térmica: {{ clima?.sensacion_termica }}°C</p>
        <p class="text-sm text-gray-500 mt-1">💨 Viento: {{ clima?.viento }} km/h</p>
        <p class="text-sm text-gray-500 mt-2">{{ ciudad }} - {{ fechaActual }}</p>
      </div>
    </main>

    <!--
      El componente del modal se renderiza aquí, fuera del <main>.
      El modal tiene estilos para posicionarse sobre todo el dashboard
      y oscurecer el fondo, manteniendo el sidebar y el fondo visibles.
    -->
    <ServiceConfigView v-if="showServiceConfigModal" @close="showServiceConfigModal = false" />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref, onMounted, watch, nextTick } from 'vue';
import axios from 'axios';
import * as anime from 'animejs';

import ServiceConfigView from '@/views/config/ServiceConfigView.vue';

// Se mantiene el router para otras funciones si las hubiera, pero no se usa en logout
const router = useRouter(); 

const showServiceConfigModal = ref(false);
const clima = ref(null);
const mostrarNieve = ref(false);
const mostrarSol = ref(false);
const mostrarNubes = ref(false);
const ciudad = 'Córdoba,AR';
const apiKey = '63625d5981558769a6d3ad2c3676dc2a';

const animateSun = () => {
  const sunElement = document.getElementById('sun-animation');
  if (sunElement && anime.default) {
    anime.default({
      targets: sunElement,
      rotate: '360deg',
      scale: [1, 1.1, 1],
      duration: 8000,
      easing: 'linear',
      loop: true
    });
  }
};

const animateCloud = () => {
    const cloudElement = document.getElementById('cloud-animation');
    const container = document.querySelector('.max-w-sm');

    if (cloudElement && container && anime.default) {
        const containerWidth = container.offsetWidth;

        anime.default({
            targets: cloudElement,
            translateX: [-500, containerWidth + 500],
            duration: 5000,
            easing: 'linear',
            loop: true,
            direction: 'alternate'
        });
    }
};

const fechaActual = new Date().toLocaleDateString('es-AR', {
  weekday: 'long',
  year: 'numeric',
  month: 'long',
  day: 'numeric'
});

onMounted(async () => {
  try {
    const response = await axios.get(
      `https://api.openweathermap.org/data/2.5/weather?q=${ciudad}&appid=${apiKey}&units=metric&lang=es`
    );

    const datos = response.data;
    clima.value = {
      temperatura: Math.round(datos.main.temp),
      sensacion_termica: Math.round(datos.main.feels_like),
      descripcion: datos.weather[0].description,
      icon: datos.weather[0].icon,
      viento: Math.round(datos.wind.speed * 3.6)
    };

    clima.value.icon = '04d';
    clima.value.descripcion = 'nublado con nubes densas';

  } catch (err) {
    console.error('Error al obtener el clima:', err);
  }
});

watch(clima, async (newClima) => {
  if (anime.default) {
    anime.default.remove('#sun-animation');
    anime.default.remove('#cloud-animation');
  }

  mostrarSol.value = false;
  mostrarNubes.value = false;
  mostrarNieve.value = false;

  if (!newClima) return;

  const icon = newClima.icon;

  mostrarNieve.value = ['13d', '13n'].includes(icon);

  if (icon === '01d') {
    mostrarSol.value = true;
    await nextTick();
    setTimeout(() => animateSun(), 50);
  }

  if (['02d', '02n', '03d', '04d', '03n', '04n'].includes(icon)) {
    mostrarNubes.value = true;
    await nextTick();
    setTimeout(() => {
    const cloudElement = document.getElementById('cloud-animation');
    if (cloudElement) animateCloud();
    }, 300);
  }
}, { immediate: true });

// 🟢 FUNCIÓN `logout` MODIFICADA para redirigir a la URL raíz
const logout = () => {
  // Limpia el token de autenticación
  localStorage.removeItem('authToken');
  // 🟢 Usa window.location.href para forzar una redirección del navegador completa a la URL raíz
  window.location.href = '/'; 
};
</script>

<style scoped>
.snowflake {
  position: absolute;
  top: -2rem;
  font-size: 1.5rem;
  color: white;
  animation-name: fall;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
}

@keyframes fall {
  0% {
    transform: translateY(0) rotate(0deg);
    opacity: 1;
  }
  100% {
    transform: translateY(120vh) rotate(360deg);
    opacity: 0;
  }
}
</style>