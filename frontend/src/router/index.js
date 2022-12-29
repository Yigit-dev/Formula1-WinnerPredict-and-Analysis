import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/teams',
      name: 'teams',
      component: () => import("../views/Teams.vue")
    },
    {
      path: '/races',
      name: 'races',
      component: () => import("../views/Races.vue")
    },
    {
      path: '/drivers',
      name: 'drivers',
      component: () => import("../views/Drivers.vue")
    },
    {
      path: '/chart',
      name: 'chart',
      component: () => import("../views/Chart.vue")
    }
  ]
})

export default router
