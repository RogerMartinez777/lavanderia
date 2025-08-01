<template>
  <!-- Overlay principal del modal con fondo semi-transparente que cubre toda la pantalla -->
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 transition-opacity duration-300">
    <!-- Contenedor del modal, ahora más compacto -->
    <div class="bg-white p-5 rounded-lg shadow-2xl max-w-2xl w-full mx-4 transition-transform duration-300 transform scale-95">
      <!-- Encabezado del modal con nuevo estilo -->
      <div class="flex justify-between items-center px-4 py-3 rounded-t-lg" style="background-color: #2C3E50;">
        <h2 class="text-xl font-bold text-white">Gestión de Servicios y Precios</h2>
        <button @click="cerrarModal" class="text-white hover:text-gray-300 transition">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Sistema de pestañas -->
      <div class="border-b border-gray-200 mt-4">
        <nav class="-mb-px flex space-x-6 px-4" aria-label="Tabs">
          <button
            @click="activeTab = 'categorias'"
            :class="[
              'whitespace-nowrap py-2 px-1 border-b-2 text-sm',
              activeTab === 'categorias'
                ? 'border-indigo-500 text-indigo-600 font-medium'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
            ]">
            Categorías
          </button>
          <button
            @click="activeTab = 'tamanios'"
            :class="[
              'whitespace-nowrap py-2 px-1 border-b-2 text-sm',
              activeTab === 'tamanios'
                ? 'border-indigo-500 text-indigo-600 font-medium'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
            ]">
            Tamaños
          </button>
          <button
            @click="activeTab = 'precios'"
            :class="[
              'whitespace-nowrap py-2 px-1 border-b-2 text-sm',
              activeTab === 'precios'
                ? 'border-indigo-500 text-indigo-600 font-medium'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
            ]">
            Precios Vigentes
          </button>
        </nav>
      </div>

      <!-- Contenido de la pestaña activa -->
      <div class="mt-4 p-3 bg-gray-50 rounded-lg">
        <!-- Pestaña: Categorías de Servicio -->
        <div v-if="activeTab === 'categorias'">
          <h3 class="text-lg font-semibold text-gray-700 mb-3">Lista de Categorías</h3>
          <div class="space-y-2 max-h-64 overflow-y-auto">
            <div
              v-for="categoria in categorias"
              :key="categoria.id"
              class="flex justify-between items-center bg-gray-100 p-2 rounded-lg shadow-sm">
              <span class="text-sm text-gray-700">{{ categoria.nombre }}</span>
            </div>
          </div>
          
          <div class="mt-4 pt-3 border-t border-gray-200">
            <h3 class="text-md font-semibold text-gray-700 mb-3">Nueva Categoría</h3>
            <div class="flex gap-3">
              <input
                type="text"
                v-model="nuevaCategoria"
                placeholder="Nombre de la nueva categoría"
                class="flex-1 px-3 py-1 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
              <button
                @click="agregarCategoria"
                class="px-4 py-1 bg-indigo-600 text-white text-sm rounded-lg hover:bg-indigo-700 transition">
                Agregar
              </button>
            </div>
          </div>
        </div>

        <!-- Pestaña: Tamaños -->
        <div v-if="activeTab === 'tamanios'">
          <h3 class="text-lg font-semibold text-gray-700 mb-3">Lista de Tamaños</h3>
          <div class="space-y-2 max-h-64 overflow-y-auto">
            <div
              v-for="tamanio in tamanios"
              :key="tamanio.id"
              class="flex justify-between items-center bg-gray-100 p-2 rounded-lg shadow-sm">
              <span class="text-sm text-gray-700">{{ tamanio.nombre }}</span>
            </div>
          </div>

          <div class="mt-4 pt-3 border-t border-gray-200">
            <h3 class="text-md font-semibold text-gray-700 mb-3">Nuevo Tamaño</h3>
            <div class="flex gap-3">
              <input
                type="text"
                v-model="nuevoTamanio"
                placeholder="Nombre del nuevo tamaño"
                class="flex-1 px-3 py-1 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
              <button
                @click="agregarTamanio"
                class="px-4 py-1 bg-indigo-600 text-white text-sm rounded-lg hover:bg-indigo-700 transition">
                Agregar
              </button>
            </div>
          </div>
        </div>

        <!-- Pestaña: Precios Vigentes (MEJORADA) -->
        <div v-if="activeTab === 'precios'">
          <h3 class="text-lg font-semibold text-gray-700 mb-3">Lista de Precios Vigentes</h3>
          
          <!-- Filtro de búsqueda -->
          <div class="mb-3">
            <input
              type="text"
              v-model="filtroPrecio"
              placeholder="Buscar por categoría o tamaño..."
              class="w-full px-3 py-1 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
          </div>

          <!-- Mensaje de confirmación o error -->
          <div v-if="mensajeConfirmacion" :class="`p-2 mb-3 text-sm text-center rounded-lg ${mensajeConfirmacion.type === 'success' ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'}`">
            {{ mensajeConfirmacion.text }}
          </div>
          
          <!-- Contenedor con scroll para la tabla -->
          <div class="max-h-64 overflow-y-auto rounded-lg shadow-sm border border-gray-200">
            <!-- Tabla de Precios -->
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-100 sticky top-0">
                <tr>
                  <th scope="col" class="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Categoría</th>
                  <th scope="col" class="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Tamaño</th>
                  <th scope="col" class="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Precio</th>
                  <th scope="col" class="relative px-4 py-2">
                    <span class="sr-only">Acciones</span>
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="precio in preciosVigentesFiltrados" :key="precio.id">
                  <td class="px-4 py-2 whitespace-nowrap text-sm font-medium text-gray-900">{{ precio.categoria.nombre }}</td>
                  <td class="px-4 py-2 whitespace-nowrap text-sm text-gray-500">{{ precio.tamanio ? precio.tamanio.nombre : 'N/A' }}</td>
                  <td class="px-4 py-2 whitespace-nowrap text-sm text-green-700 font-bold">${{ precio.precio.toFixed(2) }}</td>
                  <td class="px-4 py-2 whitespace-nowrap text-right text-sm font-medium">
                    <button @click="confirmarEliminacion(precio.id)" class="text-red-600 hover:text-red-900 transition-colors">
                      Eliminar
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Formulario de Nuevo Precio -->
          <div class="mt-4 pt-3 border-t border-gray-200">
            <h3 class="text-md font-semibold text-gray-700 mb-3">Nuevo Precio</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
              <!-- Selector de Categoría -->
              <div>
                <label for="select-categoria" class="block text-xs font-medium text-gray-700">Categoría</label>
                <select id="select-categoria"
                  v-model="selectedCategoriaId"
                  class="mt-1 block w-full px-3 py-1 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
                  <option disabled value="">Seleccione...</option>
                  <option v-for="categoria in categorias" :key="categoria.id" :value="categoria.id">
                    {{ categoria.nombre }}
                  </option>
                </select>
              </div>

              <!-- Selector de Tamaño -->
              <div>
                <label for="select-tamanio" class="block text-xs font-medium text-gray-700">Tamaño (opc.)</label>
                <select id="select-tamanio"
                  v-model="selectedTamanioId"
                  class="mt-1 block w-full px-3 py-1 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
                  <option :value="null">Sin tamaño</option>
                  <option v-for="tamanio in tamanios" :key="tamanio.id" :value="tamanio.id">
                    {{ tamanio.nombre }}
                  </option>
                </select>
              </div>

              <!-- Input de Precio -->
              <div>
                <label for="input-precio" class="block text-xs font-medium text-gray-700">Precio</label>
                <input
                  id="input-precio"
                  type="number"
                  v-model="nuevoPrecio"
                  placeholder="0.00"
                  class="mt-1 block w-full px-3 py-1 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
              </div>
            </div>
            <div class="flex justify-end gap-3 mt-3">
              <!-- Botón Cancelar agregado aquí -->
              <button @click="cerrarModal" class="px-4 py-1 bg-gray-200 text-gray-700 text-sm rounded-lg hover:bg-gray-300 transition">
                Cancelar
              </button>
              <button
                @click="agregarPrecioVigente"
                class="px-4 py-1 bg-green-600 text-white text-sm rounded-lg hover:bg-green-700 transition">
                Guardar Precio
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal de confirmación para eliminar precio -->
  <div v-if="showConfirmation" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-[60] transition-opacity duration-300">
    <div class="bg-white p-6 rounded-lg shadow-2xl max-w-sm w-full mx-4 transform scale-100 transition-transform duration-300">
      <h3 class="text-lg font-bold text-gray-800 mb-4">Confirmar Eliminación</h3>
      <p class="text-sm text-gray-600 mb-6">¿Estás seguro de que deseas eliminar este precio?</p>
      <div class="flex justify-end gap-3">
        <button @click="cancelarEliminacion" class="px-4 py-2 bg-gray-200 text-gray-700 text-sm rounded-lg hover:bg-gray-300 transition">
          Cancelar
        </button>
        <button @click="eliminarPrecioVigente(precioAEliminarId)" class="px-4 py-2 bg-red-600 text-white text-sm rounded-lg hover:bg-red-700 transition">
          Eliminar
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';

// Define los eventos que este componente puede emitir, en este caso, 'close'
const emit = defineEmits(['close']);

// URL base de tu backend. Asegúrate de actualizarla con tu dirección real
const API_BASE_URL = 'http://localhost:8000'; 

// Estado reactivo para la pestaña activa del modal
const activeTab = ref('categorias');

// Estado reactivo para la lista de categorías
const categorias = ref([]);

// Estado reactivo para el campo de texto de la nueva categoría
const nuevaCategoria = ref('');

// Estado reactivo para la lista de tamaños
const tamanios = ref([]);

// Estado reactivo para el campo de texto del nuevo tamaño
const nuevoTamanio = ref('');

// Estado reactivo para la lista de precios vigentes
const preciosVigentes = ref([]);

// Estado reactivo para los campos del formulario de nuevo precio
const selectedCategoriaId = ref(null);
const selectedTamanioId = ref(null);
const nuevoPrecio = ref(null);

// Estado para el filtro de precios
const filtroPrecio = ref('');

// Estado para mensajes de confirmación o error en la UI
const mensajeConfirmacion = ref(null);

// Estados para el modal de confirmación de eliminación
const showConfirmation = ref(false);
const precioAEliminarId = ref(null);

// Propiedad computada para filtrar los precios
const preciosVigentesFiltrados = computed(() => {
  if (!filtroPrecio.value) {
    return preciosVigentes.value;
  }
  const filtro = filtroPrecio.value.toLowerCase();
  return preciosVigentes.value.filter(precio => {
    const categoriaNombre = precio.categoria.nombre.toLowerCase();
    const tamanioNombre = precio.tamanio ? precio.tamanio.nombre.toLowerCase() : '';
    return categoriaNombre.includes(filtro) || tamanioNombre.includes(filtro);
  });
});

// Función para mostrar un mensaje temporal
const mostrarMensaje = (texto, tipo) => {
  mensajeConfirmacion.value = { text: texto, type: tipo };
  setTimeout(() => {
    mensajeConfirmacion.value = null;
  }, 3000); // El mensaje desaparece después de 3 segundos
};

// Función para obtener las categorías de servicio del backend
const fetchCategorias = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/servicios/categorias/`);
    categorias.value = response.data;
  } catch (error) {
    console.error('Error al obtener las categorías:', error);
  }
};

// Función para agregar una nueva categoría al backend
const agregarCategoria = async () => {
  if (nuevaCategoria.value.trim() === '') {
    mostrarMensaje('El nombre de la categoría no puede estar vacío.', 'error');
    return;
  }
  try {
    const response = await axios.post(`${API_BASE_URL}/servicios/categorias/`, {
      nombre: nuevaCategoria.value
    });
    // Si la adición es exitosa, se refresca la lista
    if (response.status === 201) {
      await fetchCategorias();
      // Y se limpia el campo de entrada
      nuevaCategoria.value = '';
      mostrarMensaje('Categoría agregada con éxito.', 'success');
    }
  } catch (error) {
    console.error('Error al agregar la categoría:', error);
    mostrarMensaje('Hubo un error al agregar la categoría.', 'error');
  }
};

// Función para obtener los tamaños del backend
const fetchTamanios = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/servicios/tamanios/`);
    tamanios.value = response.data;
  } catch (error) {
    console.error('Error al obtener los tamaños:', error);
  }
};

// Función para agregar un nuevo tamaño al backend
const agregarTamanio = async () => {
  if (nuevoTamanio.value.trim() === '') {
    mostrarMensaje('El nombre del tamaño no puede estar vacío.', 'error');
    return;
  }
  try {
    const response = await axios.post(`${API_BASE_URL}/servicios/tamanios/`, {
      nombre: nuevoTamanio.value
    });
    // Si la adición es exitosa, se refresca la lista
    if (response.status === 201) {
      await fetchTamanios();
      // Y se limpia el campo de entrada
      nuevoTamanio.value = '';
      mostrarMensaje('Tamaño agregado con éxito.', 'success');
    }
  } catch (error) {
    console.error('Error al agregar el tamaño:', error);
    mostrarMensaje('Hubo un error al agregar el tamaño.', 'error');
  }
};

// Función para obtener los precios vigentes del backend
const fetchPreciosVigentes = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/servicios/precios_vigentes/`);
    preciosVigentes.value = response.data;
  } catch (error) {
    console.error('Error al obtener los precios vigentes:', error);
  }
};

// Función para agregar un nuevo precio vigente
const agregarPrecioVigente = async () => {
  // Validaciones
  if (!selectedCategoriaId.value) {
    mostrarMensaje('Debe seleccionar una categoría.', 'error');
    return;
  }
  if (!nuevoPrecio.value || nuevoPrecio.value <= 0) {
    mostrarMensaje('Debe ingresar un precio válido.', 'error');
    return;
  }

  // Prepara el payload con el ID del tamaño si está seleccionado
  const payload = {
    categoria_id: selectedCategoriaId.value,
    tamanio_id: selectedTamanioId.value, // Puede ser null
    precio: nuevoPrecio.value
  };

  try {
    const response = await axios.post(`${API_BASE_URL}/servicios/precios_vigentes/`, payload);
    if (response.status === 201) {
      await fetchPreciosVigentes();
      // Limpia el formulario
      selectedCategoriaId.value = null;
      selectedTamanioId.value = null;
      nuevoPrecio.value = null;
      mostrarMensaje('Precio agregado con éxito.', 'success');
    }
  } catch (error) {
    console.error('Error al agregar el precio:', error);
    if (error.response && error.response.status === 409) {
      mostrarMensaje('Ya existe un precio para esta combinación de categoría y tamaño.', 'error');
    } else {
      mostrarMensaje('Hubo un error al agregar el precio.', 'error');
    }
  }
};

// Función para mostrar el modal de confirmación
const confirmarEliminacion = (precioId) => {
  precioAEliminarId.value = precioId;
  showConfirmation.value = true;
};

// Función para cancelar la eliminación
const cancelarEliminacion = () => {
  showConfirmation.value = false;
  precioAEliminarId.value = null;
};


// Función para eliminar un precio vigente
const eliminarPrecioVigente = async (precioId) => {
  try {
    await axios.delete(`${API_BASE_URL}/servicios/precios_vigentes/${precioId}`);
    // Oculta el modal de confirmación
    showConfirmation.value = false;
    // Actualiza la lista de precios después de la eliminación
    await fetchPreciosVigentes();
    mostrarMensaje('Precio eliminado con éxito.', 'success');
  } catch (error) {
    console.error('Error al eliminar el precio:', error);
    mostrarMensaje('Hubo un error al eliminar el precio.', 'error');
  }
};

// Nueva función para cerrar el modal y limpiar el formulario de precios
const cerrarModal = () => {
  // Limpia los campos del formulario de precios al cerrar
  selectedCategoriaId.value = null;
  selectedTamanioId.value = null;
  nuevoPrecio.value = null;
  // Emite el evento para cerrar el modal
  emit('close');
};

// Se ejecuta al montar el componente para cargar todos los datos iniciales
onMounted(() => {
  fetchCategorias();
  fetchTamanios();
  fetchPreciosVigentes();
});
</script>

<style scoped>
/* Estilos para el overlay del modal y el contenido */
.fixed.inset-0 {
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 50;
}
/* Asegura que el thead permanezca visible al hacer scroll */
.sticky.top-0 {
  position: sticky;
  top: 0;
  z-index: 10;
}
</style>
