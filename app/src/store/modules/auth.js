import api from '@/api';

export const actions = {
  checkAuth({ commit }) {
    return api.get('/auth/me')
      .then((response) => {
        commit('update', response.data);
      });
  },

  signOut({ commit }) {
    return api.post('/auth/signout')
      .then(() => {
        commit('update', {});
      });
  },
};

export const mutations = {
  refreshRequired(state) {
    state.refresh = true;
  },

  update(state, userinfo) {
    state.myUsername = userinfo.username;
    state.myAvatarURL = userinfo.avatar_url;
    state.refresh = false;
  },
};

const state = {
  myUsername: undefined,
  myAvatarURL: undefined,
  refresh: true,
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
