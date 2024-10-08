import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'welcome',
      component: () => import("../views/WelcomeView.vue")
    },
    {
      path: '/adverts',
      name: 'adverts',
      component: () => import("../views/AdvertsView.vue")
    },
    {
      path: '/favourites',
      name:'favourites',
      component: () => import("../views/FavouritesView.vue")
    },
    {
      path: '/home',
      name:'home',
      component: () => import("../views/HomeView.vue")
    },
    {
      path: '/login',
      name:'login',
      component: () => import("../views/LoginView.vue")
    },
    {
      path: '/register',
      name:'register',
      component: () => import("../views/RegisterView.vue")
    },
    {
      path: '/profile',
      name:'profile',
      component: () => import("../views/ProfileView.vue")
    },
    {
      path: '/jobs/:id', 
      name:'AdvertsView',
      component: () => import("../views/AdvertsView.vue")
    }
  ]
})

export default router
