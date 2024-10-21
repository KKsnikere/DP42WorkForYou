<template>
  <div class="container mx-auto px-4">
    <div class="bg-white shadow-md rounded-3xl p-6 mx-4 md:mx-52 mt-10 border border-slate-200">
      <h1 class="text-3xl font-bold mb-6 text-center">User Profile</h1>
      <div v-if="user" class="space-y-4">
        <div class="flex justify-center mb-4">
          <!-- Profile Image or placeholder -->
          <div
            class="relative w-32 h-32 rounded-full cursor-pointer mb-10"
            @click="triggerFileUpload"
          >
            <!-- If there's a profile image -->
            <img
              v-if="user.profileImageUrl"
              :src="user.profileImageUrl"
              alt="Profile Image"
              class="w-full h-full rounded-full object-cover"
            />

            <!-- If there's no profile image -->
            <div
              v-else
              class="w-full h-full bg-gray-200 flex items-center justify-center text-gray-500 rounded-full"
            >
              <span>No Image</span>
            </div>

            <!-- Overlay and "+" icon on hover -->
            <div
              class="absolute inset-0 flex items-center justify-center bg-black bg-opacity-0 text-white rounded-full transition duration-200 hover:bg-opacity-50"
            >
              <div
                class="text-5xl font-bold opacity-0 h-32 w-32 text-center content-center transition duration-200 hover:opacity-100"
              >
                +
              </div>
            </div>

            <!-- Hidden file input -->
            <input
              type="file"
              ref="fileInput"
              accept="image/*"
              @change="handleFileUpload"
              class="hidden"
            />
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
        <!-- Buttons container -->
        <div
          class="flex flex-col sm:flex-row sm:justify-center sm:space-x-4 mt-6 items-center"
        >
          <!-- Add Job Advert button -->
          <button
            v-if="user.user_type === 'organisation'"
            @click="showJobAdvertModal = true"
            class="bg-green text-gray-700 font-semibold py-2 px-6 rounded-lg hover:scale-110 transition duration-200 mb-4 sm:mb-0 shadow-dark"
          >
            + Add Job Advert
          </button>

          <!-- Change Password button -->
          <button
            @click="showChangePasswordModal = true"
            class="bg-accent text-gray-700 font-semibold py-2 px-6 rounded-lg hover:scale-110 transition duration-200 shadow-dark"
          >
            Change Password
          </button>

          <!-- Change Name button -->
          <button
            @click="showChangeNameModal = true"
            class="bg-blue-500 text-gray-700 font-semibold py-2 px-6 rounded-lg hover:scale-110 transition duration-200 shadow-dark"
          >
            Change Name
          </button>
        </div>
        <!-- User adverts -->
        <div class="mt-8">
          <h2 class="text-2xl font-bold mb-4 mt-20 text-center sm:text-left">
            My Adverts
          </h2>
          <div
            v-if="adverts.length > 0"
            class="flex flex-wrap justify-center sm:justify-start -ml-0 sm:-ml-10"
          >
            <div
              v-for="advert in adverts"
              :key="advert._id"
              class="bg-white border border-slate-200 rounded-3xl px-5 py-5 transition hover:-translate-y-1 hover:shadow-xl hover:scale-103 w-full sm:w-80 m-5 h-auto flex flex-col justify-between"
            >
              <h3 class="text-xl font-semibold overflow-ellipsis overflow-hidden">
                {{ advert.Job_title }}
              </h3>
              <p class="overflow-ellipsis overflow-hidden">{{ advert.description }}</p>
              <p class="text-gray-600">City: {{ advert.city }}</p>

              <!-- Buttons container to align see more and delete button -->
              <div class="flex justify-between mt-2">
                <!-- See more button -->
                <router-link
                  :to="'/Jobs/' + advert.id"
                  class="bg-accent hover:scale-110 text-center text-gray-700 font-medium py-2 px-4 rounded-lg cursor-pointer transform active:scale-100 transition-transform shadow-dark"
                >
                  See more
                </router-link>

                <!-- Delete button -->
                <button
                  @click="deleteAdvert(advert.id)"
                  class="bg-red text-gray-700 font-semibold py-2 px-6 rounded-lg hover:bg-red transition duration-200 shadow-dark hover:scale-110"
                >
                  Delete
                </button>
              </div>
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
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
      >
        <div
          class="bg-white p-8 rounded-lg shadow-lg max-w-lg w-full max-h-full overflow-y-auto relative mx-4"
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
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green"
                required
              ></textarea>
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2">Job Title</label>
              <input
                type="text"
                v-model="jobAdvert.Job_title"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green"
                required
              />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2">Phone Number</label>
              <input
                type="text"
                v-model="jobAdvert.phone_number"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green"
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
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green"
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
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green"
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
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green"
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
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green"
                required
              >
                <option value="Liepaja">Liepaja</option>
                <option value="Ogre">Ogre</option>
                <option value="Bauska">Bauska</option>
                <option value="Jurmala">Jurmala</option>
                <option value="Tukums">Tukums</option>
                <option value="Ventspils">Ventspils</option>
                <option value="Riga">Riga</option>
              </select>
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2">Work Time</label>
              <select
                v-model="jobAdvert.workTime"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green"
                required
              >
                <option value="Workdays">Workdays</option>
                <option value="Weekend">Weekend</option>
                <option value="Schedule">Schedule</option>
              </select>
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2">Salary</label>
              <input
                type="number"
                v-model="jobAdvert.salary"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green"
                required
              />
            </div>
            <button
              type="submit"
              class="w-full bg-accent text-gray-700 font-semibold py-2 px-6 rounded-lg hover:bg-accent transition duration-200 shadow-dark"
            >
              Create Job Advert
            </button>
          </form>
        </div>
      </div>

      <!-- Change Password Modal -->
      <div
        v-if="showChangePasswordModal"
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
      >
        <div
          class="bg-white p-8 rounded-lg shadow-lg max-w-lg w-full max-h-full overflow-y-auto relative mx-4"
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
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green"
                required
              />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2">New Password</label>
              <input
                type="password"
                v-model="changePasswordForm.new_password"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green"
                required
              />
            </div>
            <button
              type="submit"
              class="w-full bg-accent text-gray-700 font-semibold py-2 px-6 rounded-lg hover:bg-accent transition duration-200 shadow-dark"
            >
              Change Password
            </button>
          </form>
        </div>
      </div>

      <!-- Change Name Modal -->
      <div
        v-if="showChangeNameModal"
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
      >
        <div
          class="bg-white p-8 rounded-lg shadow-lg max-w-lg w-full max-h-full overflow-y-auto relative mx-4"
        >
          <button
            @click="showChangeNameModal = false"
            class="absolute top-4 right-4 text-gray-700 hover:text-gray-900"
          >
            &times;
          </button>
          <h2 class="text-2xl font-bold mb-4 text-center">Change Name</h2>
          <!-- Error Message -->
          <p v-if="nameFormError" class="text-red-500 mb-4">{{ nameFormError }}</p>
          <!-- Success Message -->
          <p v-if="nameFormSuccess" class="text-green-500 mb-4">{{ nameFormSuccess }}</p>
          <!-- Form -->
          <form @submit.prevent="changeName">
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2">New Name</label>
              <input
                type="text"
                v-model="changeNameForm.name"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green"
                :placeholder="user.name"
                required
              />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2">New Surname</label>
              <input
                type="text"
                v-model="changeNameForm.surname"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green"
                :placeholder="user.surname"
                required
              />
            </div>
            <button
              type="submit"
              class="w-full bg-blue-500 text-gray-700 font-semibold py-2 px-6 rounded-lg hover:bg-blue-600 transition duration-200 shadow-dark"
            >
              Update Name
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
const showChangeNameModal = ref(false)
const formError = ref('')
const passwordFormError = ref('')
const nameFormError = ref('')
const nameFormSuccess = ref('')
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
  workTime: '',
  salary: '',
})

const changePasswordForm = ref({
  old_password: '',
  new_password: '',
})

const changeNameForm = ref({
  name: '',
  surname: '',
})

const fileInput = ref(null) // Reference to the file input element

// Method to trigger the file input click
const triggerFileUpload = () => {
  fileInput.value.click()
}

// Method to handle the file upload
const handleFileUpload = async (event) => {
  const file = event.target.files[0]
  if (file) {
    try {
      const formData = new FormData()
      formData.append('file', file)

      // Upload the file to the API
      const response = await axios.post('https://gachi.gay/api/upload', formData)

      const data = response.data
      const imageUrl = data.link // Get the image URL from the response

      // Save the image URL on the server
      await axios.post('http://127.0.0.1:5000/update_profile_image', {
        email: user.value.email,
        profileImageUrl: imageUrl,
      })

      // Update the image URL on the client, adding a timestamp to prevent caching
      user.value.profileImageUrl = `${imageUrl}?t=${new Date().getTime()}`
    } catch (error) {
      console.error(
        'Error uploading profile picture:',
        error.response ? error.response.data : error.message
      )
    }
  }
}

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
    console.error(
      'Error fetching user data:',
      error.response ? error.response.data : error.message
    )
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

    const response = await axios.post(
      'http://127.0.0.1:5000/create_job_advert',
      jobAdvert.value
    )
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
    console.error(
      'Error deleting advert:',
      error.response ? error.response.data : error.message
    )
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
      new_password: changePasswordForm.value.new_password,
    }

    const response = await axios.post(
      'http://127.0.0.1:5000/password_change',
      requestData
    )

    if (response.data.error) {
      passwordFormError.value = response.data.error
    } else {
      passwordFormError.value = ''
      showChangePasswordModal.value = false
    }
  } catch (error) {
    console.error(
      'Error changing password:',
      error.response ? error.response.data : error.message
    )
    passwordFormError.value = error.response?.data?.message || 'An error occurred.'
  }
}

// New Method to handle name and surname change
const changeName = async () => {
  try {
    if (!changeNameForm.value.name || !changeNameForm.value.surname) {
      nameFormError.value = 'Please fill in both name and surname.'
      nameFormSuccess.value = ''
      return
    }

    const email = localStorage.getItem('userEmail')
    if (!email) {
      throw new Error('User email not found in localStorage')
    }

    const requestData = {
      email,
      name: changeNameForm.value.name,
      surname: changeNameForm.value.surname,
    }

    const response = await axios.post(
      'http://127.0.0.1:5000/update_name',
      requestData
    )

    if (response.data.error) {
      nameFormError.value = response.data.error
      nameFormSuccess.value = ''
    } else {
      nameFormError.value = ''
      nameFormSuccess.value = 'Name and surname updated successfully.'
      showChangeNameModal.value = false
      await fetchUserData()
    }
  } catch (error) {
    console.error(
      'Error changing name:',
      error.response ? error.response.data : error.message
    )
    nameFormError.value = error.response?.data?.message || 'An error occurred.'
    nameFormSuccess.value = ''
  }
}

onMounted(fetchUserData)
</script>

<style>
/* Add any additional styles if needed */
</style>
