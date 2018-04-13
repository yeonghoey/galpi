<template>
  <div class="app-auth">
    <b-button
      v-if="signInRequired"
      class="btn-social"
      variant="outline-light"
      size="sm"
    >
      <span class="fa fa-github"></span>
      Sign in with GitHub
    </b-button>

    <h2 v-else>
      Welcome, {{ username }}
    </h2>


  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'AppAuth',

  computed: {
    signInRequired() {
      return this.username === undefined;
    },

    ...mapState('auth', [
      'username',
    ]),
  },

  methods: {
    ...mapActions('auth', [
      'checkAuth',
    ]),
  },

  created() {
    this.checkAuth();
  },
};
</script>

<style lang="scss" scoped>
.app-auth .btn-social>:first-child {
  border-right: 1px solid $light;
}
</style>
