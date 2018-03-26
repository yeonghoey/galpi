<template>
  <div class="home">
    <h1>Galpi</h1>
    <router-link :to="{ name: 'Home' }">Home</router-link>
    <router-link :to="{ name: 'User', params: { username: 'yeonghoey' } }">yeonghoey</router-link>
    <router-link :to="{ name: 'User', params: { username: 'naviplay' } }">naviplay</router-link>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {};
  },
};
</script>
