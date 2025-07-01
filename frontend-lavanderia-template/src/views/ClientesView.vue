<template>
  <div class="min-h-screen flex bg-[#1e2235] text-gray-800">
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

        <div>
          <p class="px-4 py-2 text-purple-900 font-semibold">🧑‍🤝‍🧑 Clientes</p>
          <div class="ml-4 space-y-2">
            <router-link
              to="/clientes"
              class="block px-4 py-2 rounded-lg bg-purple-200 text-purple-900 font-semibold transition"
            >
              📋 Listado de clientes
            </router-link>
            <router-link
              to="/clientes/alta"
              class="block px-4 py-2 rounded-lg bg-purple-100 text-purple-800 hover:bg-purple-200 transition"
            >
              ➕ Crear cliente
            </router-link>
          </div>
        </div>
      </nav>
    </aside>

    <main class="flex-1 p-10 text-white">
      <div class="flex justify-between items-center mb-6">
        <h1 class="text-3xl font-bold">🧑‍🤝‍🧑 Gestión de Clientes</h1>
      </div>

      <div class="w-full max-w-3xl bg-white p-6 rounded-lg shadow-md text-gray-800">
        <h2 class="text-xl font-semibold mb-4 text-indigo-700">Listado de Clientes</h2>
        <ul class="divide-y divide-gray-200">
          <li
            v-for="cliente in clientes"
            :key="cliente.id"
            class="py-2 flex justify-between items-center"
          >
            <div>
              <p class="font-medium">{{ cliente.nombre }} {{ cliente.apellido }}</p>
              <p class="text-sm text-gray-500">
                📞 {{ cliente.telefono }} | 📨 {{ cliente.mail }}
              </p>
            </div>
            <div class="space-x-2">
              <button
                @click="consultarCliente(cliente.id)"
                class="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm transition"
              >
                🔍 Consultar
              </button>
              <button
                @click="modificarCliente(cliente.id)"
                class="bg-yellow-500 hover:bg-yellow-600 text-white px-3 py-1 rounded text-sm transition"
                >
                ✏️ Modificar
              </button>
              <button
                @click="eliminarCliente(cliente.id)"
                class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm transition"
              >
                🗑️ Eliminar
              </button>
            </div>
          </li>
        </ul>
        <div class="mt-6">
          <router-link
            to="/clientes/alta"
            class="bg-purple-700 hover:bg-purple-800 text-white px-4 py-2 rounded transition"
          >
            ➕ Crear Cliente
          </router-link>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Swal from 'sweetalert2'; 

const clientes = ref([])

onMounted(async () => {
  try {
    const response = await axios.get('http://192.168.100.132:8000/clientes')
    clientes.value = response.data
  } catch (error) {
    console.error('Error al obtener los clientes:', error)
  }
})

// Función para consultar los detalles de un cliente y mostrarlos en un modal
const consultarCliente = async (id) => {
  // 1. Mostrar un modal de carga mientras se obtienen los datos
  Swal.fire({
    title: 'Cargando...',
    text: 'Obteniendo los detalles del cliente.',
    allowOutsideClick: false,
    didOpen: () => {
      Swal.showLoading(); // Muestra el spinner de carga
    }
  });

  try {
    // 2. Realizar la petición GET al backend para obtener los detalles del cliente
    // Asegúrarse de que el backend tenga una ruta como '/clientes/{id}' que retorne un solo cliente
    const response = await axios.get(`http://192.168.100.132:8000/clientes/${id}`);
    const clienteDetalles = response.data;

    // 3. Cerrar el modal de carga
    Swal.close();

    // 4. Mostrar los detalles del cliente en un nuevo modal de SweetAlert2
    Swal.fire({
      title: `Detalles de ${clienteDetalles.nombre} ${clienteDetalles.apellido}`,
      html: `
        <p><strong>Teléfono:</strong> ${clienteDetalles.telefono}</p>
        <p><strong>Email:</strong> ${clienteDetalles.mail}</p>
        <p><strong>Dirección:</strong> ${clienteDetalles.direccion || 'No especificada'}</p>
        <p><strong>Notas:</strong> ${clienteDetalles.nota || 'Sin notas'}</p>
        `,
      icon: 'info', // O puedes usar 'question' o simplemente no poner icono para un diseño más limpio
      confirmButtonText: 'Cerrar',
      confirmButtonColor: '#3085d6' // Color azul para el botón de cerrar
    });

  } catch (error) {
    // Cerrar el modal de carga en caso de error
    Swal.close();
    console.error('Error al consultar cliente:', error);
    // Mostrar un mensaje de error si la consulta falla
    Swal.fire(
      'Error',
      'No se pudieron obtener los detalles del cliente.',
      'error'
    );
  }
};

// 🟢 Modificar Cliente
const modificarCliente = async (id) => {
  // 1. Cargar los datos del cliente para pre-llenar el formulario
  let clienteAEditar = null;
  Swal.fire({
    title: 'Cargando datos...',
    text: 'Obteniendo la información del cliente para editar.',
    allowOutsideClick: false,
    didOpen: () => {
      Swal.showLoading();
    }
  });

  try {
    const response = await axios.get(`http://192.168.100.132:8000/clientes/${id}`);
    clienteAEditar = response.data;
    Swal.close(); // Cerrar el modal de carga

  } catch (error) {
    Swal.close();
    console.error('Error al cargar cliente para edición:', error);
    Swal.fire(
      'Error',
      'No se pudo cargar la información del cliente para editar.',
      'error'
    );
    return; // Salir si no se pueden cargar los datos
  }

  // 2. Mostrar el formulario de edición con SweetAlert2
  const { value: formValues } = await Swal.fire({
    title: 'Modificar Cliente',
    html: `
      <input id="swal-input-nombre" class="swal2-input" placeholder="Nombre" value="${clienteAEditar.nombre || ''}">
      <input id="swal-input-apellido" class="swal2-input" placeholder="Apellido" value="${clienteAEditar.apellido || ''}">
      <input id="swal-input-telefono" class="swal2-input" placeholder="Teléfono" value="${clienteAEditar.telefono || ''}">
      <input id="swal-input-mail" class="swal2-input" placeholder="Email" value="${clienteAEditar.mail || ''}">
      <input id="swal-input-nota" class="swal2-input" placeholder="Nota" value="${clienteAEditar.nota || ''}">
      `,
    focusConfirm: false,
    showCancelButton: true,
    confirmButtonText: 'Guardar Cambios',
    cancelButtonText: 'Cancelar',
    preConfirm: () => {
      // Validar que los campos no estén vacíos antes de enviar
      const nombre = Swal.getPopup().querySelector('#swal-input-nombre').value;
      const apellido = Swal.getPopup().querySelector('#swal-input-apellido').value;
      const telefono = Swal.getPopup().querySelector('#swal-input-telefono').value;
      const mail = Swal.getPopup().querySelector('#swal-input-mail').value;
      const nota = Swal.getPopup().querySelector('#swal-input-nota').value;

      if (!nombre || !apellido || !telefono || !mail || !nota) {
        Swal.showValidationMessage('Todos los campos son obligatorios');
        return false;
      }
      return { nombre, apellido, telefono, mail, nota };
      // Agrega direccion y notas si las incluiste en el HTML
      // return { nombre, apellido, telefono, mail, direccion, notas };
    }
  });

  // 3. Si el usuario confirmó y pasó la validación
  if (formValues) {
    try {
      await axios.put(`http://192.168.100.132:8000/clientes/${id}`, formValues);

      // Actualizar el cliente en el array 'clientes' localmente para reflejar los cambios
      // sin tener que recargar todos los clientes del backend.
      const index = clientes.value.findIndex(c => c.id === id);
      if (index !== -1) {
        clientes.value[index] = { ...clientes.value[index], ...formValues };
      }
      
      Swal.fire(
        '¡Actualizado!',
        'El cliente ha sido actualizado con éxito.',
        'success'
      );
    } catch (error) {
      console.error('Error al actualizar cliente:', error);
      Swal.fire(
        'Error',
        'Hubo un problema al actualizar el cliente.',
        'error'
      );
    }
  }
};

const eliminarCliente = async (id) => {
  // ... (tu código existente para eliminarCliente, ya está perfecto)
  const result = await Swal.fire({
    title: '¿Estás seguro?',
    text: "¡No podrás revertir esto!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#d33',
    cancelButtonColor: '#3085d6',
    confirmButtonText: 'Sí, eliminarlo',
    cancelButtonText: 'Cancelar'
  });

  if (result.isConfirmed) {
    try {
      await axios.delete(`http://192.168.100.132:8000/clientes/${id}`);
      clientes.value = clientes.value.filter(c => c.id !== id);
      Swal.fire(
        '¡Eliminado!',
        'El cliente ha sido eliminado con éxito.',
        'success'
      );
    } catch (error) {
      console.error('Error al eliminar cliente:', error);
      Swal.fire(
        'Error',
        'Hubo un problema al eliminar el cliente.',
        'error'
      );
    }
  } else {
    Swal.fire(
      'Cancelado',
      'La eliminación del cliente ha sido cancelada.',
      'info'
    );
  }
};
</script>
