<template>
  <div>
    <ItemSelf
      :username="username"
      :self="self"
      />

    <div v-if="redirect">
    </div>
    <div v-else>
      <ItemChildren
        :username="username"
        :children="children"
        />
    </div>
  </div>
</template>

<script>
import _ from 'lodash';
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
      return _.get(this.queried, 'self', {});
    },
    redirect() {
      return _.get(this.queried, 'redirect', false);
    },
    children() {
      return _.get(this.queried, 'children', []);
    },
  },
};
</script>
