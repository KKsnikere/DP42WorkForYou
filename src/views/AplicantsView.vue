<template>
  <div class="container mx-auto p-6 h-screen">
    <h1 class="text-2xl font-bold mb-6 text-white">Applicants for Job: {{ jobTitle }}</h1>
    <div v-if="error" class="text-red-500 mb-4">{{ error }}</div>
    <div v-if="loading" class="text-gray-500">Loading applicants...</div>

    <div v-if="applicants.length > 0" class="grid grid-cols-1 gap-6">
      <div
        v-for="applicant in applicants"
        :key="applicant.email"
        class="bg-gray-800 shadow-md rounded-lg p-4 transition-transform duration-200 hover:shadow-xl"
      >
        <h2 class="text-lg font-semibold text-white">{{ applicant.name }} {{ applicant.surname }}</h2>

        <div class="flex items-center">
          <p class="text-sm mr-2 text-gray-300">
            <strong>Email: </strong> 
            <a 
              :href="'mailto:' + applicant.email" 
              class="text-blue-400 hover:text-blue-600 font-medium transition duration-200"
            >
              {{ applicant.email }}
            </a>
          </p>
          <img 
            src="../assets/Images/copy.png" 
            alt="Copy Email" 
            @click="copyEmail(applicant.email)" 
            class="w-6 h-6 cursor-pointer transition duration-200 hover:opacity-80"
          />
        </div>

        <p class="text-sm text-gray-300"><strong>Phone: </strong> {{ applicant.phone }}</p>

        <!-- Message Box -->
        <div class="bg-gray-700 border border-gray-600 rounded-lg p-3 mt-2">
          <strong class="text-white">Message:</strong>
          <p class="text-sm text-gray-300">{{ applicant.message }}</p>
        </div>

        <div v-if="applicant.files.length > 0" class="mt-2">
          <div class="flex flex-wrap space-x-4 mt-2">
            <div v-for="file in applicant.files" :key="file">
              <a 
                :href="file" 
                download 
                class="text-blue-500 hover:underline mr-4"
              >
                Download attached files
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="!loading && applicants.length === 0" class="text-gray-500">
      No applicants for this job.
    </div>
  </div>
</template>


<script>
import axios from 'axios';
import { useRouter } from "vue-router";
import { ref, onMounted, computed } from 'vue'

export default {

  data() {
    return {
      applicants: [],
      jobId: this.$route.params.id,
      jobTitle: '', 
      loading: false,
      error: null,
    };
  },

  async created() {
    await this.fetchJobTitle(); 
    await this.fetchApplicants(); 
  },
  methods: {
    async fetchJobTitle() {
      this.loading = true;
      try {
        const response = await axios.get(`http://127.0.0.1:5000/jobs/${this.jobId}`); 
        this.jobTitle = response.data.Job_title;
      } catch (error) {
        console.log("Error fetching job title:", error);
        this.error = "Failed to fetch job title.";
      } finally {
        this.loading = false;
      }
    },
    async fetchApplicants() {
      this.loading = true;
      this.error = null;

      try {
        const userEmail = localStorage.getItem('userEmail');
        const response = await axios.get(`http://127.0.0.1:5000/applicants/${this.jobId}`, {
          headers: {
            userEmail: userEmail,
          },
        });

        this.applicants = response.data.map(applicant => ({
          ...applicant,
          files: applicant.files || [],
        }));
        
      } catch (error) {
        console.log("Error fetching applicants:", error);

        if (error.response && error.response.data) {
          this.error = error.response.data.error;
        } else {
          this.error = "Failed to fetch applicants.";
        }
      } finally {
        this.loading = false;
      }
    },
    copyEmail(email) {
      navigator.clipboard.writeText(email).then(() => {
        alert("Email copied to clipboard!");
      }).catch(err => {
        console.error("Could not copy email: ", err);
      });
    },
    viewFile(file) {
      if (file) {
        window.open(file, "_blank");
      } else {
        alert("File URL is invalid or not available.");
      }
    }
  }
};
</script>
