<template>
  <div>

    <ItemSelf
      :user="user"
      :name="name"
    />

    <ItemChildren
      :user="user"
      :children="children"
    />

  </div>
</template>

<script>
import api from '@/core/api';
import ItemSelf from '@/components/ItemSelf';
import ItemChildren from '@/components/ItemChildren';

export default {
  name: 'ItemView',

  props: ['user', 'name'],

  components: {
    ItemSelf,
    ItemChildren,
  },

  data() {
    return {
      self: {},
      children: [],
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
        this.error = error;
      });
  },
};
</script>
