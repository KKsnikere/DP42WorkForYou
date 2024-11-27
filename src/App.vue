<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <Header />
  <div class="dark:bg-dark-primary">
    <RouterView /> </div>
  <Footer />
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

<style scoped>

body {
  transition: background-color 0.5s ease;
}


</style>


