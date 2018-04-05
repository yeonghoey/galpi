<template>
  <div id="app">
    <h1 class="w-75 px-2 py-3 mx-auto">
      Galpi
    </h1>
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
}
</style>
