<template>
  <div>
    <MainBreadcrumb
      :owner="owner"
      :item="item"
      />
    {{ item }}
  </div>
</template>

<script>
import { mapState } from 'vuex';
import api from '@/api';
import MainBreadcrumb from '@/components/MainBreadcrumb';

export default {
  name: 'MainView',

  props: {
    user: {
      type: String,
      required: true,
    },
    path: {
      type: String,
      default: '',
    },
  },

  components: {
    MainBreadcrumb,
  },

  data() {
    return {
      item: {},
    };
  },

  computed: {
    owner() {
      return this.user === this.me;
    },
    ...mapState('auth', ['me']),
  },

  created() {
    const url = `/${this.user}/${this.path}`;
    api.get(url).then((response) => {
      const link = response.data.link;
      if (link) {
        window.location.href = link;
      } else {
        this.item = response.data;
      }
    });
  },
};
</script>

<style scoped>
</style>
