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
  },
};

const state = {
  username: undefined,
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
