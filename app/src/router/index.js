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
      path: '/:username/:pathquery*',
      name: 'ItemView',
      component: ItemView,
      props: true,
    },
  ],
});
