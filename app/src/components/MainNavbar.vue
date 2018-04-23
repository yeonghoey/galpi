<template>
  <b-navbar toggleable="md"
            type="dark"
            variant="info"
            sticky>
    <b-navbar-brand to="/">
      Galpi
    </b-navbar-brand>
    <AppAuth class="ml-auto"/>
  </b-navbar>
</template>

<script>
import AppAuth from '@/components/AppAuth';

export default {
  name: 'MainNavbar',
  components: {
    AppAuth,
  },
};
</script>
