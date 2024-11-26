<template>
  <div
    class="fixed inset-0 bg-gray-800 bg-opacity-50 flex items-center justify-center z-50 transition-opacity duration-300 ease-out"
  >
    <div
      class="bg-white dark:bg-dark-primary p-8 rounded-xl w-full max-w-lg shadow-lg transform transition-all duration-300 ease-out"
    >
      <button
        @click="closeModal"
        class="absolute top-4 right-4 text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-white"
      >
        &times;
      </button>

      <h3
        class="text-2xl font-semibold text-gray-800 mb-6 text-center dark:text-white"
      >
        Edit Profile
      </h3>

      <!-- Section Buttons -->
      <div class="flex justify-center mb-4">
        <button
          @click="activeSection = 'name'"
          :class="{
            'bg-blue-600 text-white': activeSection === 'name',
            'bg-gray-200 text-gray-700': activeSection !== 'name',
          }"
          class="w-2/5 py-3 rounded-lg text-sm font-medium transition duration-200 "
        >
          Name & Surname
        </button>
        <button
          @click="activeSection = 'password'"
          :class="{
            'bg-blue-600 text-white': activeSection === 'password',
            'bg-gray-200 text-gray-700': activeSection !== 'password',
          }"
          class="w-2/5 py-3 rounded-lg text-sm font-medium transition duration-200 ml-5"
        >
          Password
        </button>
      </div>

      <!-- Name & Surname Section -->
      <div v-if="activeSection === 'name'" class="space-y-6">
        <!-- Error and Success Messages -->
        <p v-if="nameFormError" class="text-red-500 mb-4">
          {{ nameFormError }}
        </p>
        <p v-if="nameFormSuccess" class="text-green-500 mb-4">
          {{ nameFormSuccess }}
        </p>

        <form @submit.prevent="changeName">
          <div class="mb-4">
            <label
              for="name"
              class="block text-sm font-medium text-gray-600 dark:text-gray-300"
              >New Name</label
            >
            <input
              id="name"
              v-model="changeNameForm.name"
              type="text"
              class="mt-2 block w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white dark:border-gray-600"
              :placeholder="user ? user.name : ''"
              required
              pattern="[A-Za-z ]+"
            />
          </div>

          <div class="mb-4">
            <label
              for="surname"
              class="block text-sm font-medium text-gray-600 dark:text-gray-300"
              >New Surname</label
            >
            <input
              id="surname"
              v-model="changeNameForm.surname"
              type="text"
              class="mt-2 block w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white dark:border-gray-600"
              :placeholder="user ? user.surname : ''"
              required
              pattern="[A-Za-z ]+"
            />
          </div>

          <button
            type="submit"
            class="w-full bg-blue-600 text-white font-semibold py-2 px-6 rounded-lg hover:bg-blue-700 transition duration-200"
          >
            Update Name
          </button>
        </form>
      </div>

      <!-- Password Section -->
      <div v-if="activeSection === 'password'" class="space-y-6">
        <!-- Error Message -->
        <div
          v-if="passwordFormError"
          class="mb-4 p-4 bg-red-100 border border-red-400 text-red rounded-lg dark:bg-red-800 dark:border-red-600 dark:text-red-300"
        >
          <svg
            class="inline-block h-5 w-5 mr-2 text-red-500"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path
              fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm.707-11.707a1 1 0 00-1.414 0L8 8.586 7.707 8.293a1 1 0 10-1.414 1.414L8 11l2.707-2.707a1 1 0 000-1.414z"
              clip-rule="evenodd"
            />
          </svg>
          {{ passwordFormError }}
        </div>

        <form @submit.prevent="changePassword">
          <!-- Old Password Field -->
          <div class="mb-4 relative">
            <label
              for="old_password"
              class="block text-sm font-medium text-gray-600 dark:text-gray-300"
              >Old Password</label
            >
            <input
              id="old_password"
              :type="showOldPassword ? 'text' : 'password'"
              v-model="changePasswordForm.old_password"
              class="mt-2 block w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white dark:border-gray-600"
              required
            />
            <button
              type="button"
              @click="toggleOldPasswordVisibility"
              class="absolute inset-y-0 right-0 pr-3 flex items-center"
            >
              <img
                v-if="showOldPassword"
                src="../assets/Images/showP.png"
                alt="Show password"
                class="h-6 w-6 mt-8"
              />
              <img
                v-else
                src="../assets/Images/hideP.png"
                alt="Hide password"
                class="h-6 w-6 mt-8"
              />
            </button>
          </div>

          <!-- New Password Field -->
          <div class="mb-4 relative">
            <label
              for="new_password"
              class="block text-sm font-medium text-gray-600 dark:text-gray-300"
              >New Password</label
            >
            <input
              id="new_password"
              :type="showNewPassword ? 'text' : 'password'"
              v-model="changePasswordForm.new_password"
              class="mt-2 block w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white dark:border-gray-600"
              required
              minlength="8"
            />
            <button
              type="button"
              @click="toggleNewPasswordVisibility"
              class="absolute inset-y-0 right-0 pr-3 flex items-center"
            >
              <img
                v-if="showNewPassword"
                src="../assets/Images/showP.png"
                alt="Show password"
                class="h-6 w-6 mt-8"
              />
              <img
                v-else
                src="../assets/Images/hideP.png"
                alt="Hide password"
                class="h-6 w-6 mt-8"
              />
            </button>
          </div>

          <!-- Confirm New Password Field -->
          <div class="mb-4 relative">
            <label
              for="confirm_password"
              class="block text-sm font-medium text-gray-600 dark:text-gray-300"
              >Confirm New Password</label
            >
            <input
              id="confirm_password"
              :type="showConfirmPassword ? 'text' : 'password'"
              v-model="changePasswordForm.confirm_password"
              class="mt-2 block w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white dark:border-gray-600"
              required
              minlength="8"
            />
            <button
              type="button"
              @click="toggleConfirmPasswordVisibility"
              class="absolute inset-y-0 right-0 pr-3 flex items-center"
            >
              <img
                v-if="showConfirmPassword"
                src="../assets/Images/showP.png"
                alt="Show password"
                class="h-6 w-6 mt-8"
              />
              <img
                v-else
                src="../assets/Images/hideP.png"
                alt="Hide password"
                class="h-6 w-6 mt-8"
              />
            </button>
          </div>

          <button
            type="submit"
            class="w-full bg-blue-600 text-white font-semibold py-2 px-6 rounded-lg hover:bg-blue-700 transition duration-200"
          >
            Change Password
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

// Reactive state for the component
const user = ref(null); // user data, initially null
const activeSection = ref("name"); // Track active section (name or password)
const showOldPassword = ref(false);
const showNewPassword = ref(false);
const showConfirmPassword = ref(false);
const emit = defineEmits();

const nameFormError = ref("");
const nameFormSuccess = ref("");
const passwordFormError = ref("");
const changeNameForm = ref({
  name: "",
  surname: "",
});
const changePasswordForm = ref({
  old_password: "",
  new_password: "",
  confirm_password: "",
});

// Load user data when the component is mounted
onMounted(() => {
  loadUserData();
});

// Methods
const loadUserData = () => {
  const userData = localStorage.getItem("user");
  if (userData) {
    user.value = JSON.parse(userData);
  } else {
    console.warn("User data not found.");
  }
};

const toggleOldPasswordVisibility = () => {
  showOldPassword.value = !showOldPassword.value;
};

const toggleNewPasswordVisibility = () => {
  showNewPassword.value = !showNewPassword.value;
};

const toggleConfirmPasswordVisibility = () => {
  showConfirmPassword.value = !showConfirmPassword.value;
};

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
      console.log("Password changed successfully.");
      emit("close");  // Close the modal after success
      passwordFormError.value = "";
      passwordFormSuccess.value = "Password changed successfully!";
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
      emit("close");  // Close the modal after success
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

const closeModal = () => {
  // Emit close event
  emit("close");
};
</script>
