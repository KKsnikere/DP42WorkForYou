<template>
    <div class="max-w-lg mx-auto p-6 bg-white rounded-lg shadow-md">
      <h2 class="text-2xl font-bold mb-6 text-center">Apply Form</h2>
      
      <!-- Form -->
      <form @submit.prevent="handleSubmit">
        <!-- Name Field -->
        <div class="mb-4">
          <label for="name" class="block text-gray-700 font-medium mb-2">First Name</label>
          <input 
            type="text" 
            id="name" 
            v-model="form.name" 
            placeholder="Enter your first name"
            class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
            required
          />
        </div>
        
        <!-- Surname Field -->
        <div class="mb-4">
          <label for="surname" class="block text-gray-700 font-medium mb-2">Surname</label>
          <input 
            type="text" 
            id="surname" 
            v-model="form.surname" 
            placeholder="Enter your surname"
            class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
            required
          />
        </div>
        
        <!-- Phone Number Field -->
        <div class="mb-4">
          <label for="phone" class="block text-gray-700 font-medium mb-2">Phone Number</label>
          <input 
            type="tel" 
            id="phone" 
            v-model="form.phone" 
            placeholder="Enter your phone number"
            class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
            required
          />
        </div>
        
        <!-- Email Field -->
        <div class="mb-4">
          <label for="email" class="block text-gray-700 font-medium mb-2">Email</label>
          <input 
            type="email" 
            id="email" 
            v-model="form.email" 
            placeholder="Enter your email address"
            class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
            required
          />
        </div>
        
        <!-- Message Field -->
        <div class="mb-4">
          <label for="message" class="block text-gray-700 font-medium mb-2">Message</label>
          <textarea 
            id="message" 
            v-model="form.message" 
            placeholder="Enter your message" 
            class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
            rows="5"
            required
          ></textarea>
        </div>
        
        <!-- Upload Button (Smaller) -->
        <div class="mb-6">
          <button 
            type="button" 
            class="p-2 px-4 text-sm text-white bg-blue-500 rounded-lg focus:outline-none hover:bg-blue-400"
          >
            Upload Files
          </button>
        </div>
  
        <!-- Apply Button -->
        <div class="mb-6">
          <button 
            type="button" 
            class="w-full p-3 text-white bg-purple-600 rounded-lg focus:outline-none hover:bg-purple-500"
            @click="handleApply"
          >
            Apply
          </button>
        </div>
        
        <!-- Submit Button -->
        <div>
          <button 
            type="submit" 
            class="w-full p-3 text-white bg-green-600 rounded-lg focus:outline-none hover:bg-green-500"
          >
            Submit Application
          </button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        form: {
          name: '',
          surname: '',
          phone: '',
          email: '',
          message: ''
        }
      };
    },
    methods: {
      handleSubmit() {
        // Basic form submission logic
        console.log("Form Submitted:", this.form);
        alert('Form submitted successfully!');
        
        // Reset form after submission
        this.form = {
          name: '',
          surname: '',
          phone: '',
          email: '',
          message: ''
        };
      },
      
      handleApply() {
        // Functionality for Apply button
        console.log("Apply button clicked:", this.form);
        alert('You have applied successfully!');
        
        // You can add more logic here if needed, e.g., partial submission, tracking, etc.
      }
    }
  };
  </script>
  
  