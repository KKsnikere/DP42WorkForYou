<template>
    <div class="flex flex-col items-center justify-center min-h-screen bg-gray-100 py-8 px-4">
      <div class="text-center mb-12">
        <h1 class="text-5xl font-bold text-accent mb-4">Добро пожаловать на наш сайт поиска работы!</h1>
        <p class="text-xl text-gray-600">
          Найдите работу своей мечты или разместите вакансию прямо сейчас.
        </p>
      </div>
      
      
      <div class="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 w-full max-w-4xl">
        <div class="bg-white p-6 rounded-lg shadow-lg text-center">
          <h3 class="text-2xl font-semibold mb-4">Быстрый поиск работы</h3>
          <p class="text-gray-600">
            Используйте фильтры, чтобы найти подходящие вакансии по типу работы, профессии, городу и времени.
          </p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-lg text-center">
          <h3 class="text-2xl font-semibold mb-4">Размещение вакансий</h3>
          <p class="text-gray-600">
            Зарегистрируйтесь, чтобы легко размещать вакансии и привлекать подходящих кандидатов.
          </p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-lg text-center">
          <h3 class="text-2xl font-semibold mb-4">Избранные вакансии</h3>
          <p class="text-gray-600">
            Добавляйте вакансии в избранное и сохраняйте их для быстрого доступа позже.
          </p>
        </div>
      </div>
  
      <div class="mt-16">
        <h2 class="text-3xl font-bold text-center mb-8">Популярные категории работы</h2>
        <div class="flex flex-wrap justify-center space-x-4">
          <button
            v-for="category in popularCategories"
            :key="category"
            @click="goToCategory(category)"
            class="bg-gray-200 text-gray-700 font-medium py-2 px-4 rounded hover:bg-gray-300 transition-colors"
          >
            {{ category }}
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  const popularCategories = ref([
    'Программисты',
    'Инженеры',
    'Маркетинг',
    'Образование',
    'Кибербезопасность',
    'Искусственный интеллект'
  ])
  
  const goToCategory = (category) => {
    // Перенаправление на страницу поиска с предустановленным фильтром по категории
    router.push({ name: 'Home', query: { profession: category } })
  }
  </script>
  
  <style scoped>
  .bg-accent {
    background-color: #3498db; /* Основной цвет акцента */
  }
  .text-accent {
    color: #3498db;
  }
  </style>
  