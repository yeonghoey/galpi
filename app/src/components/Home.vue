<template>
  <div class="home">
    <h1>galpi</h1>
    <router-link :to="{ name: 'Home' }">Home</router-link>
    <p> {{ res }} </p>
  </div>
</template>

<script>
export default {
  name: 'Home',
};
</script>
