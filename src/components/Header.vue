<template>
  <header class="flex justify-between border-b border-slate-380 px-11 py-5 relative z-9">
    <!-- Left part -->
    <div class="flex items-center gap-4 shrink-0">
      <div>
        <!-- Logo -->
        <router-link to="/home">
          <img src="../assets/Images/logo.png" alt="Logo" class="w-10" />
        </router-link>
      </div>
      <div>
        <!-- Motto -->
        <h2 class="text-xl font-bold uppercase">Work For You</h2>
        <p class="text-slate-500">Realize yourself</p>
      </div>
    </div>

    <!-- Right part -->
    <div class="flex items-center gap-10 md:hidden">
      <!-- Popup Menu Button -->
      <button
        @click="toggleMenu"
        @click.stop
        class="p-2 rounded-full bg-gradient-to-br from-primary to-accent hover:from-accent hover:to-primary hover:scale-105 focus:outline-none flex items-center justify-center transition duration-200"
      >
        <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 4v16m8-8H4"
          />
        </svg>
      </button>
    </div>

    <ul class="flex items-center gap-10 hidden md:flex">
      <template v-if="!isAuthenticated">
        <li class="flex items-center cursor-pointer gap-3 text-gray-600 hover:text-green-500">
          <button
            @click="openAuthModal"
            class="text-base py-2 px-4 bg-accent text-white rounded-lg  transition duration-200 hover:scale-110"
          >
            Login/Register
          </button>
        </li>
      </template>
      <template v-else>
        <li class="flex items-center gap-3 text-gray-500">
          <router-link to="/favourites" class="py-2 px-4 flex items-center gap-3  hover:text-green-500 cursor-pointer">
            <img src="../assets/Images/heart.svg" alt="Favorite" width="25" height="25" />
            <p class="text-base">Favourites</p>
          </router-link>
          <router-link to="/profile" class="flex items-center gap-3 hover:text-green-500 mr-5 cursor-pointer">
            <img src="../assets/Images/Profile.png" alt="Profile" width="30" height="30" />
            <p class="text-sm">Profile</p>
          </router-link>
          <button
            @click="logout"
            class="text-base py-2 px-4 bg-red-500 text-white rounded-lg hover:bg-red-600 transition duration-200"
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
        v-click-outside= "closeMenu"
        class="fixed top-0 right-0 h-full w-56 bg-white shadow-md z-20 cursor-pointer"
      >
        <!-- Close Button -->
        <div class="flex justify-end p-4">
          <button
            @click="closeMenuDirectly"
            class="text-gray-600 hover:text-red-500 focus:outline-none"
          >
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
        <!-- Menu Content -->
        <div class="p-4 space-y-4">
          <template v-if="isAuthenticated">
            <router-link
              to="/favourites"
              class="py-2 flex items-center gap-3"
            >
              <img src="../assets/Images/heart.svg" alt="Favorite" width="25" height="25" />
              <p class="text-base">Favourites</p>
            </router-link>
            <router-link to="/profile" class="flex items-center gap-3">
              <img src="../assets/Images/Profile.png" alt="Profile" width="30" height="30" />
              <p class="text-sm">Profile</p>
            </router-link>
            <button
              @click="logout"
              class="w-full text-base py-2 px-4 bg-red-500 text-white rounded-lg hover:bg-red-600 transition duration-200"
            >
              Log Out
            </button>
          </template>
          <template v-else>
            <button
              @click="openAuthModal"
              class="text-base py-2 px-4 bg-accent text-white rounded-lg transition duration-200 hover:scale-110"
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

export default {
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
