<template>
  <div class="container mx-auto p-8 dark:bg-dark-primary">
    <!-- Page Title -->
    <h1 class="text-3xl font-bold text-gray-700 dark:text-white text-center mb-8">Help & Support</h1>

    <!-- Intro Section -->
    <p class="text-center text-gray-700 dark:text-gray-300 mb-8">
      Welcome to our Help Center! Find answers to frequently asked questions and navigation.
    </p>

    <!-- FAQ Section -->
    <section class="mb-12">
      <h2 class="text-2xl text-gray-700 dark:text-white font-semibold mb-4">Frequently Asked Questions</h2>
      <div class="space-y-8">
        <div v-for="(faq, index) in faqs" :key="index">
          <!-- Line before the question -->
          <h1 class="text-gray-700 dark:text-white font-bold text-2xl">{{ faq.question }}</h1>
          <p class="mt-2 text-gray-700 dark:text-gray-300 p-4 bg-gray-200 dark:bg-gray-800 rounded-lg">
            {{ faq.answer }}
          </p>
        </div>
      </div>
    </section>

    <!-- Navigation Section (Expandable) -->
    <section>
      <div
        @click="isNavOpen = !isNavOpen"
        class="flex items-center cursor-pointer mb-4 transition-transform duration-200"
      >
        <h2 class="text-2xl text-gray-700 dark:text-white font-semibold hover:scale-110 transform transition-transform duration-200">
          Navigation
        </h2>
        <svg
          :class="{ 'rotate-90': isNavOpen }"
          class="w-5 h-5 ml-2 hover:scale-110 transform transition-transform duration-200"
          fill="currentColor"
          viewBox="0 0 20 20"
        >
          <path
            fill-rule="evenodd"
            d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
            clip-rule="evenodd"
          />
        </svg>
      </div>

      <!-- Main Navigation Links -->
      <div v-if="isNavOpen" class="pl-6 text-gray-700 dark:text-gray-300 space-y-2">
        <p>Here is the navigation section that will help you navigate throughout the website!</p>

        <!-- Sub-section One -->
        <div @click="isOneOpen = !isOneOpen" class="flex items-center cursor-pointer mt-4">
          <h3 class="text-xl font-semibold hover:scale-110 transform transition-transform duration-200 text-gray-700 dark:text-white">Home</h3>
          <svg
            :class="{ 'rotate-90': isOneOpen }"
            class="w-4 h-4 ml-2 transition-transform duration-200"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path
              fill-rule="evenodd"
              d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clip-rule="evenodd"
            />
          </svg>
        </div>
        <div v-if="isOneOpen" class="pl-8 text-gray-600 dark:text-gray-300">
          <p class="text-lg font-bold text-center mb-4">Hi! This part will help you navigate through the Home page of our website.</p>
          <p class="mb-5">• To get to the main page with all adverts you need to register or log in.</p>
          <img src="../assets/Images/Help1.png" class="w-9/12 mt-2 shadow mb-5">
          <p class="mb-5">• When you click on the 'Login/Register' button, you will see a choice window. Choose the necessary option.</p>
          <img src="../assets/Images/Help2.png" class="w-9/12 mt-2 shadow mb-5">
        </div>

        <!-- Sub-section Two -->
        <div @click="isTwoOpen = !isTwoOpen" class="flex items-center cursor-pointer mt-4">
          <h3 class="text-xl font-semibold hover:scale-110 transform transition-transform duration-200 text-gray-700 dark:text-white">Adverts</h3>
          <svg
            :class="{ 'rotate-90': isTwoOpen }"
            class="w-4 h-4 ml-2 transition-transform duration-200"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path
              fill-rule="evenodd"
              d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clip-rule="evenodd"
            />
          </svg>
        </div>
        <div v-if="isTwoOpen" class="pl-8 text-gray-600 dark:text-gray-300">Navigation through Adverts:</div>

        <!-- Sub-section Three -->
        <div @click="isThreeOpen = !isThreeOpen" class="flex items-center cursor-pointer mt-4">
          <h3 class="text-xl font-semibold hover:scale-110 transform transition-transform duration-200 text-gray-700 dark:text-white">Profile</h3>
          <svg
            :class="{ 'rotate-90': isThreeOpen }"
            class="w-4 h-4 ml-2 transition-transform duration-200"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path
              fill-rule="evenodd"
              d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clip-rule="evenodd"
            />
          </svg>
        </div>
        <div v-if="isThreeOpen" class="pl-8 text-gray-600 dark:text-gray-300">Navigation through Profile:</div>
      </div>
    </section>

    <!-- Contacts Section -->
    <section>
      <div
        @click="isConOpen = !isConOpen"
        class="flex items-center cursor-pointer mb-4 transition-transform duration-200"
      >
        <h2 class="mt-2 text-2xl text-gray-700 dark:text-white font-semibold hover:scale-110 transform transition-transform duration-200">Contacts</h2>
        <svg
          :class="{ 'rotate-90': isConOpen }"
          class="w-5 h-5 ml-2 hover:scale-110 transform transition-transform duration-200"
          fill="currentColor"
          viewBox="0 0 20 20"
        >
          <path
            fill-rule="evenodd"
            d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
            clip-rule="evenodd"
          />
        </svg>
      </div>

      <!-- Main Contacts Info -->
      <div v-if="isConOpen" class="pl-6 text-gray-700 dark:text-gray-300 space-y-2">
        <p>• E-mail: Work4U@gmail.com</p>
        <p>• Contact number: +371 23277692</p>
        <p>• Address: Mazcenu aleja 31, Jaunmarupe</p>
      </div>
    </section>
  </div>
</template>

  
  <script>
  export default {
    data() {
      return {
        faqs: [
          { question: "How do I change my password?", answer: "Go to account settings and click 'Change Password'." },
          { question: "Where can I find applications on my organization's vacancy?", answer: "Check under your account information in your profile." },
        ],
        isNavOpen: false, 
        isOneOpen: false, 
        isTwoOpen: false, 
        isThreeOpen: false, 
        isConOpen: false,
      };
    },
  };
  </script>
  
