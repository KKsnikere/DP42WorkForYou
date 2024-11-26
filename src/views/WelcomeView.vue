<template>
  <div class="flex flex-col items-center justify-center min-h-screen text-gray-100 py-8 px-4 dark:bg-dark-primary dark:text-gray-100">
    <div class="text-center mb-12">
      <h1 class="text-5xl font-bold text-accent mb-4 dark:text-dark-accent">Welcome to our job search site!</h1>
      <p class="text-xl text-gray-300 dark:text-gray-300">
        Find your dream job or post a job opening now.
      </p>
    </div>

    <!-- Feature Cards -->
    <div class="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 w-full max-w-4xl">
      <div class="bg-secondary p-6 rounded-lg shadow-lg text-center dark:bg-dark-secondary dark:text-gray-300">
        <h3 class="text-2xl font-semibold text-accent mb-4 dark:text-dark-accent">Quick job search</h3>
        <p class="text-gray-300 dark:text-gray-300">
          Use the filters to find suitable vacancies by job type, profession, city, and time.
        </p>
      </div>
      <div class="bg-secondary p-6 rounded-lg shadow-lg text-center dark:bg-dark-secondary dark:text-gray-300">
        <h3 class="text-2xl font-semibold text-accent mb-4 dark:text-dark-accent">Posting vacancies</h3>
        <p class="text-gray-300 dark:text-gray-300">
          Register to easily post jobs and attract the right candidates.
        </p>
      </div>
      <div class="bg-secondary p-6 rounded-lg shadow-lg text-center dark:bg-dark-secondary dark:text-gray-300">
        <h3 class="text-2xl font-semibold text-accent mb-4 dark:text-dark-accent">Selected vacancies</h3>
        <p class="text-gray-300 dark:text-gray-300">
          Add jobs to your favorites and save them for quick access later.
        </p>
      </div>
    </div>
  </div>
</template>

  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  
  </script>
  
  
