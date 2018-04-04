<template>
  <div>
    <h1>{{ user }} / {{ name }}</h1>
    <p>{{ self.to }}</p>
    <ul>
      <li v-for="child in children" :key="child">
        {{ child.name }} {{ child.to }}
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
      self: {},
      children: [],
      errors: [],
    };
  },

  computed: {
    pq() {
      return this.$route.path;
    },
  },

  watch: {
    self(val) {
      if (this.pq.endsWith('/')) {
        return;
      }
      if (val.to !== undefined) {
        window.location.href = val.to;
      }
    },
  },

  created() {
    api.get(this.pq)
      .then((response) => {
        this.self = response.data.self;
        this.children = response.data.children;
      })
      .catch((error) => {
        this.errors.push(error);
      });
  },
};
</script>
