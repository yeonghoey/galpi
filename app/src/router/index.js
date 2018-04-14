import Vue from 'vue';
import Router from 'vue-router';

import HomeView from '@/views/HomeView';
import QueryView from '@/views/QueryView';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView,
    },
    {
      path: '/:username',
      name: 'UserView',
      component: QueryView,
      props: route => ({
        username: route.params.username,
        pathquery: '',
      }),
    },
    {
      path: '/:username/:pathquery+/',
      name: 'ItemView',
      component: QueryView,

      // Inject the trailing slash into 'pathquery'
      pathToRegexpOptions: { strict: true },
      props: route => ({
        username: route.params.username,
        pathquery: `${route.params.pathquery}/`,
      }),
    },
    {
      path: '/:username/:pathquery+',
      name: 'RedirectOrItemView',
      component: QueryView,

      pathToRegexpOptions: { strict: true },
      props: true,
    },
  ],
});
