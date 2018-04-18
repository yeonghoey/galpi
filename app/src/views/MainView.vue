<template>
  <div>
    {{ user }} / {{ path }}
  </div>
</template>

<script>
export default {
  name: 'MainView',

  props: {
    user: {
      type: String,
      required: true,
    },
    path: {
      type: String,
    },
  },
};
</script>

<style scoped>
</style>
