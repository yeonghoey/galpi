<template>
  <b-navbar-nav class="app-auth">
    <b-nav-item
      v-if="signInRequired"
      >
      <b-button
        class="btn-social"
        variant="outline-light"
        size="sm"
        @click="signIn"
        >
        <span class="fa fa-github"></span>
        Sign in with GitHub
      </b-button>
    </b-nav-item>

    <b-nav-item-dropdown
      right
      >
      <template slot="button-content">
        <b-img
          class="border border-light"
          rounded="circle"
          :alt="myUsername"
          :src="myAvatarURL"
          />
      </template>
      <b-dropdown-item
        @click="signOut"
        >
        Sign out
      </b-dropdown-item>
    </b-nav-item-dropdown>
  </b-navbar-nav>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex';

export default {
  name: 'AppAuth',

  computed: {
    signInRequired() {
      return this.myUsername == null;
    },

    ...mapState('auth', [
      'myUsername',
      'myAvatarURL',
      'refresh',
    ]),
  },

  created() {
    if (this.refresh) {
      this.checkAuth();
    }
  },

  methods: {
    signIn() {
      this.refreshRequired();
      window.location.href = `${process.env.API_BASE_URL}/auth/signin`;
    },

    ...mapMutations('auth', [
      'refreshRequired',
    ]),
    ...mapActions('auth', [
      'checkAuth',
      'signOut',
    ]),

  },
};
</script>

<style lang="scss" scoped>
.app-auth .btn-social>:first-child {
  border-right: 1px solid $light;
}
</style>
