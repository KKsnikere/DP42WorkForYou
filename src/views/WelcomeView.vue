<template>
    <div class="flex flex-col items-center justify-center min-h-screen bg-gray-100 py-8 px-4">
      <div class="text-center mb-12">
        <h1 class="text-5xl font-bold text-accent mb-4">Welcome to our job search site!</h1>
        <p class="text-xl text-gray-600">
          Find your dream job or post a job opening now.
        </p>
      </div>
      
      
      <div class="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 w-full max-w-4xl">
        <div class="bg-white p-6 rounded-lg shadow-lg text-center">
          <h3 class="text-2xl font-semibold mb-4">Quick job search</h3>
          <p class="text-gray-600">
            Use the filters to find suitable vacancies by job type, profession, city and time.
          </p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-lg text-center">
          <h3 class="text-2xl font-semibold mb-4">Posting vacancies</h3>
          <p class="text-gray-600">
            Register to easily post jobs and attract the right candidates.
          </p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-lg text-center">
          <h3 class="text-2xl font-semibold mb-4">Selected vacancies</h3>
          <p class="text-gray-600">
            Add jobs to your favorites and save them for quick access later.
          </p>
        </div>
      </div>
  
      <div class="mt-16">
        <h2 class="text-3xl font-bold text-center mb-8">Popular categories of work</h2>
        <div class="flex flex-wrap justify-center space-x-4">
          <button
            v-for="category in popularCategories"
            :key="category"
            @click="goToCategory(category)"
            class="bg-gray-200 text-gray-700 font-medium py-2 px-4 rounded hover:bg-gray-300 transition-colors shadow-dark"
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
    'Programmers',
    'Engineers',
    'Marketing',
    'Education',
    'Cybersecurity',
    'Artificial intelligence'
  ])
  
  const goToCategory = (category) => {
    // Перенаправление на страницу поиска с предустановленным фильтром по категории
    router.push({ name: 'Home', query: { profession: category } })
  }
  </script>
  
  
