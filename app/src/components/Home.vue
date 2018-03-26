<template>
  <div class="home">
    <h1>Galpi</h1>
    <router-link :to="{ name: 'Home' }">Home</router-link>
    <router-link :to="{ name: 'User', params: { username: 'yeonghoey' } }">yeonghoey</router-link>
    <router-link :to="{ name: 'User', params: { username: 'naviplay' } }">naviplay</router-link>
    <button v-on:click="greet">Greet</button>
  </div>
</template>

<script>
import api from '@/core/api';

export default {
  name: 'Home',
  data() {
    return {};
  },

  methods: {
    greet() {
      api.get('/').then((res) => {
        console.log(res);
      });
    },
  },
};
</script>
