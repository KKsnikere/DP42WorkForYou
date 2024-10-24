import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "welcome",
      component: () => import("../views/WelcomeView.vue"),
    },
    {
      path: "/adverts",
      name: "adverts",
      component: () => import("../views/AdvertsView.vue"),
    },
    {
      path: "/favourites",
      name: "favourites",
      component: () => import("../views/FavouritesView.vue"),
    },
    {
      path: "/home",
      name: "home",
      component: () => import("../views/HomeView.vue"),
    },
    {
      path: "/profile",
      name: "profile",
      component: () => import("../views/ProfileView.vue"),
    },
    {
      path: "/jobs/:id",
      name: "AdvertsView",
      component: () => import("../views/AdvertsView.vue"),
    },
    {
      path: "/profile",
      name: "profile",
      component: () => import("../views/ProfileView.vue"),
    },

    {
      path: "/jobs/:id",
      name: "AdvertsView",
      component: () => import("../views/AdvertsView.vue"),
    },
    {
      path: "/apply/:id",
      name: "apply",
      component: () => import("../views/ApplyView.vue"),
    },
    {
      path: '/applicants/:id',
      name: 'Applicants',
      component: () => import("../views/AplicantsView.vue"),
    }
  ],
});

export default router;