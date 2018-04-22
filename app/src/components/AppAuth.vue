<template>
  <b-navbar-nav class="app-auth">
    <b-nav-item v-if="signInRequired">
      <b-button class="btn-social"
                variant="outline-light"
                size="sm"
                @click="signIn">
        <i class="fa fa-github"></i>
        Sign in with GitHub
      </b-button>
    </b-nav-item>
    <b-nav-item-dropdown v-else right>
      <template slot="button-content">
        <b-img rounded="circle"
               width="32"
               height="32"
               :alt="me"
               :src="avatarURL"/>
      </template>
      <b-dropdown-item @click="signOut">
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
    ...mapState('auth', [
      'me',
      'avatarURL',
      'refresh',
    ]),
    signInRequired() {
      return this.me == null;
    },
  },
  methods: {
    ...mapMutations('auth', [
      'refreshRequired',
    ]),
    ...mapActions('auth', [
      'checkAuth',
      'signOut',
    ]),
    signIn() {
      this.refreshRequired();
      window.location.href = `${process.env.API_BASE_URL}/auth/signin`;
    },
  },
  created() {
    if (this.refresh) {
      this.checkAuth();
    }
  },
};
</script>

<style lang="scss" scoped>
.app-auth .btn-social>:first-child {
  border-right: 1px solid $light;
}
</style>
