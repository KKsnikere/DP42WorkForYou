<template>
    <div>
      <!-- Modal -->
      <div
        v-if="isModalOpen"
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
      >
        <div class="bg-white rounded-lg shadow-lg p-6 w-full max-w-lg">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-xl font-semibold">Edit Profile</h2>
            <button @click="closeModal" class="text-gray-500 hover:text-gray-700">
              ✕
            </button>
          </div>
          <!-- Name and Surname Editing Section -->
          <div class="mb-6">
            <h3 class="text-lg font-medium mb-2">Name & Surname</h3>
            <div class="space-y-2">
              <div>
                <label for="name" class="block text-sm font-medium text-gray-700">
                  Name
                </label>
                <input
                  v-model="name"
                  id="name"
                  type="text"
                  class="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
              <div>
                <label
                  for="surname"
                  class="block text-sm font-medium text-gray-700"
                >
                  Surname
                </label>
                <input
                  v-model="surname"
                  id="surname"
                  type="text"
                  class="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
            </div>
          </div>
  
          <!-- Password Editing Section -->
          <div class="mb-6">
            <h3 class="text-lg font-medium mb-2">Change Password</h3>
            <div class="space-y-2">
              <div>
                <label
                  for="current-password"
                  class="block text-sm font-medium text-gray-700"
                >
                  Current Password
                </label>
                <input
                  v-model="currentPassword"
                  id="current-password"
                  type="password"
                  class="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
              <div>
                <label
                  for="new-password"
                  class="block text-sm font-medium text-gray-700"
                >
                  New Password
                </label>
                <input
                  v-model="newPassword"
                  id="new-password"
                  type="password"
                  class="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
              <div>
                <label
                  for="confirm-password"
                  class="block text-sm font-medium text-gray-700"
                >
                  Confirm Password
                </label>
                <input
                  v-model="confirmPassword"
                  id="confirm-password"
                  type="password"
                  class="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
            </div>
          </div>
  
          <!-- Action Buttons -->
          <div class="flex justify-end space-x-4">
            <button
              @click="closeModal"
              class="bg-gray-300 text-gray-700 px-4 py-2 rounded hover:bg-gray-400"
            >
              Cancel
            </button>
            <button
              @click="saveChanges"
              class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
            >
              Save Changes
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isModalOpen: false,
        name: "",
        surname: "",
        currentPassword: "",
        newPassword: "",
        confirmPassword: "",
      };
    },
    methods: {
      openModal() {
        this.isModalOpen = true;
      },
      closeModal() {
        this.isModalOpen = false;
      },
      saveChanges() {
        // Handle saving the data
        console.log({
          name: this.name,
          surname: this.surname,
          currentPassword: this.currentPassword,
          newPassword: this.newPassword,
          confirmPassword: this.confirmPassword,
        });
  
        // Close the modal after saving changes
        this.closeModal();
      },
    },
  };
  </script>
  
  <style scoped>
  /* Custom styles (optional) */
  </style>
  