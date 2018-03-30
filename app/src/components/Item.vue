<template>
  <div>
    <ul>
      <li v-for="item in items" :key="item">
        {{ item.name }} {{ item.to }}
      </li>
    </ul>
  </div>
</template>

<script>
import api from '@/core/api';

export default {
  name: 'Item',
  props: ['user', 'name'],

  data() {
    return {
      items: [],
      errors: [],
    };
  },

  computed: {
    target() {
      if (this.name === undefined) {
        return undefined;
      }
      if (this.name.endsWith('/')) {
        return undefined;
      }
      const item = this.items.find(x => x.name === this.name);
      if (item === undefined) {
        return undefined;
      }
      return item.to;
    },
  },

  watch: {
    target(to) {
      if (to !== undefined) {
        window.location.href = to;
      }
    },
  },

  created() {
    api.get(this.$route.path)
      .then((response) => {
        this.items = response.data.items;
      })
      .catch((error) => {
        this.errors.push(error);
      });
  },
};
</script>
