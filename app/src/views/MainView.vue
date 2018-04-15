<template>
  <div class="d-flex align-items-stretch">
    <MainSidebar
      class="main-sidebar"
      :username="username"
    />
  </div>
</template>

<script>
import MainSidebar from '@/components/MainSidebar';

export default {
  name: 'MainView',

  props: {
    username: String,
  },

  components: {
    MainSidebar,
  },
};
</script>

<style scoped>
.main-sidebar {
  flex: 0 1 240px;
}
</style>
