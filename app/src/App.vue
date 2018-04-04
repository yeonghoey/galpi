<template>
  <div id="app">
    <h1>Galpi</h1>
    <a href="#" class="btn btn-block btn-social btn-github">
      <span class="fa fa-github"></span> Sign in with GitHub
    </a>
    <router-view/>
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
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
