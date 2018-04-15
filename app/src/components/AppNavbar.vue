<template>
  <b-navbar
    toggleable="md"
    type="dark"
    variant="info"
    sticky
    >

    <b-navbar-brand to="/">
      <span class="fa fa-bookmark-o p-1"></span>
      Galpi
    </b-navbar-brand>
    <AppAuth class="ml-auto"/>
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
