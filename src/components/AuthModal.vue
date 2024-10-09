<template>
  <div class="fixed inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center z-30">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
      <div class="flex justify-between items-center border-b pb-3 mb-4">
        <h3 class="text-2xl font-semibold text-gray-800">Authentication</h3>
        <button @click="$emit('close')" class="text-gray-600 hover:text-red-500 focus:outline-none">
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

      <!-- Registration and login form -->
      <div v-if="step === 'choose'" class="space-y-4">
        <div v-if="loginError" class="text-red-500 text-sm mt-2">Incorrect password or email</div>
        <button
          @click="step = 'login'"
          class="w-full bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition duration-200"
        >
          Login
        </button>
        <button
          @click="setRegisterChoice"
          class="w-full bg-green-500 text-white py-2 px-4 rounded-lg hover:bg-green-600 transition duration-200"
        >
          Register
        </button>
      </div>

      <!-- Registration form for individual -->
      <div v-if="step === 'registerChoice'" class="space-y-8">
        <div class="flex justify-center gap-4">
          <button
            @click="userType = 'individual'"
            :class="userType === 'individual' ? 'bg-blue-600' : 'bg-blue-500'"
            class="w-full text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition duration-200"
          >
            Private Person
          </button>
          <button
            @click="userType = 'organisation'"
            :class="userType === 'organisation' ? 'bg-green-600' : 'bg-green-500'"
            class="w-full text-white py-2 px-4 rounded-lg hover:bg-green-600 transition duration-200"
          >
            Organisation
          </button>
        </div>
        <div v-if="userType === 'individual'" class="space-y-6">
          <input
            v-model="name"
            type="text"
            placeholder="Name"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200"
          />
          <input
            v-model="surname"
            type="text"
            placeholder="Surname"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200"
          />
          <div v-if="nameError" class="text-red-500 text-sm mt-1">Name is required</div>
          <div v-if="surnameError" class="text-red-500 text-sm mt-1">Surname is required</div>
        </div>
        <div v-else>
          <input
            v-model="orgName"
            type="text"
            placeholder="Organisation Name"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200"
          />
          <input
            v-model="regNumber"
            type="text"
            placeholder="Registration Number"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200 mt-6"
          />
          <input
            v-model="location"
            type="text"
            placeholder="Location"
            class="w-full p-3 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200 mt-6"
          />
          <div v-if="orgNameError" class="text-red-500 text-sm mt-1">
            Organisation Name is required
          </div>
          <div v-if="regNumberError" class="text-red-500 text-sm mt-1">
            Registration Number is required
          </div>
          <div v-if="locationError" class="text-red-500 text-sm mt-1">Location is required</div>
        </div>
        <input
          v-model="email"
          type="email"
          placeholder="Email"
          class="w-full p-3 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200 mt-6"
        />
        <div v-if="emailError" class="text-red-500 text-sm mt-1">Email is required</div>
        <input
          v-model="password"
          type="password"
          placeholder="Password"
          class="w-full p-3 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200 mt-6"
        />
        <div v-if="passwordError" class="text-red-500 text-sm mt-1">Password is required</div>
        <button
          @click="register"
          class="w-full bg-green-500 text-white py-2 px-4 rounded-lg hover:bg-green-600 transition duration-200 mt-8"
        >
          Register
        </button>

        <div class="text-center">
          <p class="text-gray-600">
            Already have an account?
            <button @click="step = 'login'" class="text-blue-500 focus:outline-none">
              Login here
            </button>
          </p>
        </div>
      </div>

      <!-- Login form -->
      <div v-if="step === 'login'" class="space-y-4">
        <input
          v-model="email"
          type="email"
          placeholder="Email"
          class="w-full p-3 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200"
        />
        <div v-if="emailError" class="text-red-500 text-sm mt-1">Email is required</div>
        <input
          v-model="password"
          type="password"
          placeholder="Password"
          class="w-full p-3 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200"
        />
        <div v-if="passwordError" class="text-red-500 text-sm mt-1">Password is required</div>

        <div v-if="loginError" class="text-red-500 text-sm mt-2">Incorrect password or email</div>

        <button
          @click="login"
          class="w-full bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition duration-200"
        >
          Login
        </button>
        <div class="text-center">
          <p class="text-gray-600">
            Don't have an account yet?
            <button @click="step = 'registerChoice'" class="text-blue-500 focus:outline-none">
              Register here
            </button>
          </p>
        </div>
      </div>
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
      emailError: false,
      passwordError: false,
      nameError: false,
      surnameError: false,
      orgNameError: false,
      regNumberError: false,
      locationError: false,
      loginError: false
    }
  },
  methods: {
    setRegisterChoice() {
      this.step = 'registerChoice'
      this.userType = 'individual'
    },
    validateFields() {
      this.emailError = !this.email
      this.passwordError = !this.password
      this.nameError = this.userType === 'individual' && !this.name
      this.surnameError = this.userType === 'individual' && !this.surname
      this.orgNameError = this.userType === 'organisation' && !this.orgName
      this.regNumberError = this.userType === 'organisation' && !this.regNumber
      this.locationError = this.userType === 'organisation' && !this.location

      return !(
        this.emailError ||
        this.passwordError ||
        this.nameError ||
        this.surnameError ||
        this.orgNameError ||
        this.regNumberError ||
        this.locationError
      )
    },
    async register() {
      if (!this.validateFields()) {
        return
      }

      try {
        let payload = {
          email: this.email,
          password: this.password,
          userType: this.userType
        }

        if (this.userType === 'individual') {
          payload.name = this.name
          payload.surname = this.surname
        } else {
          payload.orgName = this.orgName
          payload.regNumber = this.regNumber
          payload.location = this.location
        }

        const response = await fetch('http://localhost:5000/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload),
          credentials: 'include'
        })

        if (response.ok) {
          const responseData = await response.json()
          localStorage.setItem('userEmail', responseData.email)
          this.$emit('login')
          this.$router.push('/home')
        } else {
          console.error('Registration failed')
        }
      } catch (error) {
        console.error('Error registering:', error)
      }
    },
    async login() {
      if (!this.email || !this.password) {
        this.emailError = !this.email
        this.passwordError = !this.password
        return
      }

      try {
        const payload = {
          email: this.email,
          password: this.password
        }

        const response = await fetch('http://localhost:5000/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload),
          credentials: 'include'
        })

        if (response.ok) {
          const responseData = await response.json()
          localStorage.setItem('userEmail', responseData.email)
          this.$emit('login')
          this.$router.push('/home')
        } else {
          this.loginError = true
        }
      } catch (error) {
        console.error('Error logging in:', error)
        this.loginError = true
      }
    }
  }
}
</script>

<style scoped></style>
