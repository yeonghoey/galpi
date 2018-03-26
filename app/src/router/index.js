import Vue from 'vue';
import Router from 'vue-router';

import Home from '@/components/Home';
import User from '@/components/User';
import Keyword from '@/components/Keyword';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/:username',
      name: 'User',
      component: User,
      props: true,
    },
    {
      path: '/:username/:keyword',
      name: 'Keyword',
      component: Keyword,
      props: true,
    },
  ],
});
