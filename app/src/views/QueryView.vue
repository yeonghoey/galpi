<template>
  <div>
    <ItemPath
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
import ItemPath from '@/components/ItemPath';
import ItemChildren from '@/components/ItemChildren';

export default {
  name: 'QueryView',

  // TODO: Make declarations specific
  props: ['username', 'pathquery'],

  components: {
    ItemPath,
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
      if (q.redirect && q.item.linkto) {
        window.location.href = q.item.linkto;
      }
    },
  },

  computed: {
    item() {
      return this.queried.item;
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
