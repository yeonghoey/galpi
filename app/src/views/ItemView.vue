<template>
  <div>
    <ItemSelf
      :username="username"
      :pathquery="pathquery"
    />

    <ItemChildren
      :username="username"
      :children="children"
    />
  </div>
</template>

<script>
import api from '@/api';
import ItemSelf from '@/components/ItemSelf';
import ItemChildren from '@/components/ItemChildren';

export default {
  name: 'ItemView',

  // TODO: Make declarations specific
  props: ['username', 'pathquery'],

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

  watch: {
    self(item) {
      // TODO: This logic should only be in API
      if (this.$route.path.endsWith('/')) {
        return;
      }

      if (item.linkto != null) {
        window.location.href = item.linkto;
      }
    },
  },

  created() {
    api.get(this.$route.path)
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
