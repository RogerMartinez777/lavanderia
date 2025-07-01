<template>
  <div class="min-h-screen flex bg-[#1e2235] text-gray-800">
    <aside class="w-64 bg-white shadow-xl p-6 space-y-6 rounded-tr-3xl rounded-br-3xl">
      <div class="text-center">
        <h2 class="text-2xl font-bold text-purple-700">Lavandería Beatriz</h2>
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
      </nav>
    </aside>

    <main class="flex-1 p-10">
      <div class="bg-blue-100 p-6 rounded-xl shadow-md flex flex-col items-center text-center max-w-sm mx-auto mb-8 ml-10 relative">
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
  </div>
</template>

<script setup>
import { ref, onMounted, watch, nextTick } from 'vue';
import axios from 'axios';
import * as anime from 'animejs'; // Mantener esta importación

const clima = ref(null);
const mostrarNieve = ref(false);
const mostrarSol = ref(false);
const mostrarNubes = ref(false);
const ciudad = 'Córdoba,AR';
const apiKey = '63625d5981558769a6d3ad2c3676dc2a';

// Función para animar el sol
const animateSun = () => {
  const sunElement = document.getElementById('sun-animation');
  if (sunElement && anime.default) { // ¡Añadir verificación de anime.default!
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

// Función para animar las nubes
const animateCloud = () => {
    const cloudElement = document.getElementById('cloud-animation');
    const container = document.querySelector('.max-w-sm'); // Tu tarjeta del clima

    if (cloudElement && container && anime.default) {
        const containerWidth = container.offsetWidth; // Ancho de la tarjeta

        anime.default({
            targets: cloudElement,
            // Empieza MUY a la izquierda, termina MUY a la derecha.
            // Esto es relativo a la posición actual del elemento (que ahora será el centro de la tarjeta si no tiene 'left' en CSS)
            translateX: [-500, containerWidth + 500], // Mueve desde 500px antes del borde izq. hasta 500px después del borde derecho
            duration: 5000, // Duración más rápida para ver el movimiento de inmediato
            easing: 'linear',
            loop: true,
            direction: 'alternate' // Para que vaya y venga
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
      viento: Math.round(datos.wind.speed * 3.6) // m/s a km/h
    };

    // Forzar clima de nieve (solo para pruebas) 
    //clima.value.icon = '13d'
    //clima.value.descripcion = 'nieve ligera'

    // Fuerza nubes para probar
    clima.value.icon = '04d'; // nubes densas de día
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

  // Mostrar nieve si corresponde
  mostrarNieve.value = ['13d', '13n'].includes(icon);

  // Mostrar y animar sol si está despejado de día
  if (icon === '01d') {
    mostrarSol.value = true;
    await nextTick();
    setTimeout(() => animateSun(), 50);
  }

  // Mostrar y animar nubes si hay nubosidad
  // ... dentro del watch
// ... dentro del watch
  if (['02d', '02n', '03d', '04d', '03n', '04n'].includes(icon)) {
    mostrarNubes.value = true;
    await nextTick();
    setTimeout(() => {
    const cloudElement = document.getElementById('cloud-animation');
  if (cloudElement) animateCloud(); // Llama a animateCloud si el elemento existe
    }, 300); // Aumentamos a 300ms
}
}, { immediate: true });


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
