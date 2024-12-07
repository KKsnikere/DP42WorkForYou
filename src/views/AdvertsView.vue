<template>
  <!-- Job Details -->
  <div class="h-8 bg-white dark:bg-dark-primary"></div>
  <div v-if="job" class="max-w-4xl mx-auto p-6 bg-white dark:bg-dark-primary shadow-md rounded-lg border border-gray-300 dark:border-gray-700 h-screen">
    <h1 class="text-3xl font-bold mb-6 text-gray-800 dark:text-white border-b pb-4">{{ job.Job_title }}</h1>
    
    <div class="mb-6">
      <h2 class="text-xl font-semibold mb-2 text-gray-700 dark:text-gray-300"> Company: {{ job.Company_name }}</h2>
      <div class="flex items-center text-gray-500 dark:text-gray-400">
        <span class="mr-2"> Reg. №: {{ job.reg_nr }}</span>
        <span>{{ job.adress }}</span>
      </div>
    </div>

    <p class="text-gray-800 dark:text-white text-wrap max-w-96 border-l-4 border-blue-500 dark:border-blue-400 pl-4">{{ job.description }}</p>

    <div class="mt-8 mb-6 bg-gray-100 dark:bg-gray-700 p-4 rounded-lg shadow-inner">
      <p class="text-gray-700 dark:text-gray-300 mb-2"><strong>Email:</strong> {{ job.email }}</p>
      <p class="text-gray-700 dark:text-gray-300 mb-2"><strong>Phone:</strong> {{ job.phone_number }}</p>
      <p class="text-gray-700 dark:text-gray-300 mb-2"><strong>Address:</strong> {{ job.address }}</p>
      <p class="text-gray-700 dark:text-gray-300 mb-2"><strong>Salary:</strong> <span class="text-green-600 dark:text-green-400 font-semibold">{{ job.salary }}€</span></p>
      <p class="text-blue-500 dark:text-blue-400 cursor-pointer text-base underline" @click="openGoogleMaps(job.address)">
        View in Google Maps
      </p>
    </div>

    <!-- Apply and Back Buttons -->
    <div class="flex mt-10 space-x-4">
      <button 
      class="transform hover:scale-110 transition">
        <router-link 
          :to="`/apply/${jobId}`"
          class="bg-accent dark:bg-dark-accent text-gray-700 dark:text-gray-200 font-bold py-2 px-4 rounded cursor-pointer transform active:scale-100 transition-transform hover:scale-110 shadow-dark"
        >
          Apply
        </router-link>
      </button>

      <!-- Back Button -->
      <button class="transform active:scale-100 transition-transform hover:scale-110 shadow-dark">
        <router-link
          to="/home"
          class="bg-red dark:bg-dark-red text-gray-700 dark:text-gray-200 font-bold py-2 px-4 rounded cursor-pointer"
        >
          Back
        </router-link>
      </button>
    </div>
  </div>

  <div v-else-if="error">
    <p class="text-gray-800 dark:text-white">Error loading job details. Please try again later.</p>
  </div>

  <div v-else>
    <p class="text-gray-800 dark:text-white">Loading...</p>
  </div>
</template>


  
  <script setup>
  import { ref, onMounted, computed } from 'vue'
  import { useRouter } from "vue-router";
  import axios from 'axios'
  import { useRoute } from 'vue-router'
  import HomeView from './HomeView.vue';
  
  const route = useRoute()
  const jobId = route.params.id
  const job = ref(null)
  const error = ref(null)

  const isAuthenticated = () => {
  // Check for JWT token in cookies or localStorage
  const token = document.cookie.split('; ').find(row => row.startsWith('token='));
  return token !== undefined;
};
  
  const fetchJobDetails = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/jobs/${jobId}`)
      job.value = response.data
    } catch (err) {
      console.error('Error fetching job details:', err)
      error.value = 'Failed to load job details'
    }
  }
  
  // Gmap link
  const googleMapsLink = computed(() => {
    if (job.value && job.value.adress) {
      const encodedAddress = encodeURIComponent(job.value.adress)
      return `https://www.google.com/maps/search/?api=1&query=${encodedAddress}`
    }
    return ''
  })
  onMounted(fetchJobDetails)
  </script>
  
  <script>
  export default {
    methods: {
      openGoogleMaps(address) {
        const url = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(address)}`
        window.open(url, '_blank')
      }
    }
  }
  </script>
  

