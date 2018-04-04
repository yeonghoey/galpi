<template>
  <div id="app">
    <a href="#" class="btn btn-block btn-social btn-github">
      <span class="fa fa-github"></span> Sign in with GitHub
    </a>
    <router-view/>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar';

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
