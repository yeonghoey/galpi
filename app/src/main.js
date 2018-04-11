// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.min.css';
import 'font-awesome/css/font-awesome.min.css';
import 'bootstrap-social/bootstrap-social.css';

import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';

import router from '@/router';
import store from '@/store';
import App from '@/App';

Vue.use(BootstrapVue);
Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
});
