<template>
  <!-- Upper separator line -->
  <div class="border-t dark:border-gray-700"></div>

  <footer class="dark:bg-dark-primary text-white bg-primary py-8">
    <div class="container mx-auto px-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
        <!-- Quick Links Section -->
        <div>
          <h3 class="text-lg font-semibold dark:text-blue-400 text-gray-700 mb-4">Quick Links</h3>
          <ul class="space-y-2">
            <li>
              <a href="/help" class="dark:text-gray-400 text-gray-600 dark:hover:text-blue-300 hover:text-dark-green transition duration-300">Help</a>
            </li>
          </ul>
        </div>

        <!-- Contact Us Section -->
        <div>
          <h3 class="text-lg font-semibold  dark:text-blue-400 text-gray-700 mb-4">Contact Us</h3>
          <div class="space-y-2">
            <p class="text-base flex items-center justify-center">
              <span class="material-icons dark:text-blue-300 text-gray-900 font-semibold mr-2">Mail</span>
              <a href="mailto:Work4U@gmail.com" class="dark:text-gray-400 text-gray-600 dark:hover:text-blue-300 hover:text-dark-green transition duration-300">Work4U@gmail.com</a>
            </p>
            <p class="text-base flex items-center justify-center">
              <span class="material-icons dark:text-blue-300 text-gray-900 font-semibold mr-2">Phone</span>
              <span class="dark:text-gray-400 text-gray-600">+23277692</span>
            </p>
          </div>
        </div>

        <!-- Social Media / Extra Section -->
        <div>
          <h3 class="text-lg font-semibold  dark:text-blue-400 text-gray-700 mb-4">Follow Us</h3>
          <div class="flex justify-center space-x-4">
            <!-- Social Media Icons -->
            <a href="https://www.facebook.com" class="dark:text-gray-400 text-gray-600 dark:hover:text-blue-300 hover:text-dark-green transition duration-300">
              <span class="material-icons">Facebook</span>
            </a>

            <!-- Add more icons as needed -->
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "FooterComponent",
};
</script>
