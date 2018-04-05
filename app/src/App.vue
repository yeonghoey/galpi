<template>
  <div id="app">
    <router-view
      class="w-75 m-auto"
      :key="$route.path"
    />
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}

.view {
  max-width: 960px;
  margin: 0 auto;
}

</style>
