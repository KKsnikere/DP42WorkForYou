<template>
    <div v-if="job" class="max-w-4xl mx-auto p-6 bg-white shadow-md rounded-lg">
      <h1 class="text-3xl font-bold mb-6">{{ job.Job_title }}</h1>
      <div class="mb-6">
        <h2 class="text-xl font-semibold mb-2">{{ job.Company_name }}</h2>
        <div class="flex items-center">
          <span class="text-gray-500 mr-2">{{ job.reg_nr }}</span>
          <span class="text-gray-500">{{ job.adress }}</span>
        </div>
      </div>
      <p class="text-gray-800 text-wrap max-w-96">{{ job.description }}</p>
      <div class="mt-8 mb-6">
        <p class="text-gray-700"><strong>Email:</strong> {{ job.email }}</p>
        <p class="text-gray-700"><strong>Phone:</strong> {{ job.phone_number }}</p>
        <p class="text-gray-700"><strong>Adress:</strong> {{ job.address }}</p>
        <p class="text-blue-500 cursor-pointer text-base" @click="openGoogleMaps(job.address)">
          View in Google Maps
        </p>
        <button
        class="mt-10  transform active:scale-100 transition-transform hover:scale-110"
        >
        <router-link
          to="/home"
          class="bg-red-500 text-white font-bold py-2 px-4 rounded cursor-pointer"
          >
          Back
        </router-link>
      </button>
      </div>
    </div>
    <div v-else-if="error">
      <p>Error loading job details. Please try again later.</p>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, computed } from 'vue'
  import axios from 'axios'
  import { useRoute } from 'vue-router'
import HomeView from './HomeView.vue';
  
  const route = useRoute()
  const jobId = route.params.id
  const job = ref(null)
  const error = ref(null)
  
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
  

