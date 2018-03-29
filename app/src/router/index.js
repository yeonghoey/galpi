import Vue from 'vue';
import Router from 'vue-router';

import Home from '@/components/Home';
import User from '@/components/User';
import Item from '@/components/Item';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/:user',
      name: 'User',
      component: User,
      props: true,
    },
    {
      path: '/:user/:name',
      name: 'Item',
      component: Item,
      props: true,
    },
  ],
});
