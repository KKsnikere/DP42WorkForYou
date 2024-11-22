<template>
  <header 
    class="flex justify-between border-b px-11 py-5 relative z-9 
           bg-primary text-gray-700 border-slate-380 dark:bg-dark-primary dark:text-gray-200 dark:border-dark-accent">
    <!-- Left part -->
    <div class="flex items-center gap-4 shrink-0">
      <div>
        <!-- Logo -->
        <router-link to="/home">
          <img src="../assets/Images/logo2.svg" alt="Logo" class="w-60 -ml-8" />
        </router-link>
      </div>
    </div>

    <!-- Right part -->
    <div class="flex items-center gap-10 md:hidden">
      <!-- Popup Menu Button -->
      <button
        @click="toggleMenu"
        @click.stop
        class="p-2 rounded-full bg-gradient-to-br from-primary to-accent hover:from-accent hover:to-primary hover:scale-105 focus:outline-none flex items-center justify-center transition duration-200 dark:from-dark-primary dark:to-dark-accent"
      >
        <svg class="h-6 w-6 text-gray-700 dark:text-gray-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
      </button>
    </div>

    <ul class="flex items-center gap-10 hidden md:flex">
      <template v-if="!isAuthenticated">
        <button
          @click="toggleDarkMode"
          class="dark-mode-toggle bg-gray-200 text-gray-800 border-gray-400 p-2 rounded-full 
                 transition-colors duration-300 ease-in-out dark:bg-dark-darker dark:text-gray-200 dark:border-gray-600"
          aria-label="Toggle Dark Mode"
        >
          <span v-if="!isDark">🌞</span>
          <span v-else>🌙</span>
        </button>
        <li class="flex items-center cursor-pointer gap-3 text-gray-600 hover:text-green-500 dark:text-gray-300 dark:hover:text-dark-greener">
          <button
            @click="openAuthModal"
            class="text-base py-2 px-4 bg-accent text-gray-700 font-medium rounded-lg  
                   transition duration-200 hover:scale-110 shadow-dark dark:bg-dark-accent dark:text-gray-200"
          >
            Login/Register
          </button>
        </li>
      </template>
      <template v-else>
        <button
          @click="toggleDarkMode"
          class="dark-mode-toggle bg-gray-200 text-gray-800 border-gray-400 p-2 rounded-full 
                 transition-colors duration-300 ease-in-out dark:bg-dark-darker dark:text-gray-200 dark:border-gray-600"
          aria-label="Toggle Dark Mode"
        >
          <span v-if="!isDark">🌞</span>
          <span v-else>🌙</span>
        </button>
        <li class="flex items-center gap-3 text-gray-500 dark:text-gray-300">
          <router-link to="/favourites" class="py-2 px-4 flex items-center gap-3 hover:text-dark-greener cursor-pointer dark:hover:text-dark-greener">
            <img src="../assets/Images/heart.svg" alt="Favorite" width="25" height="25" />
            <p class="text-base">Favourites</p>
          </router-link>
          <router-link to="/profile" class="flex items-center gap-3 hover:text-dark-greener cursor-pointer mr-5 dark:hover:text-dark-greener">
            <img src="../assets/Images/Profile.png" alt="Profile" width="30" height="30" />
            <p class="text-sm">Profile</p>
          </router-link>
          <button
            @click="logout"
            class="text-base py-2 px-4 font-medium bg-red text-gray-700 rounded-lg 
                   hover:bg-red transition duration-200 shadow-dark dark:bg-dark-red dark:text-gray-200"
          >
            Log Out
          </button>
        </li>
      </template>
    </ul>

    <!-- Popup Menu -->
    <transition name="slide">
      <div
        ref="menu"
        v-if="isMenuOpen"
        v-click-outside="closeMenu"
        class="fixed top-0 right-0 h-full w-56 bg-white shadow-md z-20 cursor-pointer dark:bg-dark-secondary dark:shadow-lg"
      >
        <!-- Close Button -->
        <div class="flex justify-end p-4">
          <button
            @click="closeMenuDirectly"
            class="text-gray-700 hover:text-red-500 dark:text-gray-300 dark:hover:text-dark-red focus:outline-none"
          >
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <!-- Menu Content -->
        <div class="p-4 space-y-4">
          <template v-if="isAuthenticated">
            <router-link to="/favourites" class="py-2 flex items-center gap-3 text-gray-700 dark:text-gray-200">
              <img src="../assets/Images/heart.svg" alt="Favorite" width="25" height="25" />
              <p class="text-base">Favourites</p>
            </router-link>
            <router-link to="/profile" class="flex items-center gap-3 text-gray-700 dark:text-gray-200">
              <img src="../assets/Images/Profile.png" alt="Profile" width="30" height="30" />
              <p class="text-sm">Profile</p>
            </router-link>
            <button
              @click="logout"
              class="w-full text-base py-2 px-4 bg-red text-gray-700 font-medium rounded-lg 
                     hover:bg-red transition duration-200 shadow-dark dark:bg-dark-red dark:text-gray-200"
            >
              Log Out
            </button>
          </template>
          <template v-else>
            <button
              @click="toggleDarkMode"
              class="dark-mode-toggle bg-gray-200 text-gray-800 border-gray-400 p-2 rounded-full 
                     transition-colors duration-300 ease-in-out dark:bg-dark-darker dark:text-gray-200 dark:border-gray-600"
              aria-label="Toggle Dark Mode"
            >
              <span v-if="!isDark">🌞</span>
              <span v-else>🌙</span>
            </button>
            <button
              @click="openAuthModal"
              class="text-base py-2 px-4 bg-accent text-gray-700 font-medium rounded-lg 
                     transition duration-200 hover:scale-110 shadow-dark dark:bg-dark-accent dark:text-gray-200"
            >
              Login/Register
            </button>
          </template>
        </div>
      </div>
    </transition>

    <AuthModal
      v-if="isAuthModalOpen"
      @close="isAuthModalOpen = false"
      @login="login"
      @register="register"
    />
  </header>
</template>

<script>
import AuthModal from './AuthModal.vue'
import { useDarkMode } from '@/composables/useDarkMode';

export default {
  setup() {
    const { isDark, toggleDarkMode } = useDarkMode(); // Fix the destructuring

    return {
      isDark, 
      toggleDarkMode
    };
  },
  components: {
    AuthModal
  },
  data() {
    return {
      isMenuOpen: false,
      isAuthModalOpen: false,
      isAuthenticated: false
    }
  },
  created() {
    this.verifyToken()
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen
    },
    closeMenuDirectly() {
      this.isMenuOpen = false
    },
    closeMenu() {
      this.isMenuOpen = false;
    },
    openAuthModal() {
      this.isAuthModalOpen = true
    },
    async login() {
      this.isAuthenticated = true
      this.isAuthModalOpen = false
    },
    async logout() {
      try {
        const response = await fetch('http://localhost:5000/logout', {
          method: 'POST',
          credentials: 'include'
        })
        if (response.ok) {
          // Remove email from localStorage
          localStorage.removeItem('userEmail')

          // Update authentication state
          this.isAuthenticated = false

          // Redirect user to login page or reload
          window.location.reload()
        } else {
          console.error('Logout failed')
        }
      } catch (error) {
        console.error('Error during logout:', error)
      }
    },
    getCookie(name) {
      const nameEQ = name + '='
      const ca = document.cookie.split(';')
      for (let i = 0; i < ca.length; i++) {
        let c = ca[i]
        while (c.charAt(0) == ' ') c = c.substring(1, c.length)
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length)
      }
      return null
    },
    
    async verifyToken() {
      try {
        const response = await fetch('http://localhost:5000/verify-token', {
          method: 'GET',
          credentials: 'include' // Important for sending cookies
        })
        if (response.ok) {
          this.isAuthenticated = true
        } else {
          this.isAuthenticated = false
        }
      } catch (error) {
        console.error('Error verifying token:', error)
        this.isAuthenticated = false
      }
    }
  }
}
</script>