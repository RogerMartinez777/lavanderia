import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path' // 🟢 NUEVA LÍNEA: Necesitas importar 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0', // esto permite el acceso a otras IPs
    port: 5173
  },
  resolve: {
    alias: {
      // 🟢 NUEVA SECCIÓN: Configuración del alias '@' para apuntar a 'src'
      '@': path.resolve(__dirname, './src'), 
    },
  },
})
