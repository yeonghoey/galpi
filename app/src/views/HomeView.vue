<template>
  <div class="h-100 d-flex flex-column">
    <HomeJumbotron class="flex-fill"/>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import HomeJumbotron from '@/components/HomeJumbotron';

export default {
  name: 'HomeView',

  components: {
    HomeJumbotron,
  },

  computed: {
    ...mapState('auth', [
      'me',
    ]),
  },

  watch: {
    me: {
      immediate: true,
      handler(user) {
        if (user) {
          this.$router.replace(`/${user}`);
        }
      },
    },
  },
};
</script>
