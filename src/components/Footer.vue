<template>
    <footer class="dark:bg-dark-primary text-white bg-gray-100 py-6">
      <div class="container mx-auto px-6">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Quick Links Section -->
          <div>
            <h3 class="text-lg font-semibold text-blue-400 mb-4">Quick Links</h3>
            <ul class="space-y-2">
              <li>
                <a href="/help" class="text-base hover:text-blue-300 transition duration-300">Help</a>
              </li>
            </ul>
          </div>
  
          <!-- Contact Us Section -->
          <div>
            <h3 class="text-lg font-semibold text-blue-400 mb-4">Contact Us</h3>
            <div class="space-y-2">
              <p class="text-base">Email: <a href="mailto:YourEmail@example.com" class="text-blue-300 hover:text-blue-400 transition duration-300">YourEmail@example.com</a></p>
              <p class="text-base">Phone: <span class="text-gray-400">+123456789</span></p>
            </div>
          </div>
  
          <!-- Extra Space (empty) for alignment purposes -->
          <div></div>
        </div>
  
        <!-- Divider line for extra style -->
        <div class="mt-8 border-t border-gray-700"></div>
  
        <!-- Rights Reserved Section -->
        <div class="mt-4 text-center text-sm text-gray-500">
          <p>&copy; 2024 Work4U. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: "FooterComponent",
  };
  </script>
  
  <style scoped>
  /* No custom styles necessary for this version, Tailwind handles the styling */
  </style>
  