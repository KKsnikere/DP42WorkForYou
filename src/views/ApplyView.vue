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
          class="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm bg-gray-200"
          readonly
        />
      </div>
      <div>
        <label class="block text-gray-700 font-semibold mb-2">Surname</label>
        <input
          type="text"
          v-model="applicant.surname"
          required
          class="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm bg-gray-200"
          readonly
        />
      </div>
      <div>
        <label class="block text-gray-700 font-semibold mb-2">Email</label>
        <input
          type="email"
          v-model="applicant.email"
          required
          class="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm bg-gray-200"
          readonly
        />
      </div>

<div>
  <label class="block text-gray-700 font-semibold mb-2">Phone</label>
  <div class="flex items-center space-x-2">
    <select v-model="selectedCountryCode" class="border border-gray-300 rounded-md px-1 py-2 text-sm">
      <option v-for="code in countryCodes" :key="code.value" :value="code.value">
        {{ code.label }} ({{ code.value }})
      </option>
    </select>
    <input
      type="text"
      v-model="applicant.phone"
      required
      maxlength="10"
      pattern="[0-9]*"
      @input="applicant.phone = applicant.phone.replace(/[^0-9]/g, '').slice(0, 10)"
      class="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm"
    />
  </div>
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
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'
import { useRouter } from "vue-router";

const route = useRoute()
const jobId = route.params.id
const router = useRouter(); 

// Define applicant data
const applicant = ref({
  name: '',
  surname: '',
  phone: '',
  email: '',
  message: ''
})


const selectedCountryCode = ref('+371') // Default country code
const countryCodes = ref([
  { label: 'LV', value: '+371' },
  { label: 'LT', value: '+370' },
  { label: 'EE', value: '+372' },
  { label: 'UK', value: '+44' },
  { label: 'DE', value: '+49' },
  { label: 'FR', value: '+33' },
  { label: 'IT', value: '+39' },
  { label: 'ES', value: '+34' },
  { label: 'PL', value: '+48' },
  { label: 'SE', value: '+46' },
  { label: 'FI', value: '+358' },
  { label: 'DK', value: '+45' },
  { label: 'NO', value: '+47' },
  { label: 'NL', value: '+31' },
  { label: 'BE', value: '+32' },
  { label: 'AT', value: '+43' },
  { label: 'CZ', value: '+420' },
  { label: 'HU', value: '+36' },
  { label: 'SK', value: '+421' },
  { label: 'IE', value: '+353' },
  { label: 'RO', value: '+40' },
  { label: 'BG', value: '+359' },
  { label: 'HR', value: '+385' },
  { label: 'SI', value: '+386' },  
])

const job = ref(null)
const error = ref(null)
const files = ref([])

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

// Fetch user data for auto-insertion
const fetchUserData = async () => {
  try {
    const email = localStorage.getItem('userEmail')
    if (!email) {
      throw new Error('User email not found in localStorage')
    }

    const response = await axios.post('http://127.0.0.1:5000/user', { email })
    const user = response.data

    // Auto-fill applicant fields if user data is available
    applicant.value.name = user.name || ''
    applicant.value.surname = user.surname || ''
    applicant.value.email = user.email || ''
    applicant.value.phone = user.phone || ''
  } catch (error) {
    console.error('Error fetching user data:', error)
  }
}

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
      location.reload();
    }
  } catch (err) {
    console.error('Error submitting application:', err)
    alert('Failed to submit application.')
  }
}

// Fetch job details and user data when the component mounts
onMounted(() => {
  fetchJobDetails()
  fetchUserData()
})
</script>
