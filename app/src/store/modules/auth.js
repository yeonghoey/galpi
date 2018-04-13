import api from '@/api';

export const actions = {
  checkAuth({ commit }) {
    return api.get('/auth/me')
      .then((response) => {
        commit('update', response.data.username);
      });
  },
};

export const mutations = {
  update(state, username) {
    state.username = username;
    state.refreshRequired = false;
  },
};

const state = {
  username: undefined,
  refreshRequired: true,
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
