<template>
  <div>
    <h1></h1>
  </div>
</template>

<script>
import api from '@/core/api';

export default {
  name: 'Item',
  props: ['user', 'name'],

  data() {
    return {
    };
  },

  mounted() {
    api.get(this.$route.path)
      .then((res) => {
        // TODO: Handle exceptional cases
        window.location.href = res.data.value;
      });
  },
};
</script>
