<template>
  <router-view
    class="h-100v"
    :key="$route.path"
    />
</template>

<script>
export default {
  name: 'App',
};
</script>
