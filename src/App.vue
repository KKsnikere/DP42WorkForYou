<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue';
</script>

<template>
  <div>
    <Header />
    <RouterView />
    <router-view /> 
  </div>
</template>

<script>
import { useDarkMode } from './composables/useDarkMode';

export default {
  setup() {
    const { isDarkMode, toggleDarkMode } = useDarkMode();

    return {
      isDarkMode,
      toggleDarkMode
    };
  }
};
</script>

<style>

body {
  transition: background-color 0.3s ease;
}

.dark {
  background-color: #121212;
  color: white;
}

.dark .bg-blue-500 {
  background-color: #3b82f6;
}

.dark .text-white {
  color: #e5e5e5;
}
</style>


