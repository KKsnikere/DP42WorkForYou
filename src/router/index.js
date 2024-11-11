import { createRouter, createWebHistory } from "vue-router";

// Define routes
const routes = [
  {
    path: "/",
    name: "welcome",
    component: () => import("../views/WelcomeView.vue"),
  },
  {
    path: "/adverts",
    name: "adverts",
    component: () => import("../views/AdvertsView.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: "/favourites",
    name: "favourites",
    component: () => import("../views/FavouritesView.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: "/home",
    name: "home",
    component: () => import("../views/HomeView.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: "/profile",
    name: "profile",
    component: () => import("../views/ProfileView.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: "/jobs/:id",
    name: "AdvertsView",
    component: () => import("../views/AdvertsView.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: "/apply/:id",
    name: "apply",
    component: () => import("../views/ApplyView.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: '/applicants/:id',
    name: 'Applicants',
    component: () => import("../views/AplicantsView.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: '/user-applications',
    name: 'UserApplications',
    component:() => import("../views/Myapplications.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: '/help',
    name: 'Help',
    component:() => import("../views/HelpView.vue"),
  }
];

// Create router
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

// Global navigation guard to check for authorization
router.beforeEach((to, from, next) => {
  // Fetch auth token from localStorage
  const isAuthenticated = !!localStorage.getItem('userEmail'); 

  console.log('Navigation to:', to.name); // Check which route is being accessed
  console.log('Authenticated:', isAuthenticated); // Verify if authentication is detected
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    console.warn('Access denied. Redirecting to welcome page.');
    next({ name: 'welcome' }); // Redirect to welcome if not authenticated
  } else {
    next(); // Allow access to route
  }
});

export default router;
