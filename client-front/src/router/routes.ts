import { RouteConfig } from 'vue-router'

const routes: RouteConfig[] = [
  {
    path: '/admin',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'home', component: () => import('pages/Index.vue') },
      { path: 'friends', name: 'friends', component: () => import('pages/Friends.vue') },
      { path: 'endpoints', name: 'endpoints', component: () => import('pages/EndPoints.vue') }
    ]
  },
  {
    path: '/admin',
    component: () => import('layouts/PublicLayout.vue'),
    children: [
      { path: 'login', name: 'login', component: () => import('pages/SignIn.vue') },
      { path: 'signup', name: 'signup', component: () => import('pages/SignUp.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
