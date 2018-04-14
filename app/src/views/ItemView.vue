<template>
  <div>
    <ItemPath
      :username="username"
      :pathquery="pathquery"
    />

    <div v-if="redirect">
    </div>
    <div v-else>
      <ItemSelf
        :username="username"
        :self="self"
      />
      <ItemChildren
        :username="username"
        :children="children"
      />
    </div>
  </div>
</template>

<script>
import api from '@/api';

import ItemPath from '@/components/ItemPath';
import ItemSelf from '@/components/ItemSelf';
import ItemChildren from '@/components/ItemChildren';

export default {
  name: 'ItemView',

  // TODO: Make declarations specific
  props: ['username', 'pathquery'],

  components: {
    ItemPath,
    ItemSelf,
    ItemChildren,
  },

  data() {
    return {
      queried: {},
    };
  },

  created() {
    const url = `/${this.username}/${this.pathquery}`;
    api.get(url).then((response) => {
      this.queried = response.data;
    });
  },

  watch: {
    queried(q) {
      if (q.redirect && q.self.linkto) {
        window.location.href = q.self.linkto;
      }
    },
  },

  computed: {
    self() {
      return this.queried.self;
    },
    redirect() {
      return this.queried.redirect;
    },
    children() {
      return this.queried.children;
    },
  },
};
</script>
