<template>
  <div id="app" class="min-h-screen dark:bg-dark-primary">
    <div class="container mx-auto dark:bg-dark-primary">
      <h1 class="text-3xl font-bold mb-4  ml-5 text-gray-800 dark:text-white">Your Favorites</h1>
      
      <div v-if="favorites.length === 0" class="text-center text-gray-500 dark:text-gray-300">
        <img src="../assets/Images/Bheart.png" class="w-96 h-96 m-auto opacity-10">
        <p class="mr-10 -mt-16">You have no favorites yet</p>
      </div>

      <div v-else class="flex flex-wrap justify-center">
        <div
          v-for="favorite in favorites"
          :key="favorite._id.$oid"
          class="bg-white dark:bg-gray-800 border border-slate-200 dark:border-gray-700 rounded-3xl px-5 py-5 transition hover:-translate-y-1 hover:shadow-xl w-80 m-5 h-96 flex flex-col justify-between"
        >
          <div>
            <h1 class="text-3xl font-bold overflow-hidden whitespace-nowrap overflow-ellipsis text-gray-800 dark:text-white">
              {{ favorite.Job_title }}
            </h1>
            <div class="flex items-center mt-2">
              <h2 class="text-lg font-semibold overflow-hidden whitespace-nowrap overflow-ellipsis text-gray-700 dark:text-gray-300">
                {{ favorite.Company_name }}
              </h2>
            </div>
            <p class="mt-4 line-clamp-[7] text-gray-700 dark:text-gray-300">{{ favorite.description }}</p>
          </div>

          <div class="flex justify-between items-end">
            <router-link
              :to="'/Jobs/' + favorite.id"
              class="bg-accent hover:bg-accent text-gray-700 dark:bg-dark-accent dark:text-gray-300 font-bold py-2 px-4 rounded cursor-pointer transform active:scale-75 transition-transform shadow-dark"
            >
              See more
            </router-link>
            <button
              @click="removeFavorite(favorite._id.$oid)"
              class="bg-red hover:bg-red dark:bg-dark-red text-gray-700 dark:text-gray-300 font-bold py-2 px-4 rounded cursor-pointer transform active:scale-75 transition-transform shadow-dark"
            >
              Remove
            </button>
          </div>
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
  
      const response = await axios.post('http://127.0.0.1:5000/favourites', { userEmail })
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
