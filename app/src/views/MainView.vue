<template>
  <div>
    <div
      v-if="renderUI"
      class="h-100 d-flex flex-column"
      >
      <AppNavbar
        class="flex-shrink-0"
        />
      <MainBreadcrumb
        class="flex-shrink-0"
        :owner="owner"
        :item="item"
        />
      <MainContent
        class="flex-fill"
        :owner="owner"
        :item="item"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import api from '@/api';

import AppNavbar from '@/components/AppNavbar';
import MainBreadcrumb from '@/components/MainBreadcrumb';
import MainContent from '@/components/MainContent';

export default {
  name: 'MainView',

  components: {
    AppNavbar,
    MainBreadcrumb,
    MainContent,
  },

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

  data() {
    return {
      renderUI: false,
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
        this.renderUI = true;
        this.item = response.data;
      }
    });
  },
};
</script>

<style scoped>
</style>
