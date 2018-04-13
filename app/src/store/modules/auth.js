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
