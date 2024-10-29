<template>
    <div class="p-4">
      <h1 class="text-2xl font-semibold mb-4">My Applications</h1>
      <div v-if="applications.length === 0" class="text-gray-500">No applications found.</div>
  
      <div v-for="application in applications" :key="application.jobId" class="bg-white p-4 shadow rounded mb-4">
        <h2 class="text-xl font-bold mb-2">{{ application.Job_title }}</h2>
        <p><strong>Company:</strong> {{ application.Company_name }}</p>
        <p><strong>Salary:</strong> ${{ application.salary }}</p>
        <p><strong>Your Message:</strong> {{ application.message }}</p>
  
        <!-- Button to navigate to the job detail page -->
        <router-link :to="`/jobs/${application.jobId}`">
          <button class="mt-4 bg-accent text-white font-semibold py-2 px-4 rounded hover:bg-blue-600 transition duration-200">
            View Job Details
          </button>
        </router-link>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { useRouter } from "vue-router";
  import { ref, onMounted, computed } from 'vue'
  
  export default {
    data() {
      return {
        applications: []
      };
    },
    created() {
      this.fetchUserApplications();
    },
    methods: {
      async fetchUserApplications() {
        const userEmail = localStorage.getItem('userEmail');
        console.log(`Sending request to backend with userEmail: ${userEmail}`);
  
        try {
          const response = await axios.get('http://127.0.0.1:5000/user-applications', {
            headers: {
              userEmail: userEmail,
            },
          });
          console.log("Response received from backend:", response.data);
          this.applications = response.data;
          console.log("Applications data stored in component:", this.applications);
        } catch (error) {
          console.error("Error fetching applications:", error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Custom styling */
  </style>
  