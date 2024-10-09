<template>
    <div class="container mx-auto">
      <h1 class="text-3xl font-bold mb-4 mt-4 ml-5">Your Favorites</h1>
      <div v-if="favorites.length === 0" class="text-center">No favorites yet.</div>
      <div v-else class="flex flex-wrap justify-center">
        <div
          v-for="favorite in favorites"
          :key="favorite._id.$oid"
          class="bg-white border border-slate-200 rounded-3xl px-5 py-5 transition hover:-translate-y-1 hover:shadow-xl w-80 m-5 h-96 flex flex-col justify-between"
        >
          <div>
            <h1 class="text-3xl font-bold overflow-hidden whitespace-nowrap overflow-ellipsis">
              {{ favorite.Job_title }}
            </h1>
            <div class="flex items-center mt-2">
              <h2 class="text-lg font-semibold overflow-hidden whitespace-nowrap overflow-ellipsis">
                {{ favorite.Company_name }}
              </h2>
            </div>
            <p class="mt-4 line-clamp-[7]">{{ favorite.description }}</p>
          </div>
          <div class="flex justify-between items-end">
            <router-link
              :to="'/Jobs/' + favorite.id"
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded cursor-pointer transform active:scale-75 transition-transform"
            >
              See more
            </router-link>
            <button
              @click="removeFavorite(favorite._id.$oid)"
              class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded cursor-pointer transform active:scale-75 transition-transform"
            >
              Remove
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  
  const favorites = ref([])
  
  const fetchFavorites = async () => {
    try {
      const userEmail = localStorage.getItem('userEmail')
      if (!userEmail) {
        throw new Error('User email not found in localStorage')
      }
  
      const response = await axios.post('http://127.0.0.1:5000/favourites', { "userEmail": userEmail })
      favorites.value = response.data
    } catch (error) {
      console.error('Error fetching favorites:', error.response ? error.response.data : error.message)
    }
  }
  
  const router = useRouter()
  
  const seeMore = (jobId) => {
    router.push({ name: 'JobDetail', params: { id: jobId } })
  }
  
  const removeFavorite = async (jobId) => {
    try {
      const userEmail = localStorage.getItem('userEmail')
      if (!userEmail) {
        throw new Error('User email not found in localStorage')
      }
  
      await axios.post('http://127.0.0.1:5000/delete-favorite', { jobId, userEmail })
      favorites.value = favorites.value.filter((favorite) => favorite._id.$oid !== jobId)
    } catch (error) {
      console.error('Error removing favorite:', error.response ? error.response.data : error.message)
    }
  }
  
  onMounted(fetchFavorites)
  </script>
  
  <style scoped></style>
  