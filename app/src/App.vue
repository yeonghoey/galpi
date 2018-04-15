<template>
  <div class="d-flex flex-column h-100v">
    <AppNavbar class="flex-shrink-0"/>
    <router-view
      :key="$route.path"
    />
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
