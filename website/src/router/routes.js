const routes = [
  {
    path: '/',
    component: () => import('layouts/Index.vue'),
    children: [
      {
        path: '',
        component: () => import('pages/Login.vue'),
      },
    ],
  },
  {
    path: '/dashboard',
    component: () => import('layouts/Dashboard.vue'),
    children: [
      {
        path: '',
        component: () => import('pages/dashboard/Main.vue'),
      },
      {
        path: 'users',
        component: () => import('pages/dashboard/Users.vue'),
        name: 'dashboard-users',
      },
    ],
  },
];

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue'),
  });
}

export default routes;
