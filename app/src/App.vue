<template>
  <div>
    <AppNavbar/>
    <router-view :key="$route.path"/>
  </div>
</template>

<script>
import AppNavbar from '@/components/AppNavbar';

export default {
  name: 'App',
  components: {
    AppNavbar,
  },
};
</script>
