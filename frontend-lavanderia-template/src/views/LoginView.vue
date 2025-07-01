<template>
  <div class="min-h-screen bg-[#1e2235] flex items-center justify-center p-4">
    <div class="w-full max-w-md bg-white/90 backdrop-blur-sm shadow-2xl border-0 p-6 rounded-xl">
      <div class="text-center pb-8">
        <div class="flex justify-center mb-6">
          <div class="bg-gradient-to-r from-purple-600 to-indigo-600 p-4 rounded-full shadow-2xl glow-effect float-animation">
            <img src="/shirt-icon.svg" class="h-12 w-12 text-white" alt="Lavandería" />
          </div>
        </div>
        <h1 class="text-3xl font-bold bg-gradient-to-r from-purple-600 to-indigo-600 bg-clip-text text-transparent">
          Lavandería Beatriz
        </h1>
        <p class="text-gray-600 text-lg">Sistema de Gestión Integral</p>
        <div class="w-16 h-1 bg-gradient-to-r from-purple-500 to-indigo-500 mx-auto mt-4 rounded-full"></div>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label class="text-gray-700 font-semibold flex items-center gap-2">
            Usuario
          </label>
          <input
            v-model="username"
            @input="errorMessage = ''"
            type="text"
            required
            class="w-full border-2 border-gray-200 focus:border-purple-500 transition-colors h-12 px-3 rounded"
            placeholder="Ingresa tu usuario"
          />
        </div>

        <div>
          <label class="text-gray-700 font-semibold flex items-center gap-2">
            Contraseña
          </label>
          <div class="relative">
            <input
              :type="showPassword ? 'text' : 'password'"
              v-model="password"
              @input="errorMessage = ''"
              required
              class="w-full border-2 border-gray-200 focus:border-purple-500 transition-colors h-12 px-3 rounded pr-12"
              placeholder="Ingresa tu contraseña"
            />

            <button
              type="button"
              class="absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-500"
              @click="togglePassword"
            >
              {{ showPassword ? '🙈' : '👁️' }}
            </button>
          </div>
        </div>
        <p v-if="errorMessage" class="text-red-600 text-sm text-center">
          {{ errorMessage }}
        </p>
        <button
          type="submit"
          :disabled="isLoading"
          class="w-full btn-primary text-white h-12 text-lg font-semibold rounded-xl"
        >
          <span v-if="isLoading" class="flex items-center gap-2">
            <span class="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></span>
            Iniciando sesión...
          </span>
          <span v-else>🚀 Iniciar Sesión</span>
        </button>
      </form>

      <div
        v-if="showSuccessModal"
        class="fixed inset-0 flex items-center justify-center bg-black/30 z-50"
>
        <div class="bg-white rounded-xl shadow-2xl p-6 max-w-sm w-full text-center animate-fade-in-up">
          <h2 class="text-2xl font-bold text-[#bd55df] mb-2">✅ ¡Login exitoso!</h2>
          <p class="text-gray-700">Bienvenido al sistema Lavandería Beatriz</p>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const showSuccessModal = ref(false)
const username = ref('')
const password = ref('')
const showPassword = ref(false)
const errorMessage = ref('')
const isLoading = ref(false)

const togglePassword = () => {
  showPassword.value = !showPassword.value
}
const loginUser = async () => {
  try {
    const response = await fetch("http://192.168.100.132:8000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username.value,
        password: password.value,
      }),
    })

    if (!response.ok) {
      throw new Error("Credenciales inválidas")
    }

    const data = await response.json()
    return data
  } catch (error) {
    throw error
  }
}

const handleLogin = async () => {
  errorMessage.value = ''
  isLoading.value = true

  try {
    const result = await loginUser()
    showSuccessModal.value = true
    setTimeout(() => {
      showSuccessModal.value = false
      router.push("/dashboard") // ✅ redirige
    }, 2000)
  } catch (err) {
    errorMessage.value = err.message || 'Error al iniciar sesión'
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}
@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 0 5px rgba(99, 102, 241, 0.5); }
  50% { box-shadow: 0 0 20px rgba(99, 102, 241, 0.8), 0 0 30px rgba(99, 102, 241, 0.6); }
}
.float-animation {
  animation: float 3s ease-in-out infinite;
}
.glow-effect {
  animation: pulse-glow 2s infinite;
}
.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  transition: all 0.3s ease;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
}
.btn-primary:disabled {
  opacity: 0.7;
  transform: none;
}
@keyframes fade-in-up {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
.animate-fade-in-up {
  animation: fade-in-up 0.4s ease-out;
}

</style>