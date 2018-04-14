import Vue from 'vue';
import Router from 'vue-router';

import HomeView from '@/views/HomeView';
import ItemView from '@/views/ItemView';

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
      name: 'ItemViewUser',
      component: ItemView,
      props: route => ({
        username: route.params.username,
        pathquery: '',
      }),
    },
    {
      path: '/:username/:pathquery+/',
      name: 'ItemView',
      component: ItemView,

      // Inject the trailing slash into 'pathquery'
      pathToRegexpOptions: { strict: true },
      props: route => ({
        username: route.params.username,
        pathquery: `${route.params.pathquery}/`,
      }),
    },
    {
      path: '/:username/:pathquery+',
      name: 'ItemViewRedirect',
      component: ItemView,

      pathToRegexpOptions: { strict: true },
      props: true,
    },
  ],
});
