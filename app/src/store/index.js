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
        'auth.myUsername',
        'auth.myAvatarURL',
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
