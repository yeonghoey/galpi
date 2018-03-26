<template>
  <div>
    <h1>{{ username }}</h1>
  </div>
</template>

<script>
export default {
  name: 'User',
  props: ['username'],
};
</script>
