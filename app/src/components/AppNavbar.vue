<template>
  <b-navbar
    toggleable="md"
    type="dark"
    variant="info"
    sticky
    >

    <b-navbar-brand to="/">
      Galpi
    </b-navbar-brand>

    <b-navbar-nav class="ml-auto">
      <AppAuth/>
    </b-navbar-nav>

  </b-navbar>
</template>

<script>
import AppAuth from '@/components/AppAuth';

export default {
  name: 'AppNavbar',
  components: {
    AppAuth,
  },
};
</script>
