import api from '@/api';

export const actions = {
  checkAuth({ commit }) {
    return api.get('/auth/me')
      .then((response) => {
        commit('update', response.data.username);
      });
  },

  signOut({ commit }) {
    return api.post('/auth/signout')
      .then(() => {
        commit('update', undefined);
      });
  },
};

export const mutations = {
  refreshRequired(state) {
    state.refresh = true;
  },

  update(state, username) {
    state.username = username;
    state.refresh = false;
  },
};

const state = {
  username: undefined,
  refresh: true,
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
