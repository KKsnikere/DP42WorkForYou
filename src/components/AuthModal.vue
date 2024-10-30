<template>
  <div class="fixed inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center z-30">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
      <div class="flex justify-between items-center border-b pb-3 mb-4">
        <h3 class="text-2xl font-semibold text-gray-800">Sign in options</h3>
        <button @click="$emit('close')" class="text-gray-600 hover:text-red focus:outline-none">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Registration and login form -->
      <div v-if="step === 'choose'" class="space-y-4">
        <div v-if="loginError" class="text-red text-sm mt-2">Incorrect password or email</div>
        <button @click="step = 'login'" class="w-full bg-green text-gray-700 py-2 px-4 rounded-lg font-medium hover:bg-green transition duration-200 shadow-dark">
          Log In
        </button>
        <button @click="setRegisterChoice" class="w-full bg-accent text-gray-700 py-2 px-4 font-medium rounded-lg hover:bg-accent transition duration-200 shadow-dark">
          Register
        </button>
      </div>

      <!-- Registration form for individual -->
      <form v-if="step === 'registerChoice'" @submit.prevent="register" class="space-y-8">
        <div class="flex justify-center gap-4">
          <button
            type="button"
            @click.prevent="userType = 'individual'"
            :class="userType === 'individual' ? 'bg-accent' : 'bg-green'"
            class="w-full text-gray-700 py-2 px-4 rounded-lg hover:bg-accent transition duration-200 shadow-dark"
          >
            Private Person
          </button>
          <button
            type="button"
            @click.prevent="userType = 'organisation'"
            :class="userType === 'organisation' ? 'bg-accent' : 'bg-green'"
            class="w-full text-gray-700 py-2 px-4 rounded-lg hover:bg-accent transition duration-200 shadow-dark"
          >
            Organisation
          </button>
        </div>

        <div v-if="userType === 'individual'" class="space-y-6">
          <input
            v-model="name"
            type="text"
            placeholder="Name"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200"
            required
            pattern="[A-Za-z ]+"
          />
          <input
            v-model="surname"
            type="text"
            placeholder="Surname"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200"
            required
            pattern="[A-Za-z ]+"
          />
        </div>
        <div v-else>
          <input
            v-model="orgName"
            type="text"
            placeholder="Organisation Name"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200"
            required
          />
          <input
            v-model="regNumber"
            type="text"
            placeholder="Registration Number"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200 mt-6"
            required
          />
          <input
            v-model="location"
            type="text"
            placeholder="Location"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200 mt-6"
            required
          />
        </div>

        <input
          v-model="email"
          type="email"
          placeholder="Email"
          class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200"
          required
        />
<!-- Password with Show/Hide Button -->
        <div class="relative">
          <input
            v-model="password"
            :type="showPassword ? 'text' : 'password'"
            placeholder="Password"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200"
            required
            minlength="8"
          />
          <button type="button" @click="togglePasswordVisibility" class="absolute inset-y-0 right-0 pr-3 flex items-center">
            <img
              v-if="showPassword"
              src="../assets/Images/showP.png"
              alt="Show password"
              class="h-6 w-6"
            />
            <img
              v-else
              src="../assets/Images/hideP.png"
              alt="Hide password"
              class="h-6 w-6"
            />
          </button>
        </div>
        <button type="submit" class="w-full bg-accent text-gray-700 py-2 px-4 rounded-lg font-medium hover:bg-accent transition duration-200 shadow-dark">
          Register
        </button>

        <div class="mt-4 text-sm text-gray-600">
        <span>Don't have an account? </span>
        <button @click="step = 'login'" class="text-blue-600">Login</button>
      </div>
      </form>

      <!-- OTP Verification Form -->
      <form v-if="step === 'verifyOtp'" @submit.prevent="verifyOtp" class="space-y-4">
        <h3 class="text-lg font-semibold text-gray-800">Enter OTP</h3>
        <input
          v-model="otp"
          type="text"
          placeholder="Enter OTP sent to your email"
          class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200"
          required
        />
        <button type="submit" class="w-full bg-accent text-gray-700 py-2 px-4 rounded-lg font-medium hover:bg-accent transition duration-200 shadow-dark">
          Verify OTP
        </button>
        <div v-if="otpError" class="text-red text-sm mt-2">{{ otpError }}</div>
      </form>

      <!-- Login form -->
<form v-if="step === 'login'" @submit.prevent="login" class="space-y-4">
  <input
    v-model="email"
    type="email"
    placeholder="Email"
    class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200"
    required
  />

  <!-- Password input with Show/Hide Button and Error Message -->
  <div class="space-y-1">
    <div class="relative flex items-center">
      <input
        v-model="password"
        :type="showPassword ? 'text' : 'password'"
        placeholder="Password"
        class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200"
        required
        minlength="8"
      />
      <button type="button" @click="togglePasswordVisibility" class="absolute inset-y-0 right-0 pr-3 flex items-center">
        <img
          v-if="showPassword"
          src="../assets/Images/showP.png"
          alt="Show password"
          class="h-6 w-6"
        />
        <img
          v-else
          src="../assets/Images/hideP.png"
          alt="Hide password"
          class="h-6 w-6"
        />
      </button>
    </div>

    <!-- Error message section, displayed below the input field -->
    <div v-if="unauthorizedError" class="text-red text-sm mt-2">{{ unauthorizedError }}</div>
    <div v-if="loginError" class="text-red text-sm mt-2">{{ loginError }}</div>
  </div>

  <button type="submit" class="w-full bg-accent text-gray-700 py-2 px-4 rounded-lg font-medium hover:bg-accent transition duration-200 shadow-dark">
    Log In
  </button>

  <div class="mt-4 text-sm text-gray-600">
    <span>Don't have an account? </span>
    <button @click="step = 'registerChoice'" class="text-blue-600">Register</button>
  </div>
</form>

    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useRouter } from "vue-router";
import { ref, onMounted, computed } from 'vue'

const router = useRouter();

export default {
  data() {
    return {
      step: 'choose', // 'choose', 'registerChoice', 'verifyOtp', 'login'
      userType: 'individual', // 'individual' or 'organisation'
      name: '',
      surname: '',
      orgName: '',
      regNumber: '',
      location: '',
      email: '',
      password: '',
      otp: '',
      loginError: '',
      otpError: '',
      unauthorizedError: '', // New property for unauthorized email error
      showPassword: false
    };
  },
  methods: {
    setRegisterChoice() {
      this.step = 'registerChoice';
      this.userType = 'individual'
    },
    togglePasswordVisibility(){
      this.showPassword = !this.showPassword;
    },

    async register() {
      const registrationData = {
        email: this.email,
        password: this.password,
        userType: this.userType,
        ...(this.userType === 'individual' ? {
          name: this.name,
          surname: this.surname
        } : {
          orgName: this.orgName,
          regNumber: this.regNumber,
          location: this.location
        })
      };

      try {
        await axios.post('http://localhost:5000/register', registrationData);
        this.step = 'verifyOtp';  // Move to OTP verification step
      } catch (error) {
        console.error('Registration error:', error.response.data);
      }
    },
    async verifyOtp() {
      const otpData = {
        email: this.email,
        otp: this.otp
      };

      try {
        await axios.post('http://localhost:5000/verify_otp', otpData);
        alert('Email verified successfully! You can now log in.');
        this.step = 'login';  // Move to login step after successful OTP verification
      } catch (error) {
        console.error('OTP verification error:', error.response.data);
        this.otpError = error.response.data.message;  // Display error message
      }
    },
    async login() {

      this.loginError = '';
      this.unauthorizedError = '';

      const loginData = {
        email: this.email,
        password: this.password
        
      };

      try {
        await axios.post('http://localhost:5000/login', loginData, { withCredentials: true });
        localStorage.setItem('userEmail', this.email); // Store email in localStorage after successful login
        this.$emit('login'); 
        this.$emit('close');  // Close modal on successful login
        this.$router.push({ name: 'home' });
      } catch (error) {
        console.error('Login error:', error.response?.data || error.message);
        
        // Check for unauthorized status or message and set error message
        if (error.response?.status === 403) {
          this.unauthorizedError = 'This email is not authorized.';
        } else if (error.response?.status === 401) {
          this.loginError = 'Incorrect email or password';
        } else {
          this.loginError = 'An unexpected error occurred. Please try again.';
        }
      }
    }
  }
};
</script>

