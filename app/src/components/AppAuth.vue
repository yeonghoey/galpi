<template>
  <div class="app-auth">
    <b-nav-item
      v-if="signInRequired"
      >

      <b-button
        class="btn-social"
        variant="outline-light"
        size="sm"
        >
        <span class="fa fa-github"></span>
        Sign in with GitHub
      </b-button>

    </b-nav-item>

    <b-nav-item-dropdown
      v-else
      :text="username"
      right
      >

      <b-dropdown-item>
        Sign out
      </b-dropdown-item>

    </b-nav-item-dropdown>
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
