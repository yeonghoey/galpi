<template>
  <div class="app-auth">
    <b-button
      class="btn-social"
      variant="outline-light"
      size="sm"
    >
      <span class="fa fa-github"></span>
      Sign in with GitHub
    </b-button>
  </div>
</template>

<script>
export default {
  name: 'AppAuth',
};
</script>

<style scoped>
.app-auth .btn-social>:first-child {
  /* bootstrap light  */
  border-right: 1px solid #f8f9fa;
}
</style>
