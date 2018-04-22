import _ from 'lodash';
import api from '@/api';

export const actions = {
  getItem({ commit }, path) {
    return api.get(path)
      .then((response) => {
        commit('setItem', response.data);
      });
  },
  putSub({ commit }, { path, name, body }) {
    return api.put(path, body)
      .then((response) => {
        commit('updateSub', { name, body });
      });
  },
  deleteSub({ commit }, { path, name }) {
    return api.delete(path)
      .then((response) => {
        commit('deleteSub', name);
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
    state.item = _.set(_.clone(state.item), `subs.${name}`, body);
  },
  deleteSub(state, name) {
    delete state.item.subs[name];
    state.item = _.omit(state.item, [`subs.${name}`]);
    // _.unset(state.item, `subs.${name}`);
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
