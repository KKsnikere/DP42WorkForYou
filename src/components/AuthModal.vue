<template>
  <div class="fixed inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center z-30">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
      <div class="flex justify-between items-center border-b pb-3 mb-4">
        <h3 class="text-2xl font-semibold text-gray-800">Sign in options</h3>
        <button @click="$emit('close')" class="text-gray-600 hover:text-red-500 focus:outline-none">
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
          />
          <input
            v-model="surname"
            type="text"
            placeholder="Surname"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200"
            required
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
          class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200 mt-6"
          required
        />

        <!-- Password with Show/Hide Button -->
        <div class="relative">
          <input
            v-model="password"
            :type="showPassword ? 'text' : 'password'"
            placeholder="Password"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200 mt-6"
            required
            minlength="8"
          />
          <button type="button" @click="togglePasswordVisibility" class="absolute inset-y-0 right-0 pr-3 flex items-center">
            <img
              v-if="showPassword"
              src="../assets/Images/showP.png"
              alt="Show password"
              class="h-6 w-6 mt-6"
            />
            <img
              v-else
              src="../assets/Images/hideP.png"
              alt="Hide password"
              class="h-6 w-6 mt-6"
            />
          </button>
        </div>

        <button type="submit" class="w-full bg-accent text-gray-700 py-2 px-4 rounded-lg hover:bg-accent transition duration-200 mt-8 shadow-dark">
          Register
        </button>

        <div class="text-center">
          <p class="text-gray-600">
            Already have an account?
            <button @click="step = 'login'" class="text-greener focus:outline-none">
              Login here
            </button>
          </p>
        </div>
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

        <!-- Password with Show/Hide Button -->
        <div class="relative">
          <input
            v-model="password"
            :type="showPassword ? 'text' : 'password'"
            placeholder="Password"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-green transition duration-200"
            required
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

        <div v-if="loginError" class="text-red text-xs">Incorrect password or email</div>

        <button type="submit" class="w-full bg-green text-gray-700 py-2 px-4 rounded-lg hover:bg-green transition duration-200 shadow-dark font-medium">
          Login
        </button>

        <div class="text-center">
          <p class="text-gray-600">
            Don't have an account yet?
            <button @click="step = 'registerChoice'" class="text-darker focus:outline-none">
              Register here
            </button>
          </p>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      step: 'choose',
      email: '',
      password: '',
      name: '',
      surname: '',
      orgName: '',
      regNumber: '',
      location: '',
      userType: 'individual',
      loginError: false,
      showPassword: false, // Added for toggling password visibility
    };
  },
  methods: {
    setRegisterChoice() {
      this.step = 'registerChoice';
      this.userType = 'individual';
    },
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    },
    async register() {
      try {
        let payload = {
          email: this.email,
          password: this.password,
          userType: this.userType,
        };

        if (this.userType === 'individual') {
          payload.name = this.name;
          payload.surname = this.surname;
        } else {
          payload.orgName = this.orgName;
          payload.regNumber = this.regNumber;
          payload.location = this.location;
        }

        const response = await fetch('http://localhost:5000/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(payload),
          credentials: 'include',
        });

        if (response.ok) {
          const responseData = await response.json();
          localStorage.setItem('userEmail', responseData.email);
          this.$emit('login');
          this.$router.push('/home');
        } else {
          console.error('Registration failed');
        }
      } catch (error) {
        console.error('Error registering:', error);
      }
    },
    async login() {
      try {
        const payload = {
          email: this.email,
          password: this.password,
        };

        const response = await fetch('http://localhost:5000/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(payload),
          credentials: 'include',
        });

        if (response.ok) {
          const responseData = await response.json();
          localStorage.setItem('userEmail', responseData.email);
          this.$emit('login');
          this.$router.push('/home');
        } else {
          this.loginError = true;
        }
      } catch (error) {
        console.error('Error logging in:', error);
        this.loginError = true;
      }
    },
  },
};
</script>

<style scoped>
/* Add any scoped styles here */
</style>
