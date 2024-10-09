<template>
    <div class="container mx-auto py-10 px-4">
      <div class="bg-white shadow-md rounded-lg p-6">
        <h1 class="text-3xl font-bold mb-6 text-center">User Profile</h1>
        <div v-if="user" class="space-y-4">
          <div class="flex justify-center mb-4">
            <img
              v-if="user.profileImageUrl"
              :src="user.profileImageUrl"
              alt="Profile Image"
              class="w-32 h-32 rounded-full object-cover"
            />
            <div v-else class="w-32 h-32 rounded-full bg-gray-200 flex items-center justify-center text-gray-500">
              <span>No Image</span>
            </div>
          </div>
          <!-- User information -->
          <div class="info-item">
            <span class="font-semibold">Email:</span>
            <span class="break-words">{{ user.email }}</span>
          </div>
          <div class="info-item">
            <span class="font-semibold">User Type:</span>
            <span class="break-words">{{ user.user_type }}</span>
          </div>
          <div v-if="user.name" class="info-item">
            <span class="font-semibold">Name:</span>
            <span class="break-words">{{ user.name }}</span>
          </div>
          <div v-if="user.surname" class="info-item">
            <span class="font-semibold">Surname:</span>
            <span class="break-words">{{ user.surname }}</span>
          </div>
          <div v-if="user.org_name" class="info-item">
            <span class="font-semibold">Organization Name:</span>
            <span class="break-words">{{ user.org_name }}</span>
          </div>
          <div v-if="user.reg_number" class="info-item">
            <span class="font-semibold">Registration Number:</span>
            <span class="break-words">{{ user.reg_number }}</span>
          </div>
          <div v-if="user.location" class="info-item">
            <span class="font-semibold">Location:</span>
            <span class="break-words">{{ user.location }}</span>
          </div>
          <!-- Add Job Advert button -->
          <button
            v-if="user.user_type === 'organisation'"
            @click="showJobAdvertModal = true"
            class="mt-6 sm:mr-12 bg-green-500 text-white font-semibold py-2 px-6 rounded-lg hover:bg-green-600 transition duration-200 mb-4"
          >
            + Add Job Advert
          </button>
  
          <!-- Change Password button -->
          <button
            @click="showChangePasswordModal = true"
            class="mt-2 bg-accent text-white font-semibold py-2 px-6 rounded-lg hover:scale-110 transition duration-200"
          >
            Change Password
          </button>
  
          <!-- User adverts -->
          <div class="mt-8">
            <h2 class="text-2xl font-bold mb-4">My Adverts</h2>
            <div v-if="adverts.length > 0">
              <div v-for="advert in adverts" :key="advert._id" class="border p-4 rounded-lg mb-4">
                <h3 class="text-xl font-semibold overflow-ellipsis overflow-hidden">
                  {{ advert.Job_title }}
                </h3>
                <p class="overflow-ellipsis overflow-hidden">{{ advert.description }}</p>
                <p class="text-gray-600">City: {{ advert.city }}</p>
                <!-- Delete button -->
                <button
                  @click="deleteAdvert(advert.id)"
                  class="mt-2 bg-red-500 text-white font-semibold py-2 px-6 rounded-lg hover:bg-red-600 transition duration-200"
                >
                  Delete
                </button>
              </div>
            </div>
            <div v-else>
              <p>No adverts found.</p>
            </div>
          </div>
        </div>
        <div v-else class="text-center">
          <p>Loading...</p>
        </div>
  
        <!-- Job Advert Modal -->
        <div
          v-if="showJobAdvertModal"
          class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50"
        >
          <div
            class="bg-white p-8 rounded-lg shadow-lg max-w-lg w-full max-h-full overflow-y-auto relative"
          >
            <button
              @click="showJobAdvertModal = false"
              class="absolute top-4 right-4 text-gray-700 hover:text-gray-900"
            >
              &times;
            </button>
            <h2 class="text-2xl font-bold mb-4 text-center">Create Job Advert</h2>
            <!-- Error Message -->
            <p v-if="formError" class="text-red-500 mb-4">{{ formError }}</p>
            <!-- Form -->
            <form @submit.prevent="createJobAdvert">
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">Company Name</label>
                <input
                  type="text"
                  v-model="jobAdvert.Company_name"
                  class="w-full px-3 py-2 border rounded-lg bg-gray-200"
                  readonly
                />
              </div>
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">Description</label>
                <textarea
                  v-model="jobAdvert.description"
                  class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                  required
                ></textarea>
              </div>
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">Job Title</label>
                <input
                  type="text"
                  v-model="jobAdvert.Job_title"
                  class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                  required
                />
              </div>
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">Phone Number</label>
                <input
                  type="text"
                  v-model="jobAdvert.phone_number"
                  class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                  required
                />
              </div>
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">Registration Number</label>
                <input
                  type="text"
                  v-model="jobAdvert.reg_nr"
                  class="w-full px-3 py-2 border rounded-lg bg-gray-200"
                  readonly
                />
              </div>
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">Address</label>
                <input
                  type="text"
                  v-model="jobAdvert.address"
                  class="w-full px-3 py-2 border rounded-lg bg-gray-200"
                  readonly
                />
              </div>
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">Email</label>
                <input
                  type="text"
                  v-model="jobAdvert.email"
                  class="w-full px-3 py-2 border rounded-lg bg-gray-200"
                  readonly
                />
              </div>
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">Work Type</label>
                <select
                  v-model="jobAdvert.worktype"
                  class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                  required
                >
                  <option value="Part-Time">Part-Time</option>
                  <option value="Full-time">Full-Time</option>
                  <option value="One-time">One-time</option>
                </select>
              </div>
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">Profession</label>
                <select
                  v-model="jobAdvert.profession"
                  class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                  required
                >
                  <option value="Programmer">Programmer</option>
                  <option value="Biotechnology">Biotechnology</option>
                  <option value="DevOps">DevOps</option>
                  <option value="AI">AI</option>
                  <option value="Engineering">Engineering</option>
                  <option value="Networking">Networking</option>
                  <option value="Educator">Educator</option>
                  <option value="Cybersecurity">Cybersecurity</option>
                  <option value="VR">VR</option>
                  <option value="Management">Management</option>
                </select>
              </div>
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">Type of Work</label>
                <select
                  v-model="jobAdvert.typeOfwork"
                  class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                  required
                >
                  <option value="Online">Online</option>
                  <option value="In-office">In-office</option>
                </select>
              </div>
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">City</label>
                <select
                  v-model="jobAdvert.city"
                  class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                  required
                >
                  <option value="Liepaja">Liepaja</option>
                  <option value="Ogre">Ogre</option>
                  <option value="Bauska">Bauska</option>
                  <option value="Jurmala">Jurmala</option>
                  <option value="Tukums">Tukums</option>
                  <option value="Ventspils">Ventspils</option>
                  <option value="Riga">Rīga</option>
                </select>
              </div>
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">Work Time</label>
                <select
                  v-model="jobAdvert.workTime"
                  class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                  required
                >
                  <option value="Workdays">Workdays</option>
                  <option value="Weekend">Weekend</option>
                  <option value="Schedule">Schedule</option>
                </select>
              </div>
              <button
                type="submit"
                class="w-full bg-blue-500 text-white font-semibold py-2 px-6 rounded-lg hover:bg-blue-600 transition duration-200"
              >
                Create Job Advert
              </button>
            </form>
          </div>
        </div>
  
        <!-- Change Password Modal -->
        <div
          v-if="showChangePasswordModal"
          class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50"
        >
          <div
            class="bg-white p-8 rounded-lg shadow-lg max-w-lg w-full max-h-full overflow-y-auto relative"
          >
            <button
              @click="showChangePasswordModal = false"
              class="absolute top-4 right-4 text-gray-700 hover:text-gray-900"
            >
              &times;
            </button>
            <h2 class="text-2xl font-bold mb-4 text-center">Change Password</h2>
            <!-- Error Message -->
            <p v-if="passwordFormError" class="text-red-500 mb-4">{{ passwordFormError }}</p>
            <!-- Form -->
            <form @submit.prevent="changePassword">
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">Old Password</label>
                <input
                  type="password"
                  v-model="changePasswordForm.old_password"
                  class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                  required
                />
              </div>
              <div class="mb-4">
                <label class="block text-gray-700 font-semibold mb-2">New Password</label>
                <input
                  type="password"
                  v-model="changePasswordForm.new_password"
                  class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                  required
                />
              </div>
              <button
                type="submit"
                class="w-full bg-blue-500 text-white font-semibold py-2 px-6 rounded-lg hover:bg-blue-600 transition duration-200"
              >
                Change Password
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const user = ref(null)
  const showJobAdvertModal = ref(false)
  const showChangePasswordModal = ref(false)
  const formError = ref('')
  const passwordFormError = ref('')
  const adverts = ref([])
  
  const jobAdvert = ref({
    Company_name: '',
    description: '',
    Job_title: '',
    phone_number: '',
    reg_nr: '',
    address: '',
    email: '',
    worktype: '',
    profession: '',
    typeOfwork: '',
    city: '',
    workTime: ''
  })
  
  const changePasswordForm = ref({
    old_password: '',
    new_password: ''
  })
  
  const fetchUserData = async () => {
    try {
      const email = localStorage.getItem('userEmail')
      if (!email) {
        throw new Error('User email not found in localStorage')
      }
  
      const response = await axios.post('http://127.0.0.1:5000/user', { email })
      user.value = response.data
      if (user.value.user_type === 'organisation') {
        jobAdvert.value.Company_name = user.value.org_name
        jobAdvert.value.reg_nr = user.value.reg_number
        jobAdvert.value.address = user.value.location
        jobAdvert.value.email = user.value.email
      }
  
      await fetchUserAdverts(email)
    } catch (error) {
      console.error('Error fetching user data:', error.response ? error.response.data : error.message)
    }
  }
  
  const fetchUserAdverts = async (email) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/my_adverts', { email })
      adverts.value = response.data
    } catch (error) {
      console.error(
        'Error fetching user adverts:',
        error.response ? error.response.data : error.message
      )
    }
  }
  
  const createJobAdvert = async () => {
    try {
      if (
        !jobAdvert.value.description ||
        !jobAdvert.value.Job_title ||
        !jobAdvert.value.phone_number ||
        !jobAdvert.value.worktype ||
        !jobAdvert.value.profession ||
        !jobAdvert.value.typeOfwork ||
        !jobAdvert.value.city ||
        !jobAdvert.value.workTime
      ) {
        formError.value = 'Please fill in all fields.'
        return
      }
  
      const response = await axios.post('http://127.0.0.1:5000/create_job_advert', jobAdvert.value)
      console.log(response.data)
      formError.value = ''
      showJobAdvertModal.value = false
      await fetchUserAdverts(user.value.email)
    } catch (error) {
      console.error(
        'Error creating job advert:',
        error.response ? error.response.data : error.message
      )
    }
  }
  
  const deleteAdvert = async (advertId) => {
    try {
      await axios.delete(`http://127.0.0.1:5000/jobs/${advertId}`)
      await fetchUserAdverts(user.value.email)
    } catch (error) {
      console.error('Error deleting advert:', error.response ? error.response.data : error.message)
    }
  }
  
  const changePassword = async () => {
    try {
      if (!changePasswordForm.value.old_password || !changePasswordForm.value.new_password) {
        passwordFormError.value = 'Please fill in all fields.'
        return
      }
  
      const email = localStorage.getItem('userEmail')
      if (!email) {
        throw new Error('User email not found in localStorage')
      }
  
      const requestData = {
        email,
        old_password: changePasswordForm.value.old_password,
        new_password: changePasswordForm.value.new_password
      }
  
      const response = await axios.post('http://127.0.0.1:5000/password_change', requestData)
  
      if (response.data.error) {
        passwordFormError.value = response.data.error
      } else {
        passwordFormError.value = ''
        showChangePasswordModal.value = false
      }
    } catch (error) {
      console.error('Error changing password:', error.response ? error.response.data : error.message)
    }
  }
  
  onMounted(fetchUserData)
  </script>
  
  <style scoped>
  /*Used style because couldnt make it in tailwind and for less code in "class" */
  .container {
    max-width: 600px;
    margin: auto;
  }
  
  .info-item {
    display: flex;
    flex-direction: column;
  }
  
  .info-item span {
    display: block;
  }
  
  .fixed {
    position: fixed;
    inset: 0;
  }
  
  .bg-black {
    background-color: rgba(0, 0, 0, 0.5);
  }
  
  .bg-white {
    background-color: #ffffff;
  }
  
  .p-8 {
    padding: 2rem;
  }
  
  .rounded-lg {
    border-radius: 0.5rem;
  }
  
  .shadow-lg {
    box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
  }
  
  .max-w-lg {
    max-width: 32rem;
  }
  
  .w-full {
    width: 100%;
  }
  
  .mb-4 {
    margin-bottom: 1rem;
  }
  
  .text-gray-700 {
    color: #4a5568;
  }
  
  .font-semibold {
    font-weight: 600;
  }
  
  .px-3 {
    padding-left: 0.75rem;
    padding-right: 0.75rem;
  }
  
  .py-2 {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
  }
  
  .border {
    border-width: 1px;
  }
  
  .focus\:outline-none {
    outline: none;
  }
  
  .focus\:border-blue-500 {
    border-color: #4299e1;
  }
  
  .bg-gray-200 {
    background-color: #edf2f7;
  }
  
  .bg-gray-500 {
    background-color: #a0aec0;
  }
  
  .hover\:bg-gray-600:hover {
    background-color: #718096;
  }
  
  .bg-blue-500 {
    background-color: #4299e1;
  }
  
  .hover\:bg-blue-600:hover {
    background-color: #3182ce;
  }
  
  .bg-green-500 {
    background-color: #48bb78;
  }
  
  .hover\:bg-green-600:hover {
    background-color: #38a169;
  }
  
  .bg-red-500 {
    background-color: #f56565;
  }
  
  .hover\:bg-red-600:hover {
    background-color: #e53e3e;
  }
  
  .text-red-500 {
    color: #e53e3e;
  }
  
  .max-h-full {
    max-height: calc(100vh - 2rem);
  }
  
  .overflow-y-auto {
    overflow-y: auto;
  }
  </style>
  
