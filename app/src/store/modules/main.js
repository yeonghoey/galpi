import _ from 'lodash';
import api from '@/api';

export const actions = {
  getItem({ commit }, path) {
    return api.get(path)
      .then((response) => {
        commit('setItem', response.data);
      });
  },
  putItem({ commit }, { path, name, body }) {
    return api.put(path, body)
      .then((response) => {
        commit('updateSub', { name, body });
      });
  },
};

export const getters = {
  base(state) {
    return _.get(state.item, 'base', []);
  },
  subs(state) {
    return _.get(state.item, 'subs', {});
  },
};

export const mutations = {
  setOwner(state, owner) {
    state.owner = owner;
  },
  setItem(state, item) {
    state.item = item;
  },
  updateSub(state, { name, body }) {
    _.set(state.item, `subs.${name}`, body);
  },
};

const state = {
  owner: false,
  item: {},
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
