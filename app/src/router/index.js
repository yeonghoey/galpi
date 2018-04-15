import Vue from 'vue';
import Router from 'vue-router';

import HomeView from '@/views/HomeView';
import MainView from '@/views/MainView';

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
      name: 'MainView',
      component: MainView,
      props: true,
    },
  ],
});
