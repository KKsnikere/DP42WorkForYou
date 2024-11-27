<template>
  <div class="h-8 bg-white dark:bg-dark-primary"></div>
  <div id="app" class="h-screen dark:bg-dark-primary">
    <div class="container mx-auto px-4 dark:bg-dark-primary">
      <div
        class="dark:bg-dark-secondary shadow-md rounded-3xl p-6 mx-4 border border-accent"
      >
        <h1 class="text-3xl font-bold mb-6 text-center text-white">
          User Profile
        </h1>
        <div v-if="user" class="space-y-4 dark:bg-dark-secondary">
          <!-- Profile Image -->
          <div class="flex justify-center mb-4">
            <div
              class="relative w-32 h-32 rounded-full cursor-pointer mb-10"
              @click="triggerFileUpload"
            >
              <!-- Profile Image or placeholder -->
              <img
                v-if="user.profileImageUrl"
                :src="user.profileImageUrl"
                alt="Profile Image"
                class="w-full h-full rounded-full object-cover"
              />
              <div
                v-else
                class="w-full h-full bg-gray-300 dark:bg-gray-600 flex items-center justify-center text-gray-500 rounded-full"
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
          <div class="info-item text-gray-600 dark:text-gray-300">
            <span class="font-semibold">Email: </span>
            <span class="break-words">{{ user.email }}</span>
          </div>
          <div class="info-item text-gray-600 dark:text-gray-300">
            <span class="font-semibold">User Type: </span>
            <span class="break-words">{{ user.user_type }}</span>
          </div>
          <div
            v-if="user.name"
            class="info-item text-gray-600 dark:text-gray-300"
          >
            <span class="font-semibold">Name: </span>
            <span class="break-words">{{ user.name }}</span>
          </div>
          <div
            v-if="user.surname"
            class="info-item text-gray-600 dark:text-gray-300"
          >
            <span class="font-semibold">Surname: </span>
            <span class="break-words">{{ user.surname }}</span>
          </div>
          <div
            v-if="user.org_name"
            class="info-item text-gray-600 dark:text-gray-300"
          >
            <span class="font-semibold">Organization Name: </span>
            <span class="break-words">{{ user.org_name }}</span>
          </div>
          <div
            v-if="user.reg_number"
            class="info-item text-gray-600 dark:text-gray-300"
          >
            <span class="font-semibold">Registration Number: </span>
            <span class="break-words">{{ user.reg_number }}</span>
          </div>
          <div
            v-if="user.location"
            class="info-item text-gray-600 dark:text-gray-300"
          >
            <span class="font-semibold">Location: </span>
            <span class="break-words">{{ user.location }}</span>
          </div>

          <!-- Buttons container -->
          <div
            class="flex flex-col sm:flex-row sm:justify-center sm:space-x-4 space-y-4 sm:space-y-0 mt-6 items-center"
          >
            <button
              @click="showEditModal = true"
              class="dark:bg-blue-600 bg-accent text-white w-full sm:w-48 font-semibold py-2 px-6 rounded-lg hover:scale-110 transition duration-200 shadow-lg hover:shadow-xl"
            >
              Edit Profile
            </button>

            <!-- Modal Component -->
            <EditProfileModal
              v-if="showEditModal"
              @close="showEditModal = false"
            />

            <button
              v-if="user.user_type === 'organisation'"
              @click="showJobAdvertModal = true"
              class="dark:bg-blue-600 bg-accent text-white w-full sm:w-48 font-semibold py-2 px-6 rounded-lg hover:scale-110 transition duration-200 shadow-lg hover:shadow-xl"
            >
              Add job advert
            </button>

            <router-link to="/user-applications"
            class="w-full sm:w-48">
              <button
                v-if="user.user_type === 'individual'"
                class="dark:bg-blue-600 bg-accent text-white w-full sm:w-48 font-semibold py-2 px-6 rounded-lg hover:scale-110 transition duration-200 shadow-lg hover:shadow-xl"
              >
                My applications
              </button>
            </router-link>

            <button
              class="bg-rose-400 text-white w-full sm:w-48 font-semibold py-2 dark:bg-dark-red px-6 rounded-lg hover:scale-110 transition duration-200 shadow-lg hover:shadow-xl"
              @click="openModal()"
            >
              Delete account
            </button>
          </div>

          <!-- User adverts -->
          <div v-if="user.user_type === 'organisation'" class="mt-8">
            <h2 class="text-2xl font-bold mb-4 text-center sm:text-left dark:text-white">
              My Adverts
            </h2>
            <div
              v-if="adverts.length > 0"
              class="flex flex-wrap justify-center sm:justify-start -ml-0 sm:-ml-10"
            >
              <div
                v-for="advert in adverts"
                :key="advert._id"
                class="bg-white border border-slate-200 rounded-3xl px-5 py-5 transition hover:-translate-y-1 hover:shadow-xl hover:scale-103 w-full sm:w-80 m-5 h-auto flex flex-col justify-between dark:bg-gray-800 dark:border-gray-700 dark:text-white"
              >
                <h3 class="text-xl font-semibold overflow-ellipsis overflow-hidden">
                  {{ advert.Job_title }}
                </h3>
                <p class="overflow-ellipsis overflow-hidden">
                  {{ advert.description }}
                </p>
                <p class="text-gray-600 dark:text-gray-400">
                  City: {{ advert.city }}
                </p>
                <div class="flex justify-between mt-2">
                  <router-link
                    :to="'/applicants/' + advert.id"
                    class="bg-accent dark:bg-blue-600 hover:scale-110 text-center w-36 h-10 text-white font-medium py-2 px-4 rounded-lg dark:bg-accent-dark dark:text-white"
                  >
                    See applicants
                  </router-link>
                  <button
                    @click="deleteAdvert(advert.id)"
                    class="dark:bg-dark-red bg-rose-300 text-white font-semibold py-2 px-6 rounded-lg hover:bg-red transition duration-200 shadow-dark hover:scale-110 dark:bg-red-600 dark:text-white"
                  >
                    Delete
                  </button>
                </div>
              </div>
            </div>
            <div v-else>
              <p class="dark:text-white">No adverts found.</p>
            </div>
          </div>
        </div>
      </div>
      <!--Deleteacc modal-->
    <div
      id="deleteAccountModal"
      class="hidden fixed inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center z-50"
    >
      <!-- Modal Content -->
      <div class="bg-gray-800 rounded-lg shadow-lg w-80 p-6 space-y-4">
        <h2 class="text-lg font-semibold text-white">Delete Account</h2>
        <p class="text-sm text-gray-300">
          Are you sure you want to delete your account? This action cannot be
          undone.
        </p>
        <!-- Password Input -->
        <input
          type="password"
          id="passwordInput"
          placeholder="Enter your password"
          class="w-full border border-gray-500 rounded-md px-3 py-2 text-sm text-gray-300"
        />
        <!-- Buttons -->
        <div class="flex justify-center space-x-20">
          <button
            @click="confirmDelete()"
            class="bg-red-600 text-white py-1 px-4 rounded hover:bg-rose-700 transition duration-200"
          >
            Delete
          </button>
          <button
            @click="closeModal()"
            class="bg-gray-700 text-white py-1 px-4 rounded hover:bg-gray-600 transition duration-200"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
      <!-- Job Advert Modal -->
      <div
        v-if="showJobAdvertModal"
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
      >
        <div
          class="bg-white dark:bg-dark-primary p-8 rounded-lg shadow-lg max-w-lg w-full max-h-full overflow-y-auto relative mx-4"
        >
          <button
            @click="showJobAdvertModal = false"
            class="absolute top-4 right-4 text-gray-700 hover:text-gray-900"
          >
            &times;
          </button>
          <h2 class="text-2xl font-bold mb-4 text-center dark:text-white">Create Job Advert</h2>
          <!-- Error Message -->
          <p v-if="formError" class="text-red-500 mb-4">{{ formError }}</p>
          <!-- Form -->
          <form @submit.prevent="createJobAdvert">
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2 dark:text-gray-300">Company Name</label>
              <input
                type="text"
                v-model="jobAdvert.Company_name"
                class="w-full px-3 py-2 border rounded-lg bg-gray-200  dark:bg-dark-primary dark:border-dark-accent dark:text-gray-100"
                readonly
              />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2 dark:text-gray-300">Description</label>
              <textarea
                v-model="jobAdvert.description"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green  dark:bg-dark-secondary dark:border-dark-accent dark:text-gray-100"
                required
              ></textarea>
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2 dark:text-gray-300">Job Title</label>
              <input
                type="text"
                v-model="jobAdvert.Job_title"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green  dark:bg-dark-secondary dark:border-dark-accent dark:text-gray-100"
                required
              />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2 dark:text-gray-300">Phone Number</label>
              <input
                type="text"
                v-model="jobAdvert.phone_number"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green  dark:bg-dark-secondary dark:border-dark-accent dark:text-gray-100"
                required
              />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2 dark:text-gray-300">Registration Number</label>
              <input
                type="text"
                v-model="jobAdvert.reg_nr"
                class="w-full px-3 py-2 border rounded-lg bg-gray-200  dark:bg-dark-primary dark:border-dark-accent dark:text-gray-100"
                readonly
              />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2 dark:text-gray-300">Address</label>
              <input
                type="text"
                v-model="jobAdvert.address"
                class="w-full px-3 py-2 border rounded-lg bg-gray-200  dark:bg-dark-primary dark:border-dark-accent dark:text-gray-100"
                readonly
              />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2 dark:text-gray-300">Email</label>
              <input
                type="text"
                v-model="jobAdvert.email"
                class="w-full px-3 py-2 border rounded-lg bg-gray-200  dark:bg-dark-primary dark:border-dark-accent dark:text-gray-100"
                readonly
              />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2 dark:text-gray-300">Work Type</label>
              <select
                v-model="jobAdvert.worktype"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none  dark:bg-dark-secondary dark:border-dark-accent dark:text-gray-100"
                required
              >
                <option value="Part-Time">Part-Time</option>
                <option value="Full-time">Full-Time</option>
                <option value="One-time">One-time</option>
              </select>
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2 dark:text-gray-300">Profession</label>
              <select
                v-model="jobAdvert.profession"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none  dark:bg-dark-secondary dark:border-dark-accent dark:text-gray-100"
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
              <label class="block text-gray-700 font-semibold mb-2 dark:text-gray-300">Type of Work</label>
              <select
                v-model="jobAdvert.typeOfwork"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green  dark:bg-dark-secondary dark:border-dark-accent dark:text-gray-100"
                required
              >
                <option value="Online">Online</option>
                <option value="In-office">In-office</option>
              </select>
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2 dark:text-gray-300">City</label>
              <select
                v-model="jobAdvert.city"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green  dark:bg-dark-secondary dark:border-dark-accent dark:text-gray-100"
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
              <label class="block text-gray-700 font-semibold mb-2 dark:text-gray-300">Work Time</label>
              <select
                v-model="jobAdvert.workTime"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green  dark:bg-dark-secondary dark:border-dark-accent dark:text-gray-100"
                required
              >
                <option value="Workdays">Workdays</option>
                <option value="Weekend">Weekend</option>
                <option value="Schedule">Schedule</option>
              </select>
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 font-semibold mb-2 dark:text-gray-300">Salary</label>
              <input
                type="number"
                v-model="jobAdvert.salary"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-green  dark:bg-dark-secondary dark:border-dark-accent dark:text-gray-100"
                required
              />
            </div>
            <button
              type="submit"
              class="dark:bg-blue-600 bg-accent text-white w-full sm:w-48 font-semibold py-2 px-6 rounded-lg hover:scale-110 transition duration-200 shadow-lg hover:shadow-xl"
            >
              Create Job Advert
            </button>
          </form>
        </div>
      </div>
  </div>
</div>
</template>


<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import EditProfileModal from "../components/EditProfile.vue";

const router = useRouter();

const user = ref(null);
const showJobAdvertModal = ref(false);
const showChangePasswordModal = ref(false);
const showChangeNameModal = ref(false);
const formError = ref("");
const passwordFormError = ref("");
const nameFormError = ref("");
const nameFormSuccess = ref("");
const adverts = ref([]);

const showOldPassword = ref(false);
const showNewPassword = ref(false);
const showConfirmPassword = ref(false);
const showEditModal = ref(false);

const toggleOldPasswordVisibility = () => {
  showOldPassword.value = !showOldPassword.value;
};

const toggleNewPasswordVisibility = () => {
  showNewPassword.value = !showNewPassword.value;
};

const toggleConfirmPasswordVisibility = () => {
  showConfirmPassword.value = !showConfirmPassword.value;
};

const jobAdvert = ref({
  Company_name: "",
  description: "",
  Job_title: "",
  phone_number: "",
  reg_nr: "",
  address: "",
  email: "",
  worktype: "",
  profession: "",
  typeOfwork: "",
  city: "",
  workTime: "",
  salary: "",
});

const changeNameForm = ref({
  name: "",
  surname: "",
});

const fileInput = ref(null); // Reference to the file input element

// Method to trigger the file input click
const triggerFileUpload = () => {
  fileInput.value.click();
};

// Method to handle the file upload
const handleFileUpload = async (event) => {
  const file = event.target.files[0];
  if (file) {
    try {
      const formData = new FormData();
      formData.append("file", file);

      // Upload the file to the API
      const response = await axios.post(
        "https://gachi.gay/api/upload",
        formData
      );

      const data = response.data;
      const imageUrl = data.link; // Get the image URL from the response

      // Save the image URL on the server
      await axios.post("http://127.0.0.1:5000/update_profile_image", {
        email: user.value.email,
        profileImageUrl: imageUrl,
      });

      // Update the image URL on the client, adding a timestamp to prevent caching
      user.value.profileImageUrl = `${imageUrl}?t=${new Date().getTime()}`;
    } catch (error) {
      console.error(
        "Error uploading profile picture:",
        error.response ? error.response.data : error.message
      );
    }
  }
};

const fetchUserData = async () => {
  try {
    const email = localStorage.getItem("userEmail");
    if (!email) {
      throw new Error("User email not found in localStorage");
    }

    const response = await axios.post("http://127.0.0.1:5000/user", { email });
    user.value = response.data;
    if (user.value.user_type === "organisation") {
      jobAdvert.value.Company_name = user.value.org_name;
      jobAdvert.value.reg_nr = user.value.reg_number;
      jobAdvert.value.address = user.value.location;
      jobAdvert.value.email = user.value.email;
    }

    await fetchUserAdverts(email);
  } catch (error) {
    console.error(
      "Error fetching user data:",
      error.response ? error.response.data : error.message
    );
  }
};

const fetchUserAdverts = async (email) => {
  try {
    const response = await axios.post("http://127.0.0.1:5000/my_adverts", {
      email,
    });
    adverts.value = response.data;
  } catch (error) {
    console.error(
      "Error fetching user adverts:",
      error.response ? error.response.data : error.message
    );
  }
};

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
      formError.value = "Please fill in all fields.";
      return;
    }

    const response = await axios.post(
      "http://127.0.0.1:5000/create_job_advert",
      jobAdvert.value
    );
    console.log(response.data);
    formError.value = "";
    showJobAdvertModal.value = false;
    await fetchUserAdverts(user.value.email);
  } catch (error) {
    console.error(
      "Error creating job advert:",
      error.response ? error.response.data : error.message
    );
  }
};

const deleteAdvert = async (advertId) => {
  try {
    await axios.delete(`http://127.0.0.1:5000/jobs/${advertId}`);
    await fetchUserAdverts(user.value.email);
  } catch (error) {
    console.error(
      "Error deleting advert:",
      error.response ? error.response.data : error.message
    );
  }
};

function openModal() {
  document.getElementById("deleteAccountModal").classList.remove("hidden");
}

function closeModal() {
  document.getElementById("deleteAccountModal").classList.add("hidden");
}

async function confirmDelete() {
  const password = document.getElementById("passwordInput").value;

  console.log("Password entered:", password); // Check the captured password

  try {
    console.log("Sending delete request to /delete-account...");
    const userEmail = localStorage.getItem("userEmail");

    const response = await fetch("http://localhost:5000/delete-account", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${userEmail}`,
      },
      credentials: "include",
      body: JSON.stringify({ password }),
    });

    console.log("Response status:", response.status); // Log the response status

    if (response.ok) {
      console.log("Account deleted successfully.");
      alert("Account deleted successfully.");
      window.location.href = "/";
    } else {
      console.warn("Failed to delete account:", response.statusText); // Log the failure reason
      alert("Failed to delete account. Please check your password.");
    }
  } catch (error) {
    console.error("Error during account deletion:", error); // Log any caught errors
    alert("An error occurred.");
  }

  closeModal();
  console.log("Modal closed after delete attempt.");
}

const changePasswordForm = ref({
  old_password: "",
  new_password: "",
  confirm_password: "",
});

const changePassword = async () => {
  try {
    // Clear previous error
    passwordFormError.value = "";

    // Check if all fields are filled
    if (
      !changePasswordForm.value.old_password ||
      !changePasswordForm.value.new_password ||
      !changePasswordForm.value.confirm_password
    ) {
      passwordFormError.value = "Please fill in all fields.";
      return;
    }

    // Check if new password matches confirmation
    if (
      changePasswordForm.value.new_password !==
      changePasswordForm.value.confirm_password
    ) {
      passwordFormError.value =
        "New password and confirm password do not match.";
      return;
    }

    const email = localStorage.getItem("userEmail");
    if (!email) {
      throw new Error("User email not found in localStorage");
    }

    // Prepare request data
    const requestData = {
      email,
      old_password: changePasswordForm.value.old_password,
      new_password: changePasswordForm.value.new_password,
    };

    // Make API request to change the password
    const response = await axios.post(
      "http://127.0.0.1:5000/password_change",
      requestData
    );

    // Handle response
    if (response.data.error) {
      passwordFormError.value = response.data.error;
    } else {
      passwordFormError.value = "";
      showChangePasswordModal.value = false;
      console.log("Password changed successfully.");
    }
  } catch (error) {
    console.error(
      "Error changing password:",
      error.response ? error.response.data : error.message
    );
    passwordFormError.value =
      error.response?.data?.message || "An error occurred.";
  }
};

// New Method to handle name and surname change
const changeName = async () => {
  try {
    if (!changeNameForm.value.name || !changeNameForm.value.surname) {
      nameFormError.value = "Please fill in both name and surname.";
      nameFormSuccess.value = "";
      return;
    }

    const email = localStorage.getItem("userEmail");
    if (!email) {
      throw new Error("User email not found in localStorage");
    }

    const requestData = {
      email,
      name: changeNameForm.value.name,
      surname: changeNameForm.value.surname,
    };

    const response = await axios.post(
      "http://127.0.0.1:5000/update_name",
      requestData
    );

    if (response.data.error) {
      nameFormError.value = response.data.error;
      nameFormSuccess.value = "";
    } else {
      nameFormError.value = "";
      nameFormSuccess.value = "Name and surname updated successfully.";
      showChangeNameModal.value = false;
      await fetchUserData();
    }
  } catch (error) {
    console.error(
      "Error changing name:",
      error.response ? error.response.data : error.message
    );
    nameFormError.value = error.response?.data?.message || "An error occurred.";
    nameFormSuccess.value = "";
  }
};

onMounted(fetchUserData);
</script>
