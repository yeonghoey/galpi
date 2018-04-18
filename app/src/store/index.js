import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

import auth from '@/store/modules/auth';

Vue.use(Vuex);

export default new Vuex.Store({
  strict: process.env.NODE_ENV !== 'production',
  plugins: [
    createPersistedState({
      storage: window.localStorage,
      paths: [
        'auth.me',
        'auth.avatarURL',
      ],
    }),
    createPersistedState({
      storage: window.sessionStorage,
      paths: [
        'auth.refresh',
      ],
    }),
  ],
  modules: {
    auth,
  },
});
