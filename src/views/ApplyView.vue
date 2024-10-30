<template>
  <div v-if="job" class="max-w-4xl mx-auto p-6 bg-white shadow-lg rounded-lg border border-gray-300 mt-8">
    <h1 class="text-3xl font-bold mb-6 text-gray-800 border-b-2 pb-4">{{ job.Job_title }}</h1>

    <!-- Form for submitting the application -->
    <form @submit.prevent="submitApplication" class="space-y-6">
      <input type="hidden" v-model="jobId" />

      <!-- Form fields -->
      <div>
        <label class="block text-gray-700 font-semibold mb-2">Name</label>
        <input
          type="text"
          v-model="applicant.name"
          required
          class="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        />
      </div>
      <div>
        <label class="block text-gray-700 font-semibold mb-2">Surname</label>
        <input
          type="text"
          v-model="applicant.surname"
          required
          class="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        />
      </div>
      <div>
        <label class="block text-gray-700 font-semibold mb-2">Email</label>
        <input
          type="email"
          v-model="applicant.email"
          required
          class="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        />
      </div>
      <div>
        <label class="block text-gray-700 font-semibold mb-2">Phone</label>
        <input
          type="tel"
          v-model="applicant.phone"
          required
          class="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        />
      </div>
      <div>
        <label class="block text-gray-700 font-semibold mb-2">Message</label>
        <textarea
          v-model="applicant.message"
          rows="4"
          class="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 resize-none"
          placeholder="Tell us why you're a good fit"
        ></textarea>
      </div>

      <!-- File Upload -->
      <div>
  <label class="block text-gray-700 font-semibold mb-2">Upload Files</label>
  
  <div class="relative w-full max-w-sm">
    <!-- Hidden File Input -->
    <input
      type="file"
      multiple
      @change="handleFileUpload"
      class="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
    />
    <!-- Custom Button Style -->
    <button
      type="button"
      class="w-full bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-150 ease-in-out"
    >
      Choose Files
    </button>
  </div>

  <!-- Display Selected Files -->
  <div v-if="files.length" class="mt-2 text-gray-600">
    <p class="font-semibold text-sm">Selected Files:</p>
    <ul class="list-disc pl-5 text-gray-800">
      <li v-for="file in files" :key="file.name">{{ file.name }}</li>
    </ul>
  </div>
</div>



      <!-- Submit button -->
      <div class="flex justify-end mt-8">
        <button
          type="submit"
          class="bg-blue-600 text-white font-semibold py-2 px-6 rounded-lg shadow-md hover:bg-blue-700 transition ease-in-out duration-150"
        >
          Apply
        </button>
      </div>
    </form>
  </div>

  <div v-else-if="error" class="text-center text-red-500 mt-10">
    <p>Error loading job details. Please try again later.</p>
  </div>

  <div v-else class="text-center text-gray-600 mt-10">
    <p>Loading...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'  // Make sure onMounted is imported
import axios from 'axios'
import { useRoute } from 'vue-router'

const route = useRoute()
const jobId = route.params.id
const applicant = ref({
  name: '',
  surname: '',
  phone: '',
  email: '',
  message: ''
})

const job = ref(null)
const error = ref(null)
const files = ref([])

// Function to handle file uploads
const handleFileUpload = (event) => {
  files.value = event.target.files
}

// Function to submit the application form
const submitApplication = async () => {
  try {
    const formData = new FormData()
    formData.append('name', applicant.value.name)
    formData.append('surname', applicant.value.surname)
    formData.append('email', applicant.value.email)
    formData.append('phone', applicant.value.phone)
    formData.append('message', applicant.value.message)
    formData.append('jobId', jobId) // Add jobId to formData

    // Append files to formData
    for (let i = 0; i < files.value.length; i++) {
      formData.append('files', files.value[i])
    }

    const response = await axios.post('http://127.0.0.1:5000/apply', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })

    if (response.status === 201) {
      alert('Application submitted successfully!')
    }
  } catch (err) {
    console.error('Error submitting application:', err)
    alert('Failed to submit application.')
  }
}

// Fetch job details
const fetchJobDetails = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/jobs/${jobId}`)
    job.value = response.data
  } catch (err) {
    console.error('Error fetching job details:', err)
    error.value = 'Failed to load job details'
  }
}

onMounted(fetchJobDetails)
</script>
