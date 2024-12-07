<template>
  <div class="h-8 bg-white dark:bg-dark-primary"></div>
  <div v-if="job" class="max-w-4xl mx-auto p-6 bg-white shadow-lg rounded-lg border border-gray-600 mt-8 dark:bg-dark-secondary">
    <h1 class="text-3xl font-bold mb-6 text-dark-primary dark:text-white border-b-2 pb-4">{{ job.Job_title }}</h1>

    <!-- Form for submitting the application -->
    <form @submit.prevent="submitApplication" class="space-y-6">
      <input type="hidden" v-model="jobId" />

      <!-- Form fields -->
      <div>
        <label class="block text-gray-500 dark:text-white font-semibold mb-2">Name</label>
        <input
          type="text"
          v-model="applicant.name"
          required
          class="w-full px-4 py-2 border rounded-md shadow-sm border-gray-600 bg-gray-200 dark:bg-gray-700 text-black  dark:text-white"
          readonly
        />
      </div>
      <div>
        <label class="block text-gray-500 dark:text-white font-semibold mb-2">Surname</label>
        <input
          type="text"
          v-model="applicant.surname"
          required
          class="w-full px-4 py-2  rounded-md shadow-sm border border-gray-600 bg-gray-200 dark:bg-gray-700 text-black  dark:text-white"
          readonly
        />
      </div>
      <div>
        <label class="block dark:text-white text-gray-500 font-semibold mb-2">Email</label>
        <input
          type="email"
          v-model="applicant.email"
          required
          class="w-full px-4 py-2 border  rounded-md shadow-sm border-gray-600 bg-gray-200 dark:bg-gray-700 text-black  dark:text-white"
          readonly
        />
      </div>

      <div>
        <label class="block dark:text-white  text-gray-500 font-semibold mb-2">Phone</label>
        <div class="flex items-center space-x-2">
          <!-- Country Code Select -->
          <select v-model="selectedCountryCode" class="border rounded-md px-1 py-2 text-sm border-gray-600 bg-white dark:bg-gray-900  dark:text-white text-black">
            <option v-for="code in countryCodes" :key="code.value" :value="code.value">
              {{ code.label }} ({{ code.value }})
            </option>
          </select>

          <!-- Phone Input -->
          <input
            type="text"
            v-model="applicant.phone"
            required
            maxlength="10"
            pattern="[0-9]*"
            @input="applicant.phone = applicant.phone.replace(/[^0-9]/g, '').slice(0, 10)"
            class="w-full px-4 py-2 border border-gray-600 rounded-md shadow-sm text-sm   bg-white dark:bg-gray-900 text-black dark:text-white"
            placeholder="123456789"
            />
        </div>
      </div>

      <div>
        <label class="block dark:text-white text-gray-500 font-semibold mb-2">Message</label>
        <textarea
          v-model="applicant.message"
          rows="4"
          class="w-full px-4 py-2 border border-gray-600 rounded-md shadow-sm focus:ring-2 resize-none bg-white dark:bg-gray-900 text-black"
          placeholder="Tell us why you're a good fit"
        ></textarea>
      </div>


      <div v-if="backendError" class="text-red-400 text-sm mt-1">
        {{ backendError }}
      </div>

      <!-- File Upload -->
      <div>
        <label class="block text-gray-500 font-semibold mb-2">Upload Files</label>

        <div class="relative w-full max-w-sm">
          <input
            type="file"
            multiple
            @change="handleFileUpload"
            class="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
          />
        
          <button
            type="button"
            class="w-full bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-150 ease-in-out"
          >
            Choose Files
          </button>
        </div>

        <!-- Display Selected Files -->
        <div v-if="files.length" class="mt-2 text-gray-400">
          <p class="font-semibold text-black text-sm">Selected Files:</p>
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

  <div v-else-if="error" class="text-center text-red-400 mt-10">
    <p>Error loading job details. Please try again later.</p>
  </div>

  <div v-else class="text-center text-gray-400 mt-10">
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
const backendError = ref(null)

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

    
    const fullPhoneNumber = `${selectedCountryCode.value}${applicant.value.phone}`

    formData.append('name', applicant.value.name)
    formData.append('surname', applicant.value.surname)
    formData.append('email', applicant.value.email)
    formData.append('phone', fullPhoneNumber)  
    formData.append('message', applicant.value.message)
    formData.append('jobId', jobId) 

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
      location.reload()
    }
  } catch (err) {
    // Handle error from backend
    if (err.response && err.response.data && err.response.data.error) {
      backendError.value = err.response.data.error 
    } else {
      console.error('Error submitting application:', err)
      alert('Failed to submit application.')
    }
  }
}


onMounted(() => {
  fetchJobDetails()
  fetchUserData()
})
</script>