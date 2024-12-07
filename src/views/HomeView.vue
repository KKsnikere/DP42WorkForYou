<template>
  <div
    class="flex flex-col justify-center items-center space-y-4 py-4 dark:bg-dark-primary"
  >
    <!-- Filter Buttons -->
    <div class="flex flex-wrap justify-center items-center space-x-4">
      <div v-for="(filter, index) in filters" :key="index" class="relative">
        <button
          ref="filterButtons"
          @click.stop
          @click="togglePopup(index)"
          :class="{
            'bg-accent dark:bg-dark-accent hover:scale-110 text-slate-600 dark:bg-accent-dark dark:text-white':
              showPopup === index,
            'bg-gray-200 dark:bg-gray-700': showPopup !== index,
          }"
          class="px-3 py-2 rounded transition text-gray-700 dark:text-gray-300 font-medium duration-150 ease-in-out mx-2 my-2 hover:scale-110 shadow-dark"
        >
          {{ filter.name }}
        </button>
        <transition name="fade">
          <div
            v-if="showPopup === index"
            v-click-outside="closePopup"
            ref="popup"
            class="absolute bg-white dark:bg-gray-800 shadow-lg p-4 mt-2 rounded z-10 w-48 -ml-8 leading-6"
          >
            <div
              v-for="(option, optionIndex) in filter.options"
              :key="optionIndex"
              class="flex items-center space-x-2 py-1"
            >
              <input
                type="checkbox"
                v-model="selectedFilters[filter.key]"
                :value="option"
                :id="`${filter.key}-${optionIndex}`"
                class="form-checkbox h-4 w-4 text-acce border-gray-300 rounded focus:ring-2 focus:ring-accent transition duration-150 ease-in-out"
                @change="applyFilters"
              />
              <label
                :for="`${filter.key}-${optionIndex}`"
                :class="{ 'font-bold': isSelected(filter.key, option) }"
                class="text-gray-700 dark:text-gray-300"
              >
                {{ option }}
              </label>
            </div>
            <button
              @click="togglePopup(null)"
              class="mt-2 text-sm text-gray-700 dark:text-gray-300 close-button"
            >
              Close
            </button>
          </div>
        </transition>
      </div>
    </div>

    <!-- Action Buttons -->
    <div class="flex justify-center items-center space-x-4">
      <div class="flex justify-center items-center space-x-4">
        <button
          @click="clearFilters"
          class="w-10 h-10 mt-2 hover:scale-110 bg-white dark:bg-gray-800 rounded-lg flex items-center justify-center mb-2 hover:bg-red-200 hover:text-gray-700 transform active:scale-75 transition-transform shadow-dark"
        >
          <img
            src="../assets/Images/clearF.png"
            alt="Clear Filter"
            class="w-8 h-8 hover:scale-110 dark:hidden"
          />
          <!-- Dark mode image -->
          <img
            src="../assets/Images/DarkclearF.png"
            alt="Clear Filter"
            class="w-8 h-8 hover:scale-110 hidden dark:block"
          />
        </button>

        <div class="relative inline-block text-left">
          <div>
            <button
              @click="toggleSortMenu"
              v-click-outside="closeSortMenu"
              class="inline-flex justify-between w-full shadow-dark bg-accent dark:bg-dark-accent hover:scale-110 text-gray-700 dark:text-gray-200 font-bold py-2 px-4 rounded mx-2 transform active:scale-75 transition-transform"
              id="options-menu"
              aria-haspopup="true"
              aria-expanded="true"
            >
              Sort
              <svg
                class="-mr-1 ml-2 h-5 w-5"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  fill-rule="evenodd"
                  d="M5.23 7.21a.75.75 0 01.1 1.06L3.58 10h13.84l-1.75-1.73a.75.75 0 111.06-1.06l3 3a.75.75 0 010 1.06l-3 3a.75.75 0 01-1.06-1.06L17.42 12H3.58l1.75 1.73a.75.75 0 11-1.06 1.06l-3-3a.75.75 0 010-1.06l3-3a.75.75 0 011.06 0z"
                  clip-rule="evenodd"
                />
              </svg>
            </button>
          </div>

          <transition name="fade">
            <div
              v-if="isSortMenuOpen"
              class="absolute right-0 z-10 mt-2 w-56 rounded-md shadow-lg bg-white dark:bg-gray-800 ring-1 ring-black ring-opacity-5"
              role="menu"
              aria-orientation="vertical"
              aria-labelledby="options-menu"
            >
              <div class="py-1" role="none">
                <button
                  @click="sortJobs('newest')"
                  class="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700 w-full text-left"
                  role="menuitem"
                >
                  Newest to Oldest
                </button>
                <button
                  @click="sortJobs('oldest')"
                  class="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700 w-full text-left"
                  role="menuitem"
                >
                  Oldest to Newest
                </button>
              </div>
            </div>
          </transition>
        </div>
      </div>
    </div>

    <!-- Search Input -->
    <div class="flex justify-start mt-3">
      <input
        v-model="searchQuery"
        @input="debounceSearch"
        placeholder="Search job advertisements..."
        class="px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-700 focus:outline-none focus:ring-2 focus:ring-green w-80 dark:bg-gray-700 dark:text-white"
      />
    </div>

    <!-- Items per page -->
    <div class="flex justify-start">
      <label
        for="itemsPerPage"
        class="mr-2 text-gray-700 dark:text-gray-300 font-medium mt-2"
        >Items per page:</label
      >
      <select
        id="itemsPerPage"
        v-model="itemsPerPage"
        @change="currentPage = 1"
        class="p-2 border border-gray-300 dark:border-gray-700 rounded dark:bg-gray-700 dark:text-white"
      >
        <option
          v-for="option in itemsPerPageOptions"
          :key="option"
          :value="option"
        >
          {{ option }}
        </option>
      </select>
    </div>

    <!-- Loading Indicator -->
    <div v-if="loading" class="text-center text-gray-700 dark:text-white">
      Searching...
    </div>

    <!-- Filtered Jobs -->
    <div v-else-if="filteredJobs.length > 0">
      <div class="flex flex-wrap justify-center">
        <div
          v-for="job in paginatedJobs"
          :key="job._id.$oid"
          class="bg-white dark:bg-gray-800 border border-slate-200 dark:border-gray-700 rounded-3xl px-5 py-5 transition hover:-translate-y-1 hover:shadow-xl hover:scale-103 w-80 m-5 h-96 flex flex-col justify-between"
        >
          <div>
            <h1
              class="text-3xl font-bold overflow-hidden whitespace-nowrap overflow-ellipsis text-gray-800 dark:text-white"
            >
              {{ job.Job_title }}
            </h1>
            <div class="flex items-center mt-2">
              <h2
                class="text-lg font-semibold overflow-hidden whitespace-nowrap overflow-ellipsis text-gray-600 dark:text-gray-300"
              >
                {{ job.Company_name }}
              </h2>
            </div>
            <p class="mt-4 line-clamp-[7] text-gray-700 dark:text-gray-300">
              {{ job.description }}
            </p>
          </div>
          <div class="flex">
            <router-link
              :to="'/Jobs/' + job.id"
              class="bg-accent dark:bg-dark-accent text-gray-700 dark:text-gray-200 font-medium py-2 px-4 rounded cursor-pointer transform hover:scale-110 active:scale-100 transition-transform shadow-dark"
            >
              See more
            </router-link>
            <button @click="toggleLikeJob(job._id.$oid)" class="h-9 w-9 ml-5">
              <div
                :style="{
                  backgroundImage: `url(${
                    job.liked
                      ? '../src/assets/Images/Like2.svg'
                      : '../src/assets/Images/Like1.svg'
                  })`,
                }"
                class="bg-cover w-9 h-9 transform active:scale-75 transition-transform"
              ></div>
            </button>
          </div>
        </div>
      </div>
    </div>

    
    <div
      v-else-if="filteredJobs.length === 0"
      class="text-center mt-4 text-gray-700 dark:text-gray-300"
    >
      No search results found
    </div>

    <!-- Pagination Controls -->
    <div class="flex justify-center mt-4 space-x-2 mb-5">
      <button
        @click="prevPage"
        :disabled="currentPage === 1"
        class="bg-accent text-white dark:bg-dark-accent px-4 py-2 rounded transition-opacity duration-200 disabled:opacity-50"
      >
        Previous
      </button>
      <span class="flex items-center text-gray-700 dark:text-gray-300">
        Page {{ currentPage }} of {{ totalPages }}
      </span>
      <button
        @click="nextPage"
        :disabled="currentPage === totalPages"
        class="bg-accent text-white dark:bg-dark-accent px-4 py-2 rounded transition-opacity duration-200 disabled:opacity-50"
      >
        Next
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import _ from "lodash";

const jobs = ref([]);
const userEmail = localStorage.getItem("userEmail");
const searchQuery = ref("");
const loading = ref(false);
const itemsPerPageOptions = ref([6, 12, 24, 32, 48]);
const itemsPerPage = ref(itemsPerPageOptions.value[1]);
const currentPage = ref(1);
const router = useRouter();

const paginatedJobs = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  return filteredJobs.value.slice(start, start + itemsPerPage.value);
});

const totalPages = computed(() => {
  return Math.ceil(filteredJobs.value.length / itemsPerPage.value);
});

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

const debounceSearch = _.debounce(async () => {
  loading.value = true;
  try {
    const queryString = buildQueryString();
    const response = await axios.get(
      `http://127.0.0.1:5000/jobs?${queryString}&search=${encodeURIComponent(
        searchQuery.value
      )}`
    );
    jobs.value = response.data;
  } catch (error) {
    console.error("Error searching jobs:", error);
  } finally {
    loading.value = false;
  }
}, 300);

// Fetch user's favorite jobs
const fetchFavorites = async () => {
  try {
    const response = await axios.post("http://127.0.0.1:5000/favourites", {
      userEmail: userEmail,
    });
    const favoriteJobs = response.data;
    return favoriteJobs.map((job) => job._id.$oid);
  } catch (error) {
    console.error("Error fetching favorites:", error);
    return [];
  }
};

// Fetch all jobs and check if they are liked
const fetchJobs = async () => {
  try {
    const favoriteJobs = await fetchFavorites();
    const response = await axios.get("http://127.0.0.1:5000/jobs");
    jobs.value = response.data.map((job) => ({
      ...job,
      liked: favoriteJobs.includes(job._id.$oid),
    }));
  } catch (error) {
    console.error("Error fetching jobs:", error);
  }
};

// Like or Unlike a job
const toggleLikeJob = (jobId) => {
  const jobIndex = jobs.value.findIndex((job) => job._id.$oid === jobId);
  if (jobIndex === -1) return;

  const job = jobs.value[jobIndex];

  if (job.liked) {
  
    axios
      .post("http://127.0.0.1:5000/delete-favorite", {
        jobId: jobId,
        userEmail: userEmail,
      })
      .then(() => {
        jobs.value[jobIndex].liked = false;
      })
      .catch((error) => {
        console.error("Error removing job from favorites:", error);
      });
  } else {

    axios
      .post("http://127.0.0.1:5000/add-favorite", {
        job_id: jobId,
        email: userEmail,
      })
      .then(() => {
        jobs.value[jobIndex].liked = true;
      })
      .catch((error) => {
        console.error("Error adding job to favorites:", error);
      });
  }
};

onMounted(() => {
  fetchJobs();
});

const buildQueryString = () => {
  const queryParams = new URLSearchParams();
  for (const key in selectedFilters.value) {
    if (selectedFilters.value[key].length > 0) {
      queryParams.append(key, selectedFilters.value[key].join(","));
    }
  }
  return queryParams.toString();
};

const togglePopup = (index) => {
  clearTimeout(closeTimer.value);
  if (showPopup.value === index) {
    closePopup();
  } else {
    showPopup.value = index;
  }
};

const applyFilters = async () => {
  const queryString = buildQueryString();
  try {
    const response = await axios.get(
      `http://127.0.0.1:5000/jobs?${queryString}`
    );
    jobs.value = response.data;
  } catch (error) {
    console.error("Error applying filters:", error);
  }
  showPopup.value = null;
};

const clearFilters = async () => {
  selectedFilters.value = {
    worktype: [],
    profession: [],
    typeOfwork: [],
    city: [],
    workTime: [],
  };
  showPopup.value = null;
  searchQuery.value = "";
  try {
    const response = await axios.get("http://127.0.0.1:5000/jobs");
    jobs.value = response.data;
  } catch (error) {
    console.error("Error clearing filters:", error);
  }
};

const filteredJobs = computed(() => {
  if (!searchQuery.value) return jobs.value;
  return jobs.value.filter(
    (job) =>
      job.Job_title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      job.Company_name.toLowerCase().includes(
        searchQuery.value.toLowerCase()
      ) ||
      job.description.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});
const navigateToJob = (jobId) => {
  router.push({ name: "JobDetail", params: { jobId } });
};

const toggleSortMenu = () => {
  isSortMenuOpen.value = !isSortMenuOpen.value;
};

const closeSortMenu = () => {
  isSortMenuOpen.value = false;
};

const sortJobs = async (order) => {
  try {
    // Append the selected sort order to the query parameters
    const queryString = buildQueryString();
    const response = await axios.get(
      `http://127.0.0.1:5000/jobs?${queryString}&sort=${order}`
    );
    jobs.value = response.data; 
  } catch (error) {
    console.error("Error fetching sorted jobs:", error);
  }
};

const closePopup = () => {
  showPopup.value = null;
};

const isSelected = (filterKey, option) => {
  return selectedFilters.value[filterKey].includes(option);
};

let selectedFilters = ref({
  worktype: [],
  profession: [],
  typeOfwork: [],
  city: [],
  workTime: [],
});

let showPopup = ref(null);
let closeTimer = ref(null);
let isSortMenuOpen = ref(false);

const filters = ref([
  {
    name: "Work Type",
    key: "worktype",
    options: ["Part-Time", "Full-time", "One-time"],
  },
  {
    name: "Profession",
    key: "profession",
    options: [
      "Programmer",
      "Biotechnology",
      "DevOps",
      "AI",
      "Engineering",
      "Networking",
      "Educator",
      "Cybersecurity",
      "VR",
      "Management",
    ],
  },
  { name: "Type Of Work", key: "typeOfwork", options: ["Online", "In-office"] },
  {
    name: "City",
    key: "city",
    options: ["Liepaja", "Ogre", "Bauska", "Jurmala", "Tukums", "Ventspils"],
  },
  {
    name: "Work Time",
    key: "workTime",
    options: ["Workdays", "Weekend", "Schedule"],
  },
]);
</script>
